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
pygame.display.set_caption("Ejercicio 1 Delgado-Gambino-Mateo")

#Bucle ejecucion
execute = True
while execute:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execute = False
