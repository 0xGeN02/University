# surf.py
import os
import cv2

# Parámetros de SURF
HESSIAN_THRESHOLD = 400  # Umbral de Hessian para filtrar puntos clave
NO_OCTAVAS = 4            # Número de octavas en la pirámide de escalas
NO_INTERVALOS = 2         # Número de intervalos por octava

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

# Inicializa el detector SURF
surf = cv2.xfeatures2d.SURF_create(hessianThreshold=HESSIAN_THRESHOLD,
                                   nOctaves=NO_OCTAVAS,
                                   nOctaveLayers=NO_INTERVALOS)

# Detecta los puntos clave y calcula los descriptores
keypoints, descriptores = surf.detectAndCompute(imagen_gris, None)

# Dibuja los puntos clave en la imagen original
imagen_con_keypoints = cv2.drawKeypoints(imagen, keypoints, None, COLOR_RESALTE,
                                        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Muestra la imagen con los puntos clave detectados
cv2.imshow('Puntos Clave de SURF', imagen_con_keypoints)

# Espera a que se pulse una tecla y cierra las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
