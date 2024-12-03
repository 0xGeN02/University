# shi_tomasi.py
import os
import cv2
import numpy as np

# Número máximo de esquinas a detectar
NUMERO_ESQUINAS = 50
# Calidad mínima de las esquinas (entre 0 y 1)
CALIDAD = 0.01
# Distancia mínima entre esquinas detectadas (en píxeles)
DISTANCIA_MINIMA = 10
# Color de resalte de las esquinas, en BGR
COLOR_RESALTE = [0, 0, 255]  # Color rojo

#Path de esta carpeta
PATH = os.path.dirname(os.path.abspath(__file__))
# Carga la imagen
imagen = cv2.imread(os.path.join(PATH, 'imagenes/uie.png'))

# Verifica que la imagen se haya cargado correctamente
if imagen is None:
    print("No se pudo cargar la imagen. Asegúrate de que el nombre y la ruta sean correctos.")
    exit()

# Convierte la imagen a escala de grises
imagen_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detecta esquinas usando el método de Shi-Tomasi
esquinas = cv2.goodFeaturesToTrack(imagen_grises, NUMERO_ESQUINAS, CALIDAD, DISTANCIA_MINIMA)

# Verifica que se hayan detectado esquinas
if esquinas is not None:
    # Convierte las coordenadas a enteros
    esquinas = np.int32(esquinas)

    # Recorre cada esquina y marca en la imagen original
    for esquina in esquinas:
        x, y = esquina.ravel()
        cv2.circle(imagen, (x, y), 4, COLOR_RESALTE, -1)
else:
    print("No se detectaron esquinas.")

# Muestra la imagen con las esquinas detectadas
cv2.imshow('Algoritmo de deteccion de esquinas de Shi-Tomasi', imagen)

# Espera a que se pulse una tecla
cv2.waitKey(0)

# Libera recursos
cv2.destroyAllWindows()
