#!/usr/bin/env python
# coding=utf-8


class HardwareStatusObject:
    """
    Object used to store every hardware information

    :ivar rpi_temperature: Number representing the rpi temperature
    :vartype rpi_temperature: float
    :ivar hardware_version: Number representing the hardware version
    :vartype hardware_version: str
    :ivar connection_up: Boolean indicating if the connection with the robot is up
    :vartype connection_up: bool
    :ivar error_message: Error message status on error
    :vartype error_message: str
    :ivar calibration_needed: Boolean indicating if a calibration is needed
    :vartype calibration_needed: bool
    :ivar calibration_in_progress: Boolean indicating if calibration is in progress
    :vartype calibration_in_progress: bool
    :ivar motor_names: List of motor names
    :vartype motor_names: list[str]
    :ivar motor_types: List of motor types
    :vartype motor_types: list[str]
    :ivar motors_temperature: List of motors_temperature
    :vartype motors_temperature: list[float]
    :ivar motors_voltage: List of motors_voltage
    :vartype motors_voltage: list[float]
    :ivar hardware_errors: List of hardware errors
    :vartype hardware_errors: list[int]
    :ivar hardware_error_messages: List of hardware error messages
    :vartype hardware_error_messages: list[str]

    """

    def __init__(self):
        self.rpi_temperature = None
        self.hardware_version = None
        self.connection_up = None
        self.error_message = None
        self.calibration_needed = None
        self.calibration_in_progress = None

        # Following list describe each motor
        # Row 0 for first motor, row 1 for second motor, row 2 for third motor, row 3 for fourth motor
        self.motor_names = None
        self.motor_types = None
        self.motors_temperature = None
        self.motors_voltage = None
        self.hardware_errors = None
        self.hardware_error_messages = None

    def init_from_message(self, msg):
        # Number representing the rpi temperature
        self.rpi_temperature = msg["rpi_temperature"]
        # Number representing the hardware version
        self.hardware_version = msg["hardware_version"]
        # Boolean indicating if the connection with the robot is up
        self.connection_up = msg["connection_up"]
        # Error message status on error
        self.error_message = msg["error_message"]
        # Boolean indicating if a calibration is needed
        self.calibration_needed = msg["calibration_needed"]
        # Boolean indicating if calibration is in progress
        self.calibration_in_progress = msg["calibration_in_progress"]

        # Following list describe each motor
        # Row 0 for first motor, row 1 for second motor, row 2 for third motor, row 3 for fourth motor
        # List of motor names
        self.motor_names = msg["motor_names"]
        # List of motor types
        self.motor_types = msg["motor_types"]
        # List of motors_temperature
        self.motors_temperature = msg["temperatures"]
        # List of motors_voltage
        self.motors_voltage = msg["voltages"]
        # List of hardware errors
        self.hardware_errors = msg["hardware_errors"]
        # List of hardware error messages
        self.hardware_error_messages = msg["hardware_errors_message"]

    def init_from_values(self, rpi_temperature, hardware_version, connection_up,
                         error_message, calibration_needed, calibration_in_progress,
                         motor_names, motor_types,
                         motors_temperature, motors_voltage, hardware_errors, hardware_error_messages):
        # Number representing the rpi temperature
        self.rpi_temperature = rpi_temperature
        # Number representing the hardware version
        self.hardware_version = hardware_version
        # Boolean indicating if the connection with the robot is up
        self.connection_up = connection_up
        # Error message status on error
        self.error_message = error_message
        # Boolean indicating if a calibration is needed
        self.calibration_needed = calibration_needed
        # Boolean indicating if calibration is in progress
        self.calibration_in_progress = calibration_in_progress

        # Following list describe each motor
        # Row 0 for first motor, row 1 for second motor, row 2 for third motor, row 3 for fourth motor
        # List of motor names
        self.motor_names = motor_names
        # List of motor types
        self.motor_types = motor_types
        # List of motors_temperature
        self.motors_temperature = motors_temperature
        # List of motors_voltage
        self.motors_voltage = motors_voltage
        # List of hardware errors
        self.hardware_errors = hardware_errors
        # List of hardware error messages
        self.hardware_error_messages = hardware_error_messages

    def __str__(self):
        list_string_ret = list()
        list_string_ret.append("Temp (°C) : {}".format(self.rpi_temperature))
        list_string_ret.append("Hardware version : {}".format(self.hardware_version))
        list_string_ret.append("Connection Up : {}".format(self.connection_up))
        list_string_ret.append("Error Message : {}".format(self.error_message))
        list_string_ret.append("Calibration Needed : {}".format(self.calibration_needed))
        list_string_ret.append("Calibration in progress : {}".format(self.calibration_in_progress))
        list_string_ret.append("MOTORS INFOS : Motor1, Motor2, Motor3, Motor4, Motor5, Motor6,")
        list_string_ret.append("Names : {}".format(self.motor_names))
        list_string_ret.append("Types : {}".format(self.motor_types))
        list_string_ret.append("Temperatures : {}".format(self.motors_temperature))
        list_string_ret.append("Voltages : {}".format(self.motors_voltage))
        list_string_ret.append("Hardware errors : {}".format(self.hardware_errors))
        list_string_ret.append("Hardware error messages : {}".format(self.hardware_error_messages))
        return "\n".join(list_string_ret)

    def __repr__(self):
        return self.__str__()


class JointStateObject:
    """
    Object used to store every joint state information

    :ivar name: List of joint names
    :vartype name: list[str]
    :ivar position: List of joint positions
    :vartype position: list[float]
    :ivar velocity: List of joint velocities
    :vartype velocity: list[float]
    :ivar effort: List of joint efforts
    :vartype effort: list[float]
    """

    def __init__(self):
        # Following list describe each joint
        # Row 0 for first joint, row 1 for second joint, row 2 for third joint, row 3 for fourth joint, ...

        # List of joint names
        self.name = None
        # List of joint positions
        self.position = None
        # List of joint velocities
        self.velocity = None
        # List of joint efforts
        self.effort = None

    def init_from_message(self, msg):
        # Following list describe each joint
        # Row 0 for first joint, row 1 for second joint, row 2 for third joint, row 3 for fourth joint, ...

        # List of joint names
        self.name = msg["name"]
        # List of joint positions
        self.position = msg["position"]
        # List of joint velocities
        self.velocity = msg["velocity"]
        # List of joint efforts
        self.effort = msg["effort"]

    def init_from_values(self, names, positions, velocities, efforts):
        # Following list describe each joint
        # Row 0 for first joint, row 1 for second joint, row 2 for third joint, row 3 for fourth joint, ...

        # List of joint names
        self.name = names
        # List of joint positions
        self.position = positions
        # List of joint velocities
        self.velocity = velocities
        # List of joint efforts
        self.effort = efforts

    def __str__(self):
        list_string_ret = list()
        list_string_ret.append("MOTORS INFOS : ")
        list_string_ret.append("Names : {}".format(self.name))
        list_string_ret.append("Positions : {}".format(self.position))
        list_string_ret.append("Velocities : {}".format(self.velocity))
        list_string_ret.append("Efforts : {}".format(self.effort))
        return "\n".join(list_string_ret)

    def __repr__(self):
        return self.__str__()
