# modelo_3d.py

import trimesh
import numpy as np

class Modelo3D:
    def __init__(self, ruta_obj):
        """
        Carga un modelo 3D desde un archivo .obj.

        :param ruta_obj: Ruta al archivo .obj
        """
        mesh = trimesh.load(ruta_obj)
        if not isinstance(mesh, trimesh.Trimesh):
            raise ValueError(f"El archivo {ruta_obj} no contiene un mesh válido.")

        self.vertices = mesh.vertices  # Array (N, 3)
        self.faces = mesh.faces        # Array (M, 3)

        # Convierte las caras a listas de índices para facilitar el renderizado
        self.faces = [face.tolist() for face in self.faces]
