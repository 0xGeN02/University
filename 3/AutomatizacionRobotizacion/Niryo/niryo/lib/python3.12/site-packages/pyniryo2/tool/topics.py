from pyniryo2.niryo_topic import NiryoTopic
from pyniryo2.tool.enums import ToolID


class ToolTopics(object):

    def __init__(self, client):
        self.__client = client

        self.tool_id_topic = NiryoTopic(self.__client,
                                        '/niryo_robot_tools_commander/current_id',
                                        'std_msgs/Int32',
                                        tool_id_topic_conversion)


def tool_id_topic_conversion(msg):
    return ToolID(msg['data'])
