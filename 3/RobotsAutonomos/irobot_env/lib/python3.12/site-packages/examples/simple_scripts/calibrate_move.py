"""
This script shows few functions you can use with PyNiryo
"""

from pyniryo2 import *

simulation_mode = True

robot_ip_address_rpi = "10.10.10.10"
robot_ip_address_simulation = "127.0.0.1"

robot_ip_address = robot_ip_address_simulation if simulation_mode else robot_ip_address_rpi

# Connecting to robot
niryo_robot = NiryoRobot(robot_ip_address)

# Trying to calibrate
niryo_robot.arm.calibrate(CalibrateMode.AUTO)
niryo_robot.arm.set_learning_mode(False)

# Getting Joints
initial_joints = niryo_robot.arm.get_joints()
print("Initial joints :\n" + str(initial_joints))

# Move Pose
niryo_robot.arm.move_pose([0.2, 0.0, 0.25, 0.0, 1.578, 0.0])

# Shift pose
niryo_robot.arm.shift_pose(RobotAxis.Y, 0.15)

# Going back to initial joints
niryo_robot.arm.move_joints(initial_joints)

niryo_robot.arm.set_learning_mode(True)

if not simulation_mode:
    # Getting hardware information
    digital_pin_array = niryo_robot.io.get_digital_io_states()
    for digital_pin in digital_pin_array:
        print(digital_pin)

    hardware_data = niryo_robot.arm.hardware_status()
    print(hardware_data)

# Close
niryo_robot.arm.set_learning_mode(True)
niryo_robot.end()
