from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth())
speed = 5  # Velocidad de 5 cm/s como requiere la Etapa 01
th = 175  

# Funciones para imprimir la posición del robot
def print_pos_inicial(robot):
    print('🐢 (Posición inicial) =', robot.pose)



# Función para verificar si el sensor frontal detecta un obstáculo
def front_obstacle(sensors):
    print(sensors[3])  # Mostrar el valor del sensor frontal
    return sensors[3] > th  # Detectar si el obstáculo está a menos de 15 cm

@event(robot.when_play)
async def play(robot):
    #ETAPA 01
    # a) Resetear la navegación del robot
    await robot.reset_navigation()
    # b) Encender luces azules y generar sonido
    await robot.set_lights_on_rgb(0, 0, 255)
    await robot.play_note(Note.A5, 1.5)
    # c) Imprimir la posición inicial del robot
    print_pos_inicial(robot)
    # d) Mover el robot a 5 cm/s en línea recta
    await robot.set_wheel_speeds(5, 5)
    # e) Detener el robot cuando esté a 15 cm del obstáculo usando el sensor frontal
    while True:
        sensors = (await robot.get_ir_proximity()).sensors
        if front_obstacle(sensors):
                await robot.set_wheel_speeds(0, 0)
                break
    # g) Cambiar luces a verde y generar sonido al final de la etapa
    await robot.set_lights_on_rgb(255, 0, 0)
    await robot.wait(2)
    await robot.set_lights_on_rgb(0, 255, 0)
    await robot.play_note(Note.A5, 1.5)
    # h) Imprimir la posición final del robot
    distancia_final = await robot.get_position()
    print(distancia_final)



# Ejecutar el programa
robot.play()
