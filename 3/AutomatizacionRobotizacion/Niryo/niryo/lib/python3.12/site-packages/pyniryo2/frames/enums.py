from enum import Enum, unique


@unique
class ManageFrames(Enum):
    """
    Enumeration of actions available for dynamic frames management
    """
    DELETE = -1
    SAVE = 1
    SAVE_WITH_POINTS = 2
    EDIT = 3
