# main.py

import cv2
import numpy as np
from configuracion import *
from captura_video import CapturaVideo
from detector_marcadores import DetectorMarcadores

def main():
    # Inicializar la captura de video
    captura = CapturaVideo(
        fuente=FUENTE_VIDEO,
        numero_camara=NUMERO_CAMARA,
        ruta_video=RUTA_VIDEO,
        ancho_frame=ANCHURA_FRAME,
        altura_frame=ALTURA_FRAME
    )

    # Inicializar el detector de marcadores
    detector = DetectorMarcadores()

    ventana = TITULO_VENTANA

    while True:
        frame = captura.leer_frame()
        if frame is None:
            print("No se pudo capturar el frame. Terminando la captura.")
            break

        # Detectar marcadores
        corners, ids = detector.detectar_marcadores(frame)

        if ids is not None:
            # Dibujar los marcadores detectados y sus IDs en el frame
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        # Mostrar el frame con los marcadores detectados
        cv2.imshow(ventana, frame)

        # Procesa los eventos de la ventana
        key = cv2.waitKey(1) & 0xFF

        # Detecta si la ventana ha sido cerrada
        window_visible = cv2.getWindowProperty(TITULO_VENTANA, cv2.WND_PROP_VISIBLE)

        if window_visible < 1:
            print("La ventana ha sido cerrada")
            break

    # Liberar recursos
    captura.liberar()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
