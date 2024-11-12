import roslibpy
from pyniryo2.tool.enums import ToolID
from pyniryo2.utils import pose_list_to_dict


class ToolServices(object):

    def __init__(self, client):
        self.__client = client

        self.update_tool_service = roslibpy.Service(self.__client,
                                                    '/niryo_robot_tools_commander/update_tool',
                                                    'niryo_robot_msgs/Trigger')

        self.equip_electromagnet_service = roslibpy.Service(self.__client,
                                                            '/niryo_robot_tools_commander/equip_electromagnet',
                                                            'niryo_robot_msgs/SetInt')

        self.enable_tcp_service = roslibpy.Service(self.__client,
                                                   '/niryo_robot_tools_commander/enable_tcp',
                                                   'niryo_robot_msgs/SetBool')

        self.set_tcp_service = roslibpy.Service(self.__client,
                                                '/niryo_robot_tools_commander/set_tcp',
                                                'niryo_robot_tools_commander/SetTCP')

        self.reset_tcp_service = roslibpy.Service(self.__client,
                                                  '/niryo_robot_tools_commander/reset_tcp',
                                                  'niryo_robot_msgs/Trigger')

    @staticmethod
    def get_trigger_request():
        return roslibpy.ServiceRequest()

    @staticmethod
    def equip_electromagnet_service_request(id_=ToolID.ELECTROMAGNET_1):
        return roslibpy.ServiceRequest({"value": id_.value})

    @staticmethod
    def enable_tcp_service_request(enable):
        return roslibpy.ServiceRequest({"value": enable})

    @staticmethod
    def set_tcp_service_request(pose):
        return roslibpy.ServiceRequest(pose_list_to_dict(pose))
