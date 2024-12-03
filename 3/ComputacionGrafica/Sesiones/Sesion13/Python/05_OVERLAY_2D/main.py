# main.py

import cv2
import numpy as np
from configuracion import *
from captura_video import CapturaVideo
from detector_marcadores import DetectorMarcadores
from motor_renderizado_2D import OverlayRenderer

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
    detector = DetectorMarcadores(
        camera_matrix=CAMERA_MATRIX,
        dist_coeffs=DIST_COEFFS
    )

    # Inicializar el renderer de overlays
    renderer = OverlayRenderer(
        camera_matrix=CAMERA_MATRIX,
        dist_coeffs=DIST_COEFFS,
        carpeta_overlay=CARPETA_OVERLAY
    )

    ventana = TITULO_VENTANA

    while True:
        frame = captura.leer_frame()
        if frame is None:
            print("No se pudo capturar el frame. Terminando la captura.")
            break

        # Detectar marcadores
        marcadores = detector.detectar_marcadores(frame)

        for marcador in marcadores:
            id_marcador = marcador['id']
            corners = marcador['corners']
            rvec = marcador['rvec']
            tvec = marcador['tvec']

            # Renderizar el overlay correspondiente
            frame = renderer.renderizar_overlay(frame, corners, rvec, tvec, id_marcador)

        # Mostrar el frame con overlays
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
