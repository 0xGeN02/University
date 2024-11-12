# Communication imports
from pyniryo2.robot_commander import RobotCommander

from .enums import ConveyorID, ConveyorCan, ConveyorTTL, ConveyorDirection, ConveyorStatus
from .services import ConveyorServices
from .topics import ConveyorTopics, conveyor_id_to_conveyor_type


class Conveyor(RobotCommander):
    # --- Public functions --- #
    def __init__(self, client):
        """
        Conveyor robot functions

        Example: ::

            ros_instance = NiryoRos("10.10.10.10") # Hotspot
            conveyor_interface = Conveyor(ros_instance)

        :param client: Niryo ROS client
        :type client: NiryoRos
        """
        super(Conveyor, self).__init__(client)

        self._services = ConveyorServices(self._client)
        self._topics = ConveyorTopics(self._client)

    def set_conveyor(self):
        """
        Scan if a conveyor is plugged or not on a can bus. 
        If a new conveyor is detected, activate it and return its conveyor ID. 
        If a conveyor is already set, return its ID

        Example: ::

            # Get the id of the conveyor plugged
            conveyor_id = conveyor.set_conveyor()

            # Scan and set the conveyor plugged
            conveyor.set_conveyor()

        :return : New conveyor ID
        :rtype: ConveyorID
        """
        req = self._services.get_ping_and_set_conveyor_request()
        resp = self._services.ping_and_set_conveyor_service.call(req)
        conveyor_id = conveyor_id_to_conveyor_type(resp["id"])

        # If new conveyor has been found
        if conveyor_id != ConveyorID.NONE:
            # print("New conveyor detected and set with id :", conveyor_id)
            return conveyor_id
        else:
            last_conveyor_id = self.get_conveyors_feedback()[0].conveyor_id
            if last_conveyor_id != ConveyorID.NONE:
                # print("No new conveyor detected, actual conveyor id :", last_conveyor_id)
                return last_conveyor_id
            else:
                # print("No conveyor detected")
                return last_conveyor_id

    def unset_conveyor(self, conveyor_id):
        """
        Remove and unset a conveyor previously plugged and set

        Example: ::

            conveyor_id = conveyor.set_conveyor()
            conveyor.unset_conveyor(conveyor_id)
            conveyor.unset_conveyor(ConveyorID.ID_1)
            conveyor.unset_conveyor(ConveyorID.ID_2)
        
        :param conveyor_id: Basically, ConveyorID.ID_1 or ConveyorID.ID_2
        :type conveyor_id: ConveyorID
        :rtype: None
        """
        self._check_instance(conveyor_id, (ConveyorID, ConveyorTTL, ConveyorCan))
        real_conv_id = self.__conveyor_number_to_conveyor_id(conveyor_id)

        req = self._services.unset_conveyor_request(real_conv_id)
        resp = self._services.ping_and_set_conveyor_service.call(req)
        self._check_result_status(resp)

    def run_conveyor(self, conveyor_id, speed=100, direction=ConveyorDirection.FORWARD):
        """
        Run conveyor at id 'conveyor_id'

        Example: ::

            # Set the conveyor and get its id and un it. 
            # By default, the conveyor will go forward at a speed of 50
            # You can't choose the parameters with this method

            conveyor_id = conveyor.set_conveyor()
            conveyor.run_conveyor(conveyor_id) 

        :param conveyor_id: The conveyor id
        :type conveyor_id: ConveyorID
        :param speed: speed percentage between 0% and 100%
        :type speed: int
        :param direction: direction = ConveyorDirection.FORWARD
        :type direction: ConveyorDirection
        :rtype: None
        """
        self.control_conveyor(conveyor_id, control_on=True, speed=speed, direction=direction)

    def stop_conveyor(self, conveyor_id):
        """
        Stop conveyor at id 'conveyor_id'
    
        Example: ::

            # Set the conveyor and get its id, run it and then stop it after 3 seconds
            # By default, the conveyor will go forward at a speed of 50
            # When the conveyor is stopped, its control_on parameter is False and its speed is 0

            import time

            conveyor_id = conveyor.set_conveyor()
            conveyor.run_conveyor(conveyor_id)
            time.sleep(3)
            conveyor.stop_conveyor(conveyor_id) 

        :param conveyor_id:
        :type conveyor_id: ConveyorID
        :rtype: None
        """
        self.control_conveyor(conveyor_id, control_on=False, speed=50, direction=ConveyorDirection.FORWARD)

    def control_conveyor(self, conveyor_id, control_on, speed, direction):
        """
        Control conveyor associated to conveyor_id.
        Then stops it if bool_control_on is False, else refreshes it speed and direction

        Example: ::

            # Example 1
            # Set the conveyor and get its id, control it and then stop it after 3 seconds
            # It this first example, we control the conveyor at a speed of 100% and in the forward direction

            import time

            conveyor_id = conveyor.set_conveyor()
            conveyor.control_conveyo(conveyor_id, True, 100, ConveyorDirection.FORWARD.value)
            time.sleep(3)
            conveyor.stop_conveyor(conveyor_id) 

        # Example 2
            # Set the conveyor and get its id, control it and then stop it after 3 seconds
            # It this second example, we control the conveyor at a speed of 30% and in the backward direction

            import time

            conveyor_id = conveyor.set_conveyor()
            conveyor.control_conveyor(conveyor_id, True, 30, ConveyorDirection.BACKWARD.value)
            time.sleep(3)
            conveyor.stop_conveyor(conveyor_id) 

        :param conveyor_id:
        :type conveyor_id: ConveyorID
        :param control_on: True for activate, False for deactivate
        :type control_on: bool
        :param speed: New speed which is a percentage of maximum speed (0% to 100%)
        :type speed: int
        :param direction: ConveyorDirection.FORWARD.value, ConveyorDirection.BACKWARD.value
        :type direction: ConveyorDirection
        :rtype: None
        """
        self._check_instance(conveyor_id, (ConveyorID, ConveyorTTL, ConveyorCan))
        self._check_type(control_on, bool)
        self._transform_to_type(speed, int)
        self._check_range_belonging(speed, 0, 100)
        self._check_enum_belonging(direction, ConveyorDirection)

        real_conv_id = self.__conveyor_number_to_conveyor_id(conveyor_id)
        req = self._services.control_conveyor_request(real_conv_id, control_on, speed, direction)
        resp = self._services.control_conveyor_service.call(req)

        self._check_result_status(resp)

    @property
    def get_conveyors_feedback(self):
        """
        Returns the conveyors feedback client which can be used synchronously or asynchronously
        to obtain the conveyors feedback: (conveyor_id, connection_state, running, speed, direction)

        Examples: ::

            # Get last value
            arm.get_conveyors_feedback()
            arm.get_conveyors_feedback.value

            # Subscribe a callback
            def conveyor_callback(conveyor_feedback):
                print conveyor_feedback

            arm.hardware_status.subscribe(conveyor_callback)
            # wait
            arm.hardware_status.unsubscribe()

        :return: namedtuple[conveyor_id, running, speed, direction]
        :rtype: namedtuple(ConveyorID, bool, int, ConveyorDirection)
        """
        return self._topics.conveyor_feedback_topic

    @property
    def conveyors(self):
        """
        Return list of registered conveyors

        :return: namedtuple[conveyor_id, running, speed, direction]
        :rtype: namedtuple(ConveyorID, bool, int, ConveyorDirection)
        """
        return self._topics.conveyor_feedback_topic()

    def __conveyor_number_to_conveyor_id(self, conveyor_number):
        if conveyor_number == ConveyorID.ID_1:
            return ConveyorTTL.ID_1 if self._client.hardware_version in ['ned2'] else ConveyorCan.ID_1
        elif conveyor_number == ConveyorID.ID_2:
            return ConveyorTTL.ID_2 if self._client.hardware_version in ['ned2'] else ConveyorCan.ID_2
        else:
            return conveyor_number

    @staticmethod
    def __conveyor_id_to_conveyor_number(conveyor_id):
        if conveyor_id in [ConveyorTTL.ID_1, ConveyorCan.ID_1]:
            return ConveyorID.ID_1
        elif conveyor_id in [ConveyorTTL.ID_2, ConveyorCan.ID_2]:
            return ConveyorID.ID_2
        elif conveyor_id in [ConveyorTTL.NONE, ConveyorCan.NONE]:
            return ConveyorID.NONE
        else:
            return conveyor_id
