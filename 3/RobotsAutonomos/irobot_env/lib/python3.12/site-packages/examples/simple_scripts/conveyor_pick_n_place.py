# !/usr/bin/env python

# Imports
from pyniryo2 import *
import time
from threading import Event

# -- MUST Change these variables
gripper_used = ToolID.GRIPPER_2  # Tool used for picking
gpio_sensor = PinID.GPIO_1A  # Pin of the sensor

# Set robot address
robot_ip_address = "192.168.1.124"

# Events
calibrated_event = Event()
calibrated_event.clear()

update_tool_event = Event()
update_tool_event.clear

close_gripper_event = Event()
close_gripper_event.clear

# -- Should Change these variables

# Poses
conveyor_pose_2 = PoseObject(
    x=0.193, y=0.199, z=0.19,
    roll=-0.071, pitch=1.527, yaw=-0.090)

conveyor_pose_1 = PoseObject(
    x=0.0, y=0.2, z=0.19,
    roll=-0.3, pitch=1.47, yaw=-0.079)

storage_pose = PoseObject(
    x=0.25, y=-0.1, z=0.135,
    roll=-0.77, pitch=1.57, yaw=-2.2)

# Variables
offset = 0.06

nb_el = 3

# Callbacks
def update_tool_success_callback(result):
    time.sleep(2)
    update_tool_event.set()
    print 'Update Tool: ', result['message']

def update_tool_error_callback(result):
    print 'Update Tool: ', result['message']

def calibrate_success_callback(result):
    calibrated_event.set()
    print 'Calibrate Callback: ', result["message"]

def calibrate_error_callback(result):
    print 'Calibrate Callback: ', result["message"]

def close_gripper_callback(result):
    print 'Close Callback: ', result["message"]

# Pick and place with conveyor
def pick_n_place_w_conveyor(robot):
    """
    Simple pick and place with a conveyor belt

    :type niyro_robot: NiryoRobot
    :rtype: None
    """
    # Run conveyor
    robot.conveyor.run_conveyor(conveyor_id)

    # Wait for sensor to turn to low state which means it has something in front of it
    while not robot.io.digital_read(gpio_sensor) == PinState.LOW:
        print(robot.io.digital_read(gpio_sensor))
    
    # Stop Conveyor
    robot.conveyor.stop_conveyor(conveyor_id)

    # Pick and place to storage position
    robot.pick_place.pick_and_place(conveyor_pose_2, storage_pose)

if __name__ == '__main__':
    # Connect to robot
    robot = NiryoRobot(robot_ip_address)

    # Set Pin Mode
    robot.io.set_pin_mode(gpio_sensor, PinMode.INPUT)
    
    # Enable connection with conveyor
    conveyor_id = robot.conveyor.set_conveyor()
    print 'Conveyor ID: ', conveyor_id

    # Calibrate robot if robot needs calibration
    robot.arm.calibrate_auto(callback=calibrate_success_callback, errback=calibrate_error_callback)
    calibrated_event.wait(20)
    if not calibrated_event.is_set():
        quit

    # Update tool
    robot.tool.update_tool(callback=update_tool_success_callback, errback=update_tool_error_callback)
    update_tool_event.wait()

    # Launching main process
    for i in range(nb_el):
        robot.pick_place.pick_and_place(storage_pose, conveyor_pose_1)
        if i < 2:
            storage_pose.y += offset
            conveyor_pose_1.x -= offset
    
    for i in range(nb_el):
        pick_n_place_w_conveyor(robot)
        storage_pose.y -= offset

    robot.tool.close_gripper(callback=close_gripper_callback)

    # Releasing connection
    robot.arm.go_to_sleep()
    robot.end()
