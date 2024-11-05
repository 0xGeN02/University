"""
FileManager
"""
import os
import json
from datetime import datetime

class FileManager:
    """
    Clase para manejar archivos
    """
    @staticmethod
    async def guardar_recorrido(data, explore):
        """
        Método para guardar el recorrido en un archivo JSON
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        path = os.path.dirname(os.path.abspath(__file__))
        directorio = os.path.join(path, 'recorridos')
        os.makedirs(directorio, exist_ok=True)
        file_path = os.path.join(directorio, f'Lab02_Entorno_{timestamp}.json')
        data = {"data": data, "explore": explore}
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        return f'{file_path} creado correctamente'
