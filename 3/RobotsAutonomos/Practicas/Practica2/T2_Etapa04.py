"""
Práctica 3: Robots Autónomos
"""

import math
from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth())

# Diccionario para variables globales
global_vars = {
    "speed": 5,
    "th": 150,
    "distance": 0.0,
    "ant_x": 0.0,
    "ant_y": 0.0,
    "theta": 0.0,
    "posiciones_visitadas": []
}

async def init_vars():
    """
    Función que inicializa las variables globales
    """
    global_vars["speed"] = 5
    global_vars["th"] = 150
    global_vars["distance"] = 0.0
    global_vars["ant_x"] = 0.0
    global_vars["ant_y"] = 0.0
    global_vars["theta"] = 0.0
    global_vars["posiciones_visitadas"] = []

# Comienza el movimiento del robot indicando luz azul y nota musical
async def movimiento(robot_instance):
    """
    Función que inicia el movimiento del robot
    """
    await robot_instance.set_lights_on_rgb(0, 0, 255)
    await robot_instance.set_wheel_speeds(global_vars["speed"], global_vars["speed"])

# Detiene el robot al detectar obstáculo, enciende luz roja y suena una nota
async def obstaculo(robot_instance):
    """
    Función que detiene el robot al detectar un obstáculo
    """
    await robot_instance.set_wheel_speeds(0, 0)
    await robot_instance.set_lights_on_rgb(255, 0, 0)
    await robot_instance.play_note(Note.A5, 1.5)
    await robot_instance.wait(1)

    final_position = await robot_instance.get_position()
    print(f"Punto final de misión: {final_position}")

    act_x = abs(final_position.x)
    act_y = abs(final_position.y)
    theta = final_position.heading
    print(f"x: {act_x}, y: {act_y}, θ: {theta}")

    # Append visited position to list
    global_vars["posiciones_visitadas"].append((act_x, act_y, theta))

    # Calcula la distancia recorrida aplicando el Teorema de Pitágoras
    global_vars["distance"] += math.sqrt(
        (act_x - global_vars["ant_x"]) ** 2 +
        (act_y - global_vars["ant_y"]) ** 2
    )
    global_vars["ant_x"] = act_x
    global_vars["ant_y"] = act_y
    global_vars["theta"] = theta

    print("Distancia recorrida:", global_vars["distance"])

# Detección de obstáculos en el frente
async def deteccion(robot_instance):
    """
    Función que detecta obstáculos en el frente
    """
    while True:
        sensors = (await robot_instance.get_ir_proximity()).sensors
        if front_obstacle(sensors):
            await obstaculo(robot_instance)

            #Luz verde
            await robot_instance.set_lights_on_rgb(0, 255, 0)
            await robot_instance.play_note(Note.A5, 1.5)

            # Luz amarilla para indicar inspección
            await robot_instance.set_lights_on_rgb(255, 255, 0)
            await robot_instance.play_note(Note.A5, 0.5)

            # Giro a la derecha para explorar la primera dirección
            await robot_instance.turn_right(90)
            sensors = (await robot_instance.get_ir_proximity()).sensors

            if front_obstacle(sensors):  # Si también hay obstáculo en esa dirección
                await robot.set_wheel_speeds(0, 0)
                await robot.set_lights_on_rgb( 255, 0 , 0)
                await robot.play_note(Note.A5, 1.5)
                await robot.set_lights_on_rgb( 0, 255 , 0)
                await robot.play_note(Note.A5, 1.5)
                await robot.set_lights_on_rgb(255, 255, 0)  # Luz amarilla para indicar inspección
                await robot.play_note(Note.A5, 0.5)
                # Giramos 180 grados para explorar la segunda dirección
                await robot_instance.turn_right(180)
                sensors = (await robot_instance.get_ir_proximity()).sensors
                if front_obstacle(sensors):  # Si hay obstáculo en ambas direcciones
                    await finalizar_mision(robot_instance)  # Se finaliza la misión
                    break
            else:
                await movimiento(robot_instance)  # Si no hay obstáculo, continuamos moviendo
        else:
            await movimiento(robot_instance)  # Continúa moviéndose si no hay obstáculos

# Finaliza la misión con luz verde y una nota musical
async def finalizar_mision(robot_instance):
    """
    Función que finaliza la misión
    """
    await robot_instance.set_wheel_speeds(0, 0)
    await robot_instance.set_lights_on_rgb(255, 0, 0)
    await robot_instance.play_note(Note.A5, 1.5)
    await robot_instance.set_lights_on_rgb(0, 255, 0)
    await robot_instance.play_note(Note.C6, 2.0)
    await robot_instance.set_lights_on_rgb(255, 255, 0)  # Luz amarilla para indicar inspección
    await robot_instance.wait(10)
    print("Misión completada: finalización de la ronda")
    print("La distancia recorrida total de la ronda ha sido:", global_vars["distance"])
    print("Posiciones visitadas:", global_vars["posiciones_visitadas"])

# Función que imprime la posición inicial
async def print_pos_inicio(robot_instance):
    """
    Función que imprime la posición inicial
    """
    print('Punto Inicio Mision =', await robot_instance.get_position())

# Función que determina si hay un obstáculo al frente
def front_obstacle(sensors):
    """
    Función que determina si hay un obstáculo al frente
    """
    print(sensors[3])  # Sensores frontales
    return sensors[3] > global_vars["th"]  # Si la lectura es mayor que el umbral, hay un obstáculo

async def ir_func(robot_instance):
    """
    Funcion de movimiento
    """
    await robot_instance.reset_navigation()  # Resetea la navegación
    await print_pos_inicio(robot_instance)  # Imprime la posición de inicio
    await robot_instance.set_lights_on_rgb(0, 0, 255)  # Luz azul
    await robot_instance.play_note(Note.A5, 1.5)  # Suena una nota para indicar el inicio
    await movimiento(robot_instance)  # Comienza el movimiento
    await deteccion(robot_instance)  # Comienza la detección de obstáculos

@event(robot.when_play)
async def play(robot_instance):
    """
    Función que se ejecuta al iniciar el robot
    """
    await init_vars()  # Inicializa las variables globales
    await ir_func(robot_instance)

# Inicia el robot
robot.play()
