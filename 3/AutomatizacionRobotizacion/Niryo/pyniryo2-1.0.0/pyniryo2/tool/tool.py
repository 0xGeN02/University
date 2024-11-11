# - Imports
from __future__ import print_function

# Communication imports
from pyniryo2.exceptions import RobotCommandException
from pyniryo2.robot_commander import RobotCommander
from pyniryo2.enums import RobotErrors
from pyniryo2.io.enums import PinID

from .enums import ToolID, ToolCommand
from .services import ToolServices
from .actions import ToolActions
from .topics import ToolTopics


class Tool(RobotCommander):
    def __init__(self, client):
        """
        Tool robot functions

        Example: ::

            ros_instance = NiryoRos("10.10.10.10") # Hotspot
            tool_interface = Tool(ros_instance)

        :param client: Niryo ROS client
        :type client: NiryoRos
        """
        super(Tool, self).__init__(client)

        self._services = ToolServices(self._client)
        self._topics = ToolTopics(self._client)
        self._actions = ToolActions(self._client)

        self.__action_timeout = 10

    @property
    def tool(self):
        """

        :return: The equipped tool ID
        :rtype: ToolID
        """
        return self.get_current_tool_id()

    @property
    def get_current_tool_id(self):
        """
        Returns the equipped tool Id client which can be used synchronously or asynchronously
        to obtain the equipped tool Id.
        The topic returns a attribute of the ToolID enum.

        Examples: ::

            # Get last value
            tool.get_current_tool_id()
            tool.get_current_tool_id.value

            # Subscribe a callback
            def tool_id_callback(tool_id_object):
                print tool_id_object

            tool.get_current_tool_id.subscribe(tool_id_callback)
            tool.get_current_tool_id.unsubscribe()

        :return: the equipped tool Id topic instance.
        :rtype: NiryoTopic
        """
        return self._topics.tool_id_topic

    def update_tool(self, callback=None, errback=None, timeout=None):
        """
        Update equipped tool

        Examples: ::

            # Synchronous use
            tool.update_tool()

            # Asynchronous use
            def update_tool_callback(result):
                if result["status"] < RobotErrors.SUCCESS.value:
                    print("Update failed")
                else:
                    print("Update completed with success")

            tool.update_tool(update_tool_callback)

        :param callback: Callback invoked on successful execution.
        :type callback: function
        :param errback: Callback invoked on error.
        :type errback: function
        :param timeout: Timeout for the operation, in seconds. Only used if blocking.
        :rtype: None
        """
        req = self._services.get_trigger_request()
        result = self._services.update_tool_service.call(req, callback, errback, timeout)

        if callback is None:
            self._check_result_status(result)

    def grasp_with_tool(self, callback=None):
        """
        Grasp with tool
        This action correspond to
        * Close gripper for Grippers
        * Pull Air for Vacuum pump
        * Activate for Electromagnet
        If a callback function is not passed in parameter, the function will be blocking.
        Otherwise, the callback will be called when the execution of the function is finished.

        Examples: ::

            tool.update_tool()
            tool.grasp_with_tool()
            
            def tool_callback(_msg)
                print("Grasped") 
                
            tool.grasp_with_tool(callback=tool_callback)

        :param callback: Callback invoked on successful execution.
        :type callback: function
        :rtype: None
        """
        tool_id = self.get_current_tool_id()

        if tool_id in (ToolID.GRIPPER_1, ToolID.GRIPPER_2, ToolID.GRIPPER_3, ToolID.GRIPPER_4):
            return self.close_gripper(callback=callback)
        elif tool_id == ToolID.VACUUM_PUMP_1:
            return self.pull_air_vacuum_pump(callback=callback)
        elif tool_id == ToolID.ELECTROMAGNET_1:
            return self.activate_electromagnet(callback=callback)

    def release_with_tool(self, callback=None):
        """
        Release with tool
        This action correspond to
        * Open gripper for Grippers
        * Push Air for Vacuum pump
        * Deactivate for Electromagnet
        If a callback function is not passed in parameter, the function will be blocking.
        Otherwise, the callback will be called when the execution of the function is finished.

        Examples: ::

            tool.update_tool()
            tool.release_with_tool()
            
            def tool_callback(_msg)
                print("Released")
                
            tool.release_with_tool(callback=tool_callback)

        :param callback: Callback invoked on successful execution.
        :type callback: function
        :rtype: None
        """
        tool_id = self.get_current_tool_id()

        if tool_id in (ToolID.GRIPPER_1, ToolID.GRIPPER_2, ToolID.GRIPPER_3, ToolID.GRIPPER_4):
            return self.open_gripper(callback=callback)
        elif tool_id == ToolID.VACUUM_PUMP_1:
            return self.push_air_vacuum_pump(callback=callback)
        elif tool_id == ToolID.ELECTROMAGNET_1:
            return self.deactivate_electromagnet(callback=callback)

    # - Gripper
    def open_gripper(self, speed=500, max_torque_percentage=100, hold_torque_percentage=30, callback=None):
        """
        Open gripper associated to the equipped gripper.
        If a callback function is not passed in parameter, the function will be blocking.
        Otherwise, the callback will be called when the execution of the function is finished.

        Examples: ::

            tool.update_tool()
            tool.open_gripper()

            # Niryo One and Ned
            tool.open_gripper(speed=850)

            # Ned2
            tool.open_gripper(max_torque_percentage=100, hold_torque_percentage=50)
            
            def tool_callback(_msg)
                print("Released")
                
            tool.open_gripper(callback=tool_callback)

        :param speed: Between 100 & 1000 (only for Niryo One and Ned1)
        :type speed: int
        :param max_torque_percentage: Closing torque percentage (only for Ned2)
        :type max_torque_percentage: int
        :param hold_torque_percentage: Hold torque percentage after closing (only for Ned2)
        :type hold_torque_percentage: int
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :rtype: None
        """
        speed = self._transform_to_type(speed, int)
        self._check_range_belonging(speed, 1, 1000)

        max_torque_percentage = self._transform_to_type(max_torque_percentage, int)
        self._check_range_belonging(max_torque_percentage, 0, 100)

        hold_torque_percentage = self._transform_to_type(hold_torque_percentage, int)
        self._check_range_belonging(hold_torque_percentage, 0, 100)

        tool_id = self.get_current_tool_id()
        if tool_id not in [ToolID.GRIPPER_1, ToolID.GRIPPER_2, ToolID.GRIPPER_3]:
            raise RobotCommandException("Call update_tool before using the open_gripper function")

        goal = self._actions.get_gripper_action_goal(tool_id, ToolCommand.OPEN_GRIPPER,
                                                     speed, max_torque_percentage, hold_torque_percentage)
        goal.send(result_callback=callback)

        if callback is None:
            self._check_result_status(goal.wait(self.__action_timeout))

    def close_gripper(self, speed=500, max_torque_percentage=100, hold_torque_percentage=30, callback=None):
        """
        Close gripper associated to 'gripper_id' with a speed 'speed'
        If a callback function is not passed in parameter, the function will be blocking.
        Otherwise, the callback will be called when the execution of the function is finished.

        Examples: ::

            tool.update_tool()
            tool.close_gripper()

            # Niryo One and Ned
            tool.close_gripper(speed=850)

            # Ned2
            tool.close_gripper(max_torque_percentage=100, hold_torque_percentage=50)

            def tool_callback(_msg)
                print("Grasped")

            tool.close_gripper(callback=tool_callback)

        :param speed: Between 100 & 1000 (only for Niryo One and Ned1)
        :type speed: int
        :param max_torque_percentage: Opening torque percentage (only for Ned2)
        :type max_torque_percentage: int
        :param hold_torque_percentage: Hold torque percentage after opening (only for Ned2)
        :type hold_torque_percentage: int
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :rtype: None
        """
        speed = self._transform_to_type(speed, int)
        self._check_range_belonging(speed, 1, 1000)

        max_torque_percentage = self._transform_to_type(max_torque_percentage, int)
        self._check_range_belonging(max_torque_percentage, 0, 100)

        hold_torque_percentage = self._transform_to_type(hold_torque_percentage, int)
        self._check_range_belonging(hold_torque_percentage, 0, 100)

        tool_id = self.get_current_tool_id()
        if tool_id not in [ToolID.GRIPPER_1, ToolID.GRIPPER_2, ToolID.GRIPPER_3]:
            raise RobotCommandException("Call update_tool before using the close_gripper function")

        goal = self._actions.get_gripper_action_goal(tool_id, ToolCommand.CLOSE_GRIPPER,
                                                     speed, max_torque_percentage, hold_torque_percentage)
        goal.send(result_callback=callback)

        if callback is None:
            self._check_result_status(goal.wait(self.__action_timeout))

        # - Vacuum

    def pull_air_vacuum_pump(self, callback=None):
        """
        Pull air of vacuum pump
        If a callback function is not passed in parameter, the function will be blocking.
        Otherwise, the callback will be called when the execution of the function is finished.

        Examples: ::

            tool.update_tool()
            tool.pull_air_vacuum_pump()

            def tool_callback(_msg)
                print("Grasped")

            tool.pull_air_vacuum_pump(callback=tool_callback)


        :param callback: Callback invoked on successful execution.
        :type callback: function
        :rtype: None
        """
        tool_id = self.get_current_tool_id()
        if tool_id not in [ToolID.VACUUM_PUMP_1]:
            raise RobotCommandException("Call update_tool before using the pull_air_vacuum_pump function")

        goal = self._actions.get_vacuum_pump_action_goal(ToolCommand.PULL_AIR_VACUUM_PUMP)
        goal.send(result_callback=callback)

        if callback is None:
            self._check_result_status(goal.wait(self.__action_timeout))

    def push_air_vacuum_pump(self, callback=None):
        """
        Push air of vacuum pump
        If a callback function is not passed in parameter, the function will be blocking.
        Otherwise, the callback will be called when the execution of the function is finished.

        Examples: ::

            tool.update_tool()
            tool.push_air_vacuum_pump()

            def tool_callback(_msg)
                print("Released")

            tool.push_air_vacuum_pump(callback=tool_callback)


        :param callback: Callback invoked on successful execution.
        :type callback: function
        :rtype: None
        """
        tool_id = self.get_current_tool_id()
        if tool_id not in [ToolID.VACUUM_PUMP_1]:
            raise RobotCommandException("Call update_tool before using the push_air_vacuum_pump function")

        goal = self._actions.get_vacuum_pump_action_goal(ToolCommand.PUSH_AIR_VACUUM_PUMP)
        goal.send(result_callback=callback)

        if callback is None:
            self._check_result_status(goal.wait(self.__action_timeout))

    # - Electromagnet

    def setup_electromagnet(self, pin_id):
        """
        Setup electromagnet on pin

        Example: ::

            tool.setup_electromagnet(PinID.GPIO_1A)
        
        :param pin_id:
        :type pin_id: PinID
        :rtype: None
        """
        self._check_instance(pin_id, (PinID, str))

        req = self._services.equip_electromagnet_service_request()
        self._services.equip_electromagnet_service.call(req)

        goal = self._actions.get_electromagnet_action_goal(ToolCommand.SETUP_DIGITAL_IO, pin_id)
        goal.send()
        self._check_result_status(goal.wait(self.__action_timeout))

    def activate_electromagnet(self, pin_id=None, callback=None):
        """
        Activate electromagnet associated to electromagnet_id on pin_id
        If a callback function is not passed in parameter, the function will be blocking.
        Otherwise, the callback will be called when the execution of the function is finished.

        Examples: ::

            tool.setup_electromagnet(PinID.GPIO_1A)
            tool.activate_electromagnet()
            tool.activate_electromagnet(PinID.GPIO_1A)
            
            def tool_callback(_msg)
                print("Grasped") 
                
            tool.activate_electromagnet(callback=tool_callback)
            
        :param pin_id:
        :type pin_id: PinID
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :rtype: None
        """
        if pin_id is not None:
            self._check_instance(pin_id, (PinID, str))

        if self.get_current_tool_id() != ToolID.ELECTROMAGNET_1:
            if pin_id:
                self.setup_electromagnet(pin_id)
            else:
                raise RobotCommandException(
                    "Call setup_electromagnet before using activate_electromagnet or specify a pin ID.")

        goal = self._actions.get_electromagnet_action_goal(ToolCommand.ACTIVATE_DIGITAL_IO, pin_id)
        goal.send(result_callback=callback)

        if callback is None:
            self._check_result_status(goal.wait(self.__action_timeout))

    def deactivate_electromagnet(self, pin_id=None, callback=None):
        """
        Deactivate electromagnet associated to electromagnet_id on pin_id
        If a callback function is not passed in parameter, the function will be blocking.
        Otherwise, the callback will be called when the execution of the function is finished.

        Examples: ::

            tool.setup_electromagnet(PinID.GPIO_1A)
            tool.deactivate_electromagnet()
            tool.deactivate_electromagnet(PinID.GPIO_1A)

            def tool_callback(_msg)
                print("Deactivated")

            tool.deactivate_electromagnet(callback=tool_callback)
            
        :param pin_id:
        :type pin_id: PinID
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :rtype: None
        """
        if pin_id is not None:
            self._check_instance(pin_id, (PinID, str))

        if self.get_current_tool_id() != ToolID.ELECTROMAGNET_1:
            if pin_id:
                self.setup_electromagnet(pin_id)
            else:
                raise RobotCommandException(
                    "Call setup_electromagnet before using deactivate_electromagnet or specify a pin ID.")

        goal = self._actions.get_electromagnet_action_goal(ToolCommand.DEACTIVATE_DIGITAL_IO, pin_id)
        goal.send(result_callback=callback)

        if callback is None:
            self._check_result_status(goal.wait(self.__action_timeout))

    def enable_tcp(self, enable=True):
        """
        Enables or disables the TCP function (Tool Center Point).
        If activation is requested, the last recorded TCP value will be applied.
        The default value depends on the gripper equipped.
        If deactivation is requested, the TCP will be coincident with the tool_link.

        :param enable: True to enable, False otherwise.
        :type enable: Bool
        :rtype: None
        """
        self._check_type(enable, bool)
        req = self._services.enable_tcp_service_request(enable)
        result = self._services.enable_tcp_service.call(req)
        self._check_result_status(result)

    def set_tcp(self, *args):
        """
        Activates the TCP function (Tool Center Point)
        and defines the transformation between the tool_link frame and the TCP frame.

        Examples: ::

            tool.set_tcp(0.02, 0.0, 0.03, 0.0, 1.57, 0.0)
            tool.set_tcp([0.02, 0.0, 0.03, 0.0, 1.57, 0.0])
            tool.set_tcp(PoseObject(0.02, 0.0, 0.03, 0.0, 1.57, 0.0))

        :param args: either 6 args (1 for each coordinates) or a list of 6 coordinates or a ``PoseObject``
        :type args: Union[tuple[float], list[float], PoseObject]
        :rtype: None
        """
        pose_list = self._args_pose_to_list(*args)
        req = self._services.set_tcp_service_request(pose_list)
        result = self._services.set_tcp_service.call(req)
        self._check_result_status(result)

    def reset_tcp(self):
        """
        Reset the TCP (Tool Center Point) transformation.
        The PCO will be reset according to the tool equipped.

        :rtype: None
        """
        req = self._services.get_trigger_request()
        result = self._services.reset_tcp_service.call(req)
        self._check_result_status(result)
