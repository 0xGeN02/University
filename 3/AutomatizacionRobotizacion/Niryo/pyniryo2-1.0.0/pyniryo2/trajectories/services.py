import roslibpy

from pyniryo2.utils import pose_quat_dict_to_list

from .enums import ManageTrajectories


class TrajectoriesServices(object):

    def __init__(self, client):
        self.__client = client

        self.get_trajectory_from_name_service = roslibpy.Service(self.__client,
                                                                 '/niryo_robot_arm_commander/get_trajectory',
                                                                 'niryo_robot_arm_commander/GetTrajectory')

        self.trajectory_manager_service = roslibpy.Service(self.__client,
                                                           '/niryo_robot_arm_commander/manage_trajectory',
                                                           'niryo_robot_arm_commander/ManageTrajectory')

        self.get_trajectory_list_service = roslibpy.Service(self.__client,
                                                            '/niryo_robot_arm_commander/get_trajectory_list',
                                                            'niryo_robot_arm_commander/GetNameDescriptionList')

    @staticmethod
    def get_trajectory_from_name_request(traj_name):
        return roslibpy.ServiceRequest({"name": traj_name})

    @staticmethod
    def save_last_learned_trajectory_request(name, description=""):
        return roslibpy.ServiceRequest(
            {"cmd": ManageTrajectories.SAVE_LAST_LEARNED.value, "name": name, "description": description})

    @staticmethod
    def save_trajectory_request(trajectory, name, description=""):
        return roslibpy.ServiceRequest(
            {"cmd": ManageTrajectories.SAVE.value, "trajectory": trajectory, "name": name, "description": description})

    @staticmethod
    def delete_trajectory_request(name):
        return roslibpy.ServiceRequest({"cmd": ManageTrajectories.DELETE.value, "name": name})

    @staticmethod
    def clean_trajectory_memory_request():
        return roslibpy.ServiceRequest({"cmd": ManageTrajectories.DELETE_ALL.value})

    @staticmethod
    def execute_registered_trajectory_request(name):
        return roslibpy.ServiceRequest({"cmd": ManageTrajectories.EXECUTE_REGISTERED.value, "name": name})

    @staticmethod
    def update_trajectory_infos_request(name, new_name, description=""):
        return roslibpy.ServiceRequest(
            {"cmd": ManageTrajectories.UPDATE.value, "name": name, "new_name": new_name, "description": description})

    @staticmethod
    def get_saved_trajectory_list_request():
        return roslibpy.ServiceRequest()

    @staticmethod
    def pose_trajectory_dict_to_list(traj_dict):
        return [pose_quat_dict_to_list(pose_dict) for pose_dict in traj_dict]

    @staticmethod
    def trajectory_to_dict(trajectory):
        traj_dict = {
            'joint_names': ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6"],
            'points': [{'positions': positions} for positions in trajectory]
        }
        return traj_dict

    @staticmethod
    def trajectory_dict_to_list(traj_dict):
        return [point["positions"] for point in traj_dict["points"]]
