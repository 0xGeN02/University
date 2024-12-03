# orb.py

import cv2
import numpy as np
import os

# Parámetros de ORB
NUMERO_PUNTOS = 500  # Número máximo de puntos clave a detectar
NIVEL_PIRAMIDE = 8    # Número de niveles en la pirámide de escala
UMBRAL_CORTE = 31     # Umbral para la detección de características

# Color de resalte de los puntos clave, en BGR
COLOR_RESALTE = (0, 255, 0)  # Verde

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

# Inicializa el detector ORB
orb = cv2.ORB_create(nfeatures=NUMERO_PUNTOS, nlevels=NIVEL_PIRAMIDE, edgeThreshold=UMBRAL_CORTE)

# Detecta los puntos clave y calcula los descriptores
keypoints, descriptores = orb.detectAndCompute(imagen_gris, None)

# Dibuja los puntos clave en la imagen original
# Los puntos clave se marcan con círculos verdes
imagen_con_keypoints = cv2.drawKeypoints(imagen, keypoints, None, COLOR_RESALTE,
                                        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Muestra la imagen con los puntos clave detectados
cv2.imshow('Puntos Clave de ORB', imagen_con_keypoints)

# Espera a que se pulse una tecla y cierra las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
