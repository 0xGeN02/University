# transformaciones.py
"""
Este fichero define funciones de transformación en el espacio 3D utilizando OpenGL.

Incluye funciones para aplicar traslaciones, rotaciones y escalado a objetos,
así como una función general que aplica todas estas transformaciones a un objeto dado.
"""

from OpenGL.GL import *  # Importa las funciones de OpenGL para transformación y renderizado
from OpenGL.GLU import *  # Importa las funciones de utilidad de OpenGL


def trasladar(x, y, z):
    """Aplica una traslación en el espacio 3D.

    Desplaza un objeto en el espacio 3D en función de las coordenadas especificadas.

    Args:
        x (float): Desplazamiento en el eje X.
        y (float): Desplazamiento en el eje Y.
        z (float): Desplazamiento en el eje Z.
    """
    glTranslatef(x, y, z)  # Aplica la traslación en el espacio 3D


def rotar(angulo, x, y, z):
    """
    Aplica una rotación en el espacio 3D.

    Rota un objeto en torno a un eje especificado (definido por x, y, z) en el espacio 3D.

    Args:
        angulo (float): Ángulo de rotación en grados.
        x (float): Componente X del eje de rotación.
        y (float): Componente Y del eje de rotación.
        z (float): Componente Z del eje de rotación.
    """
    glRotatef(angulo, x, y, z)  # Aplica la rotación en el espacio 3D


def escalar(sx, sy, sz):
    """Aplica un escalado en el espacio 3D.

    Modifica el tamaño de un objeto en el espacio 3D, escalándolo en los ejes X, Y y Z.

    Args:
        sx (float): Factor de escalado en el eje X.
        sy (float): Factor de escalado en el eje Y.
        sz (float): Factor de escalado en el eje Z.
    """
    glScalef(sx, sy, sz)  # Aplica el escalado en el espacio 3D


def transformar(t_x, t_y, t_z, angulo, eje_x, eje_y, eje_z, sx, sy, sz, objeto):
    """
    Aplica las transformaciones de traslación, rotación y escalado a un objeto y lo dibuja.

    La función encapsula las transformaciones en el espacio 3D para trasladar, rotar y escalar un objeto.
    Las transformaciones se aplican en orden de traslación, rotación y escalado.

    Args:
        t_x (float): Coordenada de traslación en X.
        t_y (float): Coordenada de traslación en Y.
        t_z (float): Coordenada de traslación en Z.
        angulo (float): Ángulo de rotación.
        eje_x (float): Componente X del eje de rotación.
        eje_y (float): Componente Y del eje de rotación.
        eje_z (float): Componente Z del eje de rotación.
        sx (float): Factor de escalado en X.
        sy (float): Factor de escalado en Y.
        sz (float): Factor de escalado en Z.
        objeto (callable): Función que representa el objeto a dibujar.

    """
    glPushMatrix()  # Guarda la matriz de transformación actual en la pila

    # Aplica las transformaciones en el orden de traslación, rotación y escalado
    trasladar(t_x, t_y, t_z)
    rotar(angulo, eje_x, eje_y, eje_z)
    escalar(sx, sy, sz)

    # Llama a la función que dibuja el objeto con las transformaciones aplicadas
    objeto()

    glPopMatrix()  # Restaura la matriz de transformación previa de la pila