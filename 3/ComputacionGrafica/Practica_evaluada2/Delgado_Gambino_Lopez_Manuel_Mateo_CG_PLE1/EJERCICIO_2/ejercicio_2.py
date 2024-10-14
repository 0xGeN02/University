import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Configuración inicial
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
POINT_SIZE = 5
current_primitive = 'P'  # Inicializa la primitiva a tipo punto
current_color = (1.0, 0.0, 0.0)  # Inicializa el color a rojo
points = []  # Lista de vértices para la primitiva de tipo punto
lines = []  # Lista de vértices para la primitiva de tipo línea
triangles = []  # Lista de vértices para la primitiva de tipo triángulo

# Proyección ortográfica
def configure_projection():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0)

# Renderiza puntos
def render_points():
    glBegin(GL_POINTS)
    for point in points:
        glVertex2f(point[0], point[1])
    glEnd()

# Renderiza líneas
def render_lines():
    glBegin(GL_LINES)
    for line in lines:
        if len(line) == 2:
            glVertex2f(line[0][0], line[0][1])
            glVertex2f(line[1][0], line[1][1])
    glEnd()

# Renderiza triángulos
def render_triangles():
    glBegin(GL_TRIANGLES)
    for triangle in triangles:
        if len(triangle) == 3:
            glVertex2f(triangle[0][0], triangle[0][1])
            glVertex2f(triangle[1][0], triangle[1][1])
            glVertex2f(triangle[2][0], triangle[2][1])
    glEnd()

# Renderizar las primitivas
def render_primitives():
    glColor3f(*current_color)  # Aplica el color actual
    render_points()
    render_lines()
    render_triangles()

# Inicialización de la ventana
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
pygame.display.set_caption("DELGADO-GAMBINO LÓPEZ MANUEL MATEO")
glPointSize(POINT_SIZE)
configure_projection()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Selecciona el tipo de primitiva
            if event.key == pygame.K_p:
                current_primitive = 'P'  # Modo punto
            elif event.key == pygame.K_l:
                current_primitive = 'L'  # Modo línea
            elif event.key == pygame.K_t:
                current_primitive = 'T'  # Modo triángulo

            # Selecciona el color del dibujo
            elif event.key == pygame.K_r:
                current_color = (1.0, 0.0, 0.0)  # Rojo
            elif event.key == pygame.K_g:
                current_color = (0.0, 1.0, 0.0)  # Verde
            elif event.key == pygame.K_b:
                current_color = (0.0, 0.0, 1.0)  # Azul

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if current_primitive == 'P':
                points.append((mouse_x, mouse_y))
            elif current_primitive == 'L':
                if len(lines) == 0 or len(lines[-1]) == 2:
                    lines.append([(mouse_x, mouse_y)])
                else:
                    lines[-1].append((mouse_x, mouse_y))
            elif current_primitive == 'T':
                if len(triangles) == 0 or len(triangles[-1]) == 3:
                    triangles.append([(mouse_x, mouse_y)])
                else:
                    triangles[-1].append((mouse_x, mouse_y))

    # Limpiar la pantalla
    glClear(GL_COLOR_BUFFER_BIT)

    # Renderizar todas las primitivas
    render_primitives()

    # Intercambiar buffers
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()