from enum import Enum, unique


@unique
class ToolID(Enum):
    """
    Enumeration of Tools IDs
    """
    NONE = 0
    GRIPPER_1 = 11
    GRIPPER_2 = 12
    GRIPPER_3 = 13
    GRIPPER_4 = 14
    ELECTROMAGNET_1 = 30
    VACUUM_PUMP_1 = 31


@unique
class ToolCommand(Enum):
    # Gripper
    OPEN_GRIPPER = 1
    CLOSE_GRIPPER = 2

    # Vacuump pump
    PULL_AIR_VACUUM_PUMP = 10
    PUSH_AIR_VACUUM_PUMP = 11

    # Tools controlled by digital I/Os
    SETUP_DIGITAL_IO = 20
    ACTIVATE_DIGITAL_IO = 21
    DEACTIVATE_DIGITAL_IO = 22
