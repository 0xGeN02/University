"""
This script shows an example of how to use Ned's vision to
make a conditioning according to the objects' color.

The objects will be conditioned in a grid of dimension grid_dimension. The Y axis corresponds
to the ObjectColor : BLUE / RED / GREEN. It will be 3
The X axis corresponds to how many objects can be put on the same line before increasing
the conditioning height.
Once a line is completed, objects will be pack over the lower level
"""

from pyniryo2 import *

# -- MUST Change these variables
simulation_mode = True
if simulation_mode:
    robot_ip_address, workspace_name = "127.0.0.1", "gazebo_1"
else:
    robot_ip_address, workspace_name = "10.10.10.10", "workspace_1"

# -- Can change these variables
grid_dimension = (3, 3)

# -- Should Change these variables
# The pose from where the image processing happen
observation_pose = PoseObject(
    x=0.20, y=0., z=0.3,
    roll=0.0, pitch=1.57, yaw=0.0,
)

# Center of the conditioning area
first_conditioning_pose = PoseObject(
    x=0.0, y=-0.25, z=0.12,
    roll=-0., pitch=1.57, yaw=-1.57
)


# -- MAIN PROGRAM
def process(niryo_robot):
    """

    :type niryo_robot: NiryoRobot
    :rtype: None
    """
    try_without_success = 0
    count_dict = {
        ObjectColor.BLUE: 0,
        ObjectColor.RED: 0,
        ObjectColor.GREEN: 0,
    }
    # Loop until too much failures
    while try_without_success < 3:
        # Moving to observation pose
        niryo_robot.arm.move_pose(observation_pose)
        # Trying to get object via Vision Pick
        obj_found, shape, color = niryo_robot.vision.vision_pick(workspace_name)
        if not obj_found:
            try_without_success += 1
            continue

        # Choose X & Z position according to how the color line is filled
        offset_x_ind = count_dict[color] % grid_dimension[0]
        offset_z_ind = count_dict[color] // grid_dimension[0]

        # Choose Y position according to ObjectColor
        if color == ObjectColor.BLUE:
            offset_y_ind = -1
        elif color == ObjectColor.RED:
            offset_y_ind = 0
        else:
            offset_y_ind = 1
        # Going to place the object
        place_pose = first_conditioning_pose.copy_with_offsets(0.05 * offset_x_ind,
                                                               0.05 * offset_y_ind,
                                                               0.025 * offset_z_ind)
        niryo_robot.pick_place.place_from_pose(place_pose)
        # Increment count
        count_dict[color] += 1
        try_without_success = 0


if __name__ == '__main__':
    # Connect to robot
    robot = NiryoRobot(robot_ip_address)
    # Changing tool
    robot.tool.update_tool()
    # Calibrate robot if robot needs calibration
    robot.arm.calibrate_auto()
    # Launching main process
    process(robot)
    # Ending
    robot.arm.go_to_sleep()
    # Releasing connection
    robot.end()
