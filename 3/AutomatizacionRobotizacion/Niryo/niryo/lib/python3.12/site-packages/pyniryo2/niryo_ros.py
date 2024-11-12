# Python libraries
import roslibpy
import socket
import time
from threading import Thread

from pyniryo2.niryo_topic import NiryoTopic


class NiryoRosTimeoutException(Exception):
    pass


class NiryoRos(roslibpy.Ros):
    def __init__(self, ip_address="127.0.0.1", port=9090):
        """
        Connect to your computer to ros: ::

            ros_instance = NiryoRos("127.0.0.1") # Simulation

            ros_instance = NiryoRos("10.10.10.10") # Hotspot

            ros_instance = NiryoRos("169.254.200.201") # Ethernet

        Based on the roslibpy ROS client: https://roslibpy.readthedocs.io/en/latest/reference/index.html#roslibpy.Ros

        :param ip_address: ip of the ros master
        :type ip_address: str
        :param port: usually 9090
        :type port: int
        """
        self.port = port
        self.ip_address = ip_address
        super(NiryoRos, self).__init__(host=ip_address, port=port)

        self.should_run = False
        self.__pyniryo2_ip = socket.gethostbyname(socket.gethostname())

        self.__ping_loop_thread = Thread(target=self.__ping_loop)
        self.__pyniryo_ping_publisher = NiryoTopic(self, '/ping_pyniryo', 'std_msgs/Bool')

        self.run(timeout=5)
        self.__ping_loop_thread.start()
        self._hardware_version = self.get_param("/niryo_robot/hardware_version")
        time.sleep(0.5)

    def close(self):
        self.should_run = False
        super(NiryoRos, self).close()

    def terminate(self):
        self.should_run = False
        super(NiryoRos, self).terminate()

    def __ping_loop(self):
        self.should_run = True
        while self.is_connected and self.should_run:
            self.__pyniryo_ping_publisher.publish(roslibpy.Message({'data': True}))
            time.sleep(0.1)

    @property
    def hardware_version(self):
        """
        Get the hardware version of the robot (one, ned, ned2)

        :return: The hardware version of the robot (one, ned, ned2)
        :rtype: str
        """
        return self._hardware_version
