"""
framework/framework.py
"""

class Framework():
    """
    Definicion del mundo (representación del folio DIN_A3).
    """
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_width(self):
        """
        Ancho del mundo.
        """
        return self.width

    def get_height(self):
        """
        Alto del mundo.
        """
        return self.height

    def get_center(self):
        """
        Centro del mundo.
        """
        return (self.width / 2, self.height / 2)

    def get_corners(self):
        """
        Esquinas del mundo.
        """
        return [(0, 0), (0, self.height), (self.width, self.height), (self.width, 0)]
