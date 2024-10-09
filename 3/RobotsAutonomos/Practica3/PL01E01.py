from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth())

# Lista para almacenar las posiciones visitadas
lugares_visitados = []

# Función para resetear la posición del robot
async def reset_position(robot_1):
    await robot_1.reset_navigation()

# Función para generar una señal luminosa azul y una señal sonora para indicar el inicio del movimiento
async def señal_inicio_movimiento(robot_1):
    await robot_1.set_lights_on_rgb(0, 0, 255)  # Luz azul
    await robot_1.play_note(Note.C4, 1.0)

# Función para mostrar la posición de inicio de la misión del robot
def print_pos_inicio(robot_1):
    x = robot_1.pose.x
    y = robot_1.pose.y
    theta = robot_1.pose.heading
    print(f'Posición de inicio: ({x:.2f}, {y:.2f}, {theta:.1f}°)')

# Función para establecer la velocidad del robot
async def set_speed(robot_1, speed):
    await robot_1.set_wheel_speeds(speed, speed)

# Función para detener el movimiento del robot cuando esté a 15 cm del obstáculo
async def detener_movimiento(robot_1, threshold):
    while True:
        sensors = (await robot_1.get_ir_proximity()).sensors
        if sensors[3] > threshold:
            await robot_1.set_wheel_speeds(0, 0)
            break

# Función para generar una señal luminosa roja y una señal sonora cuando se detecta un obstáculo
async def señal_obstaculo(robot_1):
    await robot_1.set_lights_on_rgb(255, 0, 0)  # Luz roja
    await robot_1.play_note(Note.C4, 1.0)

# Función para generar una señal luminosa verde y una señal sonora para indicar el final de la etapa
async def señal_final_etapa(robot_1):
    await robot_1.set_lights_on_rgb(0, 255, 0)  # Luz verde
    await robot_1.play_note(Note.G4, 1.0)

# Función para mostrar la nueva posición del robot y la distancia recorrida
def print_pos_nueva(robot_1):
    x = robot_1.pose.x
    y = robot_1.pose.y
    theta = robot_1.pose.heading
    print(f'Nueva posición: ({x:.2f}, {y:.2f}, {theta:.1f}°)')

# Función para girar el robot un ángulo dado 
async def girar(robot_1, theta=90):
    await robot_1.turn_right(theta)

# Función para inspeccionar ambas direcciones y determinar hacia dónde moverse
async def inspeccion_y_decision(robot_1, threshold=150):
    # Inspección hacia la derecha (90 grados)
    await robot_1.set_lights_on_rgb(255, 255, 0)  # Luz amarilla para inspección
    await girar(robot_1, 90)
    sensors_derecha = (await robot_1.get_ir_proximity()).sensors

    # Inspección hacia la izquierda (180 grados para volver a la posición original y girar hacia la izquierda)
    await girar(robot_1, 180)
    sensors_izquierda = (await robot_1.get_ir_proximity()).sensors

    # Volver a la posición original (girar 90 grados)
    await girar(robot_1, 90)

    # Decisión de movimiento basado en los sensores
    if sensors_derecha[3] <= threshold and sensors_izquierda[3] <= threshold:
        # Ambas direcciones bloqueadas
        return False
    elif sensors_derecha[3] > threshold:
        # Mover hacia la derecha
        await girar(robot_1, 90)
    elif sensors_izquierda[3] > threshold:
        # Mover hacia la izquierda
        await girar(robot_1, -90)

    return True  # Todavía hay direcciones posibles para moverse

# Función para recordar las posiciones visitadas por el robot
def recordar_posicion(robot_1):
    # Obtenemos la posición actual del robot_1
    posicion_actual = (robot_1.pose.position.x, robot_1.pose.position.y)
    
    # Verificar si ya se visitó esta posición
    if posicion_actual not in lugares_visitados:
        lugares_visitados.append(posicion_actual)
        print(f"Lugar nuevo visitado: {posicion_actual}")
    else:
        print(f"Este lugar ya fue visitado: {posicion_actual}")

# Evento de inicio de la misión
@event(robot.when_play)
async def play(robot_1):

    speed=5
    th=150

    # Etapa 1: Inicio
    await reset_position(robot_1)
    await señal_inicio_movimiento(robot_1)
    print_pos_inicio(robot_1)
    await set_speed(robot_1, speed)
    await detener_movimiento(robot_1, th)
    await señal_obstaculo(robot_1)
    await señal_final_etapa(robot_1)
    print_pos_nueva(robot_1)

    # Recordar la primera posición visitada
    recordar_posicion(robot_1)

    # Etapa 2: Inspección y Continuación hasta que ambas direcciones estén bloqueadas
    while True:
        direccion_disponible = await inspeccion_y_decision(robot_1)

        # Recordar cada nueva posición
        recordar_posicion(robot_1)

        if not direccion_disponible:
            print("Ambas direcciones bloqueadas. Deteniendo el robot.")

            # Señal roja para indicar bloqueo y detener el robot
            await robot_1.set_wheel_speeds(0, 0)
            await señal_obstaculo(robot_1)

            # Parada de 10 segundos
            print("Parada de 10 segundos...")
            await robot_1.set_wheel_speeds(0, 0)
            robot_1.wait(10)

            # Señal luminosa amarilla al finalizar la pausa
            await robot_1.set_lights_on_rgb(255, 255, 0)  # Luz amarilla
            print("Reanudando movimiento...")

            # Después de la pausa, romper el ciclo (el robot se detiene permanentemente)
            break

        # Continuar movimiento
        await set_speed(robot_1, speed)
        await detener_movimiento(robot_1, th)

        # Señal luminosa y sonora al detectar un obstáculo
        await señal_obstaculo(robot_1)

        # Final de la etapa
        await señal_final_etapa(robot_1)
        print_pos_nueva(robot_1)

# Ejecutar la función play
robot.play()
