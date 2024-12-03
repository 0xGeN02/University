# motor_renderizado_2D.py

import cv2
import numpy as np
from configuracion import *
import os

class OverlayRenderer:
    def __init__(self, camera_matrix=None, dist_coeffs=None, carpeta_overlay='overlay'):
        """
        Inicializa el renderer de overlays 2D.

        :param camera_matrix: Matriz de cámara
        :param dist_coeffs: Coeficientes de distorsión
        :param carpeta_overlay: Carpeta donde se encuentran las imágenes overlay
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

        self.carpeta_overlay = carpeta_overlay
        self.overlays = self.cargar_overlays()

    def cargar_overlays(self):
        """
        Carga las imágenes overlay desde la carpeta especificada.

        :return: Diccionario mapeando IDs de marcadores a imágenes overlay
        """
        overlays = {}
        for id_marcador, info in MODELOS_MARCADORES.items():
            ruta_imagen = os.path.join(self.carpeta_overlay, info["ruta_overlay"])
            imagen = cv2.imread(ruta_imagen, cv2.IMREAD_UNCHANGED)
            if imagen is None:
                print(f"Error al cargar la imagen overlay para el marcador ID {id_marcador}: {ruta_imagen}")
                continue
            overlays[id_marcador] = imagen
        return overlays

    def renderizar_overlay(self, frame, corners, rvec, tvec, id_marcador):
        """
        Superpone una imagen 2D sobre el marcador detectado.

        :param frame: Imagen de entrada (BGR)
        :param corners: Coordenadas de las esquinas del marcador
        :param rvec: Vector de rotación
        :param tvec: Vector de traslación
        :param id_marcador: ID del marcador
        :return: Imagen con el overlay 2D dibujado
        """
        if id_marcador not in self.overlays:
            # No hay overlay definido para este marcador
            return frame

        overlay = self.overlays[id_marcador]

        # Obtener las esquinas del overlay
        h_overlay, w_overlay = overlay.shape[:2]

        # Definir puntos de origen en la imagen overlay
        puntos_origen = np.array([
            [0, 0],
            [w_overlay - 1, 0],
            [w_overlay - 1, h_overlay - 1],
            [0, h_overlay - 1]
        ], dtype=np.float32)

        # Obtener puntos de destino desde las esquinas del marcador
        puntos_destino = corners.reshape(4, 2).astype(np.float32)

        # Calcular la homografía
        homografia, _ = cv2.findHomography(puntos_origen, puntos_destino)

        if homografia is not None:
            # Determinar el tamaño de la imagen overlay
            frame_h, frame_w = frame.shape[:2]

            # Crear máscara de overlay
            overlay_img = cv2.warpPerspective(overlay, homografia, (frame_w, frame_h), None, cv2.INTER_LINEAR, cv2.BORDER_TRANSPARENT)

            if overlay.shape[2] == 4:
                # Overlay con canal alfa
                alpha_overlay = overlay_img[:, :, 3] / 255.0
                alpha_frame = 1.0 - alpha_overlay

                for c in range(0, 3):
                    frame[:, :, c] = (alpha_overlay * overlay_img[:, :, c] +
                                      alpha_frame * frame[:, :, c])
            else:
                # Overlay sin canal alfa
                frame = cv2.addWeighted(frame, 1, overlay_img, 1, 0)

        return frame
