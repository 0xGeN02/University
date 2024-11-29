"""
Módulo para manejar archivos JSON
"""
import os
import json
from datetime import datetime

class FileManager:
    """
    Clase para manejar archivos JSON
    """
    @staticmethod
    async def guardar_recorrido(data) -> str:
        """
        Método para guardar el recorrido en un archivo JSON
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        # Cambiar la ruta base al directorio raíz del proyecto
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
        directorio = os.path.join(path, 'recorridos')
        os.makedirs(directorio, exist_ok=True)
        file_name = f'Entorno_{timestamp}.json'
        file_path = os.path.join(directorio, file_name)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        return file_name

    @staticmethod
    async def get_file(name: str) -> dict:
        """
        Método para obtener un archivo JSON
        """
        # Cambiar la ruta base al directorio raíz del proyecto
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
        file_path = os.path.join(path, 'recorridos', name)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
