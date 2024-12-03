# cinematica.py

import numpy as np

def actualizar_matrices(articulacion):
    """
    Calcula y actualiza las matrices de transformación local y global
    para una articulación y sus descendientes.
    """
    angulo_rad = np.radians(articulacion.angulo)
    cos_theta = np.cos(angulo_rad)
    sin_theta = np.sin(angulo_rad)

    matriz_rotacion = np.array([
        [cos_theta, -sin_theta, 0, 0],
        [sin_theta,  cos_theta, 0, 0],
        [0,          0,         1, 0],
        [0,          0,         0, 1]
    ])

    matriz_traslacion = np.array([
        [1, 0, 0, articulacion.r[0]],
        [0, 1, 0, articulacion.r[1]],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    articulacion.L = np.dot(matriz_traslacion, matriz_rotacion)

    if articulacion.padre:
        articulacion.W = np.dot(articulacion.padre.W, articulacion.L)
    else:
        articulacion.W = articulacion.L

    for hijo in articulacion.hijos:
        actualizar_matrices(hijo)
