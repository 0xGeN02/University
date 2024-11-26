import numpy as np

def actualizar_matrices(articulacion):
    """
    Calcula y actualiza las matrices de transformación local y global
    para una articulación y sus descendientes.

    Args:
        articulacion (Articulacion): La articulación cuya transformación se actualizará.
    """
    # Convierte el ángulo de la articulación a radianes para cálculos trigonométricos.
    angulo_rad = np.radians(articulacion.angulo)
    cos_theta = np.cos(angulo_rad)  # Calcula el coseno del ángulo.
    sin_theta = np.sin(angulo_rad)  # Calcula el seno del ángulo.

    # Crea la matriz de rotación local (2D extendida a 4x4 en coordenadas homogéneas).
    matriz_rotacion = np.array([
        [cos_theta, -sin_theta, 0, 0],
        [sin_theta,  cos_theta, 0, 0],
        [0,          0,         1, 0],
        [0,          0,         0, 1]
    ])

    # Crea la matriz de traslación local basada en el vector de desplazamiento r.
    matriz_traslacion = np.array([
        [1, 0, 0, articulacion.r[0]],  # Traslación en X
        [0, 1, 0, articulacion.r[1]],  # Traslación en Y
        [0, 0, 1, 0],                  # Sin traslación en Z
        [0, 0, 0, 1]                   # Coordenadas homogéneas
    ])

    # Combina la traslación y rotación para obtener la matriz de transformación local.
    articulacion.L = np.dot(matriz_traslacion, matriz_rotacion)

    # Si la articulación tiene un padre, calcular la matriz de transformación global
    # combinando la transformación del padre con la local. Si no, la local es la global.
    if articulacion.padre:
        articulacion.W = np.dot(articulacion.padre.W, articulacion.L)
    else:
        articulacion.W = articulacion.L

    # Llama recursivamente a los hijos de esta articulación para actualizar sus matrices.
    for hijo in articulacion.hijos:
        actualizar_matrices(hijo)
