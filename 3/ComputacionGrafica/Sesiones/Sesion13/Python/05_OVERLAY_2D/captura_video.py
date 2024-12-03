# captura_video.py

import cv2

class CapturaVideo:
    def __init__(self, fuente='camara', numero_camara=0, ruta_video='video.avi',
                 ancho_frame=640, altura_frame=480):
        """
        Inicializa la captura de video.

        :param fuente: 'camara' o 'video'
        :param numero_camara: Índice de la cámara (si fuente es 'camara')
        :param ruta_video: Ruta al archivo de video (si fuente es 'video')
        :param ancho_frame: Ancho del frame
        :param altura_frame: Altura del frame
        """
        self.fuente = fuente
        self.numero_camara = numero_camara
        self.ruta_video = ruta_video
        self.ancho_frame = ancho_frame
        self.altura_frame = altura_frame

        if self.fuente == 'camara':
            self.captura = cv2.VideoCapture(self.numero_camara)
        elif self.fuente == 'video':
            self.captura = cv2.VideoCapture(self.ruta_video)
        else:
            raise ValueError(f"Fuente de video no soportada: {self.fuente}")

        if not self.captura.isOpened():
            raise IOError(f"No se pudo abrir la fuente de video: {self.fuente}")

        # Establece la resolución
        self.captura.set(cv2.CAP_PROP_FRAME_WIDTH, self.ancho_frame)
        self.captura.set(cv2.CAP_PROP_FRAME_HEIGHT, self.altura_frame)

    def leer_frame(self):
        """
        Lee un frame de la fuente de video.

        :return: frame capturado o None si no se pudo capturar
        """
        ret, frame = self.captura.read()
        if not ret:
            return None
        return frame

    def liberar(self):
        """
        Libera la captura de video.
        """
        self.captura.release()
