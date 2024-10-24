"""
Practica 4: Funcionalizar el codigo del iRobot Create3
"""

import math
import random
from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, Create3
from irobot_edu_sdk.music import Note

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
    ORANGE = (255, 75, 8)
    VIOLET = (238, 130, 238)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BROWN = (165, 42, 42)

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
        - Navegación autónoma
        - Detección de obstáculos
        - Inspección de obstáculos
        - Recorrido y almacenamiento de posiciones
    """

    def __init__(self, backend):
        """
        Constructor de la clase ExplorerRobot que hereda de Create3
        """
        super().__init__(backend)
        #Datos de declaracion del robot
        self.data = {
            'name': 'ExplorerRobot',
            'version': '1.0.0',
            'author': 'Hugo, Jaqueline, Carlos, Mateo',
            'description': 'Robot autónomo que navega por un entorno con obstaculos y recuerda el recorrido',
            'status': 'In development',
            'license': 'MIT'
        }
        # Diccionario que agrupa toda la información del recorrido y estado del robot
        self.explore = {
            'recorrido': {
                #'0': {
                #   'posicion': {'x': 0, 'y': 0, 'theta': 0},
                #   'matriz': [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
                # },
                #'1': {
                #   'posicion': {'x': 0, 'y': 0, 'theta': 0},
                #   'matriz': [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
                # }
            }   # Recorrido completo con obstáculos y paradas
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
            'moverse': (Color.get_color('BLUE'), Note.C4),
            'deteccion': (Color.get_color('RED'), Note.B4),
            'inspeccion': (Color.get_color('YELLOW'), Note.D4),
            'finalizacion': (Color.get_color('PURPLE'), Note.E4),
            'end_phase': (Color.get_color('GREEN'), Note.F4),
            'visitado': (Color.get_color('ORANGE'), Note.G4),
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
        recorrido = self.explore['recorrido']
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

    async def append_parada(self):
        """
        Metodo para crear un punto
        [idx]:
            {
                Posicion: {'x': x,'y': y,'theta': theta},
                Matriz:   [][][],[][][],[][][]
            }
        y añadirlo al recorrido
        call: await explorer_robot.append_parada()
        """
        #Creamos la posicion [idx] y la añadimos al recorrido
        #Obtenemos el pose actual del robot
        pose = await self.get_position()
        #Creamos la matriz
        matriz = [['Undefined','Undefined','Undefined'], ['Undefined','ExplorerRobot','Undefined'], ['Undefined', 0,'Undefined']]

        # Obtenemos el numero de paradas actuales
        current_idx = len(self.explore['recorrido'])

        # Creamos y guardamos la parada como idx en el recorrido
        self.explore['recorrido'][current_idx] = {
            'posicion': pose,
            'matriz': matriz
        }
        return f'Parada {current_idx} añadida al recorrido'

    async def inspeccion(self, th: int = 150):
        """
        Método para inspeccionar los obstáculos tanto frontal como a los lados
        @exit_code: @default: None, 200=>Free Space, 400=> Blocked
        @return: Retorna la matriz de obstáculos detectados
        """

        exit_code = None

        # Cambiamos el estado el robot a inspeccion: luz amarilla
        await self.set_color_note('inspeccion', 1.5)

        # Recuperamos la ultima parada
        paradas = self.explore['recorrido']
        current_idx = len(paradas)-1
        current_parada = paradas[current_idx]
        matriz = current_parada['matriz']

        # Determinamos el obstaculo de delante
        matriz[0][1] = 1

        #hacer giro aleatorio
        turn, angle = await self.giro()

        #Si gira a la derecha:
        if (turn, angle) == ('right', 90):
            # Derecha si
            sensor = (await self.get_ir_proximity()).sensors
            if sensor[3] > th:
                matriz[1][2] = 1
                await self.set_color_note('deteccion', 1.5)
                await self.set_color_note('inspeccion', 1.5)

                # Giramos a la izquierda 180 grados
                await self.giro('left', 180)
                #Detectamos si hay obstaculo en la izquierda
                sensor = (await self.get_ir_proximity()).sensors
                if sensor[3] > th:
                    matriz[1][0] = 1
                    await self.set_color_note('deteccion', 1.5)
                    # Derecha si Izquierda si
                    exit_code = 400
                #Derecha si Izquierda no
                else:
                    matriz[1][0] = 0
                    await self.set_color_note('movimiento', 1.5)
                    exit_code = 200
            #Derecha no        exit_code = 200
            else:
                matriz[1][2] = 0
                matriz[1][0] = 'Not explored'
                await self.set_color_note('movimiento', 1.5)
                exit_code = 200

        #Si gira a la izquierda:
        elif (turn, angle) == ('left', 90):
            # Izquierda si
            sensor = (await self.get_ir_proximity()).sensors
            if sensor[3] > th:
                matriz[1][0] = 1
                await self.set_color_note('deteccion', 1.5)
                await self.set_color_note('inspeccion', 1.5)

                # Giramos a la derecha 180 grados
                await self.giro('right', 180)

                #Detectamos si hay obstaculo en la derecha
                # Izquierda si Derecha si   exit_code = 400
                sensor = (await self.get_ir_proximity()).sensors
                if sensor[3] > th:
                    matriz[1][2] = 1
                    await self.set_color_note('deteccion', 1.5)
                    exit_code = 400
                #Izquierda si Derecha no      exit_code = 200
                else:
                    matriz[1][2] = 0
                    await self.set_color_note('movimiento', 1.5)
                    exit_code = 200
            #Izquierda no        exit_code = 200
            else:
                matriz[1][0] = 0
                matriz[1][2] = 'Not explored'
                await self.set_color_note('movimiento', 1.5)
                exit_code = 200

        return matriz, current_idx, exit_code

    async def append_obstaculo(self, idx: int, matriz: list):
        """
        Método para añadir un obstáculo a la matriz de obstáculos de una parada
        @param idx: Índice de la parada
        @param matriz: Matriz de obstáculos
        @return: Retorna la matriz de obstáculos actualizada
        call: await explorer_robot.append_obstaculo(0, [[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        """
        # Añadir la matriz de obstáculos a la parada correspondiente
        self.explore['recorrido'][idx]['matriz'] = matriz
        print(f'Obstáculos añadidos a la parada {idx}')
        print(matriz)

    async def detectar_obstaculos(self, th: int = 150):
        """
        Método para detectar obstáculos y navegar por ellos
        @param th: Distancia de detección de obstáculos
        @return: 
        """
        while True:
            sensor = (await self.get_ir_proximity()).sensors
            if sensor[3] > th:
                await self.set_speed(0)
                await self.set_color_note('deteccion', 1.5)

                # Creamos la posicion P[idx] y la añadimos al recorrido
                await self.append_parada()
                #LLamamos a inspeccion
                matriz, idx, code = await self.inspeccion()

                #Añadimos la matriz a la parada
                await self.append_obstaculo(idx, matriz)

                #Hacemos un switch case para el exit_code
                if code == 200:
                    await self.set_speed(20)
                    await self.set_color_note('moverse', 1.5)
                elif code == 400:
                    await self.set_speed(0)
                    await self.set_color_note('end_phase', 1.5)
                    break
                else:
                    print('Error en el código de salida')
                    break

    async def recorrer_puntos(self, vueltas: int = 1, cambiar_color: bool = False):
        """
        Método para recorrer los puntos almacenados en el recorrido
        @param vueltas: Número de vueltas a realizar
        @param cambiar_color: Indica si se debe cambiar el color en cada punto visitado
        @if: Si i es par, recorre los puntos en el orden almacenado; si es impar, recorre inversamente el array
        @return: Retorna el recorrido completo
        """

        colores = ['CYAN', 'MAGENTA', 'ORANGE', 'VIOLET']

        for i in range(vueltas):
            # Si la vuelta es par, recorrer los puntos en orden normal
            if i % 2 != 0:
                puntos = list(self.explore['recorrido'].values())
            # Si la vuelta es impar, recorrer los puntos en orden inverso
            else:
                puntos = list(self.explore['recorrido'].values())[::-1]  # [::-1] invierte la lista

            # Imprimir los puntos que se van a recorrer en esta vuelta
            print(f'Vuelta {i + 1}: Puntos a recorrer = {[punto["posicion"] for punto in puntos]}')

            for punto in puntos:
                # Obtenemos la posicion del punto a visitar (comenzando en 0 o en el último)
                posicion = punto['posicion']
                await self.set_color_note('moverse', 1.5)

                # Dirigimos el robot a la posición almacenada
                await self.navigate_to(posicion['x'], posicion['y'], posicion['theta'])
                await self.wait(1)

                if cambiar_color is True:
                    color = random.choice(colores)
                    color_rgb = Color.get_color(color)
                    await self.set_lights_rgb(color_rgb[0], color_rgb[1], color_rgb[2])
                    await self.play_note(Note.C4, 1.5)
                else:
                    await self.set_color_note('visitado', 1.5)

        await self.set_color_note('end_phase', 1.5)
        return 'Recorrido completo'

backend_instance = Bluetooth()
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
    print('Fin de la misión')

explorer.play()
