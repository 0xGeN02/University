# detector_marcadores.py

import cv2
from configuracion import *

class DetectorMarcadores:
    def __init__(self, aruco_dict_type=cv2.aruco.DICT_4X4_50,
                 camera_matrix=None, dist_coeffs=None):
        """
        Inicializa el detector de marcadores.

        :param aruco_dict_type: Tipo de diccionario de Aruco a usar
        :param camera_matrix: Matriz de cámara
        :param dist_coeffs: Coeficientes de distorsión
        """
        self.aruco_dict = cv2.aruco.Dictionary_get(aruco_dict_type)
        self.parameters = cv2.aruco.DetectorParameters_create()

        if camera_matrix is not None and dist_coeffs is not None:
            self.camera_matrix = camera_matrix
            self.dist_coeffs = dist_coeffs
        else:
            # Si no se proporcionan parámetros de cámara, aplicamos
            # parámetros por defecto (sin distorsión)
            self.camera_matrix = np.array([[800, 0, 320],
                                           [0, 800, 240],
                                           [0, 0, 1]], dtype=np.float32)
            self.dist_coeffs = np.zeros((5, 1))

    def detectar_marcadores(self, frame):
        """
        Detecta marcadores Aruco en el frame.

        :param frame: Imagen de entrada (BGR)
        :return: lista de marcadores detectados, cada uno con su ID y pose
        """
        # Convertir a escala de grises
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecta marcadores
        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(
            gris, self.aruco_dict, parameters=self.parameters)

        marcadores = []

        if ids is not None:
            # Estima la pose de cada marcador

            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(
                corners, TAMANO_MARCADOR, self.camera_matrix, self.dist_coeffs)

            for i, id in enumerate(ids.flatten()):
                marcador = {
                    'id': int(id),
                    'corners': corners[i],
                    'rvec': rvecs[i],
                    'tvec': tvecs[i]
                }
                marcadores.append(marcador)

        return marcadores
