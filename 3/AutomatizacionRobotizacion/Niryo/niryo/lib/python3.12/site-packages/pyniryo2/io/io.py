from pyniryo2.enums import RobotErrors
from pyniryo2.exceptions import RobotCommandException
from pyniryo2.robot_commander import RobotCommander
from .enums import PinID, PinMode, PinState
from .services import IOServices
from .topics import IOTopics
from .objects import DigitalPinObject, AnalogPinObject


def check_ned2_version(func):
    """
    Decorator that check the robot version
    """

    def wrap(*args, **kwargs):
        robot_instance = args[0]
        if robot_instance.client.hardware_version != 'ned2':
            raise Exception("Error Code : BAD_HARDWARE_VERSION\n"
                            "Message : Wrong robot hardware version, feature only available on Ned2")

        return func(*args, **kwargs)

    return wrap


def check_ned_one_version(func):
    """
    Decorator that check the robot version
    """

    def wrap(*args, **kwargs):
        robot_instance = args[0]
        if robot_instance.client.hardware_version != 'ned2':
            raise Exception("Error Code : BAD_HARDWARE_VERSION\n"
                            "Message : Wrong robot hardware version, feature only available on Ned1 and One")

        return func(*args, **kwargs)

    return wrap


class IO(RobotCommander):
    # --- Public functions --- #
    def __init__(self, client):
        """
        IO robot functions

        Example: ::

            ros_instance = NiryoRos("10.10.10.10") # Hotspot
            io_interface = IO(ros_instance)

        :param client: Niryo ROS client
        :type client: NiryoRos
        """
        super(IO, self).__init__(client)

        self._services = IOServices(self._client)
        self._topics = IOTopics(self._client)

    @property
    def digital_io_states(self):
        """
        Return the value of digital ios.

        :return: State, Name, Mode of the pin
        :rtype: DigitalPinObject
        """
        return self.get_digital_io_states()

    @property
    def get_digital_io_states(self):
        """
        Returns the io state client which can be used synchronously or asynchronously to obtain the io states.
        The io state client returns a list of DigitalPinObject.

        Examples: ::

            # Get last value
            io.get_digital_io_states()
            io.get_digital_io_states.value

            # Subscribe a callback
            def io_callback(io_state):
                print io_state

            io.get_digital_io_states.subscribe(io_callback)
            io.get_digital_io_states.unsubscribe()

        :return: io state topic instance
        :rtype: NiryoTopic
        """
        return self._topics.digital_io_topic

    def get_digital_io_state(self, pin_id):
        """
        Return the value of a digital io.

        :type pin_id: PinID or str
        :return: digital io object
        :rtype: DigitalPinObject
        """
        self._check_instance(pin_id, (PinID, str))
        states = self._topics.digital_io_topic()

        for state in states:
            if state.pin_id == pin_id or state.name == pin_id:
                return state

        raise RobotCommandException('IO {} not found'.format(pin_id))

    @check_ned_one_version
    def set_pin_mode(self, pin_id, pin_mode):
        """
        Set pin number pin_id to mode pin_mode

        Examples: ::

            io.set_pin_mode(PinID.GPIO_1A, PinMode.INPUT)
            io.set_pin_mode("1A", PinMode.OUTPUT)

        :param pin_id:
        :type pin_id: PinID or str
        :param pin_mode:
        :type pin_mode: PinMode
        :rtype: None
        """
        self._check_instance(pin_id, (PinID, str))
        self._check_enum_belonging(pin_mode, PinMode)

        req = self._services.set_io_mode_request(pin_id, pin_mode)
        resp = self._services.set_digital_io_mode_service.call(req)
        self._check_result_status(resp)

    def digital_write(self, pin_id, digital_state):
        """
        Set pin_id state to digital_state

        Examples: ::

            io.digital_write(PinID.GPIO_1A, PinState.HIGH)
            io.digital_write('1A', PinState.LOW)

        :param pin_id:
        :type pin_id: PinID or String
        :param digital_state:
        :type digital_state: PinState or bool
        :rtype: None
        """
        self._check_instance(pin_id, (PinID, str))
        self._check_instance(digital_state, (PinState, bool))

        req = self._services.set_io_state_request(pin_id, digital_state)
        resp = self._services.set_digital_io_state_service.call(req)

        self._check_result_status(resp)

    def digital_read(self, pin_id):
        """
        Return the value of a digital pin.

        Examples: ::

           io.set_pin_mode(PinID.GPIO_1A, PinMode.OUTPUT)
           io.digital_read(PinID.GPIO_1A)

        :param pin_id:
        :type pin_id: PinID or str
        :rtype: bool
        """
        self._check_instance(pin_id, (PinID, str))

        req = self._services.get_io_request(pin_id)
        resp = self._services.get_digital_io_service.call(req)

        if resp["status"] < RobotErrors.SUCCESS.value:
            return None

        return resp["value"]

    @property
    def analog_io_states(self):
        """
        Return the value of analog ios.
        Only available on Ned2.

        :return: State, Name, Mode of the pin
        :rtype: AnalogPinObject
        """
        return self.get_digital_io_states()

    @property
    def get_analog_io_states(self):
        """
        Returns the io state client which can be used synchronously or asynchronously to obtain the io states.
        The io state client returns a list of AnalogPinObject.
        Only available on Ned2.

        Examples: ::

            # Get last value
            io.get_analog_io_states()
            io.get_analog_io_states.value

            # Subscribe a callback
            def io_callback(io_state):
                print io_state

            io.get_analog_io_states.subscribe(io_callback)
            io.get_analog_io_states.unsubscribe()

        :return: io state topic instance
        :rtype: NiryoTopic
        """
        return self._topics.analog_io_topic

    def get_analog_io_state(self, pin_id):
        """
        Return the value of an analog io.
        Only available on Ned2.

        :type pin_id: PinID or str
        :return: analog io object
        :rtype: AnalogPinObject
        """
        self._check_instance(pin_id, (PinID, str))
        states = self._topics.analog_io_topic()

        for state in states:
            if state.pin_id == pin_id or state.name == pin_id:
                return state

        raise RobotCommandException('Analog IO {} not found'.format(pin_id))

    def analog_write(self, pin_id, value):
        """
        Set pin_id state to digital_state.
        Only available on Ned2.

        Examples: ::

            io.digital_write(PinID.AO1, 0.0)
            io.digital_write('AO1', 5.0)

        :param pin_id:
        :type pin_id: PinID or String
        :param value: voltage
        :type value: float
        :rtype: None
        """
        self._check_instance(pin_id, (PinID, str))
        self._check_instance(value, (float, int))
        self._check_range_belonging(value, 0, 5)

        req = self._services.set_io_state_request(pin_id, value)
        resp = self._services.set_analog_io_state_service.call(req)

        self._check_result_status(resp)

    def analog_read(self, pin_id):
        """
        Read the value of an analog pin.
        Only available on Ned2.

        Examples: ::

           io.analog_read(PinID.AI1)
           io.analog_read('AI1')

        :param pin_id:
        :type pin_id: PinID or str
        :rtype: bool
        """
        self._check_instance(pin_id, (PinID, str))

        req = self._services.get_io_request(pin_id)
        resp = self._services.get_analog_io_service.call(req)

        if resp["status"] < RobotErrors.SUCCESS.value:
            return None

        return resp["value"]

    @property
    def custom_button_state(self):
        """
        Returns the io state client which can be used synchronously or asynchronously to obtain the io states.
        The button state client returns the custom button state.
        Only available on Ned2.

        Examples: ::

            # Get last value
            io.custom_button_state()
            io.custom_button_state.value

            # Subscribe a callback
            def button_callback(button_state):
                print button_state

            io.custom_button_state.subscribe(button_callback)
            io.custom_button_state.unsubscribe()

        :return: button state topic instance
        :rtype: NiryoTopic
        """
        return self.custom_button_state

    def is_custom_button_pressed(self):
        """
        Read the state of the custom button of the ned2.
        Only available on Ned2.

        :rtype: bool
        """
        return self.custom_button_state.value
