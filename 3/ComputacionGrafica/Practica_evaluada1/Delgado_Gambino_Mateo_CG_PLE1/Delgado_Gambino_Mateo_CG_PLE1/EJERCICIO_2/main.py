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
pygame.display.set_caption("Ejercicio 2 Delgado-Gambino-Mateo")

#Inicializacion de OpenGL
def initialize():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)

def dibuja():
    glPointSize(20)
    glBegin(GL_POINTS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(320, 240)
    glEnd()

#Execute
initialize()
#Bucle ejecucion
execute = True
while execute:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execute = False

    dibuja()
    pygame.display.flip()
    pygame.time.wait(20)
