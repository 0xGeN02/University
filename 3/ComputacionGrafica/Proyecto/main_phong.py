# main_phong.py
"""
Este archivo inicializa y ejecuta la aplicación gráfica en 3D utilizando Pygame y OpenGL,
incluyendo iluminación y sombreado.

Incluye la configuración de la ventana, inicialización de la cámara, control de eventos de usuario,
y el bucle principal de renderizado que dibuja los objetos en la escena con efectos de luz.
"""

# Importa las bibliotecas y módulos necesarios
from cubo_normales import cubo  # Importa el modelo de cubo con iluminación
from utilidades import *  # Funciones auxiliares para el dibujo de ejes y rejillas
from usuario import *  # Funciones para procesar entradas del usuario (teclado y ratón)
from camara import Camara  # Clase que controla la posición y orientación de la cámara
from configuracion import *  # Configuración general de la aplicación
from transformaciones import transformar  # Función para aplicar transformaciones en 3D
from luces import configurar_luces  # Configuración de las luces

# Crea una instancia de la cámara con valores iniciales.
camara = Camara()

# Inicialización de la escena.
def inicializar_escena():
    """Inicializa la ventana de Pygame y configura los ajustes de OpenGL para la escena 3D.

    Returns:
        screen: Objeto de la ventana gráfica creada por Pygame.
    """
    pygame.init()  # Inicializa Pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)  # Crea la ventana
    pygame.display.set_caption('S10_OLD')  # Establece el título de la ventana

    # Configuración de OpenGL
    # Establece el color de fondo como negro
    glClearColor(0, 0, 0, 1)

    # Activa el z-buffer
    glEnable(GL_DEPTH_TEST)
    # Activa el sombreado suave
    glShadeModel(GL_SMOOTH)
    # Selecciona la matriz de proyección
    glMatrixMode(GL_PROJECTION)
    # Configura la proyección en perspectiva
    gluPerspective(FOV, SCREEN_ASPECT_RATIO, NEAR_PLANE, FAR_PLANE)
    # Selecciona la matriz de modelo-vista
    glMatrixMode(GL_MODELVIEW)
    # Restablece la matriz a la identidad
    glLoadIdentity()

    # Configurar la iluminación
    configurar_luces()  # Llamamos a la función de configuración de luces

    return screen  # Devuelve la referencia a la ventana creada

# Dibuja un cubo en una posición específica con transformaciones opcionales
def dibujar_cubo(t_x=0.0, t_y=0.0, t_z=0.0, angulo=0.0, eje_x=0, eje_y=0, eje_z=1.0, sx=1.0, sy=1.0, sz=1.0):
    """Dibuja un cubo aplicando transformaciones de traslación, rotación y escalado.

    Args:
        t_x, t_y, t_z (float): Posición de traslación en los ejes X, Y, Z.
        angulo (float): Ángulo de rotación.
        eje_x, eje_y, eje_z (float): Ejes de rotación.
        sx, sy, sz (float): Factores de escalado en X, Y, Z.
    """
    transformar(t_x, t_y, t_z, angulo, eje_x, eje_y, eje_z, sx, sy, sz, cubo)

# Dibuja todos los objetos de la escena
def dibujar_objetos():
    """Dibuja todos los objetos de la escena."""
    dibujar_cubo(t_y=0.5)  # Dibuja un cubo centrado y elevado ligeramente en el eje Y

# Renderiza la escena
def renderizar():
    """Renderiza los elementos de la escena, incluyendo la cámara, ejes, rejilla y objetos."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpia los buffers de color y profundidad
    glLoadIdentity()  # Restablece la matriz a la identidad

    # Configura la posición y orientación de la cámara
    glRotatef(camara.roll, 0, 0, 1)  # Aplica rotación en el eje Z según el roll de la cámara
    cam_x, cam_y, cam_z = camara.obtener_posicion()  # Obtiene la posición de la cámara
    gluLookAt(cam_x, cam_y, cam_z, 0, 0, 0, 0, 1, 0)  # Configura la cámara para observar la escena

    # Desactiva la iluminación para dibujar elementos auxiliares
    glDisable(GL_LIGHTING)
    dibujar_elementos_auxiliares(ejes=True, rejilla=True)  # Dibuja ejes y rejilla
    # Reactiva la iluminación para dibujar los objetos con iluminación
    glEnable(GL_LIGHTING)
    dibujar_objetos()  # Dibuja los objetos

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
