#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2022 iRobot Corporation. All rights reserved.
#

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth())

distancia_robot=250

def print_pos_carga(robot):
    print('🐢 (Posición de carga) =', robot.pose)
def print_pos_nueva(robot):
    print('🐢 (Nueva Posicion) =', robot.pose)
def print_pos_final(robot):
    print('🐢 (Posicion final) =', robot.pose)


async def inspeccion():
    await robot.set_lights_on_rgb(255, 115, 0)
    n = 0
    while n < 12:
        await robot.turn_right(30)
        await robot.wait(0.2)
        n += 1

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
    await robot.wait(2)
    #360
    #Inspeccion 1
    await inspeccion()


    #Parte 2
    await robot.set_lights_on_rgb(0, 0, 255)
    await robot.play_note(Note.A5, 1.5)
    print('🐢 Navegando...')
    await robot.turn_right(180)
    await robot.move(100)
    await robot.turn_right(90)
    await robot.wait(2)
    await robot.set_lights_on_rgb(0, 255, 0)
    await robot.play_note(Note.A5, 1.5)
    #Inspeccion 2
    await inspeccion()

    #Parte 3
    await robot.wait(2)
    await robot.set_lights_on_rgb(0, 0, 255)
    await robot.play_note(Note.A5, 1.5)
    await robot.move(distancia_robot)
    await robot.turn_left(180)
    await robot.wait(1)
    await robot.set_lights_on_rgb(0, 255, 0)
    await robot.play_note(Note.A5, 1.5)
    #Inspeccion 3
    await inspeccion()

    #Parte 4
    await robot.wait(2)
    await robot.set_lights_on_rgb(0, 0, 255)
    await robot.play_note(Note.A5, 1.5)
    await robot.move(distancia_robot)
    #Inspeccion 4
    await inspeccion()
    await robot.turn_left(90)
    await robot.set_lights_on_rgb(0, 0, 255)
    await robot.play_note(Note.A5, 1.5)
    await robot.move(100)
    print_pos_final(robot)
    await robot.wait(1)
    await robot.set_lights_on_rgb(0, 255, 0)
    await robot.play_note(Note.A5, 1.5)


    #Docking
    #await robot.dock()



robot.play()