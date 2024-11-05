from irobot_edu_sdk.backend.bluetooth import Bluetooth
from lib.explorer import ExplorerRobot
from lib.file_manager import FileManager
from irobot_edu_sdk.robots import event

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

    print('Recorriendo puntos almacenados')
    await explorer_instance.recorrer_puntos(vueltas=1, cambiar_color=True)
    archive_name= await explorer_instance.guardar_recorrido()
    print(f'{archive_name} creado')
    print('Fin de la misión')

explorer.play()
