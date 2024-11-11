import pygame  # Importa la librería Pygame para gestionar la ventana y eventos
from pygame.locals import *  # Importa constantes de Pygame
from OpenGL.GL import *  # Importa las funciones de OpenGL necesarias
import numpy as np  # Importa NumPy para manejar arrays de datos
from configuracion import *  # Importa configuraciones generales desde un archivo externo

# Definimos las coordenadas de los tres puntos a dibujar
PUNTO_1 = [-0.5, -0.5, 0.0]  # Coordenadas del primer punto
PUNTO_2 = [0.5, -0.5, 0.0]  # Coordenadas del segundo punto
PUNTO_3 = [0.0, 0.5, 0.0]  # Coordenadas del tercer punto

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
    # Crea un nuevo shader del tipo especificado (vertex o fragment)
    shader_id = glCreateShader(shader_tipo)
    # Asigna el código fuente al shader
    glShaderSource(shader_id, shader_fuente)
    # Compila el shader
    glCompileShader(shader_id)
    # Verificamos si la compilación fue exitosa
    compilacion_exitosa = glGetShaderiv(shader_id, GL_COMPILE_STATUS)
    if not compilacion_exitosa:
        # Obtiene el mensaje de error en caso de fallo
        mensaje_error = "\n" + glGetShaderInfoLog(shader_id).decode("utf-8")
        # Elimina el shader defectuoso
        glDeleteShader(shader_id)
        # Lanza una excepción con el mensaje de error
        raise Exception(mensaje_error)
    # Retorna el ID del shader compilado
    return shader_id


def crear_programa():
    # Compila el Vertex Shader
    vertex_shader_id = compilar_shader(GL_VERTEX_SHADER, vertex_shader_code)
    # Compila el Fragment Shader
    fragment_shader_id = compilar_shader(GL_FRAGMENT_SHADER, fragment_shader_code)
    # Crea un nuevo programa de shaders
    programa_id = glCreateProgram()
    # Adjunta el Vertex Shader al programa
    glAttachShader(programa_id, vertex_shader_id)
    # Adjunta el Fragment Shader al programa
    glAttachShader(programa_id, fragment_shader_id)
    # Enlaza el programa de shaders
    glLinkProgram(programa_id)
    # Verificamos si el enlazado fue exitoso
    enlazado_exitoso = glGetProgramiv(programa_id, GL_LINK_STATUS)
    if not enlazado_exitoso:
        # Obtiene el mensaje de error en caso de fallo
        mensaje_error = "\n" + glGetShaderInfoLog(shader_id).decode("utf-8")
        # Lanza una excepción con el mensaje de error
        raise Exception(mensaje_error)
    # Elimina los shaders individuales ya enlazados al programa
    glDeleteShader(vertex_shader_id)
    glDeleteShader(fragment_shader_id)
    # Retorna el ID del programa de shaders creado
    return programa_id


def inicializar_escena():
    # Inicializa Pygame
    pygame.init()
    # Crea la ventana gráfica con las dimensiones especificadas y soporte para OpenGL
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    # Establece el título de la ventana
    pygame.display.set_caption('Punto en modo inmediato')
    # Establece el tamaño de los puntos a dibujar
    glPointSize(TAMANO_PUNTO)


# Llama a la función para inicializar la escena gráfica
inicializar_escena()

# Crea el programa de shaders compilado
programa = crear_programa()
# Activa el programa de shaders para su uso
glUseProgram(programa)

# Define el array de puntos con las tres coordenadas especificadas
puntos = np.array([
    PUNTO_1,  # Primer punto
    PUNTO_2,  # Segundo punto
    PUNTO_3  # Tercer punto
], dtype=np.float32)

# Creamos el Vertex Buffer Object (VBO)

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

# Inicia el bucle principal de la aplicación
while True:
    # Itera sobre todos los eventos de Pygame
    for event in pygame.event.get():
        # Si el evento es de cierre de ventana, finaliza la aplicación
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Limpia el buffer de color y el buffer de profundidad
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Enlaza el Vertex Array Object activo
    glBindVertexArray(VAO)
    # Dibuja tres puntos usando glDrawArrays
    # GL_POINTS indica que se dibujarán puntos
    # 0 es el índice de inicio en el VBO
    # 3 es el número de puntos a dibujar
    glDrawArrays(GL_POINTS, 0, 3)

    # Intercambia los buffers de front y back para actualizar la pantalla
    pygame.display.flip()
    # Espera un breve período para controlar la tasa de refresco (FPS)
    pygame.time.wait(int(MILLISECONDS_PER_SECOND / FPS))
