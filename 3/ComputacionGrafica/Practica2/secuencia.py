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

def dibuja_poligono(punto1, punto2, punto3, punto4):
    glLineWidth(2)
    glBegin(GL_POLYGON)
    glVertex2f(punto1[0], punto1[1])
    glVertex2f(punto2[0], punto2[1])
    glVertex2f(punto3[0], punto3[1])
    glVertex2f(punto4[0], punto4[1])
    glEnd()

inicializa()

# Definimos los parámetros de las transformaciones

# Parámetros del escalado
s_x = 1.0  # Factor de escala en el eje X
s_y = 1.0  # Factor de escala en el eje Y

# Parámetros de la rotación
angulo = 45  # Ángulo de rotación en grados

# Parámetros de la traslación
t_x = 0.0  # Traslación en el eje X
t_y = 0.0  # Traslación en el eje Y

# Definimos los puntos 2D
punto1 = np.array([2, 1])
punto2 = np.array([4, 1])
punto3 = np.array([4, 3])
punto4 = np.array([2, 3])

# Centro del objeto (punto medio del cuadrado)
centro_x = (punto1[0] + punto3[0]) / 2
centro_y = (punto1[1] + punto3[1]) / 2

# 1. Trasladamos el objeto al origen
punto1_transformado = transformacion(punto1, matriz_traslacion(-centro_x, -centro_y))
punto2_transformado = transformacion(punto2, matriz_traslacion(-centro_x, -centro_y))
punto3_transformado = transformacion(punto3, matriz_traslacion(-centro_x, -centro_y))
punto4_transformado = transformacion(punto4, matriz_traslacion(-centro_x, -centro_y))

# 2. Aplicamos la rotación sobre los puntos trasladados al origen
punto1_transformado = transformacion(punto1_transformado, matriz_rotacion(angulo))
punto2_transformado = transformacion(punto2_transformado, matriz_rotacion(angulo))
punto3_transformado = transformacion(punto3_transformado, matriz_rotacion(angulo))
punto4_transformado = transformacion(punto4_transformado, matriz_rotacion(angulo))

# 3. Trasladamos el objeto de vuelta a su posición original
punto1_transformado = transformacion(punto1_transformado, matriz_traslacion(centro_x, centro_y))
punto2_transformado = transformacion(punto2_transformado, matriz_traslacion(centro_x, centro_y))
punto3_transformado = transformacion(punto3_transformado, matriz_traslacion(centro_x, centro_y))
punto4_transformado = transformacion(punto4_transformado, matriz_traslacion(centro_x, centro_y))

# 4. Aplicamos el escalado sobre los puntos rotados y trasladados
punto1_transformado = transformacion(punto1_transformado, matriz_escalado(s_x, s_y))
punto2_transformado = transformacion(punto2_transformado, matriz_escalado(s_x, s_y))
punto3_transformado = transformacion(punto3_transformado, matriz_escalado(s_x, s_y))
punto4_transformado = transformacion(punto4_transformado, matriz_escalado(s_x, s_y))

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

    # Dibujamos el triángulo después de las transformaciones
    dibuja_poligono(punto1_transformado, punto2_transformado, punto3_transformado, punto4_transformado)

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()