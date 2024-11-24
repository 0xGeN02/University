# texturas.py

import pygame
from OpenGL.GL import *


def cargar_textura(ruta_textura):
    """Carga una textura desde un archivo y la configura en OpenGL.

    Args:
        ruta_textura (str): Ruta al archivo de imagen de la textura.

    Returns:
        int: ID de la textura en OpenGL.
    """

    # Carga la imagen desde el archivo usando Pygame.
    # Esto abre la imagen en formato de superficie de Pygame, que facilita la manipulación de imágenes.
    textura_surface = pygame.image.load(ruta_textura)

    # Convierte la imagen en una cadena de bytes en formato RGB para su uso en OpenGL.
    # `pygame.image.tostring` convierte la imagen cargada a un formato adecuado
    # para que OpenGL la interprete correctamente, preservando su información de color.
    textura_data = pygame.image.tostring(textura_surface, "RGB", 1)

    # Genera un identificador único para la textura en OpenGL.
    # `glGenTextures` devuelve un número entero que representa esta textura en la memoria de OpenGL.
    textura_id = glGenTextures(1)

    # Configura y enlaza la textura en OpenGL usando el ID generado.
    # `glBindTexture` asocia las operaciones futuras de texturas a este ID.
    glBindTexture(GL_TEXTURE_2D, textura_id)

    # Carga la textura en OpenGL.
    # `glTexImage2D` define la textura con parámetros específicos:
    # - GL_TEXTURE_2D: tipo de textura (2D).
    # - 0: nivel de detalle de mipmap (0 = nivel base).
    # - GL_RGB: formato interno de OpenGL para la textura.
    # - textura_surface.get_width() y textura_surface.get_height(): dimensiones de la textura.
    # - 0: siempre debe ser 0 (valor reservado en OpenGL).
    # - GL_RGB: formato de color de la imagen fuente.
    # - GL_UNSIGNED_BYTE: tipo de los datos de color.
    # - textura_data: datos de la imagen convertida en bytes para OpenGL.
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, textura_surface.get_width(), textura_surface.get_height(), 0, GL_RGB,
                 GL_UNSIGNED_BYTE, textura_data)

    # Configura los parámetros de la textura en OpenGL.
    # Estos parámetros controlan cómo se muestra la textura en el objeto, particularmente cómo se repite
    # y cómo se comportan las operaciones de minimización y ampliación de la textura:

    # Configuración de envoltura horizontal (S): GL_REPEAT hace que la textura se repita en el eje X.
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)

    # Configuración de envoltura vertical (T): GL_REPEAT hace que la textura se repita en el eje Y.
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    # Configuración del filtro de minimización de la textura (cuando la textura se reduce).
    # GL_LINEAR utiliza una interpolación lineal para suavizar la textura cuando se reduce.
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    # Configuración del filtro de magnificación de la textura (cuando la textura se amplía).
    # GL_LINEAR también suaviza la textura al ampliarla, evitando pixelación.
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # Devuelve el identificador de textura (textura_id) para que pueda ser utilizado en otras partes de la aplicación
    return textura_id

