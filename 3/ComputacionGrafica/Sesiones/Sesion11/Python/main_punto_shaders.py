import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np
from configuracion import *

PUNTO_X = 0.0
PUNTO_Y = 0.0
PUNTO_Z = 0.0

# Código fuente del Vertex Shader
vertex_shader_code = r"""
#version 330
in vec3 position;
void main()
{
    gl_Position = vec4(position, 1.0);
}
"""

# Código fuente del Fragment Shader
fragment_shader_code = r"""
#version 330
out vec4 fragment_color;
void main()
{
    fragment_color = vec4(1.0, 0.0, 0.0, 1.0);
}
"""

def compilar_shader(shader_tipo, shader_fuente):
    shader_id = glCreateShader(shader_tipo)
    glShaderSource(shader_id, shader_fuente)
    glCompileShader(shader_id)
    # Verificamos la compilación
    compilacion_exitosa = glGetShaderiv(shader_id, GL_COMPILE_STATUS)
    if not compilacion_exitosa:
        mensaje_error = "\n" + glGetShaderInfoLog(shader_id).decode("utf-8")
        glDeleteShader(shader_id)
        raise Exception(mensaje_error)
    return shader_id

def crear_programa():
    vertex_shader_id = compilar_shader(GL_VERTEX_SHADER, vertex_shader_code)
    fragment_shader_id = compilar_shader(GL_FRAGMENT_SHADER, fragment_shader_code)
    programa_id = glCreateProgram()
    glAttachShader(programa_id, vertex_shader_id)
    glAttachShader(programa_id, fragment_shader_id)
    glLinkProgram(programa_id)
    # Verificamos el enlazado
    enlazado_exitoso = glGetProgramiv(programa_id, GL_LINK_STATUS)
    if not enlazado_exitoso:
        mensaje_error = "\n" + glGetShaderInfoLog(shader_id).decode("utf-8")
        raise Exception(mensaje_error)
    # Los shaders individuales pueden ser eliminados después del enlace
    glDeleteShader(vertex_shader_id)
    glDeleteShader(fragment_shader_id)
    return programa_id

def inicializar_escena():
    # Inicializa Pygame
    pygame.init()
    # Crea la ventana gráfica
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    # Establece el título de la ventana
    pygame.display.set_caption('Dibujado de un punto con shaders')
    # Establece el tamaño del punto
    glPointSize(TAMANO_PUNTO)


inicializar_escena()

# Creamos el programa con los shaders
programa = crear_programa()
# Usamos el programa creado
glUseProgram(programa)

# Definimos el array de puntos
puntos = np.array([
    [PUNTO_X, PUNTO_Y, PUNTO_Z]
], dtype=np.float32)

# Creamos un Vertex Buffer Object (VBO)

# Genera un identificador único para un nuevo Vertex Buffer Object (VBO)
VBO = glGenBuffers(1)

# Enlaza el VBO generado como el buffer activo para almacenar datos de vértices
glBindBuffer(GL_ARRAY_BUFFER, VBO)

# Carga los datos de los vértices en el buffer actualmente enlazado (VBO)
# 'puntos.nbytes' especifica el tamaño de los datos en bytes
# 'puntos' son los datos de los vértices que se cargarán
# 'GL_STATIC_DRAW' indica que los datos no cambiarán con frecuencia
glBufferData(GL_ARRAY_BUFFER, puntos.nbytes, puntos, GL_STATIC_DRAW)



# Definimos el Vertex Array Object (VAO)
# Genera un identificador único para un nuevo Vertex Array Object (VAO)
VAO = glGenVertexArrays(1)

# Enlaza el VAO generado como el Vertex Array Object activo
glBindVertexArray(VAO)

# Habilita el atributo de vértice en la ubicación 0
# Esto indica que se usará este atributo para almacenar datos de vértices
glEnableVertexAttribArray(0)

# Define cómo se interpretarán los datos de vértices almacenados en el VBO
# Parámetros:
# 0 - Índice del atributo de vértice
# 3 - Número de componentes por atributo de vértice (x, y, z)
# GL_FLOAT - Tipo de dato de cada componente
# GL_FALSE - No normalizar los datos
# 0 - Tamaño del stride (espacio entre atributos consecutivos)
# None - Desplazamiento inicial en el buffer
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBindVertexArray(VAO)
    # Dibuja un solo punto
    glDrawArrays(GL_POINTS, 0, 1)

    # Intercambia los buffers
    pygame.display.flip()
    # Espera
    pygame.time.wait(int(MILLISECONDS_PER_SECOND / FPS))


