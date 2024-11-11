from enum import Enum, unique


@unique
class ManagePose(Enum):
    """
    Enumeration of actions available for saved poses management
    """
    DELETE = -1
    SAVE = 1
