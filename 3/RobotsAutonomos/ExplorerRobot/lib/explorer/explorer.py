"""
ExplorerRobot
"""
import math
import random

from irobot_edu_sdk.robots import Create3
from irobot_edu_sdk.music import Note
from lib.color_note import Color

class ExplorerRobot(Create3):
    """
    Extensión de la clase Create3 para el robot explorerRobot:
    - Navegación autónoma
    - Detección de obstáculos
    - Inspección de obstáculos
    - Recorrido y almacenamiento de posiciones
    """

    def __init__(self, backend):
        super().__init__(backend)
        self.data = {
            'name': 'ExplorerRobot',
            'version': '1.0.0',
            'dev': '0xGeN0',
            'author': 'Hugo, Jaqueline, Carlos, Mateo',
            'description': 'Robot autonomo que navega por un entorno con obstaculos y recuerda el recorrido',
            'status': 'In development',
            'license': 'MIT'
        }
        self.explore = {'recorrido': {}}

    async def set_color_note(self, select_group: str ='default', note_timer: int =1.5):
        """
        Método para cambiar el color de las luces y reproducir una nota
        """
        combinaciones = {
            'default': (Color.get_color('WHITE'), Note.A4),
            'moverse': (Color.get_color('BLUE'), Note.C4),
            'deteccion': (Color.get_color('RED'), Note.B4),
            'inspeccion': (Color.get_color('YELLOW'), Note.D4),
            'finalizacion': (Color.get_color('PURPLE'), Note.E4),
            'end_phase': (Color.get_color('GREEN'), Note.F4),
            'visitado': (Color.get_color('ORANGE'), Note.G4),
        }

        if select_group in combinaciones:
            color, nota = combinaciones[select_group]
            await self.set_lights_rgb(color[0], color[1], color[2])
            await self.play_note(nota, note_timer)
            return color, nota

        return 'Color/nota no encontrados', 'Nota no encontrada'

    async def set_speed(self, speed: int =15) -> str:
        """
        Método para establecer la velocidad de las ruedas
        """
        if speed == 0:
            await self.set_color_note('detener', 1.5)
            await self.set_wheel_speeds(0, 0)
            return 'Robot detenido'

        await self.set_color_note('moverse', 1.5)
        await self.set_wheel_speeds(speed, speed)
        return f'Robot moviéndose a {speed} mm/s'

    async def get_position(self) -> str:
        return {'x': self.pose.x, 'y': self.pose.y, 'theta': self.pose.heading}

    async def get_distance(self):
        """
        Método para obtener la distancia recorrida
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
        Método para girar a la izquierda o derecha
        """
        if turn is None:
            turn = random.choice(['left', 'right'])

        if turn == 'left':
            await self.turn_left(angle)
        elif turn == 'right':
            await self.turn_right(angle)

        return turn, angle

    async def append_parada(self):
        """
        Método para añadir una parada al recorrido
        """
        pose = await self.get_position()
        matriz = [['Undefined','Undefined','Undefined'], ['Undefined','ExplorerRobot','Undefined'], ['Undefined', 0,'Undefined']]
        current_idx = len(self.explore['recorrido'])
        self.explore['recorrido'][current_idx] = {'posicion': pose, 'matriz': matriz}
        return f'Parada {current_idx} añadida al recorrido'

    async def inspeccion(self, th: int = 150):
        """
        Método para inspeccionar los obstáculos
        @exit code: 200->seguir 400->parar
        """
        exit_code = None
        await self.set_color_note('inspeccion', 1.5)
        paradas = self.explore['recorrido']
        current_idx = len(paradas)-1
        current_parada = paradas[current_idx]
        matriz = current_parada['matriz']
        matriz[0][1] = 1
        turn, angle = await self.giro()

        if (turn, angle) == ('right', 90):
            sensor = (await self.get_ir_proximity()).sensors
            if sensor[3] > th:
                matriz[1][2] = 1
                await self.set_color_note('deteccion', 1.5)
                await self.set_color_note('inspeccion', 1.5)
                await self.giro('left', 180)
                sensor = (await self.get_ir_proximity()).sensors
                if sensor[3] > th:
                    matriz[1][0] = 1
                    await self.set_color_note('deteccion', 1.5)
                    exit_code = 400
                else:
                    matriz[1][0] = 0
                    await self.set_color_note('movimiento', 1.5)
                    exit_code = 200
            else:
                matriz[1][2] = 0
                matriz[1][0] = 'Not explored'
                await self.set_color_note('movimiento', 1.5)
                exit_code = 200

        elif (turn, angle) == ('left', 90):
            sensor = (await self.get_ir_proximity()).sensors
            if sensor[3] > th:
                matriz[1][0] = 1
                await self.set_color_note('deteccion', 1.5)
                await self.set_color_note('inspeccion', 1.5)
                await self.giro('right', 180)
                sensor = (await self.get_ir_proximity()).sensors
                if sensor[3] > th:
                    matriz[1][2] = 1
                    await self.set_color_note('deteccion', 1.5)
                    exit_code = 400
                else:
                    matriz[1][2] = 0
                    await self.set_color_note('movimiento', 1.5)
                    exit_code = 200
            else:
                matriz[1][0] = 0
                matriz[1][2] = 'Not explored'
                await self.set_color_note('movimiento', 1.5)
                exit_code = 200

        return matriz, current_idx, exit_code

    async def append_obstaculo(self, idx: int, matriz: list):
        """
        Método para añadir obstáculos a la parada
        """
        self.explore['recorrido'][idx]['matriz'] = matriz
        print(f'Obstáculos añadidos a la parada {idx}')
        print(matriz)

    async def detectar_obstaculos(self, th: int = 150):
        """
        Método para detectar obstáculos
        """
        while True:
            sensor = (await self.get_ir_proximity()).sensors
            if sensor[3] > th:
                await self.set_speed(0)
                await self.set_color_note('deteccion', 1.5)
                await self.append_parada()
                matriz, idx, code = await self.inspeccion()
                await self.append_obstaculo(idx, matriz)
                if code == 200:
                    await self.set_speed(20)
                    await self.set_color_note('moverse', 1.5)
                elif code == 400:
                    await self.set_speed(0)
                    await self.append_parada()
                    await self.set_color_note('end_phase', 1.5)
                    break
                else:
                    print('Error en el código de salida')
                    break

    async def recorrer_puntos(self, vueltas: int = 1, cambiar_color: bool = False):
        """
        Método para recorrer los puntos almacenados
        """
        colores = ['CYAN', 'MAGENTA', 'ORANGE', 'VIOLET']
        for i in range(vueltas):
            if i % 2 != 0:
                puntos = list(self.explore['recorrido'].values())
            else:
                puntos = list(self.explore['recorrido'].values())[::-1]
            print(f'Vuelta {i + 1}: Puntos a recorrer = {[punto["posicion"] for punto in puntos]}')
            for punto in puntos:
                posicion = punto['posicion']
                await self.set_color_note('moverse', 1.5)
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
        return self.explore['recorrido']

    def get_recorrido_json(self):
        """
        Método para obtener el recorrido y la data del robot en formato JSON
        """
        data = {
            "data": self.data,
            "explore": self.explore
        }
        return data

    async def recorrer_puntos_json(self, data: dict, vueltas: int = 1, cambiar_color: bool = False):
        """
        Método para recorrer los puntos almacenados en un archivo JSON
        """
        colores = ['CYAN', 'MAGENTA', 'ORANGE', 'VIOLET']
        paradas = data['explore']['recorrido'].values()

        if 'explore' not in data or 'recorrido' not in data['explore']:
            raise KeyError("El archivo JSON no contiene la estructura esperada.")

        current_position = None

        for i in range(vueltas):
            if i % 2 != 0:
                puntos = list(paradas)
            else:
                puntos = list(paradas)[::-1]
            print(f'Vuelta {i + 1}: Puntos a recorrer = {[punto["posicion"] for punto in puntos]}')
            for punto in puntos:
                posicion = punto['posicion']
                await self.set_color_note('moverse', 1.5)
                await self.navigate_to(posicion['x'], posicion['y'], posicion['theta'])
                await self.wait(1)
                current_position = posicion
                if cambiar_color:
                    color = random.choice(colores)
                    color_rgb = Color.get_color(color)
                    await self.set_lights_rgb(color_rgb[0], color_rgb[1], color_rgb[2])
                    await self.play_note(Note.C4, 1.5)
                else:
                    await self.set_color_note('visitado', 1.5)
        await self.set_color_note('end_phase', 1.5)
        return current_position