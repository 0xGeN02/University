from enum import Enum, unique

@unique
class CalibrateMode(Enum):
    """
    Enumeration of Calibration Modes
    """
    AUTO = 1
    MANUAL = 2


@unique
class RobotAxis(Enum):
    """
    Enumeration of Robot Axis : it used for Shift command
    """
    X = 0
    Y = 1
    Z = 2
    ROLL = 3
    PITCH = 4
    YAW = 5

@unique
class JogShift(Enum):
    """
    Enumeration of Jog Shift : it used for Jog commands
    """
    JOINTS_SHIFT = 1
    POSE_SHIFT = 2
