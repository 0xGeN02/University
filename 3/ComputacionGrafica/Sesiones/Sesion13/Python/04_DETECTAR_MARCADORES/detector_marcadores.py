# detector_marcadores.py

import cv2
import numpy as np

class DetectorMarcadores:
    def __init__(self, aruco_dict_type=cv2.aruco.DICT_4X4_50):
        """
        Inicializa el detector de marcadores.

        :param aruco_dict_type: Tipo de diccionario de Aruco a usar
        """
        self.aruco_dict = cv2.aruco.Dictionary_get(aruco_dict_type)
        self.parameters = cv2.aruco.DetectorParameters_create()

    def detectar_marcadores(self, frame):
        """
        Detecta marcadores Aruco en el frame.

        :param frame: Imagen de entrada (BGR)
        :return: corners, ids
        """
        # Convertir a escala de grises
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecta marcadores
        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(
            gris, self.aruco_dict, parameters=self.parameters)

        return corners, ids
