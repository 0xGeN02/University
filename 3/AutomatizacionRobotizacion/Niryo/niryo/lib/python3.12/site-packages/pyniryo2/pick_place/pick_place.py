# - Imports
from __future__ import print_function

# Communication imports
from pyniryo2.robot_commander import RobotCommander

from pyniryo2.arm.arm import Arm
from pyniryo2.tool.tool import Tool
from pyniryo2.trajectories.trajectories import Trajectories


class PickPlace(RobotCommander):
    def __init__(self, client, arm=None, tool=None, trajectories=None):
        super(PickPlace, self).__init__(client)

        if arm is None:
            self.__arm = Arm(client)
        else:
            self._check_instance(arm, Arm)
            self.__arm = arm

        if tool is None:
            self.__tool = Tool(client)
        else:
            self._check_instance(tool, Tool)
            self.__tool = tool

        if trajectories is None:
            self.__trajectories = Trajectories(client)
        else:
            self._check_instance(trajectories, Trajectories)
            self.__trajectories = trajectories

    def pick_from_pose(self, *args):
        """
        Execute a picking from a pose.

        A picking is described as : \n
        | * going over the object
        | * going down until height = z
        | * grasping with tool
        | * going back over the object

        :param args: either 6 args (1 for each coordinates) or a list of 6 coordinates or a PoseObject
        :type args: Union[list[float], tuple[float], PoseObject]
        :rtype: None
        """
        pick_pose = self._args_pose_to_pose_object(*args)
        pick_pose_high = pick_pose.copy_with_offsets(z_offset=0.05)

        self.__tool.release_with_tool()
        self.__trajectories.execute_trajectory_from_poses([pick_pose_high, pick_pose], dist_smoothing=0.0)
        self.__tool.grasp_with_tool()

        return self.__arm.move_pose(pick_pose_high)

    def place_from_pose(self, *args):
        """
        Execute a placing from a position.

        A placing is described as : \n
        | * going over the place
        | * going down until height = z
        | * releasing the object with tool
        | * going back over the place

        :param args: either 6 args (1 for each coordinates) or a list of 6 coordinates or a PoseObject
        :type args: Union[list[float], tuple[float], PoseObject]
        :rtype: None
        """

        place_pose = self._args_pose_to_pose_object(*args)
        place_pose_high = place_pose.copy_with_offsets(z_offset=0.05)

        self.__trajectories.execute_trajectory_from_poses([place_pose_high, place_pose], dist_smoothing=0.0)
        self.__tool.release_with_tool()

        return self.__arm.move_pose(place_pose_high)

    def pick_and_place(self, pick_pose, place_pose, dist_smoothing=0.0):
        """
        Execute a pick then a place

        :param pick_pose: Pick Pose : [x, y, z, roll, pitch, yaw] or PoseObject
        :type pick_pose: Union[list[float], PoseObject]
        :param place_pose: Place Pose : [x, y, z, roll, pitch, yaw] or PoseObject
        :type place_pose: Union[list[float], PoseObject]
        :param dist_smoothing: Distance from waypoints before smoothing trajectory
        :type dist_smoothing: float
        :rtype: None
        """
        pick_pose_object = self._args_pose_to_pose_object(pick_pose)
        place_pose_object = self._args_pose_to_pose_object(place_pose)

        pick_pose_high = pick_pose_object.copy_with_offsets(z_offset=0.05)
        place_pose_high = place_pose_object.copy_with_offsets(z_offset=0.05)

        self.__tool.release_with_tool()

        self.__trajectories.execute_trajectory_from_poses([pick_pose_high, pick_pose_object], dist_smoothing)
        self.__tool.grasp_with_tool()

        self.__trajectories.execute_trajectory_from_poses([pick_pose_high, place_pose_high, place_pose_object],
                                                          dist_smoothing)

        self.__tool.release_with_tool()

        return self.__arm.move_pose(place_pose_high)
