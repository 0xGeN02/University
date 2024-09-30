import numpy as np

# Función general para aplicar una transformación a un punto en coordenadas homogéneas
def transformacion(punto, matriz):
    # Convertimos el punto a coordenadas homogéneas
    punto_homogeneo = np.array([punto[0], punto[1], 1])

    # Aplicamos la matriz de transformación
    punto_transformado = np.dot(matriz, punto_homogeneo)

    # Retornamos el punto transformado sin la coordenada homogénea
    return punto_transformado[:2]

# Escala un punto en coordenadas homogéneas
def matriz_escalado(s_x, s_y):
    # Matriz de escalado homogénea 3x3
    return np.array([
        [s_x, 0,   0],
        [0,   s_y, 0],
        [0,   0,   1]
    ])

# Rotación de un punto en coordenadas homogéneas
def matriz_rotacion(angulo):
    # Convertir el ángulo de grados a radianes
    rad = np.radians(angulo)

    # Matriz de rotación homogénea 3x3
    return np.array([
        [np.cos(rad), -np.sin(rad), 0],
        [np.sin(rad), np.cos(rad),  0],
        [0,           0,            1]
    ])

# Traslación de un punto en coordenadas homogéneas
def matriz_traslacion(t_x, t_y):
    # Matriz de traslación homogénea 3x3
    return np.array([
        [1, 0, t_x],
        [0, 1, t_y],
        [0, 0, 1]
    ])

# Composición de transformaciones: escalado, rotación y traslación
def componer_transformaciones(s_x, s_y, angulo, t_x, t_y):
    # Crear las matrices de cada transformación
    escalado = matriz_escalado(s_x, s_y)
    rotacion = matriz_rotacion(angulo)
    traslacion = matriz_traslacion(t_x, t_y)

    # Multiplicamos las matrices: primero escalado, luego rotación, luego traslación
    matriz_compuesta = np.dot(traslacion, np.dot(rotacion, escalado))

    return matriz_compuesta