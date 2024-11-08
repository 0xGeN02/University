# Communication imports
from pyniryo2.robot_commander import RobotCommander
from pyniryo2.objects import PoseObject

from .services import SavedPosesServices


class SavedPoses(RobotCommander):
    # --- Public functions --- #
    def __init__(self, client):
        super(SavedPoses, self).__init__(client)

        self._services = SavedPosesServices(self._client)

    def get_pose_saved(self, pose_name):
        """
        Get pose saved in from Ned's memory

        Examples: ::

            pose = saved_poses.get_pose_saved("pose1")

        :param pose_name: Pose name in robot's memory
        :type pose_name: str
        :return: Pose associated to pose_name
        :rtype: PoseObject
        """
        self._check_type(pose_name, str)

        req = self._services.get_saved_pose_request(pose_name)
        resp = self._services.get_pose_service.call(req)

        self._check_result_status(resp)
        return self._services.get_saved_pose_response_to_pose(resp)

    def save_pose(self, pose_name, *args):
        """
        Save pose (x, y, z, roll, pitch, yaw) in robot's memory

        Examples: ::

            saved_poses.save_pose("pose1", 0.3, 0.0, 0.3, 0.0, 1.57, 0.0)
            saved_poses.save_pose("pose1", [0.3, 0.0, 0.3, 0.0, 1.57, 0.0])
            saved_poses.save_pose("pose1", PoseObject(0.3, 0.0, 0.3, 0.0, 1.57, 0.0))

        :type pose_name: str
        :param args: either 6 args (1 for each coordinates) or a list of 6 coordinates or a PoseObject
        :type args: Union[list[float], tuple[float], PoseObject]
        :rtype: None
        """
        self._check_type(pose_name, str)

        req = self._services.save_pose_request(pose_name, self._args_pose_to_list(*args))
        resp = self._services.manage_pose_service.call(req)

        self._check_result_status(resp)

    def delete_pose(self, pose_name):
        """
        Delete pose from robot's memory

        Examples: ::

            if "pose1" in saved_poses.get_saved_pose_list():
                saved_poses.delete_pose("pose1")

        :type pose_name: str
        :rtype: None
        """
        self._check_type(pose_name, str)

        req = self._services.delete_pose_request(pose_name)
        resp = self._services.manage_pose_service.call(req)

        self._check_result_status(resp)

    def get_saved_pose_list(self):
        """
        Get list of poses' name saved in robot memory

        Examples: ::

            >> print(saved_poses.get_saved_pose_list())
            ["pose1", "pose2", "pose3"]

        :rtype: list[str]
        """
        req = self._services.get_pose_list_request()
        resp = self._services.get_pose_list_service.call(req)
        return self._services.get_saved_pose_list_response_to_list(resp)
