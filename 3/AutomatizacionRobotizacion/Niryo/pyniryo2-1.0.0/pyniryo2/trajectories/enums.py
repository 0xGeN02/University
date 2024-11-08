from enum import Enum, unique


@unique
class ManageTrajectories(Enum):
    """
    Enumeration of actions available for saved trajectories management
    """
    DELETE_ALL = -2
    DELETE = -1
    SAVE = 1
    SAVE_LAST_LEARNED = 2
    UPDATE = 3
    EXECUTE = 4
    EXECUTE_REGISTERED = 5
