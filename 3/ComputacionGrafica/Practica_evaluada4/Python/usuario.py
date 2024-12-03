# usuario.py

import pygame
from pygame.locals import *
import numpy as np
from configuracion import (
    RADIO_CIRCULO,
    PROJECTION_LEFT,
    PROJECTION_RIGHT,
    PROJECTION_BOTTOM,
    PROJECTION_TOP,
    ANCHO_PANTALLA,
    ALTO_PANTALLA,
    INCREMENTO_ANGULO
)
from articulacion import Articulacion  # Importar Articulacion para acceder a la lista de articulaciones

# Definir el incremento de traslación
INCREMENTO_TRASLACION = 0.1  # Ajusta este valor según la necesidad

def obtener_coordenadas_mundo(posicion_pantalla):
    """
    Convierte las coordenadas de pantalla (píxeles) a coordenadas del mundo.
    """
    x_pantalla, y_pantalla = posicion_pantalla
    ancho_pantalla, alto_pantalla = ANCHO_PANTALLA, ALTO_PANTALLA

    # Convertir origen de la pantalla (superior izquierdo) al centro
    x_normalizado = (x_pantalla / ancho_pantalla) * (PROJECTION_RIGHT - PROJECTION_LEFT) + PROJECTION_LEFT
    y_normalizado = ((alto_pantalla - y_pantalla) / alto_pantalla) * (
                PROJECTION_TOP - PROJECTION_BOTTOM) + PROJECTION_BOTTOM

    return (x_normalizado, y_normalizado)


def seleccionar_articulacion_por_click(posicion_mundo, articulaciones, radio=RADIO_CIRCULO):
    """
    Selecciona la articulación que está cerca de la posición dada.
    """
    x_click, y_click = posicion_mundo
    articulacion_seleccionada = None
    distancia_minima = float('inf')

    for articulacion in articulaciones:
        if articulacion.angulo_max != 0 or articulacion.angulo_min != 0:
            # Obtener la posición global de la articulación
            W = articulacion.W
            x_articulacion = W[0, 3]
            y_articulacion = W[1, 3]

            # Calcular la distancia al click
            distancia = np.sqrt((x_click - x_articulacion) ** 2 + (y_click - y_articulacion) ** 2)

            # Verificar si está dentro del radio y es la más cercana
            if distancia <= radio and distancia < distancia_minima:
                distancia_minima = distancia
                articulacion_seleccionada = articulacion

    return articulacion_seleccionada


def manejar_eventos(segmento_seleccionado, articulaciones):
    """
    Maneja los eventos del usuario, como teclas presionadas y clicks de ratón, para controlar las articulaciones.
    """
    ejecutando = True

    # Procesar eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            ejecutando = False
        elif evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                ejecutando = False
            elif evento.key == K_r:
                # Reiniciar el esqueleto a la posición (0, 0) y ángulo de rotación 0 de la raíz
                if Articulacion.articulaciones:
                    # Asumimos que la raíz es la primera articulación en la lista
                    raiz = Articulacion.articulaciones[0]
                    raiz.r = [0, 0]  # Reiniciar posición de la raíz
                    raiz.angulo = 0  # Reiniciar ángulo de rotación de la raíz
        elif evento.type == MOUSEBUTTONDOWN and evento.button == 1:  # Click izquierdo del ratón
            posicion_pantalla = evento.pos
            posicion_mundo = obtener_coordenadas_mundo(posicion_pantalla)
            articulacion_click = seleccionar_articulacion_por_click(posicion_mundo, articulaciones, RADIO_CIRCULO)
            if articulacion_click:
                segmento_seleccionado = articulacion_click

    return ejecutando, segmento_seleccionado


def manejar_teclas_polling(segmento_seleccionado):
    """
    Maneja las teclas de control por polling (teclas arriba, abajo, izquierda y derecha).

    Args:
        segmento_seleccionado (Articulacion): Articulación actualmente seleccionada.

    Returns:
        Articulacion: La articulación seleccionada con el ángulo y posición actualizados.
    """
    keys = pygame.key.get_pressed()
    incremento = 0

    # Manejar incremento/decremento de ángulo
    if keys[K_UP]:  # Incrementar el ángulo de la articulación seleccionada
        incremento = INCREMENTO_ANGULO
    elif keys[K_DOWN]:  # Decrementar el ángulo de la articulación seleccionada
        incremento = -INCREMENTO_ANGULO

    if incremento != 0 and segmento_seleccionado is not None:
        # Actualizar el ángulo
        segmento_seleccionado.angulo += incremento

        # Reiniciar el ángulo a 0 si excede 360 o -360 grados
        if segmento_seleccionado.angulo >= 360 or segmento_seleccionado.angulo <= -360:
            segmento_seleccionado.angulo = 0
        else:
            # Clampear el ángulo dentro de los límites definidos
            segmento_seleccionado.angulo = max(
                min(segmento_seleccionado.angulo, segmento_seleccionado.angulo_max),
                segmento_seleccionado.angulo_min,
            )

    # Manejar traslación del esqueleto
    raiz = None
    if Articulacion.articulaciones:
        # Asumimos que la raíz es la primera articulación en la lista
        raiz = Articulacion.articulaciones[0]

    if raiz:
        if keys[K_LEFT]:  # Mover el esqueleto a la izquierda
            raiz.r[0] -= INCREMENTO_TRASLACION
        if keys[K_RIGHT]:  # Mover el esqueleto a la derecha
            raiz.r[0] += INCREMENTO_TRASLACION

    return segmento_seleccionado
