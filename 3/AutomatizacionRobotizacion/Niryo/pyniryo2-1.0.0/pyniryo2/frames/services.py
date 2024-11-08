import roslibpy

from pyniryo2.utils import pose_list_to_dict, point_list_to_dict

from .enums import ManageFrames
from .objects import DynamicFrameInfo

class FramesServices(object):

    def __init__(self, client):
        self.__client = client

        self.get_frame_from_name_service = roslibpy.Service(self.__client,
                                                            '/niryo_robot_poses_handlers/get_dynamic_frame',
                                                            'niryo_robot_poses_handlers/GetDynamicFrame')

        self.manage_frame_service = roslibpy.Service(self.__client,
                                                     '/niryo_robot_poses_handlers/manage_dynamic_frame',
                                                     'niryo_robot_poses_handlers/ManageDynamicFrame')

        self.get_frame_list_service = roslibpy.Service(self.__client,
                                                       '/niryo_robot_poses_handlers/get_dynamic_frame_list',
                                                       'niryo_robot_msgs/GetNameDescriptionList')

    @staticmethod
    def get_dynamic_frame_from_name_request(frame_name):
        return roslibpy.ServiceRequest({"name": frame_name})

    @staticmethod
    def get_dynamic_frame_from_name_response_to_named_tuple(response):
        response = response["dynamic_frame"]
        frame = DynamicFrameInfo(response["name"], response["description"], 
                                 [response["position"]["x"], response["position"]["y"], response["position"]["z"]],
                                 [response["rpy"]["roll"], response["rpy"]["pitch"], response["rpy"]["yaw"]])
        return frame

    @staticmethod
    def save_dynamic_frame_from_poses_request(frame_name, description, poses_list, belong_to_workspace):
        dynamic_frame = {"name": frame_name, "description": description,
                         "poses": [pose_list_to_dict(pose) for pose in poses_list],
                         "belong_to_workspace": belong_to_workspace}
        return roslibpy.ServiceRequest(
            {"cmd": ManageFrames.SAVE.value, "dynamic_frame": dynamic_frame})

    @staticmethod
    def save_dynamic_frame_from_points_request(frame_name, description, points_list, belong_to_workspace):
        dynamic_frame = {"name": frame_name, "description": description, "points": points_list,
                         "belong_to_workspace": belong_to_workspace}
        return roslibpy.ServiceRequest(
            {"cmd": ManageFrames.SAVE_WITH_POINTS.value, "dynamic_frame": dynamic_frame})

    @staticmethod
    def edit_dynamic_frame_request(frame_name, new_frame_name, new_description):
        dynamic_frame = {"name": frame_name, "new_name": new_frame_name, "description": new_description}
        return roslibpy.ServiceRequest({"cmd": ManageFrames.EDIT.value, "dynamic_frame": dynamic_frame})

    @staticmethod
    def delete_dynamic_frame_request(frame_name, belong_to_workspace):
        return roslibpy.ServiceRequest({"cmd": ManageFrames.DELETE.value,
                                        "dynamic_frame": {"name": frame_name,
                                                          "belong_to_workspace": belong_to_workspace}})

    @staticmethod
    def get_saved_dynamic_frame_list_request():
        return roslibpy.ServiceRequest()

    @staticmethod
    def get_saved_dynamic_frame_list_response_to_list(response):
        list_name = response["name_list"]
        desc_list = response["description_list"]
        dict={}
        for x, y in zip(list_name, desc_list):
            dict[x] = y       
        return dict
