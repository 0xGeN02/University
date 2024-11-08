# !/usr/bin/env python

# Imports
from gc import callbacks
from pyniryo2 import *
from threading import Event

from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Int32, Bool, Header

robot_ip = "192.168.1.115"
robot_ip_address_local = "127.0.0.1"

# Events
update_tool_event = Event()
update_tool_event.clear()

calibrated_event = Event()
calibrated_event.clear()

save_trajectory_event = Event()
save_trajectory_event.clear()

executed_trajectory_event = Event()
executed_trajectory_event.clear()

get_trajectory_list_event = Event()
get_trajectory_list_event.clear()

update_trajectory_event = Event()
update_trajectory_event.clear()

delete_trajectory_event = Event()
delete_trajectory_event.clear()

# Callbacks
def update_tool_success_callback(result):
    update_tool_event.set()
    print ('Update Tool: ', result['message'])
    print ("")

def update_tool_error_callback(result):
    print ('Update Tool: ', result['message'])
    print ("")

def calibrate_success_callback(result):
    calibrated_event.set()
    print ("")
    print ('Calibration : ', result["message"])
    print ("")

def calibrate_error_callback(result):
    print ('Calibration : ', result["message"])
    print ("")

def execute_registered_callback(result):
    print("Trajectory Callback : ", result["message"])
    print ("")
    executed_trajectory_event.set()

def get_trajectory_callback(result):
    print("Get Trajectory Callback : ", result["trajectory"])
    print ("")

def get_trajectory_list_callback(result):
    print("Trajectory List : ", result["name_list"])
    print("Description List : ", result["description_list"])
    print ("")
    get_trajectory_list_event.set()

def save_trajectory_callback(result):
    print("Save Trajectory Callback : ", result["message"])
    print ("")
    save_trajectory_event.set()

def delete_trajectory_callback(result):
    print("Delete Trajectory : ", result["message"])
    print ("")
    delete_trajectory_event.set()

def update_callback(result):
    print("Update Trajectory : ", result["message"])
    print("")
    update_tool_event.set()

def action_function(robot):

    """
    Don't put niryo_robot in parameter, it will take the pyniryo2 package
    add your function here
    """
    robot.trajectories.get_saved_trajectory("last_executed_trajectory")

    robot.trajectories.execute_registered_trajectory("last_executed_trajectory", callback=execute_registered_callback)
    executed_trajectory_event.wait(20)
    executed_trajectory_event.clear()

    robot.trajectories.get_saved_trajectory_list(callback=get_trajectory_list_callback)
    get_trajectory_list_event.wait(10)
    get_trajectory_list_event.clear()

    joints_list = [[-0.493, -0.32, -0.505, -0.814, -0.282, 0],
              [0.834, -0.319, -0.466, 0.822, -0.275, 0],
              [1.037, -0.081, 0.248, 1.259, -0.276, 0]]

    points_list = [JointTrajectoryPoint(positions=joints) for joints in joints_list]

    trajectory = JointTrajectory(header = Header(), joint_names =["joint_1", "joint_2", "joint_3",
             "joint_4", "joint_5", "joint_6"], points = points_list)

    robot.trajectories.save_trajectory(trajectory, "test_trajectory", "ceci est un test", callback=save_trajectory_callback)
    save_trajectory_event.wait(10)
    save_trajectory_event.clear()

    robot.trajectories.get_saved_trajectory_list(callback=get_trajectory_list_callback)
    get_trajectory_list_event.wait(10)
    get_trajectory_list_event.clear()

    robot.trajectories.delete_trajectory("test_trajectory", callback=delete_trajectory_callback)
    delete_trajectory_event.wait(10)
    delete_trajectory_event.clear()

    robot.trajectories.get_saved_trajectory_list(callback=get_trajectory_list_callback)
    get_trajectory_list_event.wait(10)
    get_trajectory_list_event.clear()

    print ('Execute Trajectory with the arm')
    robot.wait(10)
    response = input("Done ? [Press Enter]")
    print ("")

    robot.trajectories.save_last_learned_trajectory("test_py2", "coucou", callback=update_callback)
    update_trajectory_event.wait(10)
    update_trajectory_event.clear()

    robot.trajectories.get_saved_trajectory_list(callback=get_trajectory_list_callback)
    get_trajectory_list_event.wait(10)
    get_trajectory_list_event.clear()

    robot.trajectories.execute_registered_trajectory("test_py2", callback=execute_registered_callback)
    executed_trajectory_event.wait(50)
    executed_trajectory_event.clear()

    robot.trajectories.update_trajectory_infos("test_py2", "traj_changes_name", "ah que coucou", callback=update_callback)
    update_trajectory_event.wait(10)
    update_trajectory_event.clear()

    robot.trajectories.get_saved_trajectory_list(callback=get_trajectory_list_callback)
    get_trajectory_list_event.wait(10)
    get_trajectory_list_event.clear()

    robot.trajectories.delete_trajectory("traj_changes_name", callback=delete_trajectory_callback)
    delete_trajectory_event.wait(10)
    delete_trajectory_event.clear()

    robot.trajectories.get_saved_trajectory_list(callback=get_trajectory_list_callback)
    get_trajectory_list_event.wait(10)
    get_trajectory_list_event.clear()

if __name__ == "__main__":

    # Connect to robot
    robot = NiryoRobot(robot_ip)

    # Calibrate robot if robot needs calibration
    robot.arm.calibrate_auto(callback=calibrate_success_callback, errback=calibrate_error_callback)
    calibrated_event.wait(20)
    if not calibrated_event.is_set():
        quit

    robot.tool.update_tool(callback=update_tool_success_callback, errback=update_tool_error_callback)
    update_tool_event.wait()

    action_function(robot)

    # Releasing connection
    robot.arm.go_to_sleep()
    robot.end()
