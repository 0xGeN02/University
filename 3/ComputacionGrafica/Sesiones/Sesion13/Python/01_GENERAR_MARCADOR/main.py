import cv2
import cv2.aruco as aruco
import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

# Especificamos el ID del marcador
id_marcador = 1

# Definimos el tamaño de la cuadrícula (4, 5, 6 o 7)
tamano_cuadricula = 7

# Definimos el tamaño del marcador en píxeles
tamano_marcador = 500

# Mapeo de tamaños de cuadrícula a diccionarios ArUco
diccionarios_aruco = {
    4: aruco.DICT_4X4_50,
    5: aruco.DICT_5X5_100,
    6: aruco.DICT_6X6_250,
    7: aruco.DICT_7X7_1000
}

# Validamos el tamaño de la cuadrícula
if tamano_cuadricula not in diccionarios_aruco:
    raise ValueError("El tamaño de la cuadrícula debe ser 4, 5, 6 o 7.")

# Seleccionamos el diccionario especificado
diccionario = aruco.Dictionary_get(diccionarios_aruco[tamano_cuadricula])

# Verificamos que el ID esté dentro del rango válido para el diccionario seleccionado
num_marcadores = diccionario.bytesList.shape[0]
if id_marcador >= num_marcadores:
    raise ValueError(f"ID inválido. Debe estar entre 0 y {num_marcadores - 1} para el diccionario  {tamano_cuadricula}x{tamano_cuadricula}.")

# Generamos el marcador ArUco
imagen_marcador = aruco.drawMarker(diccionario, id_marcador, tamano_marcador)

# Formateamos el ID del marcador con ceros a la izquierda para tener 4 dígitos
id_formateado = f"{id_marcador:04d}"

# Creamos el nombre del archivo según el formato especificado
nombre_archivo = f'marcador_aruco_{tamano_cuadricula}x{tamano_cuadricula}_{id_formateado}.png'

# Guardamos el marcador en un archivo de imagen
cv2.imwrite(nombre_archivo, imagen_marcador)
print(f"Marcador ArUco generado y guardado como {nombre_archivo}")

# Mostramos el marcador generado
cv2.imshow(f'Marcador ArUco Cuadricula: {tamano_cuadricula}x{tamano_cuadricula} ID: {id_formateado}', imagen_marcador)
cv2.waitKey(0)
cv2.destroyAllWindows()