# - Imports
from __future__ import print_function

# Communication imports
from pyniryo2.robot_commander import RobotCommander
from pyniryo2.enums import RobotErrors
from pyniryo2.objects import PoseObject
from pyniryo2.utils import pose_dict_to_list

from .enums import ObjectShape, ObjectColor, ManageWorkspace
from .services import VisionServices
from .topics import VisionTopics

from pyniryo2.arm.arm import Arm
from pyniryo2.tool.tool import Tool


def object_pose_dict_to_pose_object(object_pose_dict):
    return PoseObject(*[object_pose_dict[axis] for axis in ["x", "y", "z", "roll", "pitch", "yaw"]])


class Vision(RobotCommander):
    # --- Public functions --- #
    def __init__(self, client, arm=None, tool=None):
        """
        Vision robot functions

        Example: ::

            ros_instance = NiryoRos("10.10.10.10") # Hotspot
            vision_interface = Vision(ros_instance)

        :param client: Niryo ROS client
        :type client: NiryoRos
        """
        super(Vision, self).__init__(client)

        self._services = VisionServices(self._client)
        self._topics = VisionTopics(self._client)

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

    @property
    def get_camera_intrinsics(self):
        """
        Get calibration object: camera intrinsics, distortions coefficients
        The topic return a namedtuple(intrinsics: list[list[float]], distortion: list[list[float]])

        Examples: ::

            vision.get_camera_intrinsics()
            vision.get_camera_intrinsics().value

            def camera_info_callback(camera_info):
                print(camera_info.intrinsics)
                print(camera_info.distortion)
                vision.get_camera_intrinsics.unsubscribe()

            vision.get_camera_intrinsics.subscribe(camera_info_callback)

        :rtype: NiryoTopic
        """
        return self._topics.camera_info_topic

    @property
    def get_img_compressed(self):
        """
        Get image from video stream in a compressed format.
        Use ``uncompress_image`` from the vision package to uncompress it

        Examples: ::

            import pyniryo

            img_compressed = vision.get_img_compressed()
            camera_info = vision.get_camera_intrinsics()
            img = pyniryo.uncompress_image(img_compressed)
            img = pyniryo.undistort_image(img, camera_info.intrinsics, camera_info.distortion)


        :return: string containing a JPEG compressed image
        :rtype: NiryoTopic
        """
        return self._topics.compressed_video_stream_topic

    @property
    def get_image_parameters(self):
        """
        Return the NiryoTopic to get last stream image parameters:
        Brightness factor, Contrast factor, Saturation factor.
        The topic return a namedtuple(brightness_factor: float, contrast_factor: float, saturation_factor: float)

        Brightness factor: How much to adjust the brightness. 0.5 will give a darkened image,
        1 will give the original image while 2 will enhance the brightness by a factor of 2.

        Contrast factor: A factor of 1 gives original image.
        Making the factor towards 0 makes the image greyer, while factor>1 increases the contrast of the image.

        Saturation factor: 0 will give a black and white image, 1 will give the original image while
        2 will enhance the saturation by a factor of 2.

        Examples: ::

            vision.get_image_parameters()
            vision.get_image_parameters.value

            def image_parameters_callback(image_parameters):
                print(image_parameters.brightness_factor)
                print(image_parameters.contrast_factor)
                print(image_parameters.saturation_factor)

                vision.get_image_parameters.unsubscribe()

            vision.get_image_parameters.subscribe(image_parameters_callback)


        :return: ImageParameters namedtuple containing the brightness factor, contrast factor and saturation factor.
        :rtype: NiryoTopic
        """
        return self._topics.video_stream_parameters_topic

    def set_brightness(self, brightness_factor):
        """
        Modify image brightness

        :param brightness_factor: How much to adjust the brightness. 0.5 will
            give a darkened image, 1 will give the original image while
            2 will enhance the brightness by a factor of 2.
        :type brightness_factor: float
        :rtype: None
        """
        self._check_not_instance(brightness_factor, bool)
        self._check_instance(brightness_factor, (int, float))
        req = self._services.get_image_parameter_request(brightness_factor)
        result = self._services.set_brightness_service.call(req)
        self._check_result_status(result)

    def set_contrast(self, contrast_factor):
        """
        Modify image contrast

        :param contrast_factor: A factor of 1 gives original image.
            Making the factor towards 0 makes the image greyer, while factor>1 increases the contrast of the image.
        :type contrast_factor: float
        :rtype: None
        """
        self._check_not_instance(contrast_factor, bool)
        self._check_instance(contrast_factor, (int, float))
        req = self._services.get_image_parameter_request(contrast_factor)
        result = self._services.set_contrast_service.call(req)
        self._check_result_status(result)

    def set_saturation(self, saturation_factor):
        """
        Modify image saturation

        :param saturation_factor: How much to adjust the saturation. 0 will
            give a black and white image, 1 will give the original image while
            2 will enhance the saturation by a factor of 2.
        :type saturation_factor: float
        :rtype: None
        """
        self._check_not_instance(saturation_factor, bool)
        self._check_instance(saturation_factor, (int, float))
        req = self._services.get_image_parameter_request(saturation_factor)
        result = self._services.set_saturation_service.call(req)
        self._check_result_status(result)

    def get_target_pose_from_rel(self, workspace_name, height_offset, x_rel, y_rel, yaw_rel):
        """
        Given a pose (x_rel, y_rel, yaw_rel) relative to a workspace, this function
        returns the robot pose in which the current tool will be able to pick an object at this pose.

        The height_offset argument (in m) defines how high the tool will hover over the workspace. If height_offset = 0,
        the tool will nearly touch the workspace.

        :param workspace_name: name of the workspace
        :type workspace_name: str
        :param height_offset: offset between the workspace and the target height
        :type height_offset: float
        :param x_rel: x relative pose (between 0 and 1)
        :type x_rel: float
        :param y_rel: y relative pose (between 0 and 1)
        :type y_rel: float
        :param yaw_rel: Angle in radians
        :type yaw_rel: float

        :return: target_pose
        :rtype: PoseObject
        """
        self._check_type(workspace_name, str)
        self._check_range_belonging(x_rel, 0.0, 1.0)
        self._check_range_belonging(y_rel, 0.0, 1.0)

        height_offset, x_rel, y_rel, yaw_rel = self._map_list([height_offset, x_rel, y_rel, yaw_rel], float)

        req = self._services.get_target_pose_service_request(workspace_name, height_offset, x_rel, y_rel, yaw_rel)
        resp = self._services.get_target_pose_service.call(req)

        pose_array = pose_dict_to_list(resp["target_pose"])
        pose_object = PoseObject(*pose_array)
        return pose_object

    def get_target_pose_from_cam(self, workspace_name, height_offset=0.0, shape=ObjectShape.ANY, color=ObjectColor.ANY):
        """
        First detects the specified object using the camera and then returns the robot pose in which the object can
        be picked with the current tool

        :param workspace_name: name of the workspace
        :type workspace_name: str
        :param height_offset: offset between the workspace and the target height
        :type height_offset: float
        :param shape: shape of the target
        :type shape: ObjectShape
        :param color: color of the target
        :type color: ObjectColor
        :return: object_found, object_pose, object_shape, object_color
        :rtype: (bool, PoseObject, ObjectShape, ObjectColor)
        """
        self._check_type(workspace_name, str)
        height_offset = self._transform_to_type(height_offset, float)
        self._check_enum_belonging(shape, ObjectShape)
        self._check_enum_belonging(color, ObjectColor)

        object_found, rel_pose, obj_shape, obj_color = self.detect_object(workspace_name, shape, color)

        if not object_found:
            obj_pose = PoseObject(0, 0, 0, 0, 0, 0)
        else:
            obj_pose = self.get_target_pose_from_rel(workspace_name, height_offset, rel_pose.x, rel_pose.y,
                                                     rel_pose.yaw)

        return object_found, obj_pose, obj_shape, obj_color

    def vision_pick(self, workspace_name, height_offset=0.0, shape=ObjectShape.ANY, color=ObjectColor.ANY):
        """
        Picks the specified object from the workspace. This function has multiple phases: \n
        | 1. detect object using the camera
        | 2. prepare the current tool for picking
        | 3. approach the object
        | 4. move down to the correct picking pose
        | 5. actuate the current tool
        | 6. lift the object

        Example::

            robot = NiryoRobot(ip_address="x.x.x.x")
            robot.arm.calibrate_auto()
            robot.arm.move_pose(<observation_pose>)
            obj_found, shape_ret, color_ret = robot.vision.vision_pick(<workspace_name>,
                                                                height_offset=0.0,
                                                                shape=ObjectShape.ANY,
                                                                color=ObjectColor.ANY)

        :param workspace_name: name of the workspace
        :type workspace_name: str
        :param height_offset: offset between the workspace and the target height
        :type height_offset: float
        :param shape: shape of the target
        :type shape: ObjectShape
        :param color: color of the target
        :type color: ObjectColor
        :return: object_found, object_shape, object_color
        :rtype: (bool, ObjectShape, ObjectColor)
        """
        self._check_type(workspace_name, str)
        height_offset = self._transform_to_type(height_offset, float)
        self._check_enum_belonging(shape, ObjectShape)
        self._check_enum_belonging(color, ObjectColor)

        object_found, rel_pose, obj_shape, obj_color = self.detect_object(workspace_name, shape, color)
        if not object_found:
            return False, "", ""

        pick_pose = self.get_target_pose_from_rel(
            workspace_name, height_offset, rel_pose.x, rel_pose.y, rel_pose.yaw)
        approach_pose = self.get_target_pose_from_rel(
            workspace_name, height_offset + 0.05, rel_pose.x, rel_pose.y, rel_pose.yaw)

        self.__tool.release_with_tool()

        self.__arm.move_pose(approach_pose)
        self.__arm.move_pose(pick_pose)

        self.__tool.grasp_with_tool()

        self.__arm.move_pose(approach_pose)
        return True, obj_shape, obj_color

    def move_to_object(self, workspace_name, height_offset, shape, color):
        """
        Same as `get_target_pose_from_cam` but directly moves to this position

        :param workspace_name: name of the workspace
        :type workspace_name: str
        :param height_offset: offset between the workspace and the target height
        :type height_offset: float
        :param shape: shape of the target
        :type shape: ObjectShape
        :param color: color of the target
        :type color: ObjectColor
        :return: object_found, object_shape, object_color
        :rtype: (bool, ObjectShape, ObjectColor)
        """
        obj_found, obj_pose, obj_shape, obj_color = self.get_target_pose_from_cam(workspace_name, height_offset, shape,
                                                                                  color)
        if not obj_found:
            return False, "", ""

        self.__arm.move_pose(obj_pose)
        return True, obj_shape, obj_color

    def detect_object(self, workspace_name, shape=ObjectShape.ANY, color=ObjectColor.ANY):
        """
        Detect object in workspace and return its pose and characteristics

        :param workspace_name: name of the workspace
        :type workspace_name: str
        :param shape: shape of the target
        :type shape: ObjectShape
        :param color: color of the target
        :type color: ObjectColor
        :return: object_found, object_pose, object_shape, object_color
        :rtype: (bool, PoseObject, str, str)
        """
        self._check_type(workspace_name, str)
        self._check_enum_belonging(shape, ObjectShape)
        self._check_enum_belonging(color, ObjectColor)

        ratio = self.get_workspace_ratio(workspace_name)
        req = self._services.obj_detection_rel_service_request(shape, color, ratio)
        resp = self._services.obj_detection_rel_service.call(req)

        obj_found = resp["status"] >= RobotErrors.SUCCESS.value
        if not obj_found:
            rel_pose = PoseObject(*(6 * [0.0]))
            shape = "ANY"
            color = "ANY"
        else:
            rel_pose = object_pose_dict_to_pose_object(resp["obj_pose"])
            shape = resp["obj_type"]
            color = resp["obj_color"]

        return obj_found, rel_pose, ObjectShape[shape], ObjectColor[color]

    # - Workspace
    def save_workspace_from_robot_poses(self, workspace_name, pose_origin, pose_2, pose_3, pose_4):
        """
        Save workspace by giving the poses of the robot to point its 4 corners
        with the calibration Tip. Corners should be in the good order.
        Markers' pose will be deduced from these poses

        Poses should be either a list [x, y, z, roll, pitch, yaw] or a PoseObject

        :param workspace_name: workspace name
        :type workspace_name: str
        :param pose_origin:
        :type pose_origin: Union[list[float], PoseObject]
        :param pose_2:
        :type pose_2: Union[list[float], PoseObject]
        :param pose_3:
        :type pose_3: Union[list[float], PoseObject]
        :param pose_4:
        :type pose_4: Union[list[float], PoseObject]

        :rtype: None
        """
        self._check_type(workspace_name, str)
        pose_list = [self._args_pose_to_list(pose) for pose in (pose_origin, pose_2, pose_3, pose_4)]
        req = self._services.add_workspace_from_poses_request(workspace_name, pose_list)
        _resp = self._services.manage_workspace_service.call(req)

    def save_workspace_from_points(self, workspace_name, point_origin, point_2, point_3, point_4):
        """
        Save workspace by giving the points of worskpace's 4 corners. Points are written as [x, y, z]
        Corners should be in the good order.

        :param workspace_name: workspace name
        :type workspace_name: str
        :param point_origin:
        :type point_origin: list[float]
        :param point_2:
        :type point_2: list[float]
        :param point_3:
        :type point_3: list[float]
        :param point_4:
        :type point_4: list[float]
        :rtype: None
        """
        self._check_type(workspace_name, str)
        point_list = [self._map_list(point, float) for point in (point_origin, point_2, point_3, point_4)]
        req = self._services.add_workspace_from_points_request(workspace_name, point_list)
        _resp = self._services.manage_workspace_service.call(req)

    def delete_workspace(self, workspace_name):
        """
        Delete workspace from robot's memory

        :param workspace_name: name of the saved workspace
        :type workspace_name: str
        :rtype: None
        """
        self._check_type(workspace_name, str)
        workspace = {"name": workspace_name}
        req = self._services.manage_workspace_service_request(ManageWorkspace.DELETE, workspace)
        _resp = self._services.manage_workspace_service.call(req)

    def get_workspace_poses(self, workspace_name):
        """
        Get the position of the tags of the workspace from the robot's memory.

        :param workspace_name:  name of the saved workspace
        :type workspace_name: str
        :return: List of the 4 workspace poses in the clockwise
        :rtype: list[PoseObject]
        """
        self._check_type(workspace_name, str)
        req = self._services.get_workspace_poses_service_request(workspace_name)
        resp = self._services.get_workspace_poses_service.call(req)
        return [PoseObject(*pose_dict_to_list(robot_pose)) for robot_pose in resp["poses"]]

    def get_workspace_ratio(self, workspace_name):
        """
        Get workspace ratio from robot's memory

        :param workspace_name: workspace name
        :type workspace_name: str
        :rtype: float
        """
        self._check_type(workspace_name, str)
        req = self._services.get_workspace_ratio_service_request(workspace_name)
        return self._services.get_workspace_ratio_service.call(req)["ratio"]

    def get_workspace_list(self):
        """
        Get list of workspaces' name store in robot's memory

        :rtype: list[str]
        """
        req = self._services.get_workspace_list_service_request()
        return self._map_list(self._services.get_workspace_list_service.call(req)["name_list"], str)
