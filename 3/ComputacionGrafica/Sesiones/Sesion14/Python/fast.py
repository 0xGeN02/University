# fast.py

import cv2
import os

# Parámetros de FAST
UMBRAL_DE_CORTE = 10  # Umbral para la detección de píxeles como esquinas
NON_MAX_SUPPRESSION = True  # Aplicar supresión de no máximos

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

# Inicializa el detector FAST
fast = cv2.FastFeatureDetector_create(threshold=UMBRAL_DE_CORTE, nonmaxSuppression=NON_MAX_SUPPRESSION)

# Detecta los puntos clave usando FAST
keypoints = fast.detect(imagen_gris, None)

# Dibuja los puntos clave en la imagen original
# Los puntos clave se marcan con círculos verdes
imagen_con_keypoints = cv2.drawKeypoints(imagen, keypoints, None, COLOR_RESALTE,
                                        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Muestra la imagen con los puntos clave detectados
cv2.imshow('Algoritmo FAST', imagen_con_keypoints)

# Espera a que se pulse una tecla y cierra las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
