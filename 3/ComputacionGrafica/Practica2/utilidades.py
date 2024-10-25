# Importación de bibliotecas
from OpenGL.GL import *

# Función para dibujar los ejes X e Y
def dibuja_ejes():
    glLineWidth(1)
    glBegin(GL_LINES)

    # Eje X (color rojo)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-10, 0)
    glVertex2f(10, 0)

    # Eje Y (color verde)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0, -10)
    glVertex2f(0, 10)

    glEnd()