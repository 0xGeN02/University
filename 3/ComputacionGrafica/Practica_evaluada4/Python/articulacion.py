# articulacion.py

from configuracion import *

class Articulacion:
    """
    Representa una articulación en un sistema de animación esqueletal 2D.

    Atributos de Clase:
        articulaciones (list): Lista que almacena todas las instancias creadas de Articulacion.
    """

    articulaciones = []  # Lista de clase para almacenar todas las articulaciones creadas

    def __init__(self, padre=None, angulo=0, angulo_min=0, angulo_max=0, r=[0, 0], color=COLOR_ARTICULACION_NO_SELECCIONADA):
        """
        Inicializa una nueva instancia de Articulacion.

        Args:
            padre (Articulacion, optional): Articulación padre a la que está conectada esta articulación.
                                            Si es None, esta articulación es la raíz del esqueleto.
                                            Por defecto es None.
            angulo (float, optional): Ángulo de rotación inicial de la articulación en grados.
                                      Por defecto es 0.
            angulo_min (float, optional): Ángulo mínimo permitido para la rotación de la articulación en grados.
                                           Por defecto es 0.
            angulo_max (float, optional): Ángulo máximo permitido para la rotación de la articulación en grados.
                                           Por defecto es 0.
            r (list of float, optional): Desplazamiento relativo [x, y] respecto a la articulación padre.
                                         Por defecto es [0, 0].
            color (tuple, optional): Color de la articulación en formato RGB.
                                     Por defecto es COLOR_GRIS definido en configuracion.py.
        """
        self.padre = padre
        self.angulo = angulo
        self.angulo_min = angulo_min
        self.angulo_max = angulo_max
        self.r = r  # Desplazamiento relativo al padre [x, y]
        self.color = color
        self.hijos = []  # Lista para almacenar las articulaciones hijas
        self.L = None  # Matriz de transformación local
        self.W = None  # Matriz de transformación global

        # Si se especifica un padre, añade esta articulación a la lista de hijos del padre
        if padre:
            padre.hijos.append(self)

        # Añade esta articulación a la lista de articulaciones de la clase
        Articulacion.articulaciones.append(self)
