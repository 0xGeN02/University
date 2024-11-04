# cubo_caras_independientes.py
'''
Este fichero contiene el modelo del cubo, incluyendo la definición de sus vértices,
sus caras mediante triángulos y una función para dibujar el cubo en OpenGL.
'''

from OpenGL.GL import *  # Importa las funciones de OpenGL necesarias para renderizar
from configuracion import *

# Definición de vértices del cubo, cada uno representado por coordenadas (x, y, z)
vertices = [
    {
        "posicion" : (+0.5, +0.5, +0.5),
        "color" : COLOR_ROJO
    },
    {
        "posicion" : (+0.5, +0.5, -0.5),
        "color" : COLOR_ROJO
    },
    {
        "posicion" : (+0.5, -0.5, +0.5),
        "color" : COLOR_ROJO
    },
    {
        "posicion" : (+0.5, +0.5, -0.5),
        "color" : COLOR_ROJO
    },
    {
        "posicion" : (+0.5, -0.5, +0.5),
        "color" : COLOR_ROJO
    },
    {
        "posicion" : (+0.5, -0.5, -0.5),
        "color" : COLOR_ROJO
    },
    {
        "posicion" : (+0.5, +0.5, +0.5),
        "color" : COLOR_AMARILLO
    },
    {
        "posicion" : (-0.5, +0.5, +0.5),
        "color" : COLOR_AMARILLO
    },
    {
        "posicion" : (+0.5, +0.5, -0.5),
        "color" : COLOR_AMARILLO
    },
    {
        "posicion" : (-0.5, +0.5, +0.5),
        "color" : COLOR_AMARILLO
    },
    {
        "posicion" : (+0.5, +0.5, -0.5),
        "color" : COLOR_AMARILLO
    },
    {
        "posicion" : (-0.5, +0.5, -0.5),
        "color" : COLOR_AMARILLO
    },
    {
        "posicion" : (-0.5, +0.5, +0.5),
        "color" : COLOR_AZUL
    },
    {
        "posicion" : (+0.5, +0.5, +0.5),
        "color" : COLOR_AZUL
    },
    {
        "posicion" : (+0.5, -0.5, +0.5),
        "color" : COLOR_AZUL
    },
    {
        "posicion" : (-0.5, +0.5, +0.5),
        "color" : COLOR_AZUL
    },
    {
        "posicion" : (-0.5, -0.5, +0.5),
        "color" : COLOR_AZUL
    },
    {
        "posicion" : (+0.5, -0.5, +0.5),
        "color" : COLOR_AZUL
    },
    {
        "posicion" : (-0.5, +0.5, -0.5),
        "color" : COLOR_NARANJA
    },
    {
        "posicion" : (-0.5, +0.5, +0.5),
        "color" : COLOR_NARANJA
    },
    {
        "posicion" : (-0.5, -0.5, -0.5),
        "color" : COLOR_NARANJA
    },
    {
        "posicion" : (-0.5, +0.5, +0.5),
        "color" : COLOR_NARANJA
    },
    {
        "posicion" : (-0.5, -0.5, -0.5),
        "color" : COLOR_NARANJA
    },
    {
        "posicion" : (-0.5, -0.5, +0.5),
        "color" : COLOR_NARANJA
    },
    {
        "posicion" : (-0.5, -0.5, +0.5),
        "color" : COLOR_BLANCO
    },
    {
        "posicion" : (+0.5, -0.5, +0.5),
        "color" : COLOR_BLANCO
    },
    {
        "posicion" : (-0.5, -0.5, -0.5),
        "color" : COLOR_BLANCO
    },
    {
        "posicion" : (+0.5, -0.5, +0.5),
        "color" : COLOR_BLANCO
    },
    {
        "posicion" : (-0.5, -0.5, -0.5),
        "color" : COLOR_BLANCO
    },
    {
        "posicion" : (+0.5, -0.5, -0.5),
        "color" : COLOR_BLANCO
    },
    {
        "posicion" : (+0.5, +0.5, -0.5),
        "color" : COLOR_VERDE
    },
    {
        "posicion" : (-0.5, +0.5, -0.5),
        "color" : COLOR_VERDE
    },
    {
        "posicion" : (-0.5, -0.5, -0.5),
        "color" : COLOR_VERDE
    },
    {
        "posicion" : (+0.5, +0.5, -0.5),
        "color" : COLOR_VERDE
    },
    {
        "posicion" : (+0.5, -0.5, -0.5),
        "color" : COLOR_VERDE
    },
    {
        "posicion" : (-0.5, -0.5, -0.5),
        "color" : COLOR_VERDE
    }
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
        glBegin(GL_TRIANGLES)  # Inicia el modo de renderizado de líneas en bucle
        for vertice_id in triangulo:
            glColor3f(*vertices[vertice_id]["color"])
            glVertex3fv(vertices[vertice_id]["posicion"])  # Primer vértice del triángulo
        glEnd()  # Finaliza el dibujo del triángulo actual
