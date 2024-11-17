"""
robot/shapes.py
"""

from typing import List, Literal

class ShapeDrawer:
    """
    Clase que dibuja formas geométricas.
    """
    @staticmethod
    def calculate_square_corners(center: List[float], side: float) -> List[List[float]]:
        """
        Calcula las esquinas de un cuadrado dado su centro y lado.
        """
        half_side = side / 2
        return [
            [center[0] - half_side, center[1] - half_side],
            [center[0] - half_side, center[1] + half_side],
            [center[0] + half_side, center[1] + half_side],
            [center[0] + half_side, center[1] - half_side]
        ]

    @staticmethod
    def calculate_triangle_corners(center: List[float], type: Literal['rectangulo', 'equilatero'], side: float) -> List[List[float]]:
        """
        Calcula las esquinas de un triángulo dado su centro y tipo.
        """
        if type == 'rectangulo':
            half_side = side / 2
            return [
                [center[0] - half_side, center[1] - half_side],
                [center[0] - half_side, center[1] + half_side],
                [center[0] + half_side, center[1] + half_side]
            ]
        elif type == 'equilatero':
            return [
                [center[0], center[1] + side],
                [center[0] - side, center[1] - side],
                [center[0] + side, center[1] - side]
            ]
