from pyniryo2.io.enums import PinMode
from pyniryo2.io.objects import DigitalPinObject, AnalogPinObject
from pyniryo2.niryo_topic import NiryoTopic


class IOTopics(object):

    def __init__(self, client):
        self.__client = client

        self.digital_io_topic = NiryoTopic(self.__client,
                                           '/niryo_robot_rpi/digital_io_state',
                                           'niryo_robot_rpi/DigitalIOState',
                                           digital_io_state_topic_conversion)

        self.analog_io_topic = NiryoTopic(self.__client,
                                          '/niryo_robot_rpi/analog_io_state',
                                          'niryo_robot_rpi/AnalogIOState',
                                          analog_io_state_topic_conversion)

        self.__custom_button_topic = NiryoTopic(self.__client,
                                                '/niryo_robot_hardware_interface/end_effector_interface/custom_button_status',
                                                'end_effector_interface/EEButtonStatus',
                                                custom_button_topic_conversion)


def digital_io_state_topic_conversion(msg):
    digital_inputs = [DigitalPinObject(str(di['name']), PinMode.INPUT, di['value']) for di in msg["digital_inputs"]]
    digital_outputs = [DigitalPinObject(str(do['name']), PinMode.OUTPUT, do['value']) for do in msg["digital_outputs"]]
    return digital_inputs + digital_outputs


def analog_io_state_topic_conversion(msg):
    analog_inputs = [AnalogPinObject(str(ai['name']), PinMode.INPUT, ai['value']) for ai in msg["analog_inputs"]]
    analog_outputs = [AnalogPinObject(str(ao['name']), PinMode.OUTPUT, ao['value']) for ao in msg["analog_outputs"]]
    return analog_inputs + analog_outputs


def custom_button_topic_conversion(msg):
    return msg["action"] != msg["NO_ACTION"]
