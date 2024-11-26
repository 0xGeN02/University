# configuracion.py

import numpy as np

# Número de cámara predeterminado (0 para la cámara predeterminada)
NUMERO_CAMARA = 0

# Resolución de la cámara
ANCHURA_FRAME = 640
ALTURA_FRAME = 480

# Fuente de video
FUENTE_VIDEO = 'camara'  # Opciones: 'camara' o 'video'

# Ruta al archivo de video (si FUENTE_VIDEO es 'video')
RUTA_VIDEO = 'video.avi'

# Dimensiones de las imágenes en píxeles
ANCHURA_IMAGEN_PX = 200
ALTURA_IMAGEN_PX = 200

# Tamaño de los marcadores impresos (m)
TAMANO_MARCADOR = 1  # Unitario para facilitar transformaciones

# Título de la ventana
TITULO_VENTANA = 'Camara'  # Cambia a 'Captura' u otro título según prefieras

# Carpeta imágenes
CARPETA_IMAGENES = "imagenes"

# Mapeo de IDs de marcadores a rutas de modelos 3D y sus transformaciones
MODELOS_MARCADORES = {
    0: {  # ID del marcador ArUco
        "ruta_modelo": "modelos/cilindro.obj",
        "traslacion": {"t_x": 0.0, "t_y": 0.5, "t_z": 0.0},
        "escala": {"s_x": 1, "s_y": 1, "s_z": 1},
        "color": (0, 0, 255)  # Formato BGR
    },
}

# Calibración de la cámara
CAMERA_MATRIX = np.array([[800, 0, 320],
                               [0, 800, 240],
                               [0, 0, 1]], dtype=np.float32)

DIST_COEFFS = np.zeros((5, 1))