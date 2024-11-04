# main_obj_phong_texturas.py

from modelo_phong_texturas import Modelo
from utilidades import *
from usuario import *
from camara import Camara
from configuracion import *
from transformaciones import transformar
from luces import configurar_luces
from texturas import cargar_textura  # Importa cargar_textura para gestionar texturas

# Inicialización de la cámara y el modelo 3D
camara = Camara()
modelo = Modelo("modelos/esfera.obj", draw_type=GL_TRIANGLES)

# Inicialización de la escena
def inicializar_escena():
    """Inicializa la ventana gráfica con Pygame y configura los ajustes de OpenGL para la escena 3D.

    Returns:
        screen: Objeto de la ventana gráfica creada por Pygame.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Visualizador 3D con Textura')

    # Configuración de OpenGL
    glClearColor(0, 0, 0, 1)  # Fondo negro
    glEnable(GL_DEPTH_TEST)  # Activa el z-buffer para la profundidad
    glShadeModel(GL_SMOOTH)  # Activa el sombreado suave
    glMatrixMode(GL_PROJECTION)  # Selecciona la matriz de proyección
    gluPerspective(FOV, SCREEN_ASPECT_RATIO, NEAR_PLANE, FAR_PLANE)  # Configura la proyección en perspectiva
    glMatrixMode(GL_MODELVIEW)  # Selecciona la matriz de modelo-vista
    glLoadIdentity()  # Restablece la matriz a la identidad

    configurar_luces()
    return screen

# Configuración e inicialización del entorno
screen = inicializar_escena()  # Crea la ventana y configura el contexto OpenGL

# Ahora que el contexto OpenGL está activo, carga la textura
textura_id = cargar_textura("texturas/ajedrez.png")  # Ajusta la ruta al archivo de textura

clock = pygame.time.Clock()
ejecutando = True

# Renderiza la escena
def renderizar():
    """Renderiza los elementos de la escena, incluyendo la cámara, elementos auxiliares y el modelo 3D."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glRotatef(camara.roll, 0, 0, 1)
    cam_x, cam_y, cam_z = camara.obtener_posicion()
    gluLookAt(cam_x, cam_y, cam_z, 0, 0, 0, 0, 1, 0)

    glDisable(GL_LIGHTING)
    dibujar_elementos_auxiliares(ejes=True, rejilla=True)
    glEnable(GL_LIGHTING)

    # Dibujar el modelo con la textura aplicada
    modelo.dibujar(textura_id = textura_id, t_x=0, t_y=0, t_z=0,
                   angulo=0, eje_x=0, eje_y=0, eje_z=0, sx=1, sy=1, sz=1)


# Bucle principal de la aplicación
while ejecutando:
    delta_time = clock.tick(FPS) / MILLISECONDS_PER_SECOND
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION, pygame.MOUSEWHEEL):
            procesar_eventos_raton(evento, camara)

    consultar_estado_teclado(camara, delta_time)
    camara.actualizar_camara()
    renderizar()
    pygame.display.flip()

pygame.quit()
