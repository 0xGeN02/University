import cv2

def lista_camaras_disponibles(max_cameras=5):
    """
    Lista las cámaras disponibles en el sistema hasta un máximo especificado.
    """
    camaras_disponibles = []
    for index in range(max_cameras):
        captura = cv2.VideoCapture(index)
        if captura.isOpened():
            camaras_disponibles.append(index)
            captura.release()
    if camaras_disponibles:
        print("Cámaras disponibles:", camaras_disponibles)
    else:
        print("No se encontraron cámaras disponibles.")

lista_camaras_disponibles()