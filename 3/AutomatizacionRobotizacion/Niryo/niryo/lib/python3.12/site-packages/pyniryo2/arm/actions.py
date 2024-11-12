import roslibpy.actionlib

from pyniryo2.enums import ArmMoveCommandType

class ArmActions(object):

    def __init__(self, client):
        self.__client = client

        self.arm_action = None
        self.arm_action = roslibpy.actionlib.ActionClient(self.__client,
                                                      '/niryo_robot_arm_commander/robot_action/',
                                                      'niryo_robot_arm_commander/RobotMoveAction')

    def __del__(self):
        if self.arm_action is not None:
            self.arm_action.cancel()
            self.arm_action.dispose()

    def get_move_joints_goal(self, joints):
        cmd = {'cmd_type': ArmMoveCommandType.JOINTS.value, 'joints': joints}
        return roslibpy.actionlib.Goal(self.arm_action, roslibpy.Message({'cmd': cmd}))

    def get_move_pose_goal(self, pose_list):
        cmd = self.pose_list_to_dict(pose_list)
        cmd['cmd_type'] = ArmMoveCommandType.POSE.value
        return roslibpy.actionlib.Goal(self.arm_action, roslibpy.Message({'cmd': cmd}))

    def get_move_linear_pose_goal(self, pose_list):
        cmd = self.pose_list_to_dict(pose_list)
        cmd['cmd_type'] = ArmMoveCommandType.LINEAR_POSE.value
        return roslibpy.actionlib.Goal(self.arm_action, roslibpy.Message({'cmd': cmd}))

    def get_shift_pose_goal(self, axis, shift_value):
        shift_cmd = {'axis_number': axis, 'value': shift_value}
        cmd = {'cmd_type': ArmMoveCommandType.SHIFT_POSE.value, 'shift': shift_cmd}
        return roslibpy.actionlib.Goal(self.arm_action, roslibpy.Message({'cmd': cmd}))

    @staticmethod
    def pose_list_to_dict(pose_list):
        return {"position": {"x": pose_list[0], "y": pose_list[1], "z": pose_list[2]},
                "rpy": {"roll": pose_list[3], "pitch": pose_list[4], "yaw": pose_list[5]}}
