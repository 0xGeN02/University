import roslibpy.actionlib

from pyniryo2.tool.enums import ToolCommand, ToolID
from pyniryo2.io.enums import PinID
from pyniryo2.exceptions import RobotCommandException


class ToolActions(object):

    def __init__(self, client):
        self.__client = client

        self.tool_action = None
        self.tool_action = roslibpy.actionlib.ActionClient(self.__client,
                                                           '/niryo_robot_tools_commander/action_server',
                                                           'niryo_robot_tools_commander/ToolAction')

    def __del__(self):
        if self.tool_action is not None:
            self.tool_action.cancel()
            self.tool_action.dispose()

    def get_gripper_action_goal(self, tool_id, tool_cmd, speed, max_torque_percentage, hold_torque_percentage):
        self._check_instance(tool_cmd, ToolCommand)
        self._check_instance(tool_id, ToolID)

        cmd = {'cmd_type': tool_cmd.value, 'tool_id': tool_id.value, 'speed': speed,
               'max_torque_percentage': max_torque_percentage, 'hold_torque_percentage': hold_torque_percentage}

        return roslibpy.actionlib.Goal(self.tool_action, roslibpy.Message({'cmd': cmd}))

    def get_vacuum_pump_action_goal(self, tool_cmd):
        self._check_instance(tool_cmd, ToolCommand)

        cmd = {'cmd_type': tool_cmd.value, 'tool_id': ToolID.VACUUM_PUMP_1.value,
               'activate': tool_cmd == ToolCommand.PULL_AIR_VACUUM_PUMP}

        return roslibpy.actionlib.Goal(self.tool_action, roslibpy.Message({'cmd': cmd}))

    def get_electromagnet_action_goal(self, tool_cmd, gpio=None):
        self._check_instance(tool_cmd, ToolCommand)
        if gpio is not None:
            self._check_instance(gpio, (PinID, str))

        pin = "" if gpio is None else gpio.value if isinstance(gpio, PinID) else gpio

        cmd = {'cmd_type': tool_cmd.value, 'tool_id': ToolID.ELECTROMAGNET_1.value,
               'activate': tool_cmd == ToolCommand.ACTIVATE_DIGITAL_IO, 'gpio': pin}

        return roslibpy.actionlib.Goal(self.tool_action, roslibpy.Message({'cmd': cmd}))

    def _check_instance(self, value, type_):
        if not isinstance(value, type_):
            self._raise_exception_expected_type(type_.__name__, value)

    def _raise_exception_expected_type(self, expected_type, given):
        raise RobotCommandException("Expected type: {}.\nGiven: {}".format(expected_type, given))
