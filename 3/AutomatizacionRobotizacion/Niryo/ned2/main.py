import pyniryo2 as pn2

# Conectivity Constants
ETHERNET_STATIC_IP : str = "169.254.200.200"
IP_ADDRESS: str = "127.0.0.1"
PORT = 9090
HOTSPOT_ADDRESS: str= "10.10.10.10"
HOTSPOT_NAME: str = "ea-40f-1a0"
HOTSPOT_PASSWORD: str = "niryorobot"

# World Constants
DIN_A3_WIDTH = 0.42
DIN_A3_HEIGHT = 0.297
ROBOT_X = None
ROBOT_Y = None
ROBOT_Z = None
ROBOT_ROLL = None
ROBOT_PITCH = None
ROBOT_YAW = None

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

class Robot():
    """
    Definicion del robot
    """
    def __init__(self, robot: pn2.NiryoRobot = None):
        self.robot = robot

    def get_robot(self):
        """
        Devuelve el robot
        """
        return self.robot

    def connect_hotspot(self, hotspot_address: str, port: int):
        """
        Conectarse al hotspot
        """

        self.robot = pn2.NiryoRobot(hotspot_address, port)
        self.robot.arm.calibrate_auto()
        self.robot.arm.go_to_sleep()
        self.robot.tool.update_tool()

    def robot_to_world(self, x:float, y: float, z: float, roll: float, pitch: float, yaw: float):
        """
        Asociar coordenadas del robot con el mundo
        """
        if(x | y | z | roll | pitch | yaw) is None:
            return "Error: No se han definido las coordenadas del robot"
        return (x, y, z, roll, pitch, yaw)

    def draw_square(self, center: list[x: float, y:float, z: float], side: float):
        """
        Dibujar un cuadrado en el mundo
        @param center_x: Centro del cuadrado en el eje x
        @param center_y: Centro del cuadrado en el eje y
        @param side: Lado del cuadrado
        @param n: Altura z del robot respecto al folio
        """
        half_center = side / 2
        corners = [(center.x - half_center, center.y - half_center),
                   (center.x - half_center, center.y + half_center),
                   (center.x + half_center, center.y + half_center),
                   (center.x + half_center, center.y - half_center)]
        for point in corners:
            self.robot.arm.move_joints([point[0], point[1], point[2], 0, 0, 0])

    def draw_triangle(self, center: list [x:float, y: float, z: float | None], type: str ='equilatero'):
        """
        
        """
        if type in ['equilatero', 'escaleno', 'isosceles']:
            if type == 'equilatero':
                pass
            elif type == 'escaleno':
                pass
            else:
                pass
        else:
            'Triangle TYPE not defined'

    def draw_circle(self, center: list[x: float, y:float, z:float | None], radius: float):
        """
        
        """
        pass         


def main():
    """
    Main function
    """
    # Create the world
    world = World(DIN_A3_WIDTH, DIN_A3_HEIGHT)

    # Create the robot
    robot = Robot()

    # Connect to the hotspot
    robot.connect_hotspot(HOTSPOT_ADDRESS, PORT)

    if robot.get_robot() is None:
        print("Robot connection failed.")
    else:
        print("Robot connected successfully.")



if __name__ == "__main__":
    main()