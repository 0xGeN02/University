# brief.py

import cv2
import numpy as np
import os

# Parámetros de los detectores y descriptores
NUMERO_PUNTOS = 500  # Número máximo de puntos clave a detectar
COLOR_RESALTE = (0, 255, 0)  # Verde en formato BGR

#Path de esta carpeta
PATH = os.path.dirname(os.path.abspath(__file__))
# Carga la imagen
imagen = cv2.imread(os.path.join(PATH, 'imagenes/uie.png'))

# Verifica que la imagen se haya cargado correctamente
if imagen is None:
    print("No se pudo cargar la imagen. Asegúrate de que el nombre y la ruta sean correctos.")
    exit()

# Convierte la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Inicializa el detector FAST
fast = cv2.FastFeatureDetector_create()

# Detecta los puntos clave usando FAST
keypoints = fast.detect(imagen_gris, None)

# Limita el número de puntos clave si es necesario
keypoints = sorted(keypoints, key=lambda x: -x.response)[:NUMERO_PUNTOS]

# Inicializa el extractor BRIEF
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

# Calcula los descriptores BRIEF para los puntos clave detectados
keypoints, descriptores = brief.compute(imagen_gris, keypoints)

# Dibuja los puntos clave en la imagen original
imagen_con_keypoints = cv2.drawKeypoints(imagen, keypoints, None, COLOR_RESALTE,
                                        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Muestra la imagen con los puntos clave detectados
cv2.imshow('Algoritmo BRIEF', imagen_con_keypoints)

# Espera a que se pulse una tecla y cierra las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
