import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

#Dimensiones de la ventana
width=800
height=600

#Inicializacion de la ventana
display = (width,height)
screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("Ejercicio 3 Delgado-Gambino-Mateo")

#Inicializacion de OpenGL
def initialize():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 300, 0, 200)

def dibuja():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(20)
    glBegin(GL_POINTS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(pos_x, pos_y)
    glEnd()

#Execute
initialize()

#Posicion inicial
pos_x = 150
pos_y = 100

#Bucle ejecucion
execute = True
while execute:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execute = False

    # Manejo de movimiento
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        pos_x -= 1
    if keys[K_RIGHT]:
        pos_x += 1
    if keys[K_UP]:
        pos_y += 1
    if keys[K_DOWN]:
        pos_y -= 1

    dibuja()
    pygame.display.flip()
    pygame.time.wait(1)
