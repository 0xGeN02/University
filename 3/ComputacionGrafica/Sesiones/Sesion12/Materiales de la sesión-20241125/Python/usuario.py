import pygame                 # Importa Pygame.
from pygame.locals import *   # Importa las constantes de Pygame en el espacio de nombres de la aplicación.
from configuracion import *   # Importar configuraciones globales.

def manejar_eventos(segmento_seleccionado, hombro, codo, muneca):
    """
    Maneja los eventos del usuario, como teclas presionadas, para controlar las articulaciones.

    Args:
        segmento_seleccionado (Articulacion): Articulación actualmente seleccionada.
        hombro (Articulacion): Referencia al hombro del sistema.
        codo (Articulacion): Referencia al codo del sistema.
        muneca (Articulacion): Referencia a la muñeca del sistema.

    Returns:
        tuple:
            ejecutando (bool): Indica si el programa sigue corriendo.
            segmento_seleccionado (Articulacion): Articulación seleccionada después del manejo de eventos.
    """
    ejecutando = True  # Controla si el bucle principal debe continuar.
    incremento = 0     # Variación del ángulo (positivo o negativo).

    # Procesar los eventos generados por el usuario.
    for evento in pygame.event.get():
        if evento.type == QUIT:  # Evento para cerrar la ventana.
            ejecutando = False
        elif evento.type == KEYDOWN:  # Evento de pulsación de una tecla.
            # Obtiene el nombre de la tecla presionada.
            key_name = pygame.key.name(evento.key)
            if evento.key == K_ESCAPE:  # Sale si se presiona Escape
                ejecutando = False
            elif key_name == 'h':  # Selecciona el hombro.
                segmento_seleccionado = hombro
            elif key_name == 'c':  # Selecciona el codo.
                segmento_seleccionado = codo
                print("Codo seleccionado")
            elif key_name == 'm':  # Selecciona la muñeca.
                segmento_seleccionado = muneca
                print("Muñeca seleccionada")

    # Obtiene el estado actual de todas las teclas.
    keys = pygame.key.get_pressed()
    if keys[K_UP]:  # Si se presiona la tecla de flecha arriba, incrementa el ángulo.
        incremento = INCREMENTO_ANGULO
    elif keys[K_DOWN]:  # Si se presiona la tecla de flecha abajo, decrementar el ángulo.
        incremento = -INCREMENTO_ANGULO

    # Ajusta el ángulo de la articulación seleccionada si hubo un cambio.
    if incremento != 0:
        segmento_seleccionado.angulo += incremento
        # Se asegura de que el ángulo esté dentro de los límites permitidos.
        segmento_seleccionado.angulo = max(
            min(segmento_seleccionado.angulo, segmento_seleccionado.angulo_max),
            segmento_seleccionado.angulo_min
        )

    return ejecutando, segmento_seleccionado  # Devuelve el estado de ejecución y la selección actual.
