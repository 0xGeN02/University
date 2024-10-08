# Importación de bibliotecas
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from utilidades import *
import numpy as np

# Inicialización de pygame
pygame.init()

# Configuración de la ventana
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)

# Configuración de la proyección
def inicializa():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Color de fondo: blanco
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-10, 10, -10, 10)


# Dibujado de líneas
def dibuja_linea(punto1, punto2):
    glLineWidth(5)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(punto1[0], punto1[1])
    glVertex2f(punto2[0], punto2[1])
    glEnd()

inicializa()

# Definimos los puntos 2D
punto1 = np.array([2, 1])
punto2 = np.array([4, 1])
punto3 = np.array([4, 3])
punto4 = np.array([2, 3])

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    glClear(GL_COLOR_BUFFER_BIT)
    dibuja_ejes()

    # Establecemos el azul como color de primer plano
    glColor3f(1.0, 1.0, 1.0)

    # Dibujamos las líneas
    dibuja_linea(punto1, punto2)
    dibuja_linea(punto2, punto3)
    dibuja_linea(punto3, punto4)
    dibuja_linea(punto4, punto1)

    pygame.display.flip()
    pygame.time.wait(100)