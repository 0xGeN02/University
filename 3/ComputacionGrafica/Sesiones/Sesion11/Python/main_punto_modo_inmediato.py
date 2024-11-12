import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from configuracion import *

PUNTO_X = 0.0
PUNTO_Y = 0.0
PUNTO_Z = 0.0

def inicializar_escena():
    # Inicializa Pygame
    pygame.init()
    # Crea la ventana gráfica
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    # Establece el título de la ventana
    pygame.display.set_caption('Dibujado de un punto en modo inmediato')
    # Configura la proyección en perspectiva
    gluPerspective(FOV, SCREEN_ASPECT_RATIO, NEAR_PLANE, FAR_PLANE)
    # Desplaza la cámara hacia atrás
    glTranslatef(0.0, 0.0, -5)
    # Establece el tamaño del punto
    glPointSize(TAMANO_PUNTO)

def dibujar_punto():
    # Inicia la definición de puntos
    glBegin(GL_POINTS)
    # Establece el color rojo
    glColor3f(*COLOR_ROJO)
    # Define la posición del punto en el centro
    glVertex3f(PUNTO_X, PUNTO_Y, PUNTO_Z)
    # Finaliza la definición de puntos
    glEnd()

inicializar_escena()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Limpia los buffer de color y profundidad
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Dibuja el punto
    dibujar_punto()

    # Intercambia los buffers
    pygame.display.flip()
    # Espera
    pygame.time.wait(int(MILLISECONDS_PER_SECOND / FPS))


