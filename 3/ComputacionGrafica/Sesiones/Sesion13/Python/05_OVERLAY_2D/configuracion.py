# configuracion.py

import numpy as np

# Configuración para la Aplicación 2: OVERLAY 2D

# Número de cámara predeterminado (0 para la cámara predeterminada)
NUMERO_CAMARA = 0

# Resolución de la cámara
ANCHURA_FRAME = 640
ALTURA_FRAME = 480

# Fuente de video
FUENTE_VIDEO = 'camara'  # Opciones: 'camara' o 'video'

# Ruta al archivo de video (si FUENTE_VIDEO es 'video')
RUTA_VIDEO = 'video.avi'

# Dimensiones de las imágenes en píxeles (para overlays)
ANCHURA_IMAGEN_PX = 200
ALTURA_IMAGEN_PX = 200

# Tamaño de los marcadores impresos (m)
TAMANO_MARCADOR = 1  # Unitario para facilitar transformaciones

# Título de la ventana
TITULO_VENTANA = 'Overlay 2D'

# Carpeta de imágenes overlay
CARPETA_OVERLAY = "overlay"

# Mapeo de IDs de marcadores a rutas de imágenes overlay
MODELOS_MARCADORES = {
    0: {  # ID del marcador ArUco
        "ruta_overlay": "imagen_1.png",
    }
}

# Calibración de la cámara
CAMERA_MATRIX = np.array([[800, 0, 320],
                               [0, 800, 240],
                               [0, 0, 1]], dtype=np.float32)

DIST_COEFFS = np.zeros((5, 1))
