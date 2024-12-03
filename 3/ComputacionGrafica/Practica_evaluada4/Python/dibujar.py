# dibujar.py

from OpenGL.GL import *
import numpy as np
from configuracion import *

def dibujar_arbol_articulaciones(articulacion_raiz, articulacion_seleccionada):
    """
    Dibuja el árbol jerárquico de articulaciones a partir de una articulación raíz.
    """
    glPushMatrix()
    dibujar_articulacion(articulacion_raiz, articulacion_seleccionada)
    glPopMatrix()

def dibujar_articulacion(articulacion, articulacion_seleccionada):
    """
    Dibuja una articulación y sus hijos de forma recursiva.
    """
    # Determina el color de la articulación
    if articulacion.padre is articulacion_seleccionada:
        glColor3f(*COLOR_ARTICULACION_SELECCIONADA)
    else:
        if (articulacion.padre):
            glColor3f(*(articulacion.padre.color))  # Usar el color de la articulación
    if articulacion.padre and articulacion.padre.angulo_max == 0 and articulacion.padre.angulo_min == 0:
        glColor3f(*COLOR_NEGRO)

    if articulacion.padre:
        # Dibuja un círculo para la articulación
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(0, 0)  # Centro del círculo
        num_segmentos = 20
        for i in range(num_segmentos + 1):
            angulo = 2 * np.pi * i / num_segmentos
            x = RADIO_CIRCULO * np.cos(angulo)
            y = RADIO_CIRCULO * np.sin(angulo)
            glVertex2f(x, y)
        glEnd()

        # Dibuja la conexión con el padre (si existe)
        glColor3f(*COLOR_NEGRO)  # Negro para las líneas
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(articulacion.r[0], articulacion.r[1], 0)
        glEnd()

    glPushMatrix()
    glMultMatrixf(articulacion.L.T.astype(np.float32))
    for hijo in articulacion.hijos:
        dibujar_articulacion(hijo, articulacion_seleccionada)
    glPopMatrix()
