# - Imports
import numpy as np
import functools

from pyniryo2.robot_commander import RobotCommander

from .services import LedRingServices
from .topics import LedRingTopics
from .enums import AnimationMode


def check_ned2_version(func):
    """
    Decorator that check the robot version
    """
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        robot_instance = args[0]
        if robot_instance.client.hardware_version != 'ned2':
            raise Exception("Error Code : BAD_HARDWARE_VERSION\n"
                            "Message : Wrong robot hardware version, feature only available on Ned2")

        return func(*args, **kwargs)

    return wrap


class LedRing(RobotCommander):
    # --- Public functions --- #
    def __init__(self, client):
        """
        LedRing robot functions

        Example: ::

            ros_instance = NiryoRos("10.10.10.10") # Hotspot
            led_ring_interface = LedRing(ros_instance)

        :param client: Niryo ROS client
        :type client: NiryoRos
        """
        super(LedRing, self).__init__(client)

        self._services = LedRingServices(self._client)
        self._topics = LedRingTopics(self._client)
        # self.__action_timeout = 10

    # - Get current status and state of led ring

    @check_ned2_version
    @property
    def status(self):
        """
        Returns the Led Ring status client which can be used synchronously or asynchronously
        to obtain the current Led Ring status (cf LedRingStatusObject).

        Examples: ::

            # Get last value
            led_ring.status()
            led_ring.status.value

            # Subscribe a callback
            def status_callback(msg):
                print([msg.r, msg.g, msg.b])

            led_ring.status.subscribe(status_callback)
            led_ring.status.unsubscribe()

        :return: Led Ring status topic.
        :rtype: NiryoTopic
        """
        return self._topics.led_ring_status_topic

    @check_ned2_version
    def get_status(self):
        """
        Get Led Ring status.

        Example: ::

            status = led_ring.get_status()
            print(status.animation)

        :return: Object with the current led ring mode, the animation played and the color used
        :rtype: LedRingStatusObject
        """
        return self._topics.led_ring_status_topic()

    # - Control Led Ring with available animations
    @check_ned2_version
    def solid(self, color):
        """
        Set the whole Led Ring to a fixed color.

        Example: ::

            led_ring.solid([15, 50, 255])

        :param color: Led color in a list of size 3[R, G, B]. RGB channels from 0 to 255.
        :type color: list[float]
        :rtype: None
        """
        self.__classic_check_and_execute_w_color(AnimationMode.SOLID, color, 0, 0, True)

    @check_ned2_version
    def turn_off(self):
        """
        Turn off all LEDs

        Example: ::

            led_ring.turn_off()

        :rtype: None
        """
        self.__classic_check_and_execute_without_color(AnimationMode.NONE, 0, 0, True)

    @check_ned2_version
    def flash(self, color, period=0, iterations=0, wait=False, callback=None, timeout=None):
        """
        Flashes a color according to a frequency. The frequency is equal to 1 / period.

        Examples: ::

            # Synchronous use
            led_ring.flash([15, 50, 255])  # Non-blocking
            led_ring.flash([15, 50, 255], 1, 100, False)  # Non-blocking
            led_ring.flash([15, 50, 255], iterations=20, wait=True)  # Wait the end

            frequency = 20  # Hz
            total_duration = 10 # seconds
            led_ring.flash([15, 50, 255], 1./frequency, total_duration * frequency , True)

            # Asynchronous use
            def led_ring_callback(result):
                if result["status"] < RobotErrors.SUCCESS.value:
                    print("Failed")
                else:
                    print("Completed with success")

            led_ring.flash([15, 50, 255], iterations=20, wait=True, callback=calibration_callback)


        :param color: Led color in a list of size 3[R, G, B]. RGB channels from 0 to 255.
        :type color: list[float]
        :param period: Execution time for a pattern in seconds. If 0, the default time will be used.
        :type period: float
        :param iterations: Number of consecutive flashes. If 0, the Led Ring flashes endlessly.
        :type iterations: int
        :param wait: The service wait for the animation to finish all iterations or not to answer. If iterations
                is 0, the service answers immediately.
        :type wait: bool
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :param timeout: Timeout for the operation, in seconds. Only used if blocking.
        :type timeout: float
        :rtype: None
        """

        self.__classic_check_and_execute_w_color(AnimationMode.FLASHING, color, period, iterations, wait, callback,
                                                 timeout)

    @check_ned2_version
    def alternate(self, color_list, period=0, iterations=0, wait=False, callback=None, timeout=None):
        """
        Several colors are alternated one after the other.

        Examples: ::

            # Synchronous use
            color_list = [
                [15, 50, 255],
                [255, 0, 0],
                [0, 255, 0],
            ]

            led_ring.alternate(color_list) # Non-blocking
            led_ring.alternate(color_list, 1, 100, False) # Non-blocking
            led_ring.alternate(color_list, iterations=20, wait=True) # Blocking

            # Asynchronous use
            def led_ring_callback(result):
                if result["status"] < RobotErrors.SUCCESS.value:
                    print("Failed")
                else:
                    print("Completed with success")

            led_ring.alternate(color_list, iterations=20, wait=True, callback=calibration_callback)

        :param color_list: Led color list of lists of size 3[R, G, B]. RGB channels from 0 to 255.
        :type color_list: list[list[float]]
        :param period: Execution time for a pattern in seconds. If 0, the default time will be used.
        :type period: float
        :param iterations: Number of consecutive alternations. If 0, the Led Ring alternates endlessly.
        :type iterations: int
        :param wait: The service wait for the animation to finish all iterations or not to answer. If iterations
                is 0, the service answers immediately.
        :type wait: bool
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :param timeout: Timeout for the operation, in seconds. Only used if blocking.
        :type timeout: float
        :rtype: None
        """
        self.__classic_check_and_execute_w_color_list(AnimationMode.ALTERNATE, color_list, period, iterations, wait,
                                                      callback,
                                                      timeout)

    @check_ned2_version
    def chase(self, color, period=00, iterations=0, wait=False, callback=None, timeout=None):
        """
        Movie theater light style chaser animation.

        Examples: ::

            # Synchronous use
            led_ring.chase([15, 50, 255]) # Non-blocking
            led_ring.chase([15, 50, 255], 1, 100, False) # Non-blocking
            led_ring.chase([15, 50, 255], iterations=20, wait=True) # Blocking

            # Asynchronous use
            def led_ring_callback(result):
                if result["status"] < RobotErrors.SUCCESS.value:
                    print("Failed")
                else:
                    print("Completed with success")

            led_ring.chase([15, 50, 255], iterations=20, wait=True, callback=calibration_callback)

        :param color: Led color in a list of size 3[R, G, B]. RGB channels from 0 to 255.
        :type color: list[float]
        :param period: Execution time for a pattern in seconds. If 0, the default time will be used.
        :type period: float
        :param iterations: Number of consecutive chase. If 0, the animation continues endlessly.
            One chase just lights one Led every 3 LEDs.
        :type iterations: int
        :param wait: The service wait for the animation to finish all iterations or not to answer. If iterations
                is 0, the service answers immediately.
        :type wait: bool
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :param timeout: Timeout for the operation, in seconds. Only used if blocking.
        :type timeout: float
        :rtype: None
        """
        self.__classic_check_and_execute_w_color(AnimationMode.CHASE, color, period, iterations, wait, callback,
                                                 timeout)

    @check_ned2_version
    def wipe(self, color, period=0, wait=False, callback=None, timeout=None):
        """
        Wipe a color across the Led Ring, light a Led at a time.

        Examples: ::

            # Synchronous use
            robot.wipe([15, 50, 255])  # Non-blocking
            led_ring.wipe([15, 50, 255], 1, False)  # Non-blocking
            led_ring.wipe([15, 50, 255], wait=True)  # Blocking

            # Asynchronous use
            def led_ring_callback(result):
                if result["status"] < RobotErrors.SUCCESS.value:
                    print("Failed")
                else:
                    print("Completed with success")

            led_ring.wipe([15, 50, 255], wait=True, callback=calibration_callback)

        :param color: Led color in a list of size 3[R, G, B]. RGB channels from 0 to 255.
        :type color: list[float]
        :param period: Execution time for a pattern in seconds. If 0, the default time will be used.
        :type period: float
        :param wait: The service wait for the animation to finish or not to answer.
        :type wait: bool
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :param timeout: Timeout for the operation, in seconds. Only used if blocking.
        :type timeout: float
        :rtype: None
        """
        self.__classic_check_and_execute_w_color(AnimationMode.COLOR_WIPE, color, period, 0, wait, callback,
                                                 timeout)

    @check_ned2_version
    def go_up(self, color, period=0, iterations=0, wait=False, callback=None, timeout=None):
        """
        LEDs turn on like a loading circle, and are then all turned off at once.

        Examples: ::

            # Synchronous use
            led_ring.go_up([15, 50, 255])  # Non-blocking
            led_ring.go_up([15, 50, 255], 1, 100, False)  # Non-blocking
            led_ring.go_up([15, 50, 255], iterations=20, wait=True)  # Blocking

            # Asynchronous use
            def led_ring_callback(result):
                if result["status"] < RobotErrors.SUCCESS.value:
                    print("Failed")
                else:
                    print("Completed with success")

            led_ring.go_up([15, 50, 255], period=2, iterations=20, wait=True, callback=calibration_callback)

        :param color: Led color in a list of size 3[R, G, B]. RGB channels from 0 to 255.
        :type color: list[float]
        :param period: Execution time for a pattern in seconds. If 0, the default time will be used.
        :type period: float
        :param iterations: Number of consecutive turns around the Led Ring. If 0, the animation
            continues endlessly.
        :type iterations: int
        :param wait: The service wait for the animation to finish or not to answer. If iterations
                is 0, the service answers immediately.
        :type wait: bool
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :param timeout: Timeout for the operation, in seconds. Only used if blocking.
        :type timeout: float
        :rtype: None
        """
        self.__classic_check_and_execute_w_color(AnimationMode.GO_UP, color, period, iterations, wait, callback,
                                                 timeout)

    @check_ned2_version
    def go_up_down(self, color, period=0, iterations=0, wait=False, callback=None, timeout=None):
        """
        LEDs turn on like a loading circle, and are turned off the same way.

        Examples: ::

            # Synchronous use
            led_ring.go_up_down([15, 50, 255])  # Non-blocking
            led_ring.go_up_down([15, 50, 255], 1, 100, False)  # Non-blocking
            led_ring.go_up_down([15, 50, 255], iterations=20, wait=True)  # Blocking

            # Asynchronous use
            def led_ring_callback(result):
                if result["status"] < RobotErrors.SUCCESS.value:
                    print("Failed")
                else:
                    print("Completed with success")

            led_ring.go_up_down([15, 50, 255], period=2, iterations=20, wait=True, callback=calibration_callback)

        :param color: Led color in a list of size 3[R, G, B]. RGB channels from 0 to 255.
        :type color: list[float]
        :param period: Execution time for a pattern in seconds. If 0, the default time will be used.
        :type period: float
        :param iterations: Number of consecutive turns around the Led Ring. If 0, the animation
            continues endlessly.
        :type iterations: int
        :param wait: The service wait for the animation to finish or not to answer. If iterations
                is 0, the service answers immediately.
        :type wait: bool
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :param timeout: Timeout for the operation, in seconds. Only used if blocking.
        :type timeout: float
        :rtype: None
        """
        self.__classic_check_and_execute_w_color(AnimationMode.GO_UP_AND_DOWN, color, period, iterations, wait,
                                                 callback,
                                                 timeout)

    @check_ned2_version
    def breath(self, color, period=0, iterations=0, wait=False, callback=None, timeout=None):
        """
        Variation of the light intensity of the LED ring, similar to human breathing.

        Examples: ::

            # Synchronous use
            led_ring.breath([15, 50, 255])  # Non-blocking
            led_ring.breath([15, 50, 255], 1, 100, False)  # Non-blocking
            led_ring.breath([15, 50, 255], iterations=20, wait=True)  # Blocking

            # Asynchronous use
            def led_ring_callback(result):
                if result["status"] < RobotErrors.SUCCESS.value:
                    print("Failed")
                else:
                    print("Completed with success")

            led_ring.breath([15, 50, 255], period=2, iterations=20, wait=True,
                callback=calibration_callback)

        :param color: Led color in a list of size 3[R, G, B]. RGB channels from 0 to 255.
        :type color: list[float]
        :param period: Execution time for a pattern in seconds. If 0, the default time will be used.
        :type period: float
        :param iterations: Number of consecutive turns around the Led Ring. If 0, the animation
            continues endlessly.
        :type iterations: int
        :param wait: The service wait for the animation to finish or not to answer. If iterations
                is 0, the service answers immediately.
        :type wait: bool
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :param timeout: Timeout for the operation, in seconds. Only used if blocking.
        :type timeout: float
        :rtype: None
        """
        self.__classic_check_and_execute_w_color(AnimationMode.BREATH, color, period, iterations, wait, callback,
                                                 timeout)

    @check_ned2_version
    def snake(self, color, period=0, iterations=0, wait=False, callback=None, timeout=None):
        """
        A small coloured snake (certainly a python :D ) runs around the LED ring.

        Examples: ::

            # Synchronous use
            led_ring.snake([15, 50, 255]) # Non-blocking
            led_ring.snake([15, 50, 255], 1, 100, True) # Blocking

            # Asynchronous use
            def led_ring_callback(result):
                if result["status"] < RobotErrors.SUCCESS.value:
                    print("Failed")
                else:
                    print("Completed with success")

            led_ring.snake([15, 50, 255], period=2, iterations=20, wait=True, callback=calibration_callback)

        :param color: Led color in a list of size 3[R, G, B]. RGB channels from 0 to 255.
        :type color: list[float]
        :param period: Execution time for a pattern in seconds. If 0, the default duration will be used.
        :type period: float
        :param iterations: Number of consecutive turns around the Led Ring. If 0, the animation
            continues endlessly.
        :type iterations: int
        :param wait: The service wait for the animation to finish or not to answer. If iterations
                is 0, the service answers immediately.
        :type wait: bool
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :param timeout: Timeout for the operation, in seconds. Only used if blocking.
        :type timeout: float
        :rtype: None
        """
        self.__classic_check_and_execute_w_color(AnimationMode.SNAKE, color, period, iterations, wait, callback,
                                                 timeout)

    @check_ned2_version
    def rainbow(self, period=0, iterations=0, wait=False, callback=None, timeout=None):
        """
        Draw rainbow that fades across all LEDs at once.

        Examples: ::

            # Synchronous use
            led_ring.rainbow()  # Non-blocking
            led_ring.rainbow(5, 2, True)  # Blocking
            led_ring.rainbow(wait=True)  # Blocking

            # Asynchronous use
            def led_ring_callback(result):
                if result["status"] < RobotErrors.SUCCESS.value:
                    print("Failed")
                else:
                    print("Completed with success")

            led_ring.rainbow(period=2, iterations=20, wait=True, callback=calibration_callback)

        :param period: Execution time for a pattern in seconds. If 0, the default time will be used.
        :type period: float
        :param iterations: Number of consecutive rainbows. If 0, the animation continues endlessly.
        :type iterations: int
        :param wait: The service wait for the animation to finish or not to answer. If iterations
                is 0, the service answers immediately.
        :type wait: bool
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :param timeout: Timeout for the operation, in seconds. Only used if blocking.
        :type timeout: float
        :rtype: None
        """
        self.__classic_check_and_execute_without_color(AnimationMode.RAINBOW, period, iterations, wait, callback,
                                                       timeout)

    @check_ned2_version
    def rainbow_cycle(self, period=0, iterations=0, wait=False, callback=None, timeout=None):
        """
        Draw rainbow that uniformly distributes itself across all LEDs.

        Examples: ::

            # Synchronous use
            led_ring.rainbow_cycle()
            led_ring.rainbow_cycle(5, 2, True)
            led_ring.rainbow_cycle(wait=True)

            # Asynchronous use
            def led_ring_callback(result):
                if result["status"] < RobotErrors.SUCCESS.value:
                    print("Failed")
                else:
                    print("Completed with success")

            led_ring.rainbow_cycle(period=2, iterations=20, wait=True, callback=calibration_callback)

        :param period: Execution time for a pattern in seconds. If 0, the default time will be used.
        :type period: float
        :param iterations: Number of consecutive rainbow cycles. If 0, the animation continues endlessly.
        :type iterations: int
        :param wait: The service wait for the animation to finish or not to answer. If iterations
                is 0, the service answers immediately.
        :type wait: bool
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :param timeout: Timeout for the operation, in seconds. Only used if blocking.
        :type timeout: float
        :rtype: None
        """
        self.__classic_check_and_execute_without_color(AnimationMode.RAINBOW_CYLE, period, iterations, wait, callback,
                                                       timeout)

    @check_ned2_version
    def rainbow_chase(self, period=0, iterations=0, wait=False, callback=None, timeout=None):
        """
        Rainbow chase animation, like the led_ring_chase method.

        Examples: ::

            # Synchronous use
            led_ring.rainbow_chase()
            led_ring.rainbow_chase(5, 2, True)
            led_ring.rainbow_chase(wait=True)

            # Asynchronous use
            def led_ring_callback(result):
                if result["status"] < RobotErrors.SUCCESS.value:
                    print("Failed")
                else:
                    print("Completed with success")

            led_ring.rainbow_chase(period=2, iterations=20, wait=True, callback=calibration_callback)

        :param period: Execution time for a pattern in seconds. If 0, the default time will be used.
        :type period: float
        :param iterations: Number of consecutive rainbow cycles. If 0, the animation continues endlessly.
        :type iterations: int
        :param wait: The service wait for the animation to finish or not to answer. If iterations
                is 0, the service answers immediately.
        :type wait: bool
        :param callback: Callback invoked on successful execution.
        :type callback: function
        :param timeout: Timeout for the operation, in seconds. Only used if blocking.
        :type timeout: float
        :rtype: None
        """
        self.__classic_check_and_execute_without_color(AnimationMode.RAINBOW_CHASE, period, iterations, wait, callback,
                                                       timeout)

    @check_ned2_version
    def custom(self, led_colors):
        """
        Sends a colour command to all LEDs of the LED ring.
        The function expects a list of colours for the 30 LEDs  of the robot.

        Example: ::

            led_list = [[i / 30. * 255 , 0, 255 - i / 30.] for i in range(30)]
            led_ring.custom(led_list)

            run_flag = True

            def french_flag_moving():
                colors = []
                colors += [[255, 255, 255] for _ in range(2)]
                colors += [[0, 0, 255] for _ in range(11)]
                colors += [[255, 255, 255] for _ in range(4)]
                colors += [[255, 0, 0] for _ in range(11)]
                colors += [[255, 255, 255] for _ in range(2)]

                rate = 10
                while run_flag:
                    for i in range(len(colors)):
                        led_ring.custom(colors[i:] + colors[:i])
                        time.sleep(1/rate)
                        if not run_flag:
                            return

            french_flag_moving()

        :param led_colors: List of size 30 of led color in a list of size 3[R, G, B].
                RGB channels from 0 to 255.
        :type led_colors: list[list[float]]
        :rtype: None
        """
        self._check_length(led_colors, 30)
        self.__classic_check_and_execute_w_color_list(AnimationMode.CUSTOM, led_colors, 0, 0, True)

    def set_led_color(self, led_id, color):
        """
        Lights up an LED in one colour. RGB colour between 0 and 255.

        Example: ::

            robot.set_led_color(5, [15, 50, 255])

        :param led_id: Id of the led: between 0 and 29
        :type led_id: int
        :param color: Led color in a list of size 3[R, G, B]. RGB channels from 0 to 255.
        :type color: list[float]
        :rtype: None
        """
        color = self._check_color(color)
        self._check_type(led_id, int)

        req = self._services.set_led_ring_color_request(led_id, color)
        resp = self._services.set_led_ring_led_color_service.call(req)
        self._check_result_status(resp)

    # Usefull method Led Ring
    def __classic_check_and_execute_w_color(self, animation, color, period, iterations, wait, callback=None,
                                            timeout=None):
        checked_color = self._check_color(color)
        self._check_instance(period, (float, int))
        self._check_type(iterations, int)
        self._check_type(wait, bool)
        self._check_enum_belonging(animation, AnimationMode)

        req = self._services.set_led_ring_request(animation, color_list=checked_color, period=period,
                                                  iterations=iterations, wait=wait)
        resp = self._services.set_led_ring_animation_service.call(req, callback=callback, timeout=timeout)

        if not callback:
            self._check_result_status(resp)

    def __classic_check_and_execute_w_color_list(self, animation, color_list, period, iterations, wait, callback=None,
                                                 timeout=None):
        self._check_instance(period, (float, int))
        self._check_type(iterations, int)
        self._check_type(wait, bool)
        self._check_enum_belonging(animation, AnimationMode)

        checked_color_list = [self._check_color(color) for index, color in enumerate(color_list)]

        req = self._services.set_led_ring_request(animation, color_list=checked_color_list, period=period,
                                                  iterations=iterations, wait=wait)
        resp = self._services.set_led_ring_animation_service.call(req, callback=callback, timeout=timeout)

        if not callback:
            self._check_result_status(resp)

    def __classic_check_and_execute_without_color(self, animation, period, iterations, wait, callback=None,
                                                  timeout=None):
        self._check_instance(period, (float, int))
        self._check_type(iterations, int)
        self._check_type(wait, bool)
        self._check_enum_belonging(animation, AnimationMode)

        req = self._services.set_led_ring_request(animation, period=period, iterations=iterations,
                                                  wait=wait)
        resp = self._services.set_led_ring_animation_service.call(req, callback=callback, timeout=timeout)

        if not callback:
            self._check_result_status(resp)
            
    def _check_color(self, color):
        checked_color = []
        self._check_type(color, list)
        if len(color) != 3:
            self._raise_exception("Color must be a list of size 3: [r, g, b]")
        for color_elem in color:
            if not 0 <= color_elem <= 255:
                self._raise_exception_expected_range(0, 255, color_elem)
            checked_color.append(self._transform_to_type(color_elem, float))
        return checked_color
