import roslibpy

from .enums import ManageSound


class SoundServices(object):

    def __init__(self, client):
        self.__client = client

        self.play_sound_service = roslibpy.Service(self.__client,
                                                   '/niryo_robot_sound/play',
                                                   'niryo_robot_sound/PlaySound')

        self.stop_sound_service = roslibpy.Service(self.__client,
                                                   '/niryo_robot_sound/stop',
                                                   'niryo_robot_msgs/Trigger')

        self.set_sound_volume_service = roslibpy.Service(self.__client,
                                                         '/niryo_robot_sound/set_volume',
                                                         'niryo_robot_msgs/SetInt')

        self.manage_sound_service = roslibpy.Service(self.__client,
                                                     '/niryo_robot_sound/manage',
                                                     'niryo_robot_msgs/ManageSound')

        self.tts_service = roslibpy.Service(self.__client,
                                            '/niryo_robot_sound/text_to_speech',
                                            'niryo_robot_sound/TextToSpeech')

    @staticmethod
    def play_sound_request(sound_name, start_time_sec=0, end_time_sec=0, wait_end=False):
        """

        :param sound_name:
        :type sound_name: str
        param start_time_sec:
        :type start_time_sec: float
        :param end_time_sec:
        :type end_time_sec: float
        :param wait_end:
        :type wait_end: bool
        :return:
        :rtype: ServiceRequest
        """
        return roslibpy.ServiceRequest({"sound_name": sound_name, "start_time_sec": start_time_sec,
                                        "end_time_sec": end_time_sec, "wait_end": wait_end})

    @staticmethod
    def stop_sound_request():
        """

        :return:
        :rtype: ServiceRequest
        """
        return roslibpy.ServiceRequest()

    @staticmethod
    def set_sound_volume_request(value):
        """

        :param value:
        :type value: int8
        :return:
        :rtype: ServiceRequest
        """
        return roslibpy.ServiceRequest({"value": value})

    @staticmethod
    def import_sound_request(sound_name, sound_data):
        """

        :param sound_name:
        :type sound_name: str
        :param sound_data:
        :type sound_data: str
        :return:
        :rtype: ServiceRequest
        """
        return roslibpy.ServiceRequest(
            {"sound_name": sound_name, "sound_data": sound_data, "action": ManageSound.ADD.value})

    @staticmethod
    def delete_sound_request(sound_name):
        """

        :param sound_name:
        :type sound_name: str
        :return:
        :rtype: ServiceRequest
        """
        return roslibpy.ServiceRequest(
            {"sound_name": sound_name, "action": ManageSound.DELETE.value})

    @staticmethod
    def tts_request(text, language):
        """

        :param text:
        :type text: str
        :param language:
        :type language: Language
        :return:
        :rtype: ServiceRequest
        """
        return roslibpy.ServiceRequest({"text": text, "language": language.value})
