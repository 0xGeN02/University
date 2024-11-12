import pygame  # Importa la librería Pygame para gestionar la ventana y eventos
from pygame.locals import *  # Importa constantes de Pygame
from OpenGL.GL import *  # Importa las funciones de OpenGL necesarias
import numpy as np  # Importa NumPy para manejar arrays de datos
from configuracion import *  # Importa configuraciones generales desde un archivo externo

# Definimos las coordenadas de los tres puntos a dibujar
PUNTO_1 = [-0.5, -0.5, 0.0]  # Coordenadas del primer punto
PUNTO_2 = [0.5, -0.5, 0.0]   # Coordenadas del segundo punto
PUNTO_3 = [0.0, 0.5, 0.0]    # Coordenadas del tercer punto

# Definimos los colores para cada punto
COLOR_1 = [1.0, 0.0, 0.0]    # Rojo para el primer punto
COLOR_2 = [0.0, 1.0, 0.0]    # Verde para el segundo punto
COLOR_3 = [0.0, 0.0, 1.0]    # Azul para el tercer punto

# Código fuente del Vertex Shader modificado para incluir el uniform 'desplazamiento'
vertex_shader_code = r"""
#version 330
layout(location = 0) in vec3 position;  // Atributo de posición en la ubicación 0
layout(location = 1) in vec3 color;     // Atributo de color en la ubicación 1

uniform vec3 desplazamiento;            // Uniform para el desplazamiento

out vec3 vertexColor;                   // Variable para pasar el color al fragment shader

void main()
{
    gl_Position = vec4(position + desplazamiento, 1.0);  // Aplica el desplazamiento a la posición del vértice
    vertexColor = color;                                 // Pasa el color al fragment shader
}
"""

# Código fuente del Fragment Shader (sin cambios)
fragment_shader_code = r"""
#version 330
in vec3 vertexColor;             // Variable recibida del vertex shader

out vec4 fragment_color;         // Variable para el color de salida

void main()
{
    fragment_color = vec4(vertexColor, 1.0); // Asigna el color recibido como color final
}
"""

def compilar_shader(shader_tipo, shader_fuente):
    shader_id = glCreateShader(shader_tipo)
    glShaderSource(shader_id, shader_fuente)
    glCompileShader(shader_id)
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
    enlazado_exitoso = glGetProgramiv(programa_id, GL_LINK_STATUS)
    if not enlazado_exitoso:
        mensaje_error = "\n" + glGetProgramInfoLog(programa_id).decode("utf-8")
        raise Exception(mensaje_error)
    glDeleteShader(vertex_shader_id)
    glDeleteShader(fragment_shader_id)
    return programa_id

def inicializar_escena():
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Dos Triángulos con Desplazamiento Uniforme')
    glPointSize(TAMANO_PUNTO)

# Inicializamos la escena
inicializar_escena()

# Creamos y usamos el programa de shaders
programa = crear_programa()
glUseProgram(programa)

# Obtenemos la ubicación de la variable uniforme 'desplazamiento'
loc_desplazamiento = glGetUniformLocation(programa, 'desplazamiento')

# Definimos los datos de los vértices y colores
puntos_colores = np.array([
    PUNTO_1 + COLOR_1,  # Primer vértice con color rojo
    PUNTO_2 + COLOR_2,  # Segundo vértice con color verde
    PUNTO_3 + COLOR_3   # Tercer vértice con color azul
], dtype=np.float32)

# Creamos el VBO
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, puntos_colores.nbytes, puntos_colores, GL_STATIC_DRAW)

# Creamos el VAO
VAO = glGenVertexArrays(1)
glBindVertexArray(VAO)

# Configuramos los atributos de posición
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * puntos_colores.itemsize, ctypes.c_void_p(0))

# Configuramos los atributos de color
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * puntos_colores.itemsize, ctypes.c_void_p(3 * puntos_colores.itemsize))

# Bucle principal de la aplicación
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBindVertexArray(VAO)

    # Dibujamos el primer triángulo sin desplazamiento
    glUniform3f(loc_desplazamiento, 0.0, 0.0, 0.0)  # Desplazamiento cero
    glDrawArrays(GL_TRIANGLES, 0, 3)

    # Dibujamos el segundo triángulo con desplazamiento en X
    glUniform3f(loc_desplazamiento, 0.5, 0.0, 0.0)  # Desplazamiento en X positivo
    glDrawArrays(GL_TRIANGLES, 0, 3)

    pygame.display.flip()
    pygame.time.wait(int(MILLISECONDS_PER_SECOND / FPS))
