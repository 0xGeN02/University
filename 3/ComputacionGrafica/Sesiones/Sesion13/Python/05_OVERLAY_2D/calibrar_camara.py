# calibrar_camara.py

import cv2
import numpy as np
import os

NUMERO_CAMARA = 0

def calibrar_camara():
    # Definir el tamaño del tablero de ajedrez
    num_cuadros_x = 7  # Número de esquinas internas por fila
    num_cuadros_y = 6  # Número de esquinas internas por columna
    tamaño_cuadro = 0.016  # Tamaño de cada cuadro en metros

    # Criterios de terminación para la búsqueda de esquinas
    criterio = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # Preparar los puntos del objeto 3D en el mundo real
    objp = np.zeros((num_cuadros_y * num_cuadros_x, 3), np.float32)
    objp[:, :2] = np.mgrid[0:num_cuadros_x, 0:num_cuadros_y].T.reshape(-1, 2)
    objp *= tamaño_cuadro

    # Listas para almacenar los puntos de objeto y los puntos de imagen de todas las imágenes
    objpoints = []  # Puntos 3D en el mundo real
    imgpoints = []  # Puntos 2D en la imagen

    # Crear directorio para guardar las imágenes capturadas
    if not os.path.exists('capturas_calibracion'):
        os.makedirs('capturas_calibracion')

    captura = cv2.VideoCapture(NUMERO_CAMARA)  # Usa la cámara predeterminada

    print("Presiona 'c' para capturar una imagen del tablero de ajedrez.")
    print("Presiona 'q' para terminar la calibración.")

    count = 0
    while True:
        ret, frame = captura.read()
        if not ret:
            print("No se pudo capturar el frame.")
            break

        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Encontrar las esquinas del tablero de ajedrez
        ret_corners, corners = cv2.findChessboardCorners(gris, (num_cuadros_x, num_cuadros_y), None)

        # Si se encuentran las esquinas, dibujarlas
        if ret_corners:
            cv2.drawChessboardCorners(frame, (num_cuadros_x, num_cuadros_y), corners, ret_corners)

        cv2.imshow('Calibracion de Camara', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('c') and ret_corners:
            objpoints.append(objp)
            # Refinar las esquinas encontradas
            corners2 = cv2.cornerSubPix(gris, corners, (11, 11), (-1, -1), criterio)
            imgpoints.append(corners2)

            # Guardar la imagen capturada
            img_nombre = f'capturas_calibracion/calib_{count}.png'
            cv2.imwrite(img_nombre, frame)
            print(f"Imagen guardada: {img_nombre}")
            count += 1

        elif key == ord('q'):
            break

    captura.release()
    cv2.destroyAllWindows()

    if len(objpoints) < 10:
        print("No se encontraron suficientes imágenes para la calibración. Captura al menos 10 imágenes.")
        return

    # Calibrar la cámara
    ret_calib, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
        objpoints, imgpoints, gris.shape[::-1], None, None)

    if ret_calib:
        print("\nCalibración exitosa.")
        print("Matriz de cámara (CAMERA_MATRIX):")
        print(mtx)
        print("\nCoeficientes de distorsión (DIST_COEFFS):")
        print(dist)

        # Guardar los parámetros en un archivo de texto
        with open('calibracion_camara.txt', 'w') as f:
            f.write("CAMERA_MATRIX = np.array([\n")
            for row in mtx:
                f.write("    " + str(row.tolist()) + ",\n")
            f.write("], dtype=np.float32)\n\n")
            f.write("DIST_COEFFS = np.array([\n")
            for coef in dist:
                f.write("    " + str(coef.tolist()) + ",\n")
            f.write("], dtype=np.float32)\n")

        print("\nParámetros de calibración guardados en 'camara_calibrada.txt'.")
    else:
        print("Calibración fallida.")


if __name__ == "__main__":
    calibrar_camara()
