from configuracion import *  # Importa los parámetros de configuración.
from usuario import *        # Importa las funciones relacionadas con los eventos de usuario.
from articulacion import *   # Importa la clase Articulacion.
from cinematica import *     # Importa las funciones para actualizar matrices de transformación.
from dibujar import *        # Importa las funciones de dibujo.

import pygame                # Importa Pygame
from pygame.locals import *  # Importa las constantes de Pygame en el espacio de nombres de la aplicación.
from OpenGL.GL import *      # Importa OpenGL
from OpenGL.GLU import *     # Importa GLU

# Inicializa Pygame y crea la ventana.
pygame.init()
pantalla = pygame.display.set_mode(
    (ANCHO_PANTALLA, ALTO_PANTALLA), DOUBLEBUF | OPENGL)  # Configura de la ventana de OpenGL.
pygame.display.set_caption('S12')  # Título de la ventana.

# Establece el color de fondo (blanco).
glClearColor(*COLOR_BLANCO, 1.0)

# Configura una proyección ortográfica (visualización 2D).
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(PROJECTION_LEFT, PROJECTION_RIGHT, PROJECTION_BOTTOM, PROJECTION_TOP)  # Define los límites del plano 2D.
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Aumentar el grosor de las líneas para mejorar la visibilidad.
glLineWidth(5)

# Crea las articulaciones.
hombro = Articulacion('hombro', angulo=ANGULO_INICIAL_HOMBRO,
                      angulo_min=ANGULO_MIN_HOMBRO, angulo_max=ANGULO_MAX_HOMBRO,
                      r=[0, 0], color=COLOR_NEGRO)

codo = Articulacion('codo', padre=hombro, angulo=ANGULO_INICIAL_CODO,
                    angulo_min=ANGULO_MIN_CODO, angulo_max=ANGULO_MAX_CODO,
                    r=[5, 0], color=COLOR_ROJO)

muneca = Articulacion('muneca', padre=codo, angulo=ANGULO_INICIAL_MUNECA,
                      angulo_min=ANGULO_MIN_MUNECA, angulo_max=ANGULO_MAX_MUNECA,
                      r=[4, 0], color=COLOR_VERDE)

nudillo = Articulacion(nombre='mano', padre=muneca, angulo=0,
                       r=[2, 0], color=COLOR_AZUL)

# Inicializa las matrices de transformación.
actualizar_matrices(hombro)

# Estado inicial: articulación seleccionada y control del bucle principal.
segmento_seleccionado = hombro  # Seleccionar inicialmente el hombro.
ejecutando = True               # Control del bucle principal.
reloj = pygame.time.Clock()     # Para limitar la frecuencia de cuadros.

# Bucle principal.
while ejecutando:
    # Manejar eventos de usuario (teclado, ratón, etc.).
    ejecutando, segmento_seleccionado = manejar_eventos(
        segmento_seleccionado, hombro, codo, muneca)

    # Actualizar las matrices de transformación según los ángulos actuales.
    actualizar_matrices(hombro)

    # Limpiar la pantalla.
    glClear(GL_COLOR_BUFFER_BIT)
    # Reiniciar la matriz de transformaciones.
    glLoadIdentity()
    # Dibujar el árbol jerárquico de articulaciones (el brazo robótico).
    dibujar_arbol_articulaciones(hombro)

    # Intercambiar buffers para mostrar el contenido renderizado.
    pygame.display.flip()
    # Limitar el programa a 60 cuadros por segundo.
    reloj.tick(60)
