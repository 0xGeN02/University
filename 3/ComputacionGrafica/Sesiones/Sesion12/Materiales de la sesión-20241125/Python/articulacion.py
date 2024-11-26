import numpy as np

class Articulacion:
    def __init__(self, nombre, padre=None, angulo=0, angulo_min=-180, angulo_max=180, r=[0, 0], color=(0, 0, 0)):
        """
        Clase que representa una articulación.

        Args:
            nombre (str): Nombre de la articulación.
            padre (Articulacion): Articulación padre, si existe.
            angulo (float): Ángulo inicial de la articulación en grados.
            angulo_min (float): Ángulo mínimo permitido para la articulación.
            angulo_max (float): Ángulo máximo permitido para la articulación.
            r (list): Vector de desplazamiento relativo al padre [x, y].
            color (tuple): Color de la articulación en formato RGB.
        """
        self.nombre = nombre  # Nombre descriptivo de la articulación.
        self.padre = padre  # Referencia a la articulación padre (o None si es raíz).
        self.hijos = []  # Lista de articulaciones hijas.
        self.angulo = angulo  # Ángulo actual de la articulación.
        self.angulo_min = angulo_min  # Límite inferior del ángulo.
        self.angulo_max = angulo_max  # Límite superior del ángulo.
        self.r = np.array([r[0], r[1], 0, 1])  # Vector de desplazamiento en coordenadas homogéneas.
        self.color = color  # Color de la articulación para visualización.
        self.L = np.identity(4)   # Matriz de transformación local (4x4), inicialmente la matriz identidad.
        self.W = np.identity(4)   # Matriz de transformación global (4x4), inicialmente la matriz identidad.

        # Si la articulación tiene un padre, agregamos la articulación actual como hija de este.
        if padre:
            padre.hijos.append(self)
