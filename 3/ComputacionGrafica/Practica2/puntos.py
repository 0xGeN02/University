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


# Dibujado de puntos
def dibuja_punto(punto, color):
    glPointSize(10)
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    glVertex2f(punto[0], punto[1])
    glEnd()

inicializa()

# Definimos los puntos 2D
punto1 = np.array([2, 1])
color1 = [1, 0, 0]  # Rojo
punto2 = np.array([4, 1])
color2 = [0, 1, 0]  # Verde
punto3 = np.array([3, 3])
color3 = [0, 0, 1]  # Azul

# Puntos extra
punto4 = np.array([-1, 2])
color4 = [1, 1, 0]  # Amarillo
punto5 = np.array([5, -3])
color5 = [1, 0, 1]  # Magenta
punto6 = np.array([-4, -4])
color6 = [0, 1, 1]  # Cian

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    glClear(GL_COLOR_BUFFER_BIT)
    dibuja_ejes()

    # Establecemos el azul como color de primer plano
    glColor3f(0.0, 0.0, 1.0)

    # Dibujamos los puntos con sus colores respectivos
    dibuja_punto(punto1, color1)
    dibuja_punto(punto2, color2)
    dibuja_punto(punto3, color3)
    dibuja_punto(punto4, color4)
    dibuja_punto(punto5, color5)
    dibuja_punto(punto6, color6)

    pygame.display.flip()
    pygame.time.wait(100)