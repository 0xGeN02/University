# main_ejercicio_4.py

# Importa las bibliotecas requeridas
#from cubo_vertices_compartidos import cubo
#from cubo_caras_independientes import cubo
from cubo_caras_independientes_color import cubo
from utilidades import *
from usuario import *
from camara import Camara
from configuracion import *
from transformaciones import transformar

# Inicialización de la cámara
camara = Camara()

# Inicialización de la escena
def inicializar_escena():
    # Inicializa pygame
    pygame.init()
    # Crea la ventana gráfica
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    # Establece el título de la ventana
    pygame.display.set_caption('S09')
    # Establece el color de fondo como negro y opacidad del 100%
    glClearColor(0, 0, 0, 1)
    # Activa el z-buffer
    glEnable(GL_DEPTH_TEST)
    # Selecciona la matriz de proyección (PROJECTION)
    glMatrixMode(GL_PROJECTION)
    # Configura la proyección en perspectiva
    gluPerspective(FOV, SCREEN_ASPECT_RATIO, NEAR_PLANE, FAR_PLANE)
    # Selecciona la matriz de modelo-vista (MODELVIEW)
    glMatrixMode(GL_MODELVIEW)
    # Restablece la matriz a la matriz identidad, que no aplica ninguna transformación
    glLoadIdentity()
    return screen

# Dibuja un cubo en una posición específica con transformaciones opcionales
def dibujar_cubo(t_x=0, t_y=0, t_z=0, angulo=0, eje_x=0, eje_y=0, eje_z=1, sx=1, sy=1, sz=1):
    transformar(t_x, t_y, t_z, angulo, eje_x, eje_y, eje_z, sx, sy, sz, cubo)

def dibujar_objetos():
    dibujar_cubo(t_x=0, t_y=0.5, t_z=0, angulo=45, eje_x=0, eje_y=1, eje_z=0, sx=1, sy=1, sz=1)

# Renderiza la escena
def renderizar():
    # Limpia los buffers de color y de profundidad
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Restablece la matriz actual (MODELVIEW) a la matriz identidad
    glLoadIdentity()
    # Rota la cámara roll grados alrededor del eje z
    glRotatef(camara.roll, 0, 0, 1)
    # Obtiene las coordenadas de la cámara en el mundo
    cam_x, cam_y, cam_z = camara.obtener_posicion()
    # Configura la orientación y posición de la cámara en espacio del mundo
    gluLookAt(cam_x, cam_y, cam_z, 0, 0, 0, 0, 1, 0)
    # Dibuja los elementos auxiliares de la escena (ejes y rejilla)
    dibujar_elementos_auxiliares(ejes=True, rejilla=True)
    # Dibuja los objetos de la escena
    dibujar_objetos()


screen = inicializar_escena() # Inicializa la escena
clock = pygame.time.Clock()  # Inicializa el reloj de Pygame
ejecutando = True # Inicializa la bandera de control del bucle de renderizado

while ejecutando:
    # Calcula el tiempo transcurrido en segundos.
    delta_time = clock.tick(FPS) / MILLISECONDS_PER_SECOND

    # Procesa los eventos del sistema y la interacción del usuario.
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            # Si se detecta un evento de cierre de la ventana, termina la ejecución del bucle.
            ejecutando = False
        elif evento.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION, pygame.MOUSEWHEEL):
            # Si se detecta un evento de ratón, lo procesa.
            procesar_eventos_raton(evento, camara)

    # Consulta el estado del teclado mediante polling.
    consultar_estado_teclado(camara, delta_time)

    # Actualiza la posición y la orientación de la cámara.
    camara.actualizar_camara()
    # Renderiza todos los elementos de la escena en el espacio 3D.
    renderizar()
    # Intercambia los buffers para mostrar el nuevo fotograma renderizado en la ventana gráfica.
    pygame.display.flip()

pygame.quit()