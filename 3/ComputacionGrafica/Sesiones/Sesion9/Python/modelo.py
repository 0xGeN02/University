# modelo.py

from OpenGL.GL import *
from transformaciones import transformar


class Modelo:
    """Clase para cargar y dibujar un modelo 3D en formato .obj."""

    def __init__(self, filename, draw_type=GL_TRIANGLES):
        """
        Inicializa el modelo cargando el archivo .obj.

        Parámetros:
            filename (str): La ruta al archivo .obj.
            draw_type (GLenum): Tipo de dibujo de OpenGL (GL_TRIANGLES o GL_LINE_LOOP).
        """
        # Inicializa listas para guardar vértices y triángulos
        self.vertices = []
        self.triangles = []
        self.filename = filename  # Nombre del archivo a cargar
        self.draw_type = draw_type  # Tipo de dibujo de OpenGL

        # Llama al método que carga el modelo desde el archivo .obj
        self.cargar_modelo()

    def cargar_modelo(self):
        """Lee el archivo .obj y extrae los vértices y triángulos."""
        # Abre el archivo .obj y lo lee línea por línea
        with open(self.filename) as file:
            for line in file:
                # Si la línea comienza con 'v ', es una línea de vértice
                if line.startswith("v "):
                    # Divide la línea en palabras y convierte las últimas tres a números decimales (float)
                    partes = line[2:].strip().split()
                    x = float(partes[0])
                    y = float(partes[1])
                    z = float(partes[2])
                    # Guarda el vértice en la lista de vértices
                    self.vertices.append((x, y, z))

                # Si la línea comienza con 'f ', es una línea de triángulo (cara)
                elif line.startswith("f "):
                    # Divide la línea en palabras y procesa cada índice de vértice
                    partes = line[2:].strip().split()
                    indices = []
                    for parte in partes:
                        # Divide cada parte (por ejemplo, '1/1/1') en los índices correspondientes
                        indice = int(parte.split('/')[0]) - 1  # Convertimos a entero y ajustamos el índice
                        indices.append(indice)

                    # Solo guarda el triángulo si tiene tres vértices
                    if len(indices) == 3:
                        self.triangles.append(tuple(indices))

    def dibujar(self, x=0, y=0, z=0, angulo=0, eje_x=0, eje_y=1, eje_z=0, sx=1, sy=1, sz=1):
        """
        Dibuja el modelo en la posición especificada y aplica transformaciones.

        Parámetros:
            x, y, z (float): Posición del modelo en el espacio.
            angulo (float): Ángulo de rotación.
            eje_x, eje_y, eje_z (float): Ejes de rotación.
            sx, sy, sz (float): Escala del modelo.
        """
        # Llama a la función de transformación antes de dibujar el objeto
        transformar(x, y, z, angulo, eje_x, eje_y, eje_z, sx, sy, sz, self._dibujar_objeto)

    def _dibujar_objeto(self):
        """Dibuja cada triángulo del modelo usando los vértices."""
        # Para cada triángulo en la lista, dibuja los tres vértices
        for v1, v2, v3 in self.triangles:
            glBegin(self.draw_type)  # Inicia el dibujo según el tipo (triángulo o contorno)

            # Dibuja cada vértice del triángulo
            glVertex3fv(self.vertices[v1])  # Primer vértice
            glVertex3fv(self.vertices[v2])  # Segundo vértice
            glVertex3fv(self.vertices[v3])  # Tercer vértice

            glEnd()  # Termina el dibujo del triángulo
