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
cubos = Modelo("modelos/cubo.obj", draw_type=GL_TRIANGLES)
cilindros = Modelo("modelos/cilindro.obj", draw_type=GL_TRIANGLES)
conos = Modelo("modelos/cono.obj", draw_type=GL_TRIANGLES)
plataforma = Modelo("modelos/cilindro.obj", draw_type=GL_TRIANGLES)
GIRAR = 0



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
textura_id_plataforma = cargar_textura("texturas/marmol.png")  # Ajusta la ruta al archivo de textura

textura_id_1 = cargar_textura("texturas/oxido.png")
textura_id_2 = cargar_textura("texturas/corteza.png")
textura_id_3 = cargar_textura("texturas/hielo.png")

textura_id_escopeta = cargar_textura("texturas/madera.png")

clock = pygame.time.Clock()
ejecutando = True

textura_actual = textura_id_2

elegida = 0

# Renderiza la escena
def renderizar():
    """Renderiza los elementos de la escena, incluyendo la cámara, elementos auxiliares y el modelo 3D."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glRotatef(camara.roll, 0, 0, 1)
    cam_x, cam_y, cam_z = camara.obtener_posicion()
    gluLookAt(cam_x, cam_y, cam_z, 0, 0, 0, 0, 1, 0)

    glDisable(GL_LIGHTING)
    #dibujar_elementos_auxiliares(ejes=True, rejilla=True)
    glEnable(GL_LIGHTING)

    # Dibujar el modelo con la textura aplicada
    #ARMA 1 PISTOLA
    #AGARRE
    cubos.dibujar(textura_id = textura_actual, t_x=-1.5-elegida, t_y=1, t_z=0,
                   angulo=-25, eje_x=0, eje_y=0, eje_z=1, sx=1, sy=2, sz=1)
    #BARRIL
    cubos.dibujar(textura_id = textura_actual, t_x=0-elegida, t_y=1.8, t_z=0,
                   angulo=0, eje_x=0, eje_y=0, eje_z=0, sx=3, sy=0.7, sz=1)

    #ARMA 2 REVOLVER
    #AGARRE
    cubos.dibujar(textura_id = textura_actual, t_x=-1.5-elegida+100, t_y=1, t_z=0,
                   angulo=-25, eje_x=0, eje_y=0, eje_z=1, sx=1, sy=2, sz=1)
    cubos.dibujar(textura_id = textura_actual, t_x=-1-elegida+100, t_y=2, t_z=0,
                   angulo=0, eje_x=0, eje_y=0, eje_z=0, sx=1, sy=1, sz=1)
    #MUNICION
    cilindros.dibujar(textura_id = textura_actual, t_x=0-elegida+100, t_y=1.8, t_z=0,
                   angulo=90, eje_x=0, eje_y=0, eje_z=1, sx=2, sy=1.5, sz=2)
    #BARRIL
    cilindros.dibujar(textura_id = textura_actual, t_x=1.7-elegida+100, t_y=2.3, t_z=0,
                   angulo=90, eje_x=0, eje_y=0, eje_z=1, sx=.6, sy=2, sz=.6)

    #ARMA 3 ESCOPETA
    #AGARRE
    conos.dibujar(textura_id = textura_actual, t_x=-4-elegida+200, t_y=1, t_z=0,
                   angulo=-90, eje_x=0, eje_y=0, eje_z=1, sx=1.5, sy=2, sz=.5)
    cubos.dibujar(textura_id = textura_actual, t_x=-2.5-elegida+200, t_y=1.6, t_z=0,
                   angulo=0, eje_x=0, eje_y=0, eje_z=0, sx=3, sy=1.2, sz=.5)
    #MUNICION
    cubos.dibujar(textura_id = textura_actual, t_x=-1.1-elegida+200, t_y=1.7, t_z=0,
                   angulo=0, eje_x=0, eje_y=0, eje_z=0, sx=2, sy=1.2, sz=.5)
    cilindros.dibujar(textura_id=textura_id_escopeta, t_x=0.7 - elegida + 200, t_y=1.7, t_z=0,#NO CAMBIAR TEXTURA DE AQUI O NO SE VE
                      angulo=90, eje_x=0, eje_y=0, eje_z=1, sx=.65, sy=2, sz=.65)
    ##BARRIL
    cubos.dibujar(textura_id = textura_actual, t_x=1.4-elegida+200, t_y=2, t_z=0,
                   angulo=0, eje_x=0, eje_y=0, eje_z=0, sx=3, sy=.5, sz=.5)



    #PLATAFORMA
    plataforma.dibujar(textura_id = textura_id_plataforma, t_x=-0, t_y=-1, t_z=0,
                   angulo=GIRAR, eje_x=0, eje_y=1, eje_z=0, sx=7, sy=0.3, sz=7)



# Bucle principal de la aplicación
while ejecutando:
    delta_time = clock.tick(FPS) / MILLISECONDS_PER_SECOND
    GIRAR += 0.5
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION, pygame.MOUSEWHEEL):
            procesar_eventos_raton(evento, camara)

    consultar_estado_teclado(camara, delta_time)
    #Se cambia texturas y modelos aqui y no en consultar_estado_teclado
    #Porque si se hace en esa, dice que no encuentra la funcion
    keys = pygame.key.get_pressed()  # Obtiene el estado actual de todas las teclas

    #CAMBIAR TEXTURAS
    if keys[K_1]:
        if textura_actual != textura_id_1:
            textura_actual = textura_id_1
    if keys[K_2]:
        if textura_actual != textura_id_2:
            textura_actual = textura_id_2
    if keys[K_3]:
        if textura_actual != textura_id_3:
            textura_actual = textura_id_3

    #CAMBAIR ARMAS
    if keys[K_b]:
        elegida = 0

    if keys[K_n]:
        elegida = 100

    if keys[K_m]:
        elegida = 200

    camara.actualizar_camara()
    configurar_luces()

    renderizar()
    pygame.display.flip()

pygame.quit()
