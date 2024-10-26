#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2022 iRobot Corporation. All rights reserved.
#

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth())


def print_pos_carga(robot):
    print('🐢 (Posición de carga) =', robot.pose)
def print_pos_nueva(robot):
    print('🐢 (Nueva Posicion) =', robot.pose)

@event(robot.when_play)
async def play(robot):
    await robot.set_lights_on_rgb(255, 0, 0)
    await robot.play_note(Note.A5, 1.5)
    await robot.set_lights_on_rgb(0,0,0)
    print_pos_carga(robot)
    await robot.move(-20)
    print_pos_nueva(robot)
    await robot.wait(1)
    await robot.set_lights_on_rgb(0, 255, 0)
    await robot.play_note(Note.A5, 1.5)
    await robot.wait(15)
    await robot.dock()

robot.play()