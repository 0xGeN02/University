# Dimensiones del plano de proyección

PROJECTION_LEFT = -16
PROJECTION_RIGHT = 16
PROJECTION_BOTTOM = -12
PROJECTION_TOP = 12

# Límites de ángulos en grados para las articulaciones.
# Estos valores definen el rango permitido de movimiento para cada articulación.

ANGULO_MIN_HOMBRO = -90    # Ángulo de rotación mínimo del hombro.
ANGULO_MAX_HOMBRO = 45     # Ángulo de rotación máximo del hombro.

ANGULO_MIN_CODO = 0        # Ángulo de rotación mínimo del codo.
ANGULO_MAX_CODO = 135      # Ángulo de rotación máximo del codo.

ANGULO_MIN_MUNECA = -45    # Ángulo de rotación mínimo de la muñeca.
ANGULO_MAX_MUNECA = 45     # Ángulo de rotación máximo de la muñeca.

# Ángulos iniciales de las articulaciones.
ANGULO_INICIAL_HOMBRO = 0  # Ángulo inicial del hombro.
ANGULO_INICIAL_CODO = 0    # Ángulo inicial del codo.
ANGULO_INICIAL_MUNECA = 0  # Ángulo inicial de la muñeca.

# Incremento de ángulo para cada pulsación de tecla.
INCREMENTO_ANGULO = 2  # Cada pulsación ajusta el ángulo en 2 grados.

# Dimensiones de la pantalla de visualización (en píxeles).
ANCHO_PANTALLA = 800  # Ancho de la ventana.
ALTO_PANTALLA = 600   # Alto de la ventana.

# Definición de colores en formato RGB (valores entre 0.0 y 1.0).
COLOR_AZUL = (0.0, 0.0, 1.0)    # Azul
COLOR_BLANCO = (1.0, 1.0, 1.0)  # Blanco
COLOR_MAGENTA = (1.0, 0.0, 1.0) # Magenta
COLOR_NEGRO = (0.0, 0.0, 0.0)   # Negro
COLOR_ROJO = (1.0, 0.0, 0.0)    # Rojo
COLOR_VERDE = (0.0, 1.0, 0.0)   # Verde
