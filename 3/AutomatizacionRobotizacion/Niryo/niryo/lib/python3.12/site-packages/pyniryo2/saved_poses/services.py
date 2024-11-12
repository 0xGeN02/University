import roslibpy

from pyniryo2.objects import PoseObject
from pyniryo2.utils import pose_dict_to_list

from pyniryo2.saved_poses.enums import ManagePose


class SavedPosesServices(object):

    def __init__(self, client):
        self.__client = client

        self.manage_pose_service = roslibpy.Service(self.__client,
                                                    '/niryo_robot_poses_handlers/manage_pose',
                                                    'niryo_robot_poses_handlers/ManagePose')

        self.get_pose_list_service = roslibpy.Service(self.__client,
                                                      '/niryo_robot_poses_handlers/get_pose_list',
                                                      'niryo_robot_poses_handlers/GetNameDescriptionList')

        self.get_pose_service = roslibpy.Service(self.__client,
                                                 '/niryo_robot_poses_handlers/get_pose',
                                                 'niryo_robot_poses_handlers/GetPose')

    @staticmethod
    def save_joint_pose_request(name, joints, description=""):
        niryo_pose = roslibpy.ServiceRequest({"name": name, "description": description, "joints": joints})
        return roslibpy.ServiceRequest({"cmd": ManagePose.SAVE.value, "pose": niryo_pose})

    @staticmethod
    def save_pose_request(name, pose, description=""):
        niryo_pose = {"name": name, "description": description, "position": dict(zip(["x", "y", "z"], pose[:3]))}

        if len(pose) == 7:
            niryo_pose["orientation"] = dict(zip(["x", "y", "z", "w"], pose[3:]))
        else:
            niryo_pose["rpy"] = dict(zip(["roll", "pitch", "yaw"], pose[3:]))

        return roslibpy.ServiceRequest({"cmd": ManagePose.SAVE.value, "pose": niryo_pose})

    @staticmethod
    def delete_pose_request(name):
        return roslibpy.ServiceRequest({"cmd": ManagePose.DELETE.value, "pose": {"name": name}})

    @staticmethod
    def get_pose_list_request():
        return roslibpy.ServiceRequest()

    @staticmethod
    def get_saved_pose_request(name):
        return roslibpy.ServiceRequest({"name": name})

    @staticmethod
    def get_saved_pose_response_to_pose(response):
        return PoseObject(*pose_dict_to_list(response["pose"]))

    @staticmethod
    def get_saved_pose_list_response_to_list(response):
        return [str(pose_name) for pose_name in response["name_list"]]
