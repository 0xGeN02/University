# utilidades.py

"""
Este archivo contiene funciones de utilidad para dibujar elementos auxiliares en una
escena 3D, como ejes, flechas en los extremos de los ejes y una rejilla de referencia.
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from configuracion import *


def dibujar_elementos_auxiliares(ejes=False, rejilla=False):
    """Dibuja elementos auxiliares en la escena, como ejes y rejilla.

    Args:
        ejes (bool): Si es True, dibuja los ejes.
        rejilla (bool): Si es True, dibuja la rejilla.
    """
    if ejes:
        dibujar_ejes()
    if rejilla:
        dibujar_rejilla()


def dibujar_ejes():
    """Dibuja los ejes del mundo y sus puntas de flecha en cada extremo."""
    # Dibuja los ejes en X, Y y Z
    dibujar_eje_con_flecha(EJE_X_MIN, 0, 0, EJE_X_MAX, 0, 0, COLOR_EJE_X, rotacion=(90, 0, 1, 0))
    dibujar_eje_con_flecha(0, EJE_Y_MIN, 0, 0, EJE_Y_MAX, 0, COLOR_EJE_Y, rotacion=(-90, 1, 0, 0))
    dibujar_eje_con_flecha(0, 0, EJE_Z_MIN, 0, 0, EJE_Z_MAX, COLOR_EJE_Z)


def dibujar_eje_con_flecha(x1, y1, z1, x2, y2, z2, color, rotacion=None):
    """Dibuja un eje con una flecha en el extremo positivo.

    Args:
        x1, y1, z1: Coordenadas de inicio del eje.
        x2, y2, z2: Coordenadas de fin del eje.
        color: Color del eje y la flecha.
        rotacion: Tupla con los parámetros de rotación (angulo, x, y, z) para la flecha.
    """
    dibujar_segmento(x1, y1, z1, x2, y2, z2, color)
    glColor3f(*color)
    glPushMatrix()
    glTranslatef(x2, y2, z2)  # Posiciona en el extremo positivo del eje
    if rotacion:
        glRotatef(*rotacion)  # Aplica la rotación necesaria para orientar la flecha
    dibujar_cono()
    glPopMatrix()


def dibujar_segmento(x1, y1, z1, x2, y2, z2, color):
    """Dibuja un segmento de línea en 3D.

    Args:
        x1, y1, z1 (float): Coordenadas de inicio del segmento.
        x2, y2, z2 (float): Coordenadas de fin del segmento.
        color (tuple): Color en formato RGB.
    """
    glBegin(GL_LINES)
    glColor3f(*color)
    glVertex3f(x1, y1, z1)
    glVertex3f(x2, y2, z2)
    glEnd()


def dibujar_cono():
    """Dibuja un cono que representa la punta de una flecha de un eje."""
    cone = gluNewQuadric()
    gluCylinder(cone,
                EJE_FLECHA_BASE,
                EJE_FLECHA_PUNTA,
                EJE_FLECHA_LONGITUD,
                EJE_FLECHA_REBANADAS,
                EJE_FLECHA_PILAS)


def dibujar_rejilla():
    """Dibuja una rejilla en el plano XZ utilizando líneas."""
    glColor3f(*REJILLA_COLOR)
    glBegin(GL_LINES)
    for i in range(-REJILLA_TAMANO, REJILLA_TAMANO + 1):
        # Líneas paralelas al eje X
        dibujar_linea(-REJILLA_TAMANO, 0, i, REJILLA_TAMANO, 0, i)
        # Líneas paralelas al eje Z
        dibujar_linea(i, 0, -REJILLA_TAMANO, i, 0, REJILLA_TAMANO)
    glEnd()


def dibujar_linea(x1, y1, z1, x2, y2, z2):
    """Dibuja una línea entre dos puntos.

    Args:
        x1, y1, z1 (float): Coordenadas del primer punto.
        x2, y2, z2 (float): Coordenadas del segundo punto.
    """
    glVertex3f(x1 * REJILLA_PASO, y1, z1 * REJILLA_PASO)
    glVertex3f(x2 * REJILLA_PASO, y2, z2 * REJILLA_PASO)
