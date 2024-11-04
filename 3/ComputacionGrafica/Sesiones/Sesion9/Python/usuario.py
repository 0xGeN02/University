# usuario.py
'''
En este fichero se procesa la entrada de usuario a través del ratón y el teclado.
'''

import pygame
from pygame.locals import *
from configuracion import *

boton_izquierdo_presionado = False # Bandera que indica si el botón izquierdo está presionado
ultimo_x, ultimo_y = 0, 0 # Última posición del ratón en los ejes X e Y.

def procesar_eventos_raton(evento, camara):
    """Procesa los eventos del ratón para interactuar con la cámara.

    Controla la rotación, desplazamiento y zoom de la cámara en función de los eventos
    de ratón, como clic, movimiento y rueda de desplazamiento.

    Args:
        evento: Evento de Pygame que representa la acción del ratón (clic, movimiento o rueda).
        camara: Instancia de la clase Camara que será modificada en función de los eventos.

    Variables Globales:
        boton_izquierdo_presionado (bool): Indica si el botón izquierdo del ratón está presionado.
        ultimo_x (int): Última posición X del ratón.
        ultimo_y (int): Última posición Y del ratón.
    """
    global boton_izquierdo_presionado, ultimo_x, ultimo_y

    # Verifica si se ha presionado el botón izquierdo del ratón
    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == BOTON_IZQUIERDO_RATON:
        boton_izquierdo_presionado = True  # Activa el seguimiento del movimiento
        ultimo_x, ultimo_y = evento.pos  # Guarda la posición inicial del clic

    # Verifica si se ha liberado el botón izquierdo del ratón
    elif evento.type == pygame.MOUSEBUTTONUP and evento.button == BOTON_IZQUIERDO_RATON:
        boton_izquierdo_presionado = False  # Detiene el seguimiento del movimiento

    # Verifica si el ratón se mueve mientras el botón izquierdo está presionado
    elif evento.type == pygame.MOUSEMOTION and boton_izquierdo_presionado:
        # Calcula el desplazamiento del ratón en ambos ejes
        dx, dy = evento.pos[0] - ultimo_x, evento.pos[1] - ultimo_y
        # Ajusta la rotación horizontal (yaw) en función del desplazamiento en X
        camara.ajustar_yaw(dx * SENSIBILIDAD_ROTACION * INVERTIR_CONTROLES)
        # Ajusta la rotación vertical (pitch) en función del desplazamiento en Y
        camara.ajustar_pitch(-dy * SENSIBILIDAD_ROTACION * INVERTIR_CONTROLES)
        # Actualiza la última posición del ratón
        ultimo_x, ultimo_y = evento.pos

    # Verifica si la rueda del ratón se ha movido
    elif evento.type == pygame.MOUSEWHEEL:
        # Ajusta el zoom de la cámara en función del movimiento de la rueda
        camara.ajustar_radio(-evento.y * SENSIBILIDAD_ZOOM * INVERTIR_CONTROLES, RADIO_MIN, RADIO_MAX)

def consultar_estado_teclado(camara, delta_time):
    """Procesa el estado del teclado para ajustar la cámara.

    Controla la rotación, inclinación y zoom de la cámara en función del estado
    de las teclas de control.

    Args:
        camara: Instancia de la clase Camara que se ajustará en función del estado del teclado.
        delta_time (float): Tiempo transcurrido desde el último fotograma.

    Teclas de Control:
        K_UP: Inclina la cámara hacia arriba.
        K_DOWN: Inclina la cámara hacia abajo.
        K_LEFT: Rota la cámara hacia la izquierda.
        K_RIGHT: Rota la cámara hacia la derecha.
        K_q: Aleja la cámara (zoom out).
        K_a: Acerca la cámara (zoom in).
        K_e: Aumenta el roll (rotación) de la cámara en sentido horario.
        K_d: Disminuye el roll (rotación) de la cámara en sentido antihorario.
        K_r: Restablece la cámara a su estado inicial.
    """
    keys = pygame.key.get_pressed()  # Obtiene el estado actual de todas las teclas

    # Calcula las velocidades de rotación y zoom, sensibles al tiempo transcurrido (delta_time)
    velocidad_rotacion = VELOCIDAD_ROTACION * delta_time * INVERTIR_CONTROLES
    velocidad_vertical = VELOCIDAD_ROTACION * delta_time
    velocidad_zoom = VELOCIDAD_ZOOM * delta_time * INVERTIR_CONTROLES

    # Control de inclinación (pitch) vertical hacia arriba.
    if keys[K_UP]:
        camara.ajustar_pitch(-velocidad_vertical)

    # Control de inclinación (pitch) vertical hacia abajo.
    if keys[K_DOWN]:
        camara.ajustar_pitch(velocidad_vertical)

    # Control de rotación horizontal (yaw) hacia la izquierda.
    if keys[K_LEFT]:
        camara.ajustar_yaw(-velocidad_rotacion)

    # Control de rotación horizontal (yaw) hacia la derecha.
    if keys[K_RIGHT]:
        camara.ajustar_yaw(velocidad_rotacion)

    # Control de zoom (radio) para alejar la cámara.
    if keys[K_q]:
        camara.ajustar_radio(-velocidad_zoom, RADIO_MIN, RADIO_MAX)

    # Control de zoom (radio) para acercar la cámara.
    if keys[K_a]:
        camara.ajustar_radio(velocidad_zoom, RADIO_MIN, RADIO_MAX)

    # Control del roll de la cámara en sentido horario.
    if keys[K_e]:
        camara.ajustar_roll(velocidad_rotacion)

    # Control del roll de la cámara en sentido antihorario.
    if keys[K_d]:
        camara.ajustar_roll(-velocidad_rotacion)

    # Restablece la cámara a su estado inicial.
    if keys[K_r]:
        camara.reset()

