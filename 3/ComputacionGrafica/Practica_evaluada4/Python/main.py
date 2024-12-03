# main.py

from usuario import manejar_eventos, manejar_teclas_polling
from dibujar import *
from esqueleto import *

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Inicialización de Pygame y OpenGL
pygame.init()
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Delgado-Gambino López manuel Mateo - Práctica 4')

glClearColor(*COLOR_BLANCO, 1.0)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(PROJECTION_LEFT, PROJECTION_RIGHT, PROJECTION_BOTTOM, PROJECTION_TOP)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glLineWidth(5)

# Configura el esqueleto
raiz, articulaciones = configurar_esqueleto()

# Inicializa la articulación seleccionada
articulacion_seleccionada = raiz

ejecutando = True
reloj = pygame.time.Clock()

while ejecutando:
    # Manejar eventos de teclas y ratón
    ejecutando, articulacion_seleccionada = manejar_eventos(articulacion_seleccionada, articulaciones)

    # Manejar teclas de movimiento (arriba y abajo)
    articulacion_seleccionada = manejar_teclas_polling(articulacion_seleccionada)

    # Actualizar matrices de transformación
    actualizar_matrices(raiz)

    # Limpiar la pantalla y dibujar el sistema
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    dibujar_arbol_articulaciones(raiz, articulacion_seleccionada)

    # Intercambia buffers y limita a 60 FPS
    pygame.display.flip()
    reloj.tick(FPS)
