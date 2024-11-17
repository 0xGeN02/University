"""
    main.py
"""
from constants import config
from framework.framework import Framework
from robot.robot import RobotDrawer

def main():
    """
    Punto de entrada del programa.
    """
    # Crear el marco
    paper = Framework(config.DIN_A3_WIDTH, config.DIN_A3_HEIGHT)

    # Conectar al robot
    robot = RobotDrawer(config.HOTSPOT_ADDRESS, config.PORT)

    # Verificar la conexión
    if robot is None:
        print("ERROR: Conexión fallida.")
        return
    print("")
    print("--------------------------")
    print("")
    print("Robot conectado con éxito.")
    print("")

    print(f'El punto de inicio es: {robot.arm.get_pose()}')
    # Calcular el centro del marco
    paper_center = paper.get_center()
    print(f"Centro del papel: {paper_center}")
    paper_corners = paper.get_corners()
    print(f'Esquinas del papel : {paper_corners}')

    # Dibujar un cuadrado
    robot.draw_square(paper_center, 0.1)

    # Mover al modo de reposo
    robot.arm.go_to_sleep()

if __name__ == "__main__":
    main()
