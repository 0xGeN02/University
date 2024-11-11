from enum import Enum, unique


@unique
class ConveyorID(Enum):
    """
    ConveyorID to be able to have CAN (id 12 and 13) and TTL (id 9 and 10) conveyor in any possible combination

    ID_1 = 12   # One, Ned
    ID_2 = 13   # One, Ned
    ID_3 = 9    # Ned2
    ID_4 = 10   # Ned2
    """
    NONE = 0
    ID_1 = -1
    ID_2 = -2


@unique
class ConveyorCan(Enum):
    """
    ConveyorID to control conveyors with CAN interface
    """

    NONE = 0
    ID_1 = 12
    ID_2 = 13


@unique
class ConveyorTTL(Enum):
    """
    ConveyorID to control conveyors with TTL interface
    """

    NONE = 0
    ID_1 = 9
    ID_2 = 10


@unique
class ConveyorDirection(Enum):
    """
    Enumeration of the directions of the conveyor
    """

    FORWARD = 1
    BACKWARD = -1


@unique
class ConveyorStatus(Enum):
    """
    Enumeration of the different Conveyor status
    """

    ADD = 1
    REMOVE = 2
