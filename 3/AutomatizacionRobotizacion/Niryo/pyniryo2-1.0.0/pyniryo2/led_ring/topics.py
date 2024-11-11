from pyniryo2.niryo_topic import NiryoTopic
from pyniryo2.led_ring.objects import LedRingStatusObject


class LedRingTopics(object):

    def __init__(self, client):
        self.__client = client

        self.led_ring_status_topic = NiryoTopic(self.__client,
                                                '/niryo_robot_led_ring/led_ring_status',
                                                'niryo_robot_led_ring/LedRingStatus',
                                                led_status_topic_conversion)


def led_status_topic_conversion(msg):
    led_status = LedRingStatusObject()
    led_status.init_from_message(msg)
    return led_status
