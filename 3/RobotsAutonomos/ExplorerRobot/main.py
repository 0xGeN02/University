"""
Proyecto: Robots Autónomos
"""
from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event
from lib.explorer import ExplorerRobot
from lib.file_manager import FileManager

ROBOT_NAME = "C3_UIEC_Grupo1"
backend_instance = Bluetooth(ROBOT_NAME)
explorer = ExplorerRobot(backend_instance)

@event(explorer.when_play)
async def play(explorer_instance):
    """
    Función que inicia la misión
    """
    print('Iniciando robot ...')
    await explorer_instance.set_color_note()
    print('Posición inicial:', await explorer_instance.get_position())

    print('Inicio de la misión')
    await explorer_instance.set_speed()
    await explorer_instance.detectar_obstaculos()

    print('Fin de la fase de exploración')
    print('Posición final:', await explorer_instance.get_position())
    print('Distancia recorrida:', await explorer_instance.get_distance())

    #print('Recorriendo puntos almacenados')
    #await explorer_instance.recorrer_puntos(vueltas=1, cambiar_color=False)

    print('Creando Archivo JSON con el recorrido')
    data_recorrido = explorer_instance.get_recorrido_json()
    archive_name= await FileManager.guardar_recorrido(data_recorrido, explorer_instance.explore)
    print(f'{archive_name} creado')

    print(f'Recorriendo los puntos del archivo {archive_name}')
    file_data = await FileManager.get_file(archive_name)
    await explorer_instance.recorrer_puntos_json(file_data, vueltas=2, cambiar_color=True)
    print('Fin de la misión')

explorer.play()
