from pyniryo2.niryo_topic import NiryoTopic
from pyniryo2.arm.objects import HardwareStatusObject, JointStateObject
from pyniryo2.objects import PoseObject


class ArmTopics(object):

    def __init__(self, client):
        self.__client = client

        self.joint_states_topic = NiryoTopic(self.__client,
                                             '/joint_states',
                                             'sensor_msgs/JointState',
                                             joint_states_topic_conversion)

        self.robot_state_topic = NiryoTopic(self.__client,
                                            '/niryo_robot/robot_state',
                                            'niryo_robot_msgs/RobotState',
                                            robot_state_topic_conversion)

        self.hardware_status_topic = NiryoTopic(self.__client,
                                                '/niryo_robot_hardware_interface/hardware_status',
                                                'niryo_robot_msgs/HardwareStatus',
                                                hardware_status_topic_conversion)

        self.learning_mode_state_topic = NiryoTopic(self.__client,
                                                    '/niryo_robot/learning_mode/state',
                                                    'std_msgs/Bool',
                                                    learning_mode_state_topic_conversion)

        self.max_velocity_scaling_factor_topic = NiryoTopic(self.__client,
                                                            '/niryo_robot/max_velocity_scaling_factor',
                                                            'std_msgs/Int32',
                                                            max_velocity_scaling_factor_topic_conversion)


def joint_states_topic_conversion(msg):
    joint_state = JointStateObject()
    joint_state.init_from_message(msg)
    return joint_state


def robot_state_topic_conversion(msg):
    pose = PoseObject(x=msg["position"]["x"],
                      y=msg["position"]["y"],
                      z=msg["position"]["z"],
                      roll=msg["rpy"]["roll"],
                      pitch=msg["rpy"]["pitch"],
                      yaw=msg["rpy"]["yaw"])
    return pose


def hardware_status_topic_conversion(msg):
    hardware_status = HardwareStatusObject()
    hardware_status.init_from_message(msg)
    return hardware_status


def learning_mode_state_topic_conversion(msg):
    return msg["data"]


def max_velocity_scaling_factor_topic_conversion(msg):
    return msg["data"]
