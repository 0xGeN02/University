# - Imports
from pyniryo2.robot_commander import RobotCommander
from pyniryo2.utils import point_list_to_dict
from pyniryo2.objects import PoseObject

from .services import FramesServices


class Frames(RobotCommander):
    # --- Public functions --- #
    def __init__(self, client):
        super(Frames, self).__init__(client)

        self._services = FramesServices(self._client)

    # Main purpose
    def get_saved_dynamic_frame_list(self):
        """
        Get list of saved dynamic frames

        Example: ::

            list_frame, list_desc = robot.frames.get_saved_dynamic_frame_list()
            print(list_frame)
            print(list_desc)

        :return: list of dynamic frames name, list of description of dynamic frames
        :rtype: dictionnaire{name:description}
        """
        req = self._services.get_saved_dynamic_frame_list_request()
        response = self._services.get_frame_list_service.call(req)
        return self._services.get_saved_dynamic_frame_list_response_to_list(response)

    def get_saved_dynamic_frame(self, frame_name):
        """
        Get name, description and pose of a dynamic frame

        Example: ::

            frame = robot.frames.get_saved_dynamic_frame("default_frame")

        :param frame_name: name of the frame
        :type frame_name: str
        :return: name, description, position and orientation of a frame
        :rtype: namedtuple(name(str), description(str), position(list[float]), orientation(list[float]))
        """
        self._check_type(frame_name, str)
        req = self._services.get_dynamic_frame_from_name_request(frame_name)
        response = self._services.get_frame_from_name_service.call(req)
        self._check_result_status(response)

        return self._services.get_dynamic_frame_from_name_response_to_named_tuple(response)

    def save_dynamic_frame_from_poses(self, frame_name, description, pose_origin, pose_x, pose_y,
                                      belong_to_workspace=False):
        """
        Create a dynamic frame with 3 poses (origin, x, y)

        Example: ::

            pose_o = [0.1, 0.1, 0.1, 0, 0, 0]
            pose_x = [0.2, 0.1, 0.1, 0, 0, 0]
            pose_y = [0.1, 0.2, 0.1, 0, 0, 0]

            robot.frames.save_dynamic_frame_from_poses("name", "une description test", pose_o, pose_x, pose_y)

        :param frame_name: name of the frame
        :type frame_name: str
        :param description: description of the frame
        :type description: str
        :param pose_origin: pose of the origin of the frame
        :type pose_origin: list[float] [x, y, z, roll, pitch, yaw]
        :param pose_x: pose of the point x of the frame
        :type pose_x: list[float] [x, y, z, roll, pitch, yaw]
        :param pose_y: pose of the point y of the frame
        :type pose_y: list[float] [x, y, z, roll, pitch, yaw]
        :param belong_to_workspace: indicate if the frame belong to a workspace
        :type belong_to_workspace: boolean
        :return: status, message
        :rtype: (int, str)
        """
        self._check_type(frame_name, str)
        self._check_type(description, str)
        self._check_type(belong_to_workspace, bool)
        self._check_instance(pose_origin, (list, PoseObject))
        self._check_instance(pose_x, (list, PoseObject))
        self._check_instance(pose_y, (list, PoseObject))

        self._check_length(pose_origin, 6)
        self._check_length(pose_x, 6)
        self._check_length(pose_y, 6)

        pose_list = [self._args_pose_to_list(pose) for pose in (pose_origin, pose_x, pose_y)]
        req = self._services.save_dynamic_frame_from_poses_request(frame_name, description, pose_list,
                                                                   belong_to_workspace)
        response = self._services.manage_frame_service.call(req)
        self._check_result_status(response)

    def save_dynamic_frame_from_points(self, frame_name, description, point_origin, point_x, point_y,
                                       belong_to_workspace=False):
        """
        Create a dynamic frame with 3 points (origin, x, y)

        Example: ::

            point_o = [-0.1, -0.1, 0.1]
            point_x = [-0.2, -0.1, 0.1]
            point_y = [-0.1, -0.2, 0.1]

            robot.frames.save_dynamic_frame_from_points("name", "une description test", point_o, point_x, point_y)

        :param frame_name: name of the frame
        :type frame_name: str
        :param description: description of the frame
        :type description: str
        :param point_origin: origin point of the frame
        :type point_origin: list[float] [x, y, z]
        :param point_x: point x of the frame
        :type point_x: list[float] [x, y, z]
        :param point_y: point y of the frame
        :type point_y: list[float] [x, y, z]
        :param belong_to_workspace: indicate if the frame belong to a workspace
        :type belong_to_workspace: boolean
        :return: status, message
        :rtype: (int, str)
        """
        self._check_type(frame_name, str)
        self._check_type(description, str)
        self._check_type(belong_to_workspace, bool)
        self._check_type(point_origin, list)
        self._check_type(point_x, list)
        self._check_type(point_y, list)

        self._check_length(point_origin, 3)
        self._check_length(point_x, 3)
        self._check_length(point_y, 3)

        points_list_raw = [point_origin, point_x, point_y]
        points_list = [point_list_to_dict(point) for point in points_list_raw]

        req = self._services.save_dynamic_frame_from_points_request(frame_name, description, points_list,
                                                                    belong_to_workspace)
        response = self._services.manage_frame_service.call(req)
        self._check_result_status(response)

    def edit_dynamic_frame(self, frame_name, new_frame_name, new_description):
        """
        Modify a dynamic frame

        Example: ::

            robot.frames.edit_dynamic_frame("name", "new_name", "new description")

        :param frame_name: name of the frame
        :type frame_name: str
        :param new_frame_name: new name of the frame
        :type new_frame_name: str
        :param new_description: new description of the frame
        :type new_description: str
        :return: status, message
        :rtype: (int, str)
        """
        self._check_type(frame_name, str)
        self._check_type(new_frame_name, str)
        self._check_type(new_description, str)

        req = self._services.edit_dynamic_frame_request(frame_name, new_frame_name, new_description)
        response = self._services.manage_frame_service.call(req)
        self._check_result_status(response)

    def delete_saved_dynamic_frame(self, frame_name, belong_to_workspace=False):
        """
        Delete a dynamic frame

        Example: ::

            robot.frames.delete_saved_dynamic_frame("name")

        :param frame_name: name of the frame to remove
        :type frame_name: str
        :param belong_to_workspace: indicate if the frame belong to a workspace
        :type belong_to_workspace: boolean
        :return: status, message
        :rtype: (int, str)
        """
        self._check_type(frame_name, str)
        self._check_type(belong_to_workspace, bool)

        req = self._services.delete_dynamic_frame_request(frame_name, belong_to_workspace)
        response = self._services.manage_frame_service.call(req)
        self._check_result_status(response)
