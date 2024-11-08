import roslibpy

from pyniryo2.utils import pose_list_to_dict, point_list_to_dict

from .enums import ManageWorkspace


class VisionServices(object):

    def __init__(self, client):
        self.__client = client

        self.get_target_pose_service = roslibpy.Service(self.__client,
                                                        '/niryo_robot_poses_handlers/get_target_pose',
                                                        'niryo_robot_vision/GetTargetPose')

        self.obj_detection_rel_service = roslibpy.Service(self.__client,
                                                          '/niryo_robot_vision/obj_detection_rel',
                                                          'niryo_robot_vision/ObjDetection')

        self.manage_workspace_service = roslibpy.Service(self.__client,
                                                         '/niryo_robot_poses_handlers/manage_workspace',
                                                         'niryo_robot_poses_handlers/ManageWorkspace')

        self.get_workspace_poses_service = roslibpy.Service(self.__client,
                                                            '/niryo_robot_poses_handlers/get_workspace_poses',
                                                            'niryo_robot_poses_handlers/GetWorkspaceRobotPoses')

        self.get_workspace_ratio_service = roslibpy.Service(self.__client,
                                                            '/niryo_robot_poses_handlers/get_workspace_ratio',
                                                            'niryo_robot_msgs/GetWorkspaceRatio')

        self.get_workspace_list_service = roslibpy.Service(self.__client,
                                                           '/niryo_robot_poses_handlers/get_workspace_list',
                                                           'niryo_robot_msgs/GetNameDescriptionList')

        self.set_brightness_service = roslibpy.Service(self.__client,
                                                       '/niryo_robot_vision/set_brightness',
                                                       'niryo_robot_vision/SetImageParameter')

        self.set_contrast_service = roslibpy.Service(self.__client,
                                                     '/niryo_robot_vision/set_contrast',
                                                     'niryo_robot_vision/SetImageParameter')

        self.set_saturation_service = roslibpy.Service(self.__client,
                                                       '/niryo_robot_vision/set_saturation',
                                                       'niryo_robot_vision/SetImageParameter')

    @staticmethod
    def get_trigger_request():
        return roslibpy.ServiceRequest()

    @staticmethod
    def get_target_pose_service_request(workspace, height_offset, x_rel, y_rel, yaw_rel):
        return roslibpy.ServiceRequest(
            {"workspace": workspace, "height_offset": height_offset, "x_rel": x_rel, "y_rel": y_rel,
             "yaw_rel": yaw_rel})

    @staticmethod
    def obj_detection_rel_service_request(obj_type, obj_color, workspace_ratio, ret_image=False):
        return roslibpy.ServiceRequest(
            {"obj_type": obj_type.value, "obj_color": obj_color.value, "workspace_ratio": workspace_ratio,
             "ret_image": ret_image})

    @staticmethod
    def manage_workspace_service_request(cmd, workspace):
        if not isinstance(cmd, ManageWorkspace):
            raise TypeError
        return roslibpy.ServiceRequest({"cmd": cmd.value, "workspace": workspace})

    @staticmethod
    def add_workspace_from_poses_request(workspace_name, pose_list):
        workspace = {"name": workspace_name, "poses": [pose_list_to_dict(pose) for pose in pose_list]}
        return VisionServices.manage_workspace_service_request(ManageWorkspace.SAVE, workspace)

    @staticmethod
    def add_workspace_from_points_request(workspace_name, point_list):
        workspace = {"name": workspace_name,
                     "points": [point_list_to_dict(point) for point in point_list]}
        return VisionServices.manage_workspace_service_request(ManageWorkspace.SAVE_WITH_POINTS, workspace)

    @staticmethod
    def get_workspace_poses_service_request(workspace_name):
        return roslibpy.ServiceRequest({"name": workspace_name})

    @staticmethod
    def get_workspace_ratio_service_request(workspace_name):
        return roslibpy.ServiceRequest({"workspace": workspace_name})

    @staticmethod
    def get_workspace_list_service_request():
        return VisionServices.get_trigger_request()

    @staticmethod
    def get_image_parameter_request(factor):
        return roslibpy.ServiceRequest({"factor": factor})
