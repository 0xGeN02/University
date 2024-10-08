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

#Dibujado de poligono
def dibuja_poligono(punto1, punto2, punto3, punto4):
    glLineWidth(2)
    glBegin(GL_POLYGON)
    glVertex2f(punto1[0], punto1[1])
    glVertex2f(punto2[0], punto2[1])
    glVertex2f(punto3[0], punto3[1])
    glVertex2f(punto4[0], punto4[1])
    glEnd()

inicializa()

# Parámetros de las transformaciones
s_x = 0.5  # Factor de escala en el eje X
s_y = 0.5  # Factor de escala en el eje Y
angulo = 45  # Ángulo de rotación en grados
t_x = 3.0  # Traslación en el eje X
t_y = 2.0  # Traslación en el eje Y

# Definimos los puntos 2D del triángulo
punto1 = np.array([2, 1])
punto2 = np.array([4, 1])
punto3 = np.array([4, 3])
punto4 = np.array([2, 3])

# Calculamos el baricentro del cuadrado
baricentro = np.array([(punto1[0] + punto2[0] + punto3[0] + punto4[0]) / 4,
                       (punto1[1] + punto2[1] + punto3[1] + punto4[1]) / 4])

# Matriz de traslación al origen
matriz_traslacion_origen = np.array([
    [1, 0, -baricentro[0]],
    [0, 1, -baricentro[1]],
    [0, 0, 1]
])

# Matriz de traslación de vuelta a la posición original
matriz_traslacion_vuelta = np.array([
    [1, 0, baricentro[0]],
    [0, 1, baricentro[1]],
    [0, 0, 1]
])

# Matriz de escalado uniforme
matriz_escalado = np.array([
    [s_x, 0, 0],
    [0, s_y, 0],
    [0, 0, 1]
])

# Composición de las transformaciones
matriz_compuesta = matriz_traslacion_vuelta @ matriz_escalado @ matriz_traslacion_origen

# Aplicamos la matriz compuesta a los puntos
punto1_transformado = transformacion(punto1, matriz_compuesta)
punto2_transformado = transformacion(punto2, matriz_compuesta)
punto3_transformado = transformacion(punto3, matriz_compuesta)
punto4_transformado = transformacion(punto4, matriz_compuesta)

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

    # Dibujamos el triángulo original
    dibuja_poligono(punto1, punto2, punto3, punto4)

    # Establecemos el magenta como color de primer plano
    glColor3f(1.0, 0.0, 1.0)

    # Dibujamos el triángulo transformado con la matriz compuesta
    dibuja_poligono(punto1_transformado, punto2_transformado, punto3_transformado, punto4_transformado)

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()