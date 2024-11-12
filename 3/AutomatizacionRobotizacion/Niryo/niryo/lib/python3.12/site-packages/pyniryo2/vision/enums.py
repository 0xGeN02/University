from enum import Enum, unique

# - Vision
@unique
class ObjectColor(Enum):
    """
    Enumeration of Colors available for image processing
    """
    RED = "RED"
    BLUE = "BLUE"
    GREEN = "GREEN"
    ANY = "ANY"


@unique
class ObjectShape(Enum):
    """
    Enumeration of Shapes available for image processing
    """
    SQUARE = "SQUARE"
    CIRCLE = "CIRCLE"
    ANY = "ANY"

@unique
class ManageWorkspace(Enum):
    """
    Enumeration of actions available for workspaces management
    """
    SAVE = 1
    SAVE_WITH_POINTS = 2
    DELETE = -1
