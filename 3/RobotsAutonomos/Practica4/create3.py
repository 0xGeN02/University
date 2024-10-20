"""
Practica 4: Funcionalizar el codigo del iRobot Create3
"""

import math
import random
from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth())

# Clase de colores
class Color:
    """
    Clase que contiene los colores
    """
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    PURPLE = (128, 0, 128)
    ORANGE = (255, 165, 0)
    VIOLET = (238, 130, 238)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, color_name):
        self.color_name = color_name
        self.rgb = getattr(Color, color_name.upper(), Color.WHITE) # Default color is WHITE

    def __str__(self):
        return f"Color: {self.color_name}, RGB: {self.rgb}"

    @staticmethod
    def get_color(color_name):
        """
        Método para obtener el color en RGB
        """
        return getattr(Color, color_name.upper(), Color.WHITE)

# Clase del robot explorerRobot
class ExplorerRobot(Create3):
    """
        Extensión de la clase Create3 para el robot explorerRobot:
            -deteccion_obstaculos: Método para detectar obstáculos✅
            -moverse: Método para moverse✅
            -inspeccion: Método para inspeccionar (aleatorio o en una dirección específica)✅
            -get_position: Método para obtener la posición del robot✅
            -get_distance: Método para obtener la distancia total recorrida✅
            -navegacion: Método para navegar por los obstáculos guradados
            -set_color_note: Método para crear agrupaciones de color y nota✅
    """

    def __init__(self, backend):
        """
        Constructor de la clase ExplorerRobot que hereda de Create3
        """
        super().__init__(backend)

        # Diccionario que agrupa toda la información del recorrido y estado del robot
        self.estado_robot = {
            'recorrido': {}  # Recorrido completo con obstáculos y paradas
            # recorrido = {'parada'={'posicion': {'x': 0, 'y': 0, 'θ': 0}, 'obstaculos': [[0, 0, 0], [0, 1, 0], [0, 0, 0]]}, parada2=...}
        }

    async def set_color_note(self, select_group: str ='default', note_timer: int =1.5):
        """
        Método para crear agrupaciones de color y nota.
        @param select_group: Elige un grupo predefinido de color y nota.
        @param note_timer: El tiempo que sonará la nota.
        @return: Retorna la combinación de color y nota correspondiente.
        call: await explorer_robot.set_color_note('moverse', 1)
        """

        # Definir las combinaciones de color y notas predefinidas
        combinaciones = {
            'default': (Color.get_color('WHITE'), Note.A4),
            'moverse': (Color.get_color('BLUE'), Note.C2),
            'deteccion': (Color.get_color('RED'), Note.B1),
            'inspeccion': (Color.get_color('YELLOW'), Note.C2_SHARP),
            'finalizacion': (Color.get_color('GREEN'), Note.A3)
        }

        # Buscar la combinación seleccionada
        if select_group in combinaciones:
            color, nota = combinaciones[select_group]
            # Asignar color y hacer sonar la nota
            await self.set_lights_rgb(color[0], color[1], color[2])
            await self.play_note(nota, note_timer)
            return color, nota

        # En caso de que no se encuentre una combinación válida
        return 'Color/nota no encontrados', 'Nota no encontrada'

    async def set_speed(self, speed: int =15) -> str:
        """
        Método para mover el robot
        @param speed: Velocidad del robot
        @return: Retorna el movimiento del robot
        call: await explorer_robot.set_speed(10)
        """
        if speed == 0:
            # Cambiamos el estado del robot a detenido: luz roja
            await self.set_color_note('detener', 1.5)
            await self.set_wheel_speeds(0, 0)
            return 'Robot detenido'

        # Cambiamos el estado del robot a moverse: luz azul
        await self.set_color_note('moverse', 1.5)

        # Movemos el robot a la velocidad indicada
        await self.set_wheel_speeds(speed, speed)
        return f'Robot moviéndose a {speed} mm/s'

    async def get_position(self) -> str:
        """
        Método para obtener la posición del robot
        @return: Retorna la posición del robot en cartesianos (x,y) y su angular (θ)
        call: explorer_robot.position
        """
        return {'x': self.pose.x, 'y': self.pose.y, 'theta': self.pose.heading}


    async def get_distance(self):
        """
        Método para obtener la distancia total recorrida
        @return: Retorna la distancia total recorrida
        call: explorer_robot.get_distance()
        """
        distance = 0
        recorrido = self.estado_robot['recorrido']
        paradas = list(recorrido.values())

        for i in range(1, len(paradas)):
            pos_actual = paradas[i]['posicion']
            pos_anterior = paradas[i - 1]['posicion']
            distance += math.sqrt(
                (pos_actual['x'] - pos_anterior['x']) ** 2 +
                (pos_actual['y'] - pos_anterior['y']) ** 2
            )
        return distance

    async def giro(self, turn: str = None, angle: float = 90) -> str:
        """
        Método para girar aleatoriamente o en una dirección específica
        @param turn: Dirección del giro ('left', 'right' o None para aleatorio)
        @param angle: Ángulo de giro en grados
        @return: Retorna el sentido del giro y el ángulo en grados
        call: await explorer_robot.giro()
        """

        # Determinar la dirección del giro
        if turn is None:
            turn = random.choice(['left', 'right'])

        if turn == 'left':
            await self.turn_left(angle)
        elif turn == 'right':
            await self.turn_right(angle)

        return turn, angle

    async def detectar_obstaculos(self, th: int = 15):
        """
        Método para detectar obstáculos
        """
        while True:
            sensor = (await self.get_ir_proximity()).sensors
            if sensor[2] < th:
                await self.set_color_note('deteccion', 1.5)
                await self.set_speed(0)

    async def inspeccion(self, th: int = 15):
        """
        Método para inspeccionar los obstáculos tanto frontal como a los lados
        @return: Retorna la matriz de obstáculos detectados
        """
        # Cambiamos el estado el robot a inspeccion: luz amarilla
        await self.set_color_note('inspeccion', 1.5)

        # Creamos una matriz 3x3 donde la posición 1,1 es la posición del robot
        matriz = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]  # Inicialmente sin obstáculos

        # Comprobamos si hay obstáculos delante
        sensor = await self.get_ir_proximity()
        if sensor.sensors[2] < th:
            matriz[0][1] = 1  # Obstáculo frontal

        # Giramos el robot para inspeccionar los lados
        await self.giro('left', 90)
        sensor_left = await self.get_ir_proximity()
        if sensor_left.sensors[2] < th:
            matriz[1][0] = 1  # Obstáculo a la izquierda

        await self.giro('right', 180)
        sensor_right = await self.get_ir_proximity()
        if sensor_right.sensors[2] < th:
            matriz[1][2] = 1  # Obstáculo a la derecha

        # Devolvemos el robot a la posición original
        await self.giro('left', 90)

        return matriz

    def append_parada(self):
        """
        Método para añadir una parada (posición y obstáculos) al recorrido
        """
        # Obtenemos la posición actual del robot
        position = self.get_position()
        # Obtenemos la matriz de obstáculos detectados
        matriz_obstaculos = self.inspeccion()
        # Añadimos la parada al recorrido
        self.estado_robot['recorrido'][f'parada_{len(self.estado_robot["recorrido"])+1}'] = {
            'posicion': position,
            'obstaculos': matriz_obstaculos
        }

# Ejemplo de uso
explorer_robot = ExplorerRobot(Bluetooth())

# Evento de inicio del robot
@event(explorer_robot.when_play)
async def play():
    """
    Evento de inicio del robot
    """
    print(explorer_robot.get_position())  # Imprime la posición inicial
    await explorer_robot.set_color_note('moverse', 1)
    await explorer_robot.set_speed(20)  # Mover el robot
    print(explorer_robot.get_position())  # Imprime la posición después de moverse
    await explorer_robot.giro()  # giro aleatorio

# Inicia el robot
explorer_robot.play()
