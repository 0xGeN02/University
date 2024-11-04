# main_obj.py
"""
Este archivo inicializa y ejecuta una aplicación gráfica que carga y visualiza un modelo 3D en formato .obj
utilizando Pygame y OpenGL. Incluye configuración de cámara, renderizado y control de eventos de usuario.
"""

# Importa los módulos necesarios para el manejo del modelo, entrada del usuario y transformaciones en 3D
from modelo import Modelo  # Maneja la carga y renderizado de modelos en formato .obj
from utilidades import *  # Funciones auxiliares para dibujar elementos de la escena
from usuario import *  # Control de entrada del usuario (teclado y ratón)
from camara import Camara  # Clase que controla la posición y orientación de la cámara
from configuracion import *  # Configuración general de la aplicación (dimensiones, colores, etc.)
from transformaciones import transformar  # Función para aplicar transformaciones en 3D

# Inicialización de la cámara y del modelo 3D
camara = Camara()  # Crea una instancia de la cámara
modelo1 = Modelo("modelos/donut.obj", draw_type=GL_LINE_LOOP)  # Carga el modelo 3D en formato .obj con un estilo de línea
modelo2 = Modelo("modelos/teapot.obj", draw_type=GL_LINE_LOOP)  # Carga el modelo 3D en formato .obj con un estilo de línea

# Inicialización de la escena
def inicializar_escena():
    """Inicializa la ventana gráfica con Pygame y configura los ajustes de OpenGL para la escena 3D.

    Returns:
        screen: Objeto de la ventana gráfica creada por Pygame.
    """
    pygame.init()  # Inicializa Pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)  # Crea la ventana con buffers doble y OpenGL
    pygame.display.set_caption('Visualizador 3D')  # Establece el título de la ventana

    # Configuración de OpenGL
    glClearColor(0, 0, 0, 1)  # Fondo negro
    glEnable(GL_DEPTH_TEST)  # Activa el z-buffer para la profundidad
    glMatrixMode(GL_PROJECTION)  # Selecciona la matriz de proyección
    gluPerspective(FOV, SCREEN_ASPECT_RATIO, NEAR_PLANE, FAR_PLANE)  # Configura la proyección en perspectiva
    glMatrixMode(GL_MODELVIEW)  # Selecciona la matriz de modelo-vista
    glLoadIdentity()  # Restablece la matriz a la identidad
    return screen  # Devuelve la referencia a la ventana creada

# Renderiza la escena
def renderizar():
    """Renderiza los elementos de la escena, incluyendo la cámara, elementos auxiliares y el modelo 3D."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpia los buffers de color y profundidad
    glLoadIdentity()  # Restablece la matriz de modelo-vista a la identidad

    # Configura la posición y orientación de la cámara
    glRotatef(camara.roll, 0, 0, 1)  # Aplica rotación en el eje Z según el roll de la cámara
    cam_x, cam_y, cam_z = camara.obtener_posicion()  # Obtiene la posición de la cámara
    gluLookAt(cam_x, cam_y, cam_z, 0, 0, 0, 0, 1, 0)  # Configura la cámara para observar la escena

    # Dibuja elementos auxiliares y el modelo en la escena
    dibujar_elementos_auxiliares(ejes=True, rejilla=True)  # Dibuja ejes y rejilla
    modelo1.dibujar(x=2, y=0, z=-2, angulo=0, eje_x=0, eje_y=1, eje_z=0, sx=0.5, sy=0.5, sz=0.5)  # Dibuja el modelo en el origen
    modelo2.dibujar(x=-2, y=0, z=2, angulo=0, eje_x=0, eje_y=1, eje_z=0, sx=0.5, sy=0.5, sz=0.5)  # Dibuja el modelo en el origen

# Configuración e inicialización del entorno
screen = inicializar_escena()  # Crea la ventana y configura la escena
clock = pygame.time.Clock()  # Inicializa el reloj de Pygame para medir el tiempo entre fotogramas
ejecutando = True  # Define la bandera que controla el bucle de renderizado

# Bucle principal de la aplicación
while ejecutando:
    # Calcula el tiempo transcurrido en segundos para suavizar los movimientos
    delta_time = clock.tick(FPS) / MILLISECONDS_PER_SECOND

    # Procesa los eventos de Pygame, incluyendo el cierre de la ventana y eventos de ratón
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False  # Termina el bucle si se cierra la ventana
        elif evento.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION, pygame.MOUSEWHEEL):
            procesar_eventos_raton(evento, camara)  # Procesa los eventos de ratón para controlar la cámara

    # Consulta el estado del teclado y ajusta la cámara en consecuencia
    consultar_estado_teclado(camara, delta_time)

    # Actualiza la posición y orientación de la cámara
    camara.actualizar_camara()
    renderizar()  # Renderiza todos los elementos de la escena en el espacio 3D
    pygame.display.flip()  # Intercambia los buffers para actualizar el fotograma en pantalla

# Finaliza la aplicación y cierra Pygame
pygame.quit()
