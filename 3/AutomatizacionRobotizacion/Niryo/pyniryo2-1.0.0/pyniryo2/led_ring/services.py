import roslibpy

from .enums import AnimationMode


class LedRingServices(object):

    def __init__(self, client):
        self.__client = client

        self.set_led_ring_animation_service = roslibpy.Service(self.__client,
                                                               '/niryo_robot_led_ring/set_user_animation',
                                                               'niryo_robot_led_ring/LedUser')

        self.set_led_ring_led_color_service = roslibpy.Service(self.__client,
                                                               '/niryo_robot_led_ring/set_led_color',
                                                               'niryo_robot_led_ring/SetLedColor')

    def set_led_ring_request(self, animation_nb, color_list=None, period=0, iterations=0, wait=False):
        animation_mode = {'animation': animation_nb.value if isinstance(animation_nb, AnimationMode) else animation_nb}

        if not isinstance(color_list, list) or len(color_list) < 1:
            color_list_rgb = []
        elif not isinstance(color_list[0], list):
            color_list_rgb = [self.color_to_color_rgba(color) for color in [color_list]]
        else:
            color_list_rgb = [self.color_to_color_rgba(color) for color in color_list]

        return roslibpy.ServiceRequest({"animation_mode": animation_mode,
                                        "colors": color_list_rgb,
                                        "period": period,
                                        "iterations": iterations,
                                        "wait_end": wait})

    def set_led_ring_color_request(self, led_id, color):
        color_rgba = [] if not isinstance(color, list) else color[:]
        return roslibpy.ServiceRequest({"led_id": led_id,
                                        "color": self.color_to_color_rgba(color_rgba)})

    @staticmethod
    def color_to_color_rgba(color):
        color_rgb = color if len(color) >= 3 else color[:] + (3 - len(color)) * [0]
        return {'r': color_rgb[0], 'g': color_rgb[1], 'b': color_rgb[2], 'a': 0}
