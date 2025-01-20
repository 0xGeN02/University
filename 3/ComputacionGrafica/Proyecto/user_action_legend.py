# user_action_legend.py

def mostrar_leyenda():
    """Muestra la leyenda de las acciones disponibles para el usuario."""
    leyenda = """
    Leyenda de Acciones:
    --------------------
    Cambiar Texturas:
    - Presiona '1' para textura de óxido.
    - Presiona '2' para textura de corteza.
    - Presiona '3' para textura de hielo.

    Cambiar Armas:
    - Presiona 'B' para seleccionar la pistola.
    - Presiona 'N' para seleccionar el revolver.
    - Presiona 'M' para seleccionar la escopeta.

    Control de Cámara:
    - Flecha Arriba: Inclina la cámara hacia arriba.
    - Flecha Abajo: Inclina la cámara hacia abajo.
    - Flecha Izquierda: Rota la cámara hacia la izquierda.
    - Flecha Derecha: Rota la cámara hacia la derecha.
    - Tecla 'Q': Aleja la cámara (zoom out).
    - Tecla 'A': Acerca la cámara (zoom in).
    - Tecla 'E': Aumenta el roll (rotación) de la cámara en sentido horario.
    - Tecla 'D': Disminuye el roll (rotación) de la cámara en sentido antihorario.
    - Tecla 'R': Restablece la cámara a su estado inicial.
    - Tecla 'C': Restablece la cámara al estado de captura de pantalla.

    Control del Ratón:
    - Botón Izquierdo: Presiona y arrastra para rotar la cámara.
    - Rueda del Ratón: Desplaza para ajustar el zoom.
    """
    print(leyenda)