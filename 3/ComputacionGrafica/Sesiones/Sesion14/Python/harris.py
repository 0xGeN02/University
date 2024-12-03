# harris.py
import os
import cv2
import numpy as np

# Tamaño del vecindario alrededor de cada píxel
BLOCKSIZE = 2
# Tamaño del kernel utilizado para calcular las derivadas en las direcciones X e Y.
KSIZE = 3
# Parámetro libre de Harris, controla la sensibilidad del detector.
K = 0.04
# Umbral relativo
UMBRAL = 0.01
# Color de resalte de las esquinas, en BGR
COLOR_RESALTE = [0, 0, 255] # Color rojo

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

# Convierte el tipo de datos a float32
imagen_grises = np.float32(imagen_grises)

# Aplicar el algoritmo de detección de esquinas de Harris
esquinas = cv2.cornerHarris(imagen_grises, BLOCKSIZE, KSIZE, K)

# Dilata las esquinas para resaltarlas
esquinas = cv2.dilate(esquinas, None)

# Umbraliza la imagen para marcar las esquinas sobre la imagen original
imagen[esquinas > UMBRAL * esquinas.max()] = COLOR_RESALTE

# Muetras la imagen con las esquinas detectadas
cv2.imshow('Algoritmo de deteccion de esquinas de Harris', imagen)

# Espera a que se pulse una tecla
cv2.waitKey(0)

# Libera recursos
cv2.destroyAllWindows()
