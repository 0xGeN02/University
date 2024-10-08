# Importación de bibliotecas
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from utilidades import *
from transformaciones import *
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

# Dibujado de polígonos
def dibuja_poligono(punto1, punto2, punto3, punto4):
    glLineWidth(2)
    glBegin(GL_POLYGON)
    glVertex2f(punto1[0], punto1[1])
    glVertex2f(punto2[0], punto2[1])
    glVertex2f(punto3[0], punto3[1])
    glVertex2f(punto4[0], punto4[1])
    glEnd()


inicializa()

# Definimos el factor de escalado
s_x = 2.0  # Factor de escala en el eje X
s_y = -0.5  # Factor de escala en el eje Y

# Definimos los puntos 2D
punto1 = np.array([2, 1])
punto2 = np.array([4, 1])
punto3 = np.array([4, 3])
punto4 = np.array([2, 3])

# Aplicamos la matriz de escalado
punto1_escalado = transformacion(punto1, matriz_escalado(s_x, s_y))
punto2_escalado = transformacion(punto2, matriz_escalado(s_x, s_y))
punto3_escalado = transformacion(punto3, matriz_escalado(s_x, s_y))
punto4_escalado = transformacion(punto4, matriz_escalado(s_x, s_y))

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

    # Dibujamos el poligono
    dibuja_poligono(punto1, punto2, punto3, punto4)

    # Establecemos el magenta como color de primer plano
    glColor3f(1.0, 0.0, 1.0)

    # Dibujamos el punto
    dibuja_poligono(punto1_escalado, punto2_escalado, punto3_escalado, punto4_escalado)

    pygame.display.flip()
    pygame.time.wait(100)