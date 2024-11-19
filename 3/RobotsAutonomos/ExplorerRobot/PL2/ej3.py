import math
import os
import pandas as pd

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth('C3_UIEC_Grupo1'))

th = 150  # Umbral de detección de obstáculo (15 cm)
speed = 10.0  # Velocidad del robot
ronda_aleatoria = True  # Controla la ejecución de la ronda
notas = [Note.A2, Note.B2, Note.C3, Note.D3, Note.E3, Note.F3, Note.G3, Note.A3, Note.B3, Note.C4]
nota_index = 0
colores = [
    (255, 192, 203),  # Rosa
    (255, 64, 0),     # Naranja
    (101, 197, 181),  # Azul verdoso
    (111, 71, 127),   # Púrpura
    (127, 127, 127),  # Gris
    (127, 32, 0),     # Naranja oscuro
    (255, 255, 255),  # Blanco
    (55, 35, 63),     # Púrpura oscuro
    (60, 60, 60),     # Gris oscuro
    (255, 165, 0)     # Naranja brillante
]

color_index = 0

lista = []
lista_distancias = [0]
distancia_total = 0
primer_regreso = True
obstaculos_totales = [[0, 0, 0]]
obstaculos = []
recorrido_excel = True
obstaculo_enfrente = False

def front_obstacle(sensors):
    '''
    Detecta si hay un obstáculo a 15 cm
    '''
    print(sensors[3])  # Mostrar valor del sensor frontal
    return sensors[3] > th


def guardar_lugares_visitados(lista, obstaculos_totales, lista_distancias):
    '''
    Guarda la información de los lugares visitados, los obstáculos y las distancias en un archivo Excel.
    '''
    # Crear un DataFrame para lugares visitados
    df_lugares = pd.DataFrame(lista, columns=['Coordenada X', 'Coordenada Y', 'Coordenada Theta'])

    # Crear un DataFrame para obstáculos
    df_obstaculos = pd.DataFrame(obstaculos_totales, columns=['Enfrente', 'Derecha', 'Izquierda'])

    # Crear un DataFrame para distancias recorridas
    df_distancias = pd.DataFrame(lista_distancias, columns=['Distancia'])

    # Guardar ambos DataFrames en el mismo archivo Excel en hojas diferentes
    with pd.ExcelWriter("Lab02_Entorno.xlsx", engine='openpyxl') as writer:
        df_lugares.to_excel(writer, sheet_name='Lugares Visitados', index=False)
        df_obstaculos.to_excel(writer, sheet_name='Obstáculos', index=False)
        df_distancias.to_excel(writer, sheet_name='Distancias', index=False)

    print("Los datos han sido guardados en Lab02_Entorno.xlsx en dos hojas: 'Lugares Visitados' y 'Obstáculos'.")


def leer_excel():
    """
    Leer las coordenadas e información de los obstáculos del excel
    """
    global lista, obstaculos_totales, lista_distancias
    # Obtener la ruta completa del archivo Excel
    file_path = os.path.join(os.path.dirname(__file__), 'Lab02_Entorno.xlsx')
    df_lugares = pd.read_excel(file_path, sheet_name='Lugares Visitados')
    df_obstaculos = pd.read_excel(file_path, sheet_name='Obstáculos')
    df_distancias = pd.read_excel(file_path, sheet_name='Distancias')
    lista = df_lugares[['Coordenada X', 'Coordenada Y', 'Coordenada Theta']].values.tolist()
    print(f'Lista: {lista}')
    obstaculos_totales = df_obstaculos[['Enfrente', 'Derecha', 'Izquierda']].values.tolist()
    print(f'Lista obstáculos: {obstaculos_totales}')
    lista_distancias = df_distancias['Distancia'].values.tolist()
    print(lista_distancias)

async def movimiento():
    '''
    El robot se mueve hasta que detecta un obstáculo a 15 cm
    '''
    await robot.set_lights_on_rgb(0, 0, 255)  # Luz azul durante el movimiento
    await robot.play_note(Note.A5, .4)  # Tocar nota al inicio
    await robot.set_wheel_speeds(speed, speed)  # Iniciar movimiento

    ejecutando = True

    while ejecutando:
        sensors = (await robot.get_ir_proximity()).sensors
        if front_obstacle(sensors):
            await robot.set_wheel_speeds(0, 0)  # Detener el robot
            await robot.set_lights_on_rgb(255, 0, 0)  # Luz roja por el obstáculo
            await robot.play_note(Note.A5, .5)
            await robot.set_lights_on_rgb(0, 255, 0)  # Luz verde tras la detención
            await robot.play_note(Note.A3, .3)      
            ejecutando = False

async def inspeccion():
    '''
    Gira a la derecha 90 grados y si hay un obstáculo, gira 180 grados,
    y si se encuentra con otro obstáculo, termina la ronda
    '''
    global ronda_aleatoria, obstaculos
    obstaculos = [0, 0, 0]
    obstaculos[0] = 1
    await robot.set_lights_on_rgb(255, 255, 0)  # Luz amarilla durante la inspección
    await robot.play_note(Note.A5, .4)
    await robot.turn_right(90)
    sensors = (await robot.get_ir_proximity()).sensors
    if front_obstacle(sensors):
        await robot.set_lights_on_rgb(255, 0, 0)  # Obstáculo detectado
        await robot.play_note(Note.A5, .5)
        await robot.set_lights_on_rgb(255, 255, 0)
        await robot.play_note(Note.A5, .4)
        obstaculos[1] = 1
        await robot.turn_left(180)
        sensors = (await robot.get_ir_proximity()).sensors
        if front_obstacle(sensors):
            ronda_aleatoria = False  # Termina la ronda si encuentra otro obstáculo
            await robot.set_lights_on_rgb(255, 0, 0)
            await robot.play_note(Note.A5, .5)
            obstaculos[2] = 1
        else:
            await robot.set_lights_on_rgb(0, 255, 0)  # Sin obstáculo
            await robot.play_note(Note.A3, .3)
    else:
        obstaculos[2] = 1
        await robot.set_lights_on_rgb(0, 255, 0)  # Sin obstáculo
        await robot.play_note(Note.A3, .3)

    print(f'Obstáculos: {obstaculos}')

    #guardar_lugares_visitados(obstaculos)
    obstaculos_totales.append(obstaculos)
    print(f'Obstáculos totales: {obstaculos_totales}')


async def memorizar_punto():
    '''
    Memoriza el punto después del movimiento con luz amarilla y sonido y calcula la distancia
    '''
    global lista, distancia_total
    punto = await robot.get_position()  # Obtener la posición actual
    punto_x = punto.x
    punto_y = punto.y
    punto_heading = punto.heading
    coordenadas = [punto_x, punto_y, punto_heading]
    if len(lista) > 0:
        # Si ya hay puntos en la lista, calcula la distancia
        distancia = math.sqrt((punto_x - lista[-1][0]) ** 2 + (punto_y - lista[-1][1]) ** 2)
    else:
        distancia = 0 
    lista_distancias.append(round(distancia, 2))
    print(f"Distancias recorridas: {lista_distancias}") # nuevo
    distancia_total += distancia
    print(f'Distancia total: {round(distancia_total, 2)}')
    lista.append(coordenadas)  # Agregar las coordenadas a la lista
    print(f"Puntos memorizados hasta ahora: {lista}")

async def regresar():
    '''
    Regresa al inicio recordando los puntos recorridos y en cada punto se pone amarillo y espera 10 segundos.
    Comienza desde el último punto de recorrer y va hacia atrás.
    '''
    global primer_regreso, color_index, nota_index

    i = len(lista) - 2  # Último punto antes del inicio
    color_index = (color_index - 2) % len(colores)  # Decrementa el índice de color

    while i >= 0:
        await robot.set_lights_on_rgb(0, 0, 255)
        await robot.navigate_to(lista[i][0], lista[i][1])
        print(f'Punto: ({lista[i][0]}, {lista[i][1]})')

        if primer_regreso:
            await robot.set_lights_on_rgb(255, 255, 0)
            await robot.play_note(Note.A5, .2)
            await robot.wait(5)
        else:
            # Utiliza los últimos índices de color y nota de 'recorrer' y ve restando
            print(f"Color actual (Regresar): {colores[color_index]}")
            await robot.set_lights_on_rgb(*colores[color_index])

            color_index = (color_index - 1) % len(colores)  # Decrementa el índice de color

            await robot.play_note(notas[nota_index], 0.5)
            nota_index = (nota_index - 1) % len(notas)  # Decrementa el índice de nota

            await robot.wait(3)

        i -= 1

