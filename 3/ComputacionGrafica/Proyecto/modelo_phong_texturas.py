# modelo_phong_texturas.py

from OpenGL.GL import *  # Importa las funciones de OpenGL necesarias para renderizar.
from transformaciones import transformar  # Importa funciones para realizar transformaciones en 3D (traslación, rotación, escalado).


class Modelo:
    """Clase para cargar y dibujar un modelo 3D en formato .obj, con soporte para texturas."""

    def __init__(self, filename, draw_type=GL_TRIANGLES):
        """
        Constructor que inicializa el modelo 3D cargando la información desde un archivo .obj.

        Args:
            filename (str): Ruta al archivo .obj que contiene el modelo 3D.
            draw_type (GLenum): Tipo de dibujo OpenGL (por defecto GL_TRIANGLES).

        Atributos:
            vertices (list): Lista de coordenadas de vértices del modelo.
            normales (list): Lista de normales para cada vértice.
            coordenadas_textura (list): Lista de coordenadas de textura para cada vértice.
            triangles (list): Lista de triángulos, cada uno con vértices, normales y coordenadas de textura.
            filename (str): Nombre del archivo .obj que contiene el modelo.
            draw_type (GLenum): Tipo de primitiva a utilizar para renderizar (GL_TRIANGLES por defecto).
        """
        self.vertices = []  # Almacena las coordenadas de los vértices del modelo 3D.
        self.normales = []  # Almacena las normales de los vértices para la iluminación.
        self.coordenadas_textura = []  # Almacena las coordenadas de textura para el mapeo de texturas.
        self.triangles = []  # Almacena los triángulos, definidos por índices de vértices, normales y texturas.
        self.filename = filename  # Archivo que contiene el modelo 3D.
        self.draw_type = draw_type  # Tipo de dibujo en OpenGL (por ejemplo, GL_TRIANGLES para triángulos).
        self.cargar_modelo()  # Llama al método para cargar el modelo desde el archivo .obj.

    def cargar_modelo(self):
        """
        Carga el modelo desde un archivo .obj, extrayendo vértices, normales y coordenadas de textura.

        Lee el archivo línea por línea y clasifica los datos en vértices, normales y coordenadas de textura.
        Luego, asocia estos elementos en triángulos.
        """
        with open(self.filename) as file:
            for line in file:
                # Si la línea define un vértice (v x y z)
                if line.startswith("v "):
                    partes = line[2:].strip().split()  # Extrae las coordenadas X, Y, Z.
                    x, y, z = map(float, partes)  # Convierte las coordenadas a float.
                    self.vertices.append((x, y, z))  # Añade el vértice a la lista.

                # Si la línea define una normal de vértice (vn x y z)
                elif line.startswith("vn "):
                    partes = line[3:].strip().split()  # Extrae las componentes de la normal.
                    nx, ny, nz = map(float, partes)  # Convierte las componentes a float.
                    self.normales.append((nx, ny, nz))  # Añade la normal a la lista.

                # Si la línea define coordenadas de textura (vt u v)
                elif line.startswith("vt "):
                    partes = line[2:].strip().split()  # Extrae las coordenadas U, V de la textura.
                    u, v = map(float, partes)  # Convierte las coordenadas a float.
                    self.coordenadas_textura.append((u, v))  # Añade las coordenadas de textura a la lista.

                # Si la línea define una cara (f v1/t1/n1 v2/t2/n2 v3/t3/n3)
                elif line.startswith("f "):
                    partes = line[2:].strip().split()  # Separa cada vértice de la cara.
                    indices = []  # Para almacenar los índices de vértices.
                    normal_indices = []  # Para almacenar los índices de normales.
                    textura_indices = []  # Para almacenar los índices de texturas.
                    for parte in partes:
                        # Divide cada componente en vértice/textura/normal.
                        vals = parte.split('/')
                        indice_v = int(vals[0]) - 1  # Índice de vértice (se resta 1 porque .obj usa índices desde 1).
                        indice_t = int(vals[1]) - 1  # Índice de coordenada de textura.
                        indice_n = int(vals[2]) - 1  # Índice de normal.
                        indices.append(indice_v)  # Añade el índice de vértice.
                        textura_indices.append(indice_t)  # Añade el índice de textura.
                        normal_indices.append(indice_n)  # Añade el índice de normal.
                    if len(indices) == 3:  # Solo se procesan triángulos (tres vértices).
                        self.triangles.append((indices, normal_indices, textura_indices))  # Se guarda el triángulo.


    def dibujar(self, textura_id, t_x=0, t_y=0, t_z=0, angulo=0, eje_x=0, eje_y=0, eje_z=0, sx=1, sy=1, sz=1):
        """
        Dibuja el modelo en la posición especificada, aplicando transformaciones y textura.

        Args:
            textura_id (int): ID de la textura cargada en OpenGL.
            t_x, t_y, t_z (float): Traslación en los ejes X, Y, Z.
            angulo (float): Ángulo de rotación en grados.
            eje_x, eje_y, eje_z (float): Ejes de rotación en X, Y, Z.
            sx, sy, sz (float): Factores de escalado en los ejes X, Y, Z.

        Aplica las transformaciones en orden: traslación, rotación, escalado.
        Luego dibuja el modelo con la textura aplicada.
        """
        # Aplica transformaciones de traslación, rotación y escalado usando la función 'transformar'.
        # La función 'lambda' garantiza que las transformaciones se apliquen antes de dibujar el objeto.
        transformar(t_x, t_y, t_z, angulo, eje_x, eje_y, eje_z, sx, sy, sz, lambda: self._dibujar_objeto(textura_id))

    def _dibujar_objeto(self, textura_id):
        """
        Dibuja cada triángulo del modelo con texturas.

        Args:
            textura_id (int): ID de la textura cargada en OpenGL.

        Habilita el modo de textura, asigna la textura y dibuja los triángulos del modelo,
        aplicando las normales y las coordenadas de textura a cada vértice.
        """
        glEnable(GL_NORMALIZE)  # Normaliza las normales automáticamente para asegurar que sean unitarias.
        glEnable(GL_TEXTURE_2D)  # Habilita el modo de texturas en OpenGL.
        glBindTexture(GL_TEXTURE_2D, textura_id)  # Asocia la textura con el modelo.

        # Recorre cada triángulo del modelo y dibuja sus vértices, normales y coordenadas de textura.
        for (vert_indices, norm_indices, tex_indices) in self.triangles:
            glBegin(self.draw_type)  # Inicia el dibujo usando el tipo especificado (por defecto GL_TRIANGLES).
            for vi, ni, ti in zip(vert_indices, norm_indices, tex_indices):
                glNormal3fv(self.normales[ni])  # Aplica la normal a cada vértice para la iluminación.
                glTexCoord2fv(self.coordenadas_textura[ti])  # Aplica las coordenadas de textura a cada vértice.
                glVertex3fv(self.vertices[vi])  # Define la posición de cada vértice en el espacio.
            glEnd()  # Finaliza el dibujo del triángulo.

        glDisable(GL_TEXTURE_2D)  # Desactiva el modo de texturas después de dibujar el objeto.
