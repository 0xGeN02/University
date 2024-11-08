from pyniryo2.niryo_topic import NiryoTopic


class SoundTopics(object):

    def __init__(self, client):
        self.__client = client

        self.sound_database_topic = NiryoTopic(self.__client,
                                               '/niryo_robot_sound/sound_database',
                                               'niryo_robot_sound/SoundList',
                                               sound_database_conversion)

        self.current_sound_topic = NiryoTopic(self.__client,
                                              '/niryo_robot_sound/sound',
                                              'std_msgs/String',
                                              current_sound_conversion)

        self.volume_topic = NiryoTopic(self.__client,
                                       '/niryo_robot_sound/volume',
                                       'std_msgs/UInt8',
                                       volume_sound_conversion)


def sound_database_conversion(msg):
    return {str(sound["name"]): sound["duration"] for sound in msg["sounds"]}


def current_sound_conversion(msg):
    return str(msg["data"])


def volume_sound_conversion(msg):
    return int(msg["data"])
