#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021-2022 iRobot Corporation. All rights reserved.
#

# Very basic example for avoiding front obstacles.

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth())
speed = 5
th = 150

#comienza el movimiento del robot indicando luz azul y nota musical
async def movimiento(robot):
    await robot.set_lights_on_rgb(0, 0, 255)
    await robot.set_wheel_speeds(5, 5)

async def obstaculo(robot):
    await robot.set_wheel_speeds(0,0)
    await robot.set_lights_on_rgb(255, 0, 0)
    await robot.play_note(Note.A5, 1.5)
    await robot.wait(1)

def print_pos_inicio(robot):
    print('Punto Inicio Mision =', robot.pose)


def front_obstacle(sensors):
    print(sensors[3])
    return sensors[3] > th


@event(robot.when_play)
async def play(robot):
    await robot.reset_navigation()
    
    print_pos_inicio(robot)
    await robot.set_lights_on_rgb(0, 0, 255)
    await robot.play_note(Note.A5, 1.5)
    await movimiento(robot)
    
    #cuando ve un obstaculo a 15 cm se para
    while True:
        sensors = (await robot.get_ir_proximity()).sensors
        if front_obstacle(sensors):
            await obstaculo(robot)
            break
    await robot.set_lights_on_rgb(0, 255, 0)
    await robot.play_note(Note.A5, .5)
    distancia_final = await robot.get_position()
    print(distancia_final)
    
    #etapa2
    #INSPACCION
    

    while True:
        await robot.set_lights_on_rgb(255, 255, 0)
        await robot.play_note(Note.A5, .5)
        await robot.turn_right(90)
        await robot.play_note(Note.A5, .5)
        
        
        sensors = (await robot.get_ir_proximity()).sensors
        if front_obstacle(sensors):
            await obstaculo(robot)
            await robot.set_lights_on_rgb(255, 255, 0)
            await robot.play_note(Note.A5, .5)
            await robot.turn_left(180)
            break
        else:
            await robot.set_wheel_speeds(5, 5)
            break

    await movimiento(robot)
    await robot.play_note(Note.A5, 1.0)
    #cuando ve un obstaculo a 15 cm se para
    while True:
        sensors = (await robot.get_ir_proximity()).sensors
        if front_obstacle(sensors):
            await obstaculo(robot)
            break
    await robot.set_lights_on_rgb(0, 255, 0)
    await robot.play_note(Note.A5, 1.5)
    distancia_final2 = await robot.get_position()
    print(distancia_final2)


#etapa3
    while True:
        await robot.set_lights_on_rgb(255, 255, 0)
        await robot.play_note(Note.A5, .5)
        await robot.turn_right(90)
    
    
        
        sensors = (await robot.get_ir_proximity()).sensors
        if front_obstacle(sensors):
            await obstaculo(robot)
            await robot.set_lights_on_rgb(255, 255, 0)
            await robot.play_note(Note.A5, .5)
            await robot.turn_left(180)
            break
        else:
            await robot.set_wheel_speeds(5, 5)
            break

    await movimiento(robot)
    await robot.play_note(Note.A5, 1.0)
    #cuando ve un obstaculo a 15 cm se para
    while True:
        sensors = (await robot.get_ir_proximity()).sensors
        if front_obstacle(sensors):
            await obstaculo(robot)
            break
    await robot.set_lights_on_rgb(0, 255, 0)
    await robot.play_note(Note.A5, 1.5)
    distancia_final3 = await robot.get_position()
    print(distancia_final3)
    
#etapa 4
    while True:
        await robot.set_lights_on_rgb(255, 255, 0)
        await robot.play_note(Note.A5, .5)
        await robot.turn_right(90)
        await robot.play_note(Note.A5, .5)
        
        
        sensors = (await robot.get_ir_proximity()).sensors
        if front_obstacle(sensors):
            await obstaculo(robot)
            await robot.set_lights_on_rgb(255, 255, 0)
            await robot.play_note(Note.A5, .5)
            await robot.turn_left(180)
            break
        else:
            await robot.set_lights_on_rgb(0, 255, 0)
            await robot.set_wheel_speeds(5, 5)
            break

    await movimiento(robot)
    await robot.play_note(Note.A5, 1.0)
    #cuando ve un obstaculo a 15 cm se para
    while True:
        sensors = (await robot.get_ir_proximity()).sensors
        if front_obstacle(sensors):
            await obstaculo(robot)
            await robot.set_lights_on_rgb(255, 255, 0)
            await robot.play_note(Note.A5, .5)
            await robot.turn_right(90)
            sensors = (await robot.get_ir_proximity()).sensors
            if front_obstacle(sensors):
                await obstaculo(robot)
                await robot.set_lights_on_rgb(255, 255, 0)
                await robot.play_note(Note.A5, .5)
                await robot.turn_right(180)
                sensors = (await robot.get_ir_proximity()).sensors
                if front_obstacle(sensors):
                    await robot.set_lights_on_rgb(255,0, 0)
                    await robot.play_note(Note.A5, 1.5)
                    break
            break
    await robot.set_lights_on_rgb(0, 255, 0)
    await robot.play_note(Note.A5, 1.5)
    distancia_final3 = await robot.get_position()
    print(distancia_final3)
robot.play()