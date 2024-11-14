"""
 Practica 0: Dibujar figuras en el papel DinA3
"""
from typing import List, Literal
import pyniryo2 as pn2

# Conectivity Constants
ETHERNET_STATIC_IP : str = "169.254.200.200"
IP_ADDRESS: str = "127.0.0.1"
PORT = 9090
HOTSPOT_ADDRESS: str= "10.10.10.10"
HOTSPOT_NAME: str = "ea-40f-1a0"
HOTSPOT_PASSWORD: str = "niryorobot"

# World Constants
DIN_A3_WIDTH = 0.043
DIN_A3_HEIGHT = -0.2

# Robot Constants
ROBOT_X = -3.0
ROBOT_Y = 0.609
ROBOT_Z = -0.728
ROBOT_ROLL = -1.213
ROBOT_PITCH = 1.558
ROBOT_YAW = 0.061
INITIAL_COORDENATE = [ROBOT_X, ROBOT_Y, ROBOT_Z, ROBOT_ROLL, ROBOT_PITCH, ROBOT_YAW]

class World():
    """
    Definicion del mundo (representracion del folio DIN_A3)
    """
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_width(self):
        """
        Ancho del mundo
        """
        return self.width

    def get_height(self):
        """
        Alto del mundo
        """
        return self.height

    def get_center(self):
        """
        Centro del mundo
        """
        return (self.width / 2, self.height / 2)

    def get_corners(self):
        """
        Esquinas del mundo
        """
        return [(0, 0), (0, self.height), (self.width, self.height), (self.width, 0)]

class RobotDrawer(pn2.NiryoRobot):
    """
    Definicion del robot que es capaz de dibujar
    """
    def __init__(self, hotspot_address: str, port: int):
        super().__init__(hotspot_address, port)
        self.arm.calibrate_auto()
        self.arm.go_to_sleep()
        self.tool.update_tool()

    def draw_square(self, center: List[float], side: float, height: float = 0.1):
        """
        Dibujar un cuadrado en el mundo
        @param center_x: Centro del cuadrado en el eje x
        @param center_y: Centro del cuadrado en el eje y
        @param side: Lado del cuadrado
        @param n: Altura z del robot respecto al folio
        """
        half_side = side / 2
        corners = [
            (center[0] - half_side, center[1] - half_side),
            (center[0] - half_side, center[1] + half_side),
            (center[0] + half_side, center[1] + half_side),
            (center[0] + half_side, center[1] - half_side)
        ]

        for point in corners:
            if point == corners[0]:
                self.arm.pose([point[0], point[1], -height, 0.0, 0.0, 0.0])
            self.arm.pose([point[0], point[1], 0.0, 0.0, 0.0, 0.0])

    def draw_triangle(self, center: List[float], type: Literal['equilatero', 'escaleno', 'isosceles']):
        """
        Dibujar un triángulo
        """
        if type in ['equilatero', 'escaleno', 'isosceles']:
            if type == 'equilatero':
                pass
            elif type == 'escaleno':
                pass
            else:
                pass
        else:
            print('Triangle TYPE not defined')

    def draw_circle(self, center: List[float], radius: float):
        """
        Dibujar un circulo dado el radio
        """
        pass         

def main():
    """
    Main function
    """
    # Crear el mundo
    paper = World(DIN_A3_WIDTH, DIN_A3_HEIGHT)

    # Conectar al robot
    robot = RobotDrawer(HOTSPOT_ADDRESS, PORT)

    # Verificar la conexión del robot
    if robot is None:
        print("Robot connection failed.")
    else:
        print("Robot connected successfully.")

    # Calcular el centro del mundo
    paper_center = paper.get_center()

    #Subimos en el eje z el robot para no pintar el papel mientras lo llevamos al primer vertice
    height = 0,1
    INITIAL_COORDENATE[3] = INITIAL_COORDENATE[3] + height
    robot.arm.move_joints(INITIAL_COORDENATE)

    #Asociamos el centro del robot con las coordenadas del robot
    robot_center = [paper_center[0]+ ROBOT_X, paper_center[1] + ROBOT_Y]

    # Dibujar un cuadrado
    robot.draw_square([robot_center[0], robot_center[1]], 0.1)

if __name__ == "__main__":
    main()
