# - Imports

# Python libraries
from __future__ import print_function

# Communication imports
from .exceptions import RobotCommandException
from .objects import PoseObject
from .enums import RobotErrors
from .niryo_ros import NiryoRos


class RobotCommander(object):
    def __init__(self, client):
        assert (isinstance(client, NiryoRos))

        self._client = client

        self._services = None
        self._topics = None
        self._actions = None

    def __str__(self):
        return "NiryoRobot"

    def __repr__(self):
        return self.__str__()

    @property
    def client(self):
        return self._client

    # Parameters checker
    def _check_enum_belonging(self, value, enum_):
        """
        Check if a value belong to an enum
        """
        if value not in enum_:
            self._raise_exception_expected_choice([v for v in enum_], value)

    def _check_list_belonging(self, value, list_):
        """
        Check if a value belong to a list
        """
        if value not in list_:
            self._raise_exception_expected_choice(list_, value)

    def _check_range_belonging(self, value, range_min, range_max):
        """
        Check if a value belong to a range
        """
        if not range_min <= value <= range_max:
            self._raise_exception_expected_range(range_min, range_max, value)

    def _check_dict_belonging(self, value, dict_):
        """
        Check if a value belong to a dictionary
        """
        if value not in dict_.keys():
            self._raise_exception_expected_choice(dict_.keys(), value)

    def _check_type(self, value, type_):
        if type(value) is not type_:
            self._raise_exception_expected_type(type_.__name__, value)

    def _check_instance(self, value, type_):
        if not isinstance(value, type_):
            self._raise_exception_expected_type(
                type_.__name__ if not isinstance(type_, tuple) else " or ".join([type__.__name__ for type__ in type_]),
                value)

    def _check_not_instance(self, value, type_):
        if isinstance(value, type_):
            self._raise_exception_unexpected_type(
                type_.__name__ if not isinstance(type_, tuple) else " or ".join([type__.__name__ for type__ in type_]),
                value)

    def _check_list_type(self, values_list, type_):
        for value in values_list:
            self._check_type(value, type_)

    def _check_length(self, values, length):
        if len(values) != length:
            self._raise_exception_length(len(values), length)

    @staticmethod
    def _check_result_status(result):
        if "status" in result:
            if result["status"] < RobotErrors.SUCCESS.value:
                raise RobotCommandException("Error Code : {}\nMessage : {}".format(result["status"], result["message"]))
        elif "success" in result:
            if not result["success"]:
                raise RobotCommandException(
                    "Success : Failure\nMessage : {}".format(result["status"], result["message"]))

    def _map_list(self, list_, type_):
        """
        Try to map a list to another type (Very useful for list like joints
        which are acquired as string)
        """
        try:
            map_list = list(map(type_, list_))
            return map_list
        except ValueError:
            self._raise_exception_expected_type(type_.__name__, list_)

    def _transform_to_type(self, value, type_):
        """
        Try to change value type to another
        """
        try:
            value = type_(value)
            return value
        except ValueError:
            self._raise_exception_expected_type(type_.__name__, value)

    # -- Useful functions
    def _args_pose_to_list(self, *args):
        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, PoseObject):
                return arg.to_list()
            else:
                pose_list = arg
        else:
            pose_list = args

        pose_list_float = self._map_list(pose_list, float)
        if len(pose_list_float) != 6:
            self._raise_exception("A pose should contain 6 elements (x, y, z, roll, pitch, yaw)")
        return pose_list_float

    def _args_pose_to_pose_object(self, *args):
        if len(args) == 1:
            arg = args[0]
        else:
            arg = args

        if isinstance(arg, PoseObject):
            return arg
        elif len(arg) == 6:
            pose_list_float = self._map_list(arg, float)
            return PoseObject(*pose_list_float)
        elif len(arg) == 7:
            pose_list_float = self._map_list(arg, float)
            pose_list_rpy = pose_list_float[:3] + list(PoseObject.quaternion_to_euler_angle(*pose_list_float[3:]))
            return PoseObject(*pose_list_rpy)
        else:
            self._raise_exception("A pose should contain either 6 elements (x, y, z, roll, pitch, yaw), "
                                  "either 7 elements (x, y, z, qx, qy, qz, qw), either a PoseObject.")

    def _args_joints_to_list(self, *args):
        """
        Convert args into a list
        Either if args = (1.1,5.6,-6.7) or args = ([1.1,5.6,-6.7],) , the
        function will return (1.1,5.6,-6.7)

        :param args: Union[list, tuple]
        :return: list of float
        """
        if len(args) == 1:
            args = args[0]

        joints = self._map_list(args, float)
        if len(joints) != 6:
            self._raise_exception("The robot has 6 joints")

        return joints

    # Error Handlers
    def _raise_exception_expected_choice(self, expected_choice, given):
        raise RobotCommandException("Expected one of the following: {}.\nGiven: {}".format(expected_choice, given))

    def _raise_exception_expected_type(self, expected_type, given):
        raise RobotCommandException("Expected type: {}.\nGiven: {}".format(expected_type, given))

    def _raise_exception_unexpected_type(self, unexpected_type, given):
        raise RobotCommandException("Unexpected type: {}.\nGiven: {}".format(unexpected_type, given))

    def _raise_exception_expected_range(self, range_min, range_max, given):
        raise RobotCommandException(
            "Expected the following condition: {} <= value <= {}\nGiven: {}".format(range_min, range_max, given))

    def _raise_exception_length(self, expected_length, given):
        raise RobotCommandException("Expected length: {}.\n Given: {}".format(expected_length, given))

    def _raise_exception(self, message):
        raise RobotCommandException("Exception message : {}".format(message))
