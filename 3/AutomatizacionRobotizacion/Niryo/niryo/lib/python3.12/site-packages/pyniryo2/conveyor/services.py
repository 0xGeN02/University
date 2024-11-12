import roslibpy
from .enums import ConveyorStatus, ConveyorID, ConveyorDirection


class ConveyorServices(object):

    def __init__(self, client):
        self.__client = client

        self.ping_and_set_conveyor_service = roslibpy.Service(self.__client,
                                                              '/niryo_robot/conveyor/ping_and_set_conveyor',
                                                              'conveyor_interface/SetConveyor')

        self.control_conveyor_service = roslibpy.Service(self.__client,
                                                         '/niryo_robot/conveyor/control_conveyor',
                                                         'conveyor_interface/ControlConveyor')

    @staticmethod
    def get_ping_and_set_conveyor_request():
        return roslibpy.ServiceRequest({"cmd": ConveyorStatus.ADD.value})

    @staticmethod
    def unset_conveyor_request(conveyor_id):
        """

        :param conveyor_id:
        :type conveyor_id: ConveyorID
        :return:
        :rtype: ServiceRequest
        """
        return roslibpy.ServiceRequest({"cmd": ConveyorStatus.REMOVE.value, "id": conveyor_id.value})

    @staticmethod
    def control_conveyor_request(conveyor_id, control_on, speed, direction):
        """

        :param conveyor_id:
        :type conveyor_id: ConveyorID
        :param control_on:
        :type control_on: bool
        :param speed:
        :type speed: int
        :param direction:
        :type direction: ConveyorDirection
        :return:
        :rtype: ServiceRequest
        """
        return roslibpy.ServiceRequest(
            {"id": conveyor_id.value, "control_on": control_on, "speed": speed, "direction": direction.value})
