# modelo_phong.py

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
        # Inicializa listas para guardar vértices, triángulos y normales
        self.vertices = []
        self.normales = []  # Lista para almacenar las normales del archivo .obj
        self.triangles = []
        self.filename = filename  # Nombre del archivo a cargar
        self.draw_type = draw_type  # Tipo de dibujo de OpenGL

        # Llama al método que carga el modelo desde el archivo .obj
        self.cargar_modelo()

    def cargar_modelo(self):
        """Lee el archivo .obj y extrae los vértices, normales y triángulos."""

        with open(self.filename) as file:
            for line in file:
                # Leer vértices
                if line.startswith("v "):
                    partes = line[2:].strip().split()
                    x = float(partes[0])
                    y = float(partes[1])
                    z = float(partes[2])
                    self.vertices.append((x, y, z))

                # Leer normales
                elif line.startswith("vn "):
                    partes = line[3:].strip().split()
                    nx = float(partes[0])
                    ny = float(partes[1])
                    nz = float(partes[2])
                    self.normales.append((nx, ny, nz))

                # Leer caras
                elif line.startswith("f "):
                    partes = line[2:].strip().split()
                    indices = []
                    normal_indices = []

                    for parte in partes:
                        # Divide la parte en índices de vértice/normal
                        indice_v = int(parte.split('/')[0]) - 1
                        indice_n = int(parte.split('/')[-1]) - 1

                        indices.append(indice_v)
                        normal_indices.append(indice_n)

                    # Solo se procesan triángulos
                    if len(indices) == 3:
                        self.triangles.append((indices, normal_indices))

    def dibujar(self, t_x=0, t_y=0, t_z=0, angulo=0, eje_x=0, eje_y=0, eje_z=0, sx=1, sy=1, sz=1):
        """
        Dibuja el modelo en la posición especificada y aplica transformaciones.

        Parámetros:
            x, y, z (float): Posición del modelo en el espacio.
            angulo (float): Ángulo de rotación.
            eje_x, eje_y, eje_z (float): Ejes de rotación.
            sx, sy, sz (float): Escala del modelo.
        """
        # Llama a la función de transformación antes de dibujar el objeto
        transformar(t_x, t_y, t_z, angulo, eje_x, eje_y, eje_z, sx, sy, sz, self._dibujar_objeto)

    def _dibujar_objeto(self):
        """Dibuja cada triángulo del modelo usando los vértices y sus normales."""
        glEnable(GL_NORMALIZE)  # Normaliza las normales para efectos de iluminación

        # Para cada triángulo en la lista, dibuja los tres vértices con sus normales
        for (vert_indices, norm_indices) in self.triangles:
            glBegin(self.draw_type)  # Inicia el dibujo según el tipo (triángulo o contorno)

            for vi, ni in zip(vert_indices, norm_indices):
                glNormal3fv(self.normales[ni])  # Asigna la normal correspondiente
                glVertex3fv(self.vertices[vi])  # Dibuja el vértice correspondiente

            glEnd()  # Termina el dibujo del triángulo