async def recorrer_con_info(i):
    '''
    Recorre de un punto a otro que ya tenemos previamente mediante la distancia que hay de un punto a otro
    y si hay un obstáculo de por medio, se detiene y sale del bucle principal
    '''
    global distancia_recorrida, recorrido_excel, distancia_recorrida, obstaculo_enfrente
    await robot.set_wheel_speeds(speed, speed)  # Iniciar movimiento
    await robot.set_lights_on_rgb(0, 0, 255)

    posicion_anterior = await robot.get_position()
    posicion_anterior_x = posicion_anterior.x
    posicion_anterior_y = posicion_anterior.y

    distancia_recorrida = 0
    ejecutando = True

    while ejecutando and distancia_recorrida < lista_distancias[i]:
        sensors = (await robot.get_ir_proximity()).sensors
        if front_obstacle(sensors):
            await robot.set_wheel_speeds(0, 0)
            ejecutando = False
            recorrido_excel = False
            lista_distancias[i] = distancia_recorrida
            lista[i] = [posicion_actual_x, posicion_actual_y, posicion_actual_theta]
            obstaculo_enfrente = True
            await robot.set_lights_on_rgb(255, 0, 0)
            await robot.play_note(Note.A1, .3)
            await robot.set_lights_on_rgb(255, 255, 0)
            await robot.play_note(Note.A2, .3)
            await robot.turn_right(90)
            sensors = (await robot.get_ir_proximity()).sensors
            if front_obstacle(sensors):
                await robot.set_lights_on_rgb(255, 0, 0)
                await robot.play_note(Note.A1, .3)
                obstaculos_totales[i][1] = 1
                obstaculos_totales[i][2] = 0
                await robot.set_lights_on_rgb(255, 255, 0)
                await robot.play_note(Note.A2, .3)
                await robot.turn_left(180)
                await robot.set_lights_on_rgb(0, 255, 0)
                await robot.play_note(Note.A2, .3)
            else:
                await robot.set_lights_on_rgb(0, 255, 0)
                await robot.play_note(Note.A2, .3)
                obstaculos_totales[i][1] = 0
                obstaculos_totales[i][2] = 1

        posicion_actual = await robot.get_position()
        posicion_actual_x = posicion_actual.x
        posicion_actual_y = posicion_actual.y
        posicion_actual_theta = posicion_actual.heading
        distancia_recorrida = math.sqrt(
                (posicion_actual_x - posicion_anterior_x) ** 2 +
                (posicion_actual_y - posicion_anterior_y) ** 2
        )
        print(f'Distancia: {distancia_recorrida}')
    await robot.set_wheel_speeds(0, 0)  # Detener el robot
    print(f"Distancia recorrida: {distancia_recorrida:.2f} cm")

async def inspeccion2(i):
    global recorrido_excel
    '''
    Tras haber llegado con éxito a un punto mediante recorrer_con_info(), comprueba si los obstáculos concuerdan con los almacenados en 
    el fichero excel
    '''
    global no_obstaculo_enfrente
    no_obstaculo_enfrente = False
    if i < len(obstaculos_totales) and obstaculos_totales[i][0] == 1:
        sensors = (await robot.get_ir_proximity()).sensors
        if not front_obstacle(sensors):
            obstaculos_totales[i][0] = 0
            obstaculos_totales[i][1] = 1
            obstaculos_totales[i][2] = 1
            recorrido_excel = False
            no_obstaculo_enfrente = True
            await robot.set_lights_on_rgb(0, 255, 0)
            await robot.play_note(Note.A5, .3)

    if i < len(obstaculos_totales) and obstaculos_totales[i][1] == 0:
        await robot.turn_right(90)
        if front_obstacle(sensors):
            await robot.set_lights_on_rgb(255, 0, 0)
            await robot.play_note(Note.A1, .3)
            obstaculos_totales[i][0] = 1
            obstaculos_totales[i][1] = 1
            obstaculos_totales[i][2] = 0
            recorrido_excel = False
    
    if i < len(obstaculos_totales) and obstaculos_totales[i][2] == 0:
        await robot.turn_left(90)
        if front_obstacle(sensors):
            await robot.set_lights_on_rgb(255, 0, 0)
            await robot.play_note(Note.A1, .3)
            obstaculos_totales[i][0] = 1
            obstaculos_totales[i][1] = 0
            obstaculos_totales[i][2] = 1
            recorrido_excel = False

async def recorrer_sin_info():
    global ronda_aleatoria
    await memorizar_punto()

    while ronda_aleatoria:
        await movimiento()
        await memorizar_punto()
        await inspeccion()

@event(robot.when_play)
async def play(robot):

    leer_excel()

    i = 1
    while i <= len(lista_distancias)-1:
        if recorrido_excel:
            await recorrer_con_info(i)
            if recorrido_excel:
                await inspeccion2(i)

            else:
                break
        else:
            break
        i+=1

    if obstaculo_enfrente:
        i+=1
    elif no_obstaculo_enfrente:
        i-=1

    await robot.wait(5)

    while i <= len(lista_distancias)-1:
        lista.pop(i)
        lista_distancias.pop(i)
        obstaculos_totales.pop(i)
        
    while ronda_aleatoria:
        await movimiento()
        await memorizar_punto()
        await inspeccion()

    print()
    print(f'Coordenadas{lista}')
    print(f'Lista distancias: {lista_distancias}')
    print(f'Obstáculos totales: {obstaculos_totales}')

    guardar_lugares_visitados(lista, obstaculos_totales, lista_distancias)

    print('Finalizado')


# Iniciar el robot
robot.play()