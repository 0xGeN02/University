# main.py

from modelo import Modelo
from utilidades import *
from usuario import *
from camara import Camara
from configuracion import *
from luces import configurar_luces
from texturas import cargar_textura  # Importa cargar_textura para gestionar texturas

# Inicialización de la cámara y el modelo 3D
camara = Camara()

# Inicialización de la escena
def inicializar_escena():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption('DELGADO_GAMBINO MANUEL')

    glClearColor(0, 0, 0, 1)  # Fondo negro
    glEnable(GL_DEPTH_TEST)  # Activa el z-buffer para la profundidad
    glShadeModel(GL_SMOOTH)  # Activa el sombreado suave
    glMatrixMode(GL_PROJECTION)
    gluPerspective(FOV, SCREEN_ASPECT_RATIO, NEAR_PLANE, FAR_PLANE)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    configurar_luces()
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    return screen

# Configuración e inicialización del entorno
screen = inicializar_escena()  # Crea la ventana y configura el contexto OpenGL

# Path
path = "C:\\Users\\manue\\University\\3\\ComputacionGrafica\\Practica_evaluada3\\Python\\"
# Modelos
cubo = Modelo(path + "modelos\\cubo.obj")  # Cubo para la base
cilindro = Modelo(path + "modelos\\cilindro.obj")  # Cilindro para los postes

# Texturas
textura_base = cargar_textura(path + "texturas\\marron.png")  # Textura marrón para la base
textura_palo = cargar_textura(path + "texturas\\gris.png")  # Textura gris para los postes
texturas_discos = [
    cargar_textura(path + "texturas\\azul.png"),    # Textura azul
    cargar_textura(path + "texturas\\verde.png"),   # Textura verde
    cargar_textura(path + "texturas\\amarillo.png"),# Textura amarillo
    cargar_textura(path + "texturas\\naranja.png"), # Textura naranja
    cargar_textura(path + "texturas\\rojo.png")     # Textura rojo
]

clock = pygame.time.Clock()
ejecutando = True

# Renderiza la escena
def renderizar():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glRotatef(camara.roll, 0, 0, 1)
    cam_x, cam_y, cam_z = camara.obtener_posicion()
    gluLookAt(cam_x, cam_y, cam_z, 0, 0, 0, 0, 1, 0)

    glDisable(GL_LIGHTING)
    dibujar_elementos_auxiliares(ejes=True, rejilla=True)
    glEnable(GL_LIGHTING)

    # Dibuja la base
    cubo.dibujar(textura_id=textura_base, t_x=0.0, t_y=-0.1, t_z=0.0,
                 angulo=0.0, eje_x=0.0, eje_y=0.0, eje_z=0.0, sx=6.0, sy=0.2, sz=2.0)

    # Dibuja los tres postes
    for i in [-2.0, 0.0, 2.0]:  # Posición de los tres postes en X
        cilindro.dibujar(textura_id=textura_palo, t_x=i, t_y=1.0, t_z=0.0,
                         angulo=0.0, eje_x=0.0, eje_y=0.0, eje_z=0.0, sx=0.2, sy=2.0, sz=0.2)

    # Dibuja los cinco discos en el primer poste
    for idx, diametro in enumerate([2.0, 1.7, 1.4, 1.1, 0.8]):
        cilindro.dibujar(textura_id=texturas_discos[idx], t_x=-2.0, t_y=0.1 + idx * 0.2, t_z=0.0,
                     angulo=0.0, eje_x=0.0, eje_y=0.0, eje_z=0.0, sx=diametro, sy=0.2, sz=diametro)

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
    configurar_luces()
    renderizar()
    pygame.display.flip()

pygame.quit()
