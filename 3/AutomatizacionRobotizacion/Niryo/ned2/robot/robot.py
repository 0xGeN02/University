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

    def move_to_position(self, x: float = None, y: float = None, z: float = None,
                               roll: float = None, pitch: float = None, yaw: float = None):
        """
        Mueve el robot a una posición específica desde la actual.
        """
        current_pose: NiryoTopic = self.arm.get_pose()
        print(f'La posición actual es:\n {current_pose}')
        if current_pose is None:
            raise ValueError("No se puede obtener la posición actual del robot.")

        new_pose = [
            (current_pose.x + x) if x is not None else current_pose.x,
            (current_pose.y + y) if y is not None else current_pose.y,
            (current_pose.z + z) if z is not None else current_pose.z,
            (current_pose.roll + roll) if roll is not None else current_pose.roll,
            (current_pose.pitch + pitch) if pitch is not None else current_pose.pitch,
            (current_pose.yaw + yaw) if yaw is not None else current_pose.yaw
        ]
        self.arm.move_pose(new_pose)

    def move_to_starting_point(self):
        """
        Mueve el robot a las coordenadas iniciales definidas.
        """
        self.arm.move_pose(config.INITIAL_COORDENATE)

    def draw_square(self,center: List[float], side:float) -> None:
        """
        Dibuja un cuadrado en el papel.
        """
        corners = ShapeDrawer.calculate_square_corners(center, side)
        # Mover el robot a cada esquina del cuadrado
        for point in corners:
            self.move_to_position(x=point[0], y=point[1])

        #Volvemos al punto de inicio para cerrar el cuadrado
        self.move_to_position(x=corners[0][0], y=corners[0][1])
