"""
robot/robot.py
"""

from typing import List
import pyniryo2 as pn2
from pyniryo2 import NiryoTopic
from constants import config
from robot.shapes import ShapeDrawer

class RobotDrawer(pn2.NiryoRobot):
    """
    Definición del robot que es capaz de dibujar.
    """
    def __init__(self, hotspot_address: str, port: int):
        super().__init__(hotspot_address, port)
        self.arm.calibrate_auto()
        self.arm.go_to_sleep()
        self.tool.update_tool()

    def move_to_starting_point(self):
        """
        Mueve el robot a las coordenadas iniciales definidas.
        """
        self.arm.move_pose(config.INITIAL_COORDENATE)

    def draw_square(self,center: List[float], side:float) -> None:
        """
        Dibuja un cuadrado en el espacio de lado @param:side
        """
        corners = ShapeDrawer.calculate_square_corners(center, side)
        # Mover el robot a cada esquina del cuadrado
        for point in corners:
            punto = self.relative_pose()
            self.arm.move_pose()

        #Volvemos al punto de inicio para cerrar el cuadrado
        self.arm.move_pose()
    