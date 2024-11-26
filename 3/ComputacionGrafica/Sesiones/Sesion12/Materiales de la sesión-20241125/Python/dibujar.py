from OpenGL.GL import *  # Importa OpenGL.
import numpy as np


def dibujar_arbol_articulaciones(articulacion_raiz):
    """
    Dibuja el árbol jerárquico de articulaciones a partir de una articulación raíz.

    Args:
        articulacion_raiz (Articulacion): Articulación principal del sistema.
    """
    glPushMatrix()  # Guarda el estado actual de la pila de transformaciones.
    # Multiplica por la matriz global de transformación de la articulación raíz.
    glMultMatrixf(articulacion_raiz.W.T)
    # Dibuja la articulación raíz.
    dibujar_articulacion(articulacion_raiz)
    glPopMatrix()  # Restaurar el estado de la pila de transformaciones.


def dibujar_articulacion(articulacion):
    """
    Dibuja una articulación y sus hijos de forma recursiva.

    Args:
        articulacion (Articulacion): La articulación a dibujar.
    """
    # Establece el color de la articulación.
    glColor3f(*articulacion.color)
    glBegin(GL_LINES)  # Comienza a dibujar líneas.
    # Dibuja una línea desde el origen (0, 0, 0) hasta el vector de desplazamiento r.
    glVertex3f(0, 0, 0)
    glVertex3f(articulacion.r[0], articulacion.r[1], 0)
    glEnd()  # Finaliza el dibujado de líneas.

    # Aplica la transformación local para posicionar a los hijos.
    glPushMatrix()  # Guarda el estado actual de la pila de transformaciones.
    glMultMatrixf(articulacion.L.T.astype(np.float32))  # Multiplica por la matriz local de la articulación.
    # Dibuja recursivamente los hijos de la articulación actual.
    for hijo in articulacion.hijos:
        dibujar_articulacion(hijo)
    glPopMatrix()  # Restaura el estado de la pila de transformaciones.
