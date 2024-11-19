# cubo_caras_independientes.py
'''
Este fichero contiene el modelo del cubo, incluyendo la definición de sus vértices,
sus caras mediante triángulos y una función para dibujar el cubo en OpenGL.
'''

from OpenGL.GL import *  # Importa las funciones de OpenGL necesarias para renderizar

# Definición de vértices del cubo, cada uno representado por coordenadas (x, y, z)
vertices = [
    (+0.5, +0.5, +0.5), # Vértice 0, esquina superior derecha frontal
    (+0.5, +0.5, -0.5), # Vértice 1, esquina superior derecha trasera
    (+0.5, -0.5, +0.5), # Vértice 2, esquina inferior derecha frontal
    (+0.5, +0.5, -0.5), # Vértice 3, repetido para definir otra cara
    (+0.5, -0.5, +0.5), # Vértice 4, repetido para definir otra cara
    (+0.5, -0.5, -0.5), # Vértice 5, esquina inferior derecha trasera
    (+0.5, +0.5, +0.5), # Vértice 6, repetido para otra cara
    (-0.5, +0.5, +0.5), # Vértice 7, esquina superior izquierda frontal
    (+0.5, +0.5, -0.5), # Vértice 8, repetido para otra cara
    (-0.5, +0.5, +0.5), # Vértice 9, repetido para otra cara
    (+0.5, +0.5, -0.5), # Vértice 10, repetido para otra cara
    (-0.5, +0.5, -0.5), # Vértice 11, esquina superior izquierda trasera
    (-0.5, +0.5, +0.5), # Vértice 12, repetido para otra cara
    (+0.5, +0.5, +0.5), # Vértice 13, repetido para otra cara
    (+0.5, -0.5, +0.5), # Vértice 14, repetido para otra cara
    (-0.5, +0.5, +0.5), # Vértice 15, repetido para otra cara
    (-0.5, -0.5, +0.5), # Vértice 16, esquina inferior izquierda frontal
    (+0.5, -0.5, +0.5), # Vértice 17, repetido para otra cara
    (-0.5, +0.5, -0.5), # Vértice 18, repetido para otra cara
    (-0.5, +0.5, +0.5), # Vértice 19, repetido para otra cara
    (-0.5, -0.5, -0.5), # Vértice 20, esquina inferior izquierda trasera
    (-0.5, +0.5, +0.5), # Vértice 21, repetido para otra cara
    (-0.5, -0.5, -0.5), # Vértice 22, repetido para otra cara
    (-0.5, -0.5, +0.5), # Vértice 23, repetido para otra cara
    (-0.5, -0.5, +0.5), # Vértice 24, repetido para otra cara
    (+0.5, -0.5, +0.5), # Vértice 25, repetido para otra cara
    (-0.5, -0.5, -0.5), # Vértice 26, repetido para otra cara
    (+0.5, -0.5, +0.5), # Vértice 27, repetido para otra cara
    (-0.5, -0.5, -0.5), # Vértice 28, repetido para otra cara
    (+0.5, -0.5, -0.5), # Vértice 29, esquina inferior derecha trasera
    (+0.5, +0.5, -0.5), # Vértice 30, repetido para otra cara
    (-0.5, +0.5, -0.5), # Vértice 31, repetido para otra cara
    (-0.5, -0.5, -0.5), # Vértice 32, repetido para otra cara
    (+0.5, +0.5, -0.5), # Vértice 33, repetido para otra cara
    (+0.5, -0.5, -0.5), # Vértice 34, repetido para otra cara
    (-0.5, -0.5, -0.5), # Vértice 35, repetido para otra cara
]

# Definición de triángulos, cada triángulo se define por índices de los vértices
triangulos = [
    # Cara R (Right): x = +0.5
    [ 0,  1,  2], # Triángulo 0
    [ 3,  4,  5], # Triángulo 1
    # Cara U (Up): y = +0.5
    [ 6,  7,  8],  # Triángulo 2
    [ 9, 10, 11],  # Triángulo 3
    # Cara F (Front): z = +0.5
    [12, 13, 14],  # Triángulo 4
    [15, 16, 17],  # Triángulo 5
    # Cara L (Left): x = -0.5
    [18, 19, 20],  # Triángulo 6
    [21, 22, 23],  # Triángulo 7
    # Cara D (Down): y = -0.5
    [24, 25, 26],  # Triángulo 8
    [27, 28, 29],  # Triángulo 9
    # Cara B (Back): z = -0.5
    [30, 31, 32],  # Triángulo 10
    [33, 34, 35],  # Triángulo 11
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
        glVertex3fv(vertices[triangulo[0]])  # Primer vértice del triángulo
        glVertex3fv(vertices[triangulo[1]])  # Segundo vértice del triángulo
        glVertex3fv(vertices[triangulo[2]])  # Tercer vértice del triángulo
        glEnd()  # Finaliza el dibujo del triángulo actual
