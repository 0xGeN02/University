# sift.py
import os
import cv2
import numpy as np

# Parámetros de SIFT
NUMERO_ESQUINAS = 0  # 0 significa que detectará todas las esquinas posibles
CONTRASTE_THRESHOLD = 0.04  # Umbral de contraste para filtrar puntos clave débiles
EDGE_THRESHOLD = 10  # Umbral para filtrar puntos clave en bordes
SIGMA = 1.6  # Desviación estándar para el filtro Gaussiano

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

# Inicializa el detector SIFT

sift = cv2.SIFT_create(nfeatures=NUMERO_ESQUINAS,
                       contrastThreshold=CONTRASTE_THRESHOLD,
                       edgeThreshold=EDGE_THRESHOLD,
                       sigma=SIGMA)

# Detecta los puntos clave y calcula los descriptores
keypoints, descriptores = sift.detectAndCompute(imagen_gris, None)

# Dibuja los puntos clave en la imagen original
imagen_con_keypoints = cv2.drawKeypoints(imagen, keypoints, None, COLOR_RESALTE,
                                        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Muestra la imagen con los puntos clave detectados
cv2.imshow('Algoritmo SIFT', imagen_con_keypoints)

# Espera a que se pulse una tecla y cierra las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
