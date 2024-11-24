# cubo_normales.py
'''
Este fichero contiene el modelo del cubo, incluyendo la definición de sus vértices,
sus caras mediante triángulos, normales para cada cara y una función para dibujar el cubo en OpenGL con iluminación.
'''

from OpenGL.GL import *  # Importa las funciones de OpenGL necesarias para renderizar
from configuracion import *

# Definición de vértices del cubo, cada uno representado por coordenadas (x, y, z)
vertices = [
    (+0.5, +0.5, +0.5), # Vértice 0, esquina superior derecha frontal
    (+0.5, +0.5, -0.5), # Vértice 1, esquina superior derecha trasera
    (+0.5, -0.5, +0.5), # Vértice 2, esquina inferior derecha frontal
    (+0.5, -0.5, -0.5), # Vértice 3, esquina inferior derecha trasera
    (-0.5, +0.5, +0.5), # Vértice 4, esquina superior izquierda frontal
    (-0.5, +0.5, -0.5), # Vértice 5, esquina superior izquierda trasera
    (-0.5, -0.5, +0.5), # Vértice 6, esquina inferior izquierda frontal
    (-0.5, -0.5, -0.5), # Vértice 7, esquina inferior izquierda trasera
]

# Definición de triángulos, cada triángulo se define por índices de los vértices
triangulos = [
    # Cara R (Right): x = +0.5
    [0, 1, 2], [1, 3, 2],
    # Cara L (Left): x = -0.5
    [4, 5, 6], [5, 7, 6],
    # Cara U (Up): y = +0.5
    [0, 1, 4], [1, 5, 4],
    # Cara D (Down): y = -0.5
    [2, 3, 6], [3, 7, 6],
    # Cara F (Front): z = +0.5
    [0, 2, 4], [2, 6, 4],
    # Cara B (Back): z = -0.5
    [1, 3, 5], [3, 7, 5],
]

# Definición de normales
normales = [
    # Cara R (Right): x = +0.5
    (1, 0, 0), (1, 0, 0),
    # Cara L (Left): x = -0.5
    (-1, 0, 0), (-1, 0, 0),
    # Cara U (Up): y = +0.5
    (0, 1, 0), (0, 1, 0),
    # Cara D (Down): y = -0.5
    (0, -1, 0), (0, -1, 0),
    # Cara F (Front): z = +0.5
    (0, 0, 1), (0, 0, 1),
    # Cara B (Back): z = -0.5
    (0, 0, -1), (0, 0, -1),
]

def cubo():
    """Dibuja el modelo del cubo utilizando triángulos con iluminación."

    Recorre la lista de triángulos y dibuja cada uno en el espacio 3D utilizando
    la función GL_TRIANGLES de OpenGL, que conecta los tres vértices de cada triángulo.
    """
    for i in range(len(triangulos)):
        glBegin(GL_TRIANGLES)

        # Asigna la normal a cada triángulo
        glNormal3fv(normales[i])

        for indice in triangulos[i]:
            glVertex3fv(vertices[indice])  # Define cada uno de los vértices del triángulo
        glEnd()


