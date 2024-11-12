from pyniryo2.niryo_topic import NiryoTopic

from .objects import ConveyorInfo
from .enums import ConveyorID, ConveyorTTL, ConveyorCan, ConveyorDirection


class ConveyorTopics(object):

    def __init__(self, client):
        self.__client = client

        self.conveyor_feedback_topic = NiryoTopic(self.__client,
                                                  '/niryo_robot/conveyor/feedback',
                                                  'conveyor_interface/ConveyorFeedbackArray',
                                                  conveyor_feedback_topic_conversion)


def conveyor_feedback_topic_conversion(msg):
    return [ConveyorInfo(conveyor_id=conveyor_id_to_conveyor_type(conveyor['conveyor_id']),
                         running=conveyor['running'],
                         speed=conveyor['speed'],
                         direction=ConveyorDirection(conveyor['direction'])) for conveyor in msg['conveyors']]


def conveyor_id_to_conveyor_type(conveyor_id):
    try:
        return ConveyorID(conveyor_id)
    except ValueError:
        try:
            return ConveyorTTL(conveyor_id)
        except ValueError:
            try:
                return ConveyorCan(conveyor_id)
            except ValueError:
                return conveyor_id
