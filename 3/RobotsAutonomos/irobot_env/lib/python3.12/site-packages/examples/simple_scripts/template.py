# !/usr/bin/env python

# Imports
from pyniryo2 import *
from threading import Event

robot_ip = "xxx.xxx.xxx.xxx"
robot_ip_address_local = "127.0.0.1"

# Events
update_tool_event = Event()
update_tool_event.clear()

calibrated_event = Event()
calibrated_event.clear()

# Poses
pose_1 = PoseObject()

pose_2 = PoseObject()

# Callbacks
def update_tool_success_callback(result):
    update_tool_event.set()
    print ('Update Tool: ', result['message'])

def update_tool_error_callback(result):
    print ('Update Tool: ', result['message'])

def calibrate_success_callback(result):
    calibrated_event.set()
    print ('Calibrate Callback: ', result["message"])

def calibrate_error_callback(result):
    print ('Calibrate Callback: ', result["message"])

    """
    Add Callbacks Here
    """

def action_function(robot):

    """
    Don't put niryo_robot in parameter, it will take the pyniryo2 package
    add your function here
    """


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
