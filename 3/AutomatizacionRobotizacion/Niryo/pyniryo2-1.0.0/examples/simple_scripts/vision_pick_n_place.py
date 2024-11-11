# !/usr/bin/env python3

# Imports
from pyniryo2 import *
from threading import Event

robot_ip, default_workspace_name = "192.168.1.124", "test_ws-2"

# Pointer Offset
pointer_offset = 0.05

# Events
update_tool_event = Event()
update_tool_event.clear()

calibrated_event = Event()
calibrated_event.clear()

move_pose_event = Event()
move_pose_event.clear()

close_event = Event()
close_event.clear()

# Poses - Modify According to your setup
observation_pose = PoseObject(x=0.220,y=0.0, z=0.376, roll=-1.51, pitch=1.526, yaw=-1.395)

place_pose = PoseObject(x=0.0, y=0.268, z=0.17, roll=-0.974, pitch=1.5, yaw=0.72)

# Callbacks
def update_tool_success_callback(result):
    update_tool_event.set()
    print 'Update Tool: ', result['message']
    print ("")

def update_tool_error_callback(result):
    print 'Update Tool: ', result['message']
    print ("")

def calibrate_success_callback(result):
    calibrated_event.set()
    print 'Calibrate Callback: ', result["message"]
    print ("")

def calibrate_error_callback(result):
    print 'Calibrate Callback: ', result["message"]
    print ("")

def close_gripper_callback(result):
    close_event.set()
    print 'Close Callback: ', result["message"]
    print ("")

def move_pose_callback(result):
    move_pose_event.set()
    print 'Close Callback: ', result["message"]
    print ("")

def check_ws(robot, workspace_name):
    ws_list = robot.vision.get_workspace_list()
    if len(ws_list) !=0 and workspace_name in ws_list:
        print ("Workspace Found !")
        print ("")
    else:
        print("Workspace Not Found ! Please define a Workspace name !")
        print ("")
        workspace_name = workspace_definition(robot)
    return workspace_name

def workspace_name_definition():
    ws_validation = False
    while not ws_validation:
        workspace_response = raw_input("Workspace Name ? ")
        print ("")
        response = raw_input("Validate ? [y/n] : ")
        while response not in ["y","n"]:
            print ("Please enter <y> or <n>")
            print ("")
            response = raw_input("Validate ? [y/n] : ")
            print ("")
        if response == "y":
            workspace_name = workspace_response
            ws_validation = True
        elif response == "n":
            print ("Ok ! Let's try again !")
    return workspace_name

def workspace_definition(robot):
    print ("")
    print ("Please set Pointer on the robot")
    response = raw_input("Done ? [Press Enter] ")
    print ("")
    robot.wait(1)
    workspace_name = workspace_name_definition()
    workspace_poses = []
    for i in range(4):
        validation = False
        while not validation:
            ws_list = robot.vision.get_workspace_list()
            if len(ws_list) !=0 and workspace_name in ws_list:
                robot.vision.delete_workspace(workspace_name)
            print ("")
            print ("Place Pointer on workspace pose number "+str(i+1))
            response = raw_input("Done ? [Press Enter]")
            x, y, z, roll, pitch, yaw = robot.arm.get_pose().to_list()
            print ("")
            print ("Pose "+str(i+1)+": "+str(x)+" "+str(y)+" "+str(z)+" "+str(roll)+" "+str(pitch)+" "+str(yaw))
            print ("")
            response = raw_input("Validate ? [y/n] : ")
            print ("")
            while response not in ['y','n']:
                print ("Please enter <y> or <n>")
                print ("")
                response = raw_input("Validate ? [y/n] : ")
                print ("")
            if response == 'y':
                print ("Point Validated")
                print ("")
                Pose = PoseObject(x, y, z, roll, pitch, yaw)
                workspace_poses.append(Pose)
                validation = True
            elif response == 'n':
                print ("Ok ! Let's try again !")
                print ("")
    print("Recap: ")
    print (workspace_name)
    print("Pose 1", workspace_poses[0])
    print("Pose 2", workspace_poses[1])
    print("Pose 3", workspace_poses[2])
    print("Pose 4", workspace_poses[3])
    print ("")
    robot.arm.move_to_home_pose()
    robot.vision.save_workspace_from_robot_poses(workspace_name,workspace_poses[0], workspace_poses[1], workspace_poses[2], workspace_poses[3])
    return workspace_name
    

def vision_pick_n_place(robot, workspace_name):
    """
    Simple pick and place with vision: Example 2

    :type niyro_robot: NiryoRobot
    :rtype: None
    """
    # Loop
    try_without_success = 0
    while try_without_success < 5:
        # Moving to observation pose
        robot.arm.move_pose(observation_pose, callback=move_pose_callback)
        move_pose_event.wait()
        robot.wait(5)

        # Trying to pick target using camera
        ret = robot.vision.vision_pick(workspace_name,
                                                 height_offset=-0.02,
                                                 shape=ObjectShape.ANY,
                                                 color=ObjectColor.BLUE)
        obj_found, shape_ret, color_ret = ret
        if not obj_found:
            try_without_success += 1
            continue
        # Vision pick has succeed which means that Ned should have already catch the object !

        # Everything is good, so we going to place the object
        robot.pick_place.place_from_pose(place_pose)
        break

if __name__ == "__main__":
    
    # Connect to robot
    robot = NiryoRobot(robot_ip)
    
    # Calibrate robot if robot needs calibration
    robot.arm.calibrate_auto(callback=calibrate_success_callback, errback=calibrate_error_callback)
    calibrated_event.wait(20)
    if not calibrated_event.is_set():
        quit

    workspace_def_response = raw_input("Do you want to define a workspace ? [y/n] : ")
    print ("")
    while workspace_def_response not in ['y','n']:
        print ("Please enter <y> or <n>")
        print ("")
        workspace_def_response = raw_input("Validate ? [y/n] : ")
        print ("")
    if workspace_def_response == 'y':
        print("Let's define the vision workspace !")
        workspace_name = workspace_definition(robot)
    elif workspace_def_response == 'n':
        print ("Ok ! Let's check your default workspace")
        workspace_name = check_ws(robot, default_workspace_name)

    robot.wait(1)
    print ("Please set Tool on the robot")
    print ("")
    response = raw_input("Done ? [Press Enter] ")

    robot.arm.move_to_home_pose()

    robot.tool.update_tool(callback=update_tool_success_callback, errback=update_tool_error_callback)
    update_tool_event.wait()

    vision_pick_n_place(robot, workspace_name)

    robot.tool.close_gripper(callback=close_gripper_callback)
    close_event.wait()
    # Releasing connection
    robot.arm.go_to_sleep()
    robot.end()


