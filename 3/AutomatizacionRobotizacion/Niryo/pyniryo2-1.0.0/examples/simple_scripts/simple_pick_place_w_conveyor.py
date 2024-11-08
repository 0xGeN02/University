"""
This file shows how to use PyNiryo2 to do a simple pick and place
with Ned using a conveyor
"""

# Imports
from pyniryo2 import *

# -- MUST Change these variables
gripper_used = ToolID.GRIPPER_2  # Tool used for picking
gpio_sensor = PinID.GPIO_1A  # Pin of the sensor
# Set robot address
robot_ip_address = "192.168.1.52"

# -- Should Change these variables
# The pick pose
pick_pose = PoseObject(
    x=0.25, y=0., z=0.14,
    roll=-0., pitch=1.57, yaw=0.0,
)
# The Place pose
place_pose = PoseObject(
    x=-0.01, y=-0.23, z=0.12,
    roll=-0., pitch=1.57, yaw=-1.57)


def pick_n_place_w_conveyor(niyro_robot):
    """
    Simple pick and place with a conveyor belt

    :type niyro_robot: NiryoRobot
    :rtype: None
    """
    # Enable connection with conveyor
    conveyor_id = niyro_robot.conveyor.set_conveyor()
    # Turn conveyor on
    niyro_robot.conveyor.control_conveyor(conveyor_id=conveyor_id, control_on=True,
                                          speed=50, direction=ConveyorDirection.FORWARD)
    # Wait for sensor to turn to low state which means it has something in front of it
    while not niyro_robot.io.digital_read(gpio_sensor) == PinState.LOW:
        print(niyro_robot.io.digital_read(gpio_sensor))
        niyro_robot.wait(0.1)
    # Turn conveyor off
    niyro_robot.conveyor.control_conveyor(conveyor_id=conveyor_id, control_on=False,
                                          speed=0, direction=ConveyorDirection.FORWARD)
    # Pick
    niyro_robot.pick_place.pick_from_pose(pick_pose)
    # Place
    niyro_robot.pick_place.place_from_pose(place_pose)


# -- MAIN PROGRAM

if __name__ == '__main__':
    # Connect to robot
    robot = NiryoRobot(robot_ip_address)
    # Calibrate robot if robot needs calibration
    robot.arm.calibrate_auto()
    # Update tool
    robot.tool.update_tool()
    # Launching main process
    pick_n_place_w_conveyor(robot)
    # Releasing connection
    robot.arm.go_to_sleep()
    robot.end()
