# captura_video.py

import cv2
import numpy as np
from configuracion import *
from motor_renderizado import MotorRenderizado
import cv2.aruco as aruco

def main():
    # Inicializar la cámara
    if FUENTE_VIDEO == 'camara':
        cap = cv2.VideoCapture(NUMERO_CAMARA)
    else:
        cap = cv2.VideoCapture(RUTA_VIDEO)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, ANCHURA_FRAME)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, ALTURA_FRAME)

    # Inicializar el motor de renderizado
    motor = MotorRenderizado(camera_matrix=CAMERA_MATRIX, dist_coeffs=DIST_COEFFS, carpeta_imagenes=CARPETA_IMAGENES)

    # Definir el diccionario ArUco a usar
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters_create()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detectar marcadores
        corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

        if ids is not None:
            # Estimar la pose de cada marcador
            rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, TAMANO_MARCADOR, CAMERA_MATRIX, DIST_COEFFS)

            for i, id_marcador in enumerate(ids.flatten()):
                if id_marcador in MODELOS_MARCADORES:
                    rvec = rvecs[i]
                    tvec = tvecs[i]

                    # Renderizar el modelo correspondiente
                    frame = motor.renderizar_modelo(frame, rvec, tvec, id_marcador)
                else:
                    # Opcional: Imprimir un mensaje de depuración
                    print(f"Marcador ID {id_marcador} detectado pero no está definido en MODELOS_MARCADORES. Ignorando.")

        # Mostrar la imagen resultante
        cv2.imshow(TITULO_VENTANA, frame)

        # Procesa eventos de la ventana
        key = cv2.waitKey(20) & 0xFF

        # Detecta si la ventana ha sido cerrada
        window_visible = cv2.getWindowProperty(TITULO_VENTANA, cv2.WND_PROP_VISIBLE)

        if window_visible < 1:
            print("La ventana ha sido cerrada")
            break
    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
