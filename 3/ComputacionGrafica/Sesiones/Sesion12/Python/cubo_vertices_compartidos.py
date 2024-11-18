# cubo_indices.py
'''
Este fichero contiene el modelo del cubo utilizando vértices compartidos,
definición de sus caras mediante triángulos y una función para dibujar el cubo en OpenGL.
'''

from OpenGL.GL import *  # Importa las funciones de OpenGL necesarias para renderizar

# Definición de los vértices únicos del cubo, cada uno representado por coordenadas (x, y, z)
vertices = [
    (+0.5, +0.5, +0.5),  # Vértice 0
    (+0.5, +0.5, -0.5),  # Vértice 1
    (+0.5, -0.5, +0.5),  # Vértice 2
    (+0.5, -0.5, -0.5),  # Vértice 3
    (-0.5, +0.5, +0.5),  # Vértice 4
    (-0.5, +0.5, -0.5),  # Vértice 5
    (-0.5, -0.5, +0.5),  # Vértice 6
    (-0.5, -0.5, -0.5),  # Vértice 7
]

# Definición de triángulos.
triangulos = [
    # Cara R (Right): x = +0.5
    [0, 1, 2],
    [3, 2, 1],
    # Cara U (Up): y = +0.5
    [0, 4, 1],
    [5, 1, 4],
    # Cara F (Front): z = +0.5
    [0, 2, 4],
    [6, 4, 2],
    # Cara L (Left): x = -0.5
    [4, 5, 6],
    [7, 6, 5],
    # Cara D (Down): y = -0.5
    [2, 3, 6],
    [7, 6, 3],
    # Cara B (Back): z = -0.5
    [1, 5, 3],
    [7, 3, 5],
]

def cubo():
    """Dibuja el modelo del cubo utilizando líneas para cada triángulo.

    Recorre la lista de triángulos y dibuja cada uno en el espacio 3D utilizando
    la función GL_LINE_LOOP de OpenGL, que conecta los tres vértices de cada triángulo
    con líneas para delinear la estructura del cubo.
    """
    for triangulo in triangulos:
        glBegin(GL_LINE_LOOP)  # Inicia el modo de renderizado de líneas en bucle
        glVertex3fv(vertices[triangulo[0]])  # Primer vértice del triángulo
        glVertex3fv(vertices[triangulo[1]])  # Segundo vértice del triángulo
        glVertex3fv(vertices[triangulo[2]])  # Tercer vértice del triángulo
        glEnd()  # Finaliza el dibujo del triángulo actual

