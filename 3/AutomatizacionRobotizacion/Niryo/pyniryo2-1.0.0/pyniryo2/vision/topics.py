import numpy as np
import base64

from pyniryo2.niryo_topic import NiryoTopic
from .objects import CameraInfo, ImageParameters


class VisionTopics(object):

    def __init__(self, client):
        self.__client = client

        self.compressed_video_stream_topic = NiryoTopic(self.__client,
                                                        '/niryo_robot_vision/compressed_video_stream',
                                                        'sensor_msgs/CompressedImage',
                                                        compressed_video_stream_topic_conversion)

        self.camera_info_topic = NiryoTopic(self.__client,
                                            '/niryo_robot_vision/camera_intrinsics',
                                            'sensor_msgs/CameraInfo',
                                            camera_info_topic_conversion)

        self.video_stream_parameters_topic = NiryoTopic(self.__client,
                                                        '/niryo_robot_vision/video_stream_parameters',
                                                        'niryo_robot_vision/ImageParameters',
                                                        video_stream_parameters_topic_conversion)


def compressed_video_stream_topic_conversion(msg):
    # Convert base64 into uint8 array
    return base64.b64decode(msg['data'])


def camera_info_topic_conversion(msg):
    mtx = np.reshape(msg['K'], (3, 3))
    dist = np.expand_dims(msg['D'], axis=0)

    return CameraInfo(intrinsics=mtx, distortion=dist)


def video_stream_parameters_topic_conversion(msg):
    return ImageParameters(brightness_factor=msg["brightness_factor"], contrast_factor=msg["contrast_factor"],
                           saturation_factor=msg["saturation_factor"])
