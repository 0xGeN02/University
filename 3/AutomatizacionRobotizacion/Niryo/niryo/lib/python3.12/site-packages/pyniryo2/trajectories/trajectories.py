# - Imports
import numpy as np

from pyniryo2.robot_commander import RobotCommander
from pyniryo2.objects import PoseObject

from .services import TrajectoriesServices
from .actions import TrajectoriesActions


class Trajectories(RobotCommander):
    # --- Public functions --- #
    def __init__(self, client, action_timeout=3600):
        super(Trajectories, self).__init__(client)

        self._services = TrajectoriesServices(self._client)
        self._actions = TrajectoriesActions(self._client)

        self.__action_timeout = action_timeout

    # - Main purpose
    def get_saved_trajectory(self, trajectory_name):
        """
        Get saved trajectory from robot intern storage
        Will raise error if position does not exist

        Example: ::

            trajectories.get_saved_trajectory("trajectory_01")

        :param trajectory_name: name of the trajectory
        :type trajectory_name: str
        :raises NiryoRosWrapperException: If trajectory file doesn't exist
        :return: list of [j1, j2, j3, j4, j5, j6] in rad
        :rtype: list[list[float]]
        """
        self._check_type(trajectory_name, str)

        req = self._services.get_trajectory_from_name_request(trajectory_name)
        result = self._services.get_trajectory_from_name_service.call(req)
        self._check_result_status(result)

        trajectory = self._services.trajectory_dict_to_list(result["trajectory"])
        return trajectory

    def execute_registered_trajectory(self, trajectory_name, callback=None):
        """
        Execute trajectory from Ned's memory
        If a callback function is not passed in parameter, the function will be blocking.
        Otherwise, the callback will be called when the execution of the function is finished.

        Examples: ::

            trajectories.execute_trajectory_saved("trajectory_01")

            from threading import Event
            trajectory_event = Event()
            trajectory_event.clear()

            def trajectory_callback(result):
                print(result)
                trajectory_event.set()

            trajectories.execute_trajectory_saved("trajectory_01", callback=trajectory_callback)
            trajectory_event.wait()

        :param callback: Callback invoked on successful execution.
        :type callback: function
        :type trajectory_name: str
        :rtype: None
        """
        self._check_type(trajectory_name, str)
        req = self._services.execute_registered_trajectory_request(trajectory_name)
        response = self._services.trajectory_manager_service.call(req, callback)
        if callback is None:
            self._check_result_status(response)

    def execute_trajectory_from_poses(self, list_poses, dist_smoothing=0.0, callback=None):
        """
        Execute trajectory from list of poses
        If a callback function is not passed in parameter, the function will be blocking.
        Otherwise, the callback will be called when the execution of the function is finished.

        Examples: ::

            trajectory = [[0.3, 0.1, 0.3, 0., 0., 0., 1.],
                          [0.3, -0.1, 0.3, 0., 0., 0., 1.],
                          [0.3, -0.1, 0.4, 0., 0., 0., 1.],
                          [0.3, 0.1, 0.4, 0., 0., 0., 1.]]

            trajectories.execute_trajectory_from_poses(trajectory)
            trajectories.execute_trajectory_from_poses(trajectory, dist_smoothing=0.02)
            trajectories.execute_trajectory_from_poses([[0.3, 0.1, 0.3, 0., 0., 0., 1.], #[x,y,z,qx,qy,qz,qw]
                                                 PoseObject(0.3, -0.1, 0.3, 0., 0., 0.),
                                                 [0.3, -0.1, 0.4, 0., 0., 0.], #[x,y,z,roll,pitch,yaw]
                                                 PoseObject(0.3, 0.1, 0.4, 0., 0., 0.)])

            from threading import Event
            trajectory_event = Event()
            trajectory_event.clear()

            def trajectory_callback(result):
                print(result)
                trajectory_event.set()

            trajectories.execute_trajectory_from_poses(trajectory, callback=trajectory_callback)
            trajectory_event.wait()

        :param callback: Callback invoked on successful execution.
        :type callback: function
        :param list_poses: List of: [x,y,z,qx,qy,qz,qw] or [x,y,z,roll,pitch,yaw] or PoseObject
        :type list_poses: list[Union[tuple[float], list[float], PoseObject]]
        :param dist_smoothing: Distance from waypoints before smoothing trajectory
        :type dist_smoothing: float
        :rtype: None
        """
        self._check_range_belonging(dist_smoothing, 0.0, np.Inf)
        trajectory = self.__list_pose_to_trajectory(list_poses)
        goal = self._actions.get_execute_trajectories_goal(
            trajectory, dist_smoothing)
        goal.send(result_callback=callback)
        if callback is None:
            _result = goal.wait(self.__action_timeout)

    def save_trajectory(self, trajectory, trajectory_name, description):
        """
        Save trajectory in robot's memory

        Examples: ::

            trajectory = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                          [1.57, 0.0, 0.0, 0.0, -1.57, 0.0],
                          [-1.57, 0.0, 0.0, 0.0, -1.57, 0.0]]

            trajectories.save_trajectory(trajectory, "trajectory_1", "test description trajectory_1")


        :param trajectory: list of joints positions the robot needs to pass by in the trajectory
        :type trajectory: list[joints]
        :param trajectory_name: name you give trajectory in the robot's memory
        :type trajectory_name: str
        :param description: description you give trajectory in the robot's memory
        :type description: str

        :rtype: None
        """

        self._check_type(trajectory_name, str)
        self._check_type(description, str)
        self._check_type(trajectory, list)
        for i, position in enumerate(trajectory):
            if len(position) != 6:
                self._raise_exception(
                    "The robot has 6 joints, position {} at index {} has only {} values".format(
                        position, i, len(position)))

        traj_message = self._services.trajectory_to_dict(trajectory)
        req = self._services.save_trajectory_request(traj_message, trajectory_name, description)
        result = self._services.trajectory_manager_service.call(req)

        self._check_result_status(result)

    def save_last_learned_trajectory(self, trajectory_name, description):
        """
        Save last executed trajectory in robot's memory

        Examples: ::

            trajectories.save_last_learned_trajectory("trajectory_1", "test description trajectory_1")

        :param trajectory_name: name you give trajectory in the robot's memory
        :type trajectory_name: str
        :param description: description you give trajectory in the robot's memory
        :type description: str
        :rtype: None
        """
        self._check_type(trajectory_name, str)
        self._check_type(description, str)

        req = self._services.save_last_learned_trajectory_request(trajectory_name, description)
        result = self._services.trajectory_manager_service.call(req)
        self._check_result_status(result)

    def delete_trajectory(self, trajectory_name):
        """
        Delete trajectory from robot's memory

        Example: ::

            if "trajectory_1" in trajectories.get_saved_trajectory_list():
                trajectories.delete_trajectory("trajectory_1")

        :type trajectory_name: str
        :rtype: None
        """
        self._check_type(trajectory_name, str)

        req = self._services.delete_trajectory_request(trajectory_name)
        response = self._services.trajectory_manager_service.call(req)
        self._check_result_status(response)

    def clean_trajectory_memory(self):
        """
        Delete all trajectories from robot's memory

        Example: ::

           trajectories.clean_trajectory_memory()

        :rtype: None
        """

        req = self._services.clean_trajectory_memory_request()
        response = self._services.trajectory_manager_service.call(req)
        self._check_result_status(response)

    def get_saved_trajectory_list(self):
        """
        Get list of trajectories' name saved in robot memory

        Example: ::

            if "trajectory_1" in trajectories.get_saved_trajectory_list():
                trajectories.delete_trajectory("trajectory_1")

        :return: list of tuple(trajectory name, trajectory definition)
        :rtype: list[tuple(str, str)]
        """
        req = self._services.get_saved_trajectory_list_request()
        response = self._services.get_trajectory_list_service.call(req)
        return list(zip(response["name_list"], response["description_list"]))

    def update_trajectory_infos(self, name, new_name, description=""):
        """
        Update the trajectory informations: name and description

        Example: ::

            trajectories.update_trajectory_infos("trajectory_1", "trajectory_2", callback="change description")

        :param name: name of the trajectory you want to change infos
        :type name: str
        :param new_name: new name you want to give to the trajectory
        :type new_name: str
        :param description: new description you want to give to the trajectory
        :type description: str
        :rtype: None
        """
        req = self._services.update_trajectory_infos_request(name, new_name, description)
        response = self._services.trajectory_manager_service.call(req)
        self._check_result_status(response)

    def __list_pose_to_trajectory(self, list_poses):
        """
        Convert a list of [x,y,z,qx,qy,qz,qw], [x,y,z,roll,pitch,yaw] and PoseObjects into a [x,y,z,qx,qy,qz,qw] list

        :param list_poses: List of: [x,y,z,qx,qy,qz,qw] or [x,y,z,roll,pitch,yaw] or PoseObject
        :type list_poses: list[Union[tuple[float], list[float], PoseObject]]
        :return: list[[x,y,z,qx,qy,qz,qw]] which represents a trajectory from the list_poses
        :rtype: list[list[float]]
        """
        self._check_type(list_poses, list)
        trajectory = []
        for pose in list_poses:
            if isinstance(pose, PoseObject):
                trajectory.append(pose.quaternion_pose)
            else:
                self._check_type(pose, list)
                if len(pose) == 7:
                    trajectory.append(self._map_list(pose[:], float))
                elif len(pose) == 6:
                    trajectory.append(PoseObject(*pose).quaternion_pose)
                else:
                    self._raise_exception("7 parameters expected in a pose [x,y,z,qx,qy,qz,qw], or  "
                                          "6 parameters expected in a pose [x,y,z,roll,pitch,yaw], or"
                                          "PoseObject expected in a pose [x,y,z,roll,pitch,yaw], "
                                          "{} given".format(pose))
        return trajectory
