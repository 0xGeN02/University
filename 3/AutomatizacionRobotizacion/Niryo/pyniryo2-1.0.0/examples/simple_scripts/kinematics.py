"""
This script shows how to use kinematics with PyNiryo2
"""
import sys
from pyniryo2 import NiryoRobot

simulation = "-simu" in sys.argv
robot_ip_address_rpi = "10.10.10.10"
robot_ip_address_simu = "127.0.0.1"
robot_ip_address = robot_ip_address_simu if simulation else robot_ip_address_rpi

# Connecting to robot
niyro_robot = NiryoRobot(robot_ip_address)

# Calibrating Robot
niyro_robot.arm.calibrate_auto()

# Getting initial pose
initial_pose = niyro_robot.arm.get_pose()

# Calculating pose with FK and moving to this pose
pose_target = niyro_robot.arm.forward_kinematics(0.2, 0.0, -0.4, 0.0, 0.0, 0.0)
niyro_robot.arm.move_pose(pose_target)

# Calculating joints via IK and moving to these joints
joints_target = niyro_robot.arm.inverse_kinematics(initial_pose)
niyro_robot.arm.move_joints(joints_target)

# Leaving
niyro_robot.arm.set_learning_mode(True)
niyro_robot.end()

