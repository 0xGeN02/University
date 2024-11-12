import roslibpy.actionlib

from pyniryo2.enums import ArmMoveCommandType


class TrajectoriesActions(object):

    def __init__(self, client):
        self.__client = client

        self.trajectory_action = None
        self.trajectory_action = roslibpy.actionlib.ActionClient(self.__client,
                                                                 '/niryo_robot_arm_commander/robot_action/',
                                                                 'niryo_robot_arm_commander/RobotMoveAction')

    def __del__(self):
        if self.trajectory_action is not None:
            self.trajectory_action.cancel()
            self.trajectory_action.dispose()

    def get_execute_trajectories_goal(self, pose_list, dist_smoothing=0):
        cmd = {'cmd_type': ArmMoveCommandType.EXECUTE_TRAJ.value,
               'list_poses': [self.pose_quat_list_to_dict(pose) for pose in pose_list],
               'dist_smoothing': dist_smoothing}
        return roslibpy.actionlib.Goal(self.trajectory_action, roslibpy.Message({'cmd': cmd}))

    @staticmethod
    def pose_quat_list_to_dict(pose_list):
        return {"position": dict(zip(["x", "y", "z"], pose_list[:3])),
                "orientation": dict(zip(["x", "y", "z", "w"], pose_list[3:]))}
