# motor_renderizado.py

import cv2
import numpy as np
import math
from configuracion import *
from modelo_3d import Modelo3D


class MotorRenderizado:
    def __init__(self, camera_matrix=None, dist_coeffs=None, carpeta_imagenes='imagenes'):
        """
        Inicializa el motor de renderizado.

        :param camera_matrix: Matriz de cámara
        :param dist_coeffs: Coeficientes de distorsión
        :param carpeta_imagenes: Carpeta donde se encuentran las imágenes a superponer (overlay)
        """
        if camera_matrix is not None and dist_coeffs is not None:
            self.camera_matrix = camera_matrix
            self.dist_coeffs = dist_coeffs
        else:
            # Parámetros por defecto (sin distorsión)
            self.camera_matrix = np.array([[800, 0, 320],
                                           [0, 800, 240],
                                           [0, 0, 1]], dtype=np.float32)
            self.dist_coeffs = np.zeros((5, 1))

        # Cargar los modelos 3D usando Modelo3D
        self.modelos_marcadores = {}
        for id_marcador, info_modelo in MODELOS_MARCADORES.items():
            ruta_modelo = info_modelo["ruta_modelo"]
            try:
                modelo = Modelo3D(ruta_modelo)
                # Almacenar modelo, transformaciones y color
                self.modelos_marcadores[id_marcador] = {
                    "modelo": modelo,
                    "traslacion": info_modelo["traslacion"],
                    "escala": info_modelo["escala"],
                    "color": info_modelo["color"]
                }
                print(f"Modelo cargado para marcador ID {id_marcador}: {ruta_modelo}")
            except Exception as e:
                print(f"Error al cargar el modelo para el marcador ID {id_marcador}: {e}")

        # Rotación adicional (COMENTADA)
        # angle = math.radians(90)  # Convertir a radianes
        # self.rotation_matrix_additional = np.array([
        #     [math.cos(angle), 0, math.sin(angle)],
        #     [0, 1, 0],
        #     [-math.sin(angle), 0, math.cos(angle)]
        # ], dtype=np.float32)

    def obtener_color(self, id_marcador):
        """
        Obtiene el color asignado al ID del marcador desde la configuración.

        :param id_marcador: ID del marcador
        :return: Tupla de color en formato BGR
        """
        if id_marcador in self.modelos_marcadores:
            return self.modelos_marcadores[id_marcador]["color"]
        else:
            # No se utiliza color por defecto
            return None

    def obtener_modelo_y_transformaciones(self, id_marcador):
        """
        Obtiene el modelo 3D y sus transformaciones asociados al ID del marcador.

        :param id_marcador: ID del marcador
        :return: Tuple (Modelo3D, dict de traslación, dict de escala)
        """
        if id_marcador in self.modelos_marcadores:
            info = self.modelos_marcadores[id_marcador]
            return info["modelo"], info["traslacion"], info["escala"]
        else:
            return None, None, None

    def aplicar_transformaciones(self, vertices, traslacion, escala):
        """
        Aplica escalado, rotación de +90° en X y traslación a los vértices del modelo.

        :param vertices: Array de vértices (N, 3)
        :param traslacion: Dict con 't_x', 't_y', 't_z'
        :param escala: Dict con 's_x', 's_y', 's_z'
        :return: Array de vértices transformados (N, 3)
        """
        # Escalar los vértices
        escala_vector = np.array([escala["s_x"], escala["s_y"], escala["s_z"]], dtype=np.float32)
        vertices_escalados = vertices * escala_vector

        # Rotar los vértices +90 grados alrededor del eje X
        angle = math.radians(90)  # Rotación de +90 grados
        rotation_x = np.array([
            [1, 0, 0],
            [0, math.cos(angle), -math.sin(angle)],
            [0, math.sin(angle), math.cos(angle)]
        ], dtype=np.float32)
        vertices_rotados = vertices_escalados @ rotation_x.T

        # Aplicar la traslación
        traslacion_vector = np.array([traslacion["t_x"], traslacion["t_z"], traslacion["t_y"]], dtype=np.float32)
        vertices_transformados = vertices_rotados + traslacion_vector  # (N,3) + (3,)

        return vertices_transformados

    def renderizar_modelo(self, frame, rvec, tvec, id_marcador):
        """
        Superpone un modelo 3D sobre el marcador detectado.

        :param frame: Imagen de entrada (BGR)
        :param rvec: Vector de rotación
        :param tvec: Vector de traslación
        :param id_marcador: ID del marcador
        :return: Imagen con el modelo 3D dibujado
        """
        # Obtiene el color para este marcador desde la configuración
        color = self.obtener_color(id_marcador)

        # Obtener el modelo y sus transformaciones correspondientes al marcador
        modelo, traslacion, escala = self.obtener_modelo_y_transformaciones(id_marcador)
        if modelo is None:
            # Opcional: Imprimir un mensaje de depuración
            print(f"Marcador ID {id_marcador} detectado pero no está definido en MODELOS_MARCADORES. Ignorando.")
            return frame

        # Imprimir las transformaciones para depuración
        print(f"Marcador ID: {id_marcador}")
        print(f"Traslación: {traslacion}")
        print(f"Escala: {escala}")

        # Verificar y ajustar la forma de tvec
        if tvec.shape == (3, 1):
            tvec = tvec.T.ravel()  # Convertir a (1, 3) y luego a (3,)
        elif tvec.shape == (1, 3):
            tvec = tvec.ravel()  # Convertir a (3,)
        else:
            tvec = tvec.flatten()  # Aplanar en cualquier otro caso

        # Escalar y rotar los vértices del modelo
        transformed_vertices = self.aplicar_transformaciones(modelo.vertices, traslacion, escala)  # (N,3)

        # Transformar los vértices según la pose del marcador
        rot_matrix, _ = cv2.Rodrigues(rvec)
        transformed_vertices = (rot_matrix @ transformed_vertices.T).T + tvec  # (N,3) + (3,)

        # Proyectar los vértices 3D en 2D
        puntos_2D, _ = cv2.projectPoints(transformed_vertices, np.zeros((3, 1)), np.zeros((3, 1)),
                                         self.camera_matrix, self.dist_coeffs)
        puntos_2D = puntos_2D.reshape(-1, 2).astype(int)

        # Dibujar las aristas del modelo 3D usando el color asignado
        for face in modelo.faces:
            # Asegúrate de que cada cara tenga al menos dos vértices
            if len(face) < 2:
                continue
            # Itera sobre los vértices de la cara para dibujar las líneas
            for i in range(len(face)):
                pt1 = tuple(puntos_2D[face[i]])
                pt2 = tuple(puntos_2D[face[(i + 1) % len(face)]])
                cv2.line(frame, pt1, pt2, color, 2)

        return frame
