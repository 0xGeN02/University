"""
Little Script which shows how to read a position with PyNiryo2
"""
# !/usr/bin/env python

from pyniryo2 import NiryoRobot
import sys

if sys.version_info[0] == 2:
    input_func = raw_input
else:
    input_func = input

simulation = "-simu" in sys.argv
robot_ip_address_rpi = "10.10.10.10"
robot_ip_address_simu = "127.0.0.1"
robot_ip_address = robot_ip_address_simu if simulation else robot_ip_address_rpi

# Connecting to robot
niryo_robot = NiryoRobot(ip_address=robot_ip_address)

niryo_robot.arm.calibrate_auto()

while "User to not quit":
    # Going to learning mode
    niryo_robot.arm.set_learning_mode(True)

    input_func("Press enter to switch to turn learning mode off")
    niryo_robot.arm.set_learning_mode(False)

    # Reading pose and displaying it
    pose = niryo_robot.arm.get_pose()
    print(pose)
    if input_func("Press enter to get new pose / q to leave ") == 'q':
        break

niryo_robot.arm.set_learning_mode(True)
# Close
niryo_robot.end()

