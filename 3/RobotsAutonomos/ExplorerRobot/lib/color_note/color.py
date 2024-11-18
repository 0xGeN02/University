"""
Módulo que contiene la clase Color
"""
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
