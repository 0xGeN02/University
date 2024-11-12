# Configuración de la ventana gráfica
SCREEN_WIDTH        = 1280                           # Anchura de la ventana gráfica
SCREEN_HEIGHT       = 720                           # Altura de la ventana gráfica
SCREEN_ASPECT_RATIO = SCREEN_WIDTH / SCREEN_HEIGHT  # Relación de aspecto de la ventana gráfica

# Configuración de la proyección
FOV         = 45    # (Field Of View) Campo o ángulo de vision desde el centro de la cámara.
NEAR_PLANE  = 0.1   # Distancia del plano más cercano a la cámara.
FAR_PLANE   = 50    # Distancia del plano más lejano a la cámara.

# Configuración del dibujo
TAMANO_PUNTO = 10

# Definición de colores
COLOR_ROJO      =  (1.0, 0.0, 0.0)     # Color rojo primario

# Configuración del bucle de renderizado
FPS = 60
MILLISECONDS_PER_SECOND = 1000.0    # Número de milisegundos en un segundo.

# Control del ratón
BOTON_IZQUIERDO_RATON = 1  # pygame.BUTTON_LEFT

# Sensibilidad y velocidades
SENSIBILIDAD_ROTACION = 0.1  # Ajustar según preferencia
SENSIBILIDAD_ZOOM = 0.5      # Ajustar según preferencia
INVERTIR_CONTROLES = -1       # 1 o -1 para invertir controles
VELOCIDAD_ROTACION = 50.0    # Grados por segundo
VELOCIDAD_ZOOM = 10.0        # Unidades por segundo

RADIO_MIN = 1.0
RADIO_MAX = 50.0