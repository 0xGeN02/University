import cv2
import cv2.aruco as aruco
import os
import numpy as np
import shutil

# Configuración de parámetros
AREA_MINIMA_CONTORNO = 1000  # Área mínima para considerar un contorno
N = 9  # Tamaño de la rejilla NxN, debe ser mayor o igual a 3
NOMBRE_IMAGEN_ENTRADA = "imagen_1.png"  # Nombre del archivo de imagen de entrada
CARPETA_SALIDA = "resultados"  # Carpeta donde se guardarán los resultados

# Ruta absoluta del archivo de imagen
ruta_imagen = os.path.join(os.path.dirname(__file__), NOMBRE_IMAGEN_ENTRADA)

def limpiar_carpeta(carpeta):
    """
    Limpia el contenido de una carpeta. Si no existe, la crea.
    """
    if os.path.exists(carpeta):
        shutil.rmtree(carpeta)
    os.makedirs(carpeta)

def es_contorno_similar(contornos_existentes, nuevo_contorno, umbral_area=0.3, umbral_distancia=20):
    """
    Verifica si un nuevo contorno es similar a alguno de los contornos existentes.
    """
    area_nueva = cv2.contourArea(nuevo_contorno)
    if area_nueva == 0:
        return False

    M_nueva = cv2.moments(nuevo_contorno)
    if M_nueva["m00"] == 0:
        return False
    cx_nueva = int(M_nueva["m10"] / M_nueva["m00"])
    cy_nueva = int(M_nueva["m01"] / M_nueva["m00"])

    for cont in contornos_existentes:
        area_existente = cv2.contourArea(cont)
        if area_existente == 0:
            continue

        diferencia_area = abs(area_existente - area_nueva)
        if diferencia_area > umbral_area * area_existente:
            continue

        M_existente = cv2.moments(cont)
        if M_existente["m00"] == 0:
            continue
        cx_existente = int(M_existente["m10"] / M_existente["m00"])
        cy_existente = int(M_existente["m01"] / M_existente["m00"])

        distancia = np.sqrt((cx_existente - cx_nueva) ** 2 + (cy_existente - cy_nueva) ** 2)
        if distancia < umbral_distancia:
            return True

    return False

def ordenar_puntos(puntos):
    """
    Ordena los puntos de un cuadrilátero en el orden: arriba-izquierda, arriba-derecha,
    abajo-derecha, abajo-izquierda, independientemente de la orientación del polígono.
    """
    puntos = puntos.reshape(4, 2)
    # Calcular el centroide
    centroide = np.mean(puntos, axis=0)
    # Calcular el ángulo de cada punto con respecto al centroide
    angulos = np.arctan2(puntos[:,1] - centroide[1], puntos[:,0] - centroide[0])
    # Ordenar los puntos en sentido antihorario
    orden = np.argsort(angulos)
    puntos_ordenados = puntos[orden]
    return puntos_ordenados.astype("float32")

def decodificar_marcador(aruco_dict, marker_id):
    """
    Obtiene los bits binarios de un marcador del diccionario.
    """
    codigo_marcador = aruco_dict.bytesList[marker_id]
    bits = np.unpackbits(codigo_marcador).astype(np.uint8)
    numero_bits_marcador = aruco_dict.markerSize ** 2
    bits = bits[:numero_bits_marcador]
    bits = bits.reshape((aruco_dict.markerSize, aruco_dict.markerSize))
    return bits

def procesar_candidato(contorno, imagen_original, index, carpeta_salida):
    """
    Procesa un contorno candidato para extraer la secuencia binaria de sus celdas.
    """
    # Verificar la orientación del contorno y ajustar si es necesario
    area_orientada = cv2.contourArea(contorno, oriented=True)
    if area_orientada < 0:
        contorno = contorno[::-1]

    # Ordenar los puntos del contorno
    puntos_ordenados = ordenar_puntos(contorno)

    # Definir un tamaño fijo para la transformación
    tamano_fijo = N * 20  # Escalar para mayor resolución
    puntos_destino = np.array([
        [0, 0],
        [tamano_fijo - 1, 0],
        [tamano_fijo - 1, tamano_fijo - 1],
        [0, tamano_fijo - 1]
    ], dtype="float32")

    # Calcular la matriz de transformación de perspectiva
    matriz_perspectiva = cv2.getPerspectiveTransform(puntos_ordenados, puntos_destino)

    # Aplicar la transformación de perspectiva
    imagen_transformada = cv2.warpPerspective(imagen_original, matriz_perspectiva, (tamano_fijo, tamano_fijo))

    # Guardar la imagen del candidato transformado
    nombre_candidato = f"05_candidato_{index:02d}.png"
    ruta_candidato = os.path.join(carpeta_salida, nombre_candidato)
    cv2.imwrite(ruta_candidato, imagen_transformada)

    # Convertir a escala de grises y binarizar
    imagen_gris = cv2.cvtColor(imagen_transformada, cv2.COLOR_BGR2GRAY)
    _, imagen_binarizada = cv2.threshold(imagen_gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Guardar la imagen binarizada
    nombre_binarizado = f"05_candidato_{index:02d}_binarizado.png"
    ruta_binarizado = os.path.join(carpeta_salida, nombre_binarizado)
    cv2.imwrite(ruta_binarizado, imagen_binarizada)

    # Recortar el borde exterior
    paso = max(tamano_fijo // N, 1)
    recorte = imagen_binarizada[paso: tamano_fijo - paso, paso: tamano_fijo - paso]

    # Verificar que el recorte no sea vacío
    if recorte.size == 0:
        print(f"Advertencia: El recorte del candidato {index} está vacío. Se omite el procesamiento.")
        return

    # Guardar el recorte de la imagen
    nombre_recorte = f"05_candidato_{index:02d}_recorte.png"
    ruta_recorte = os.path.join(carpeta_salida, nombre_recorte)
    cv2.imwrite(ruta_recorte, recorte)

    # Procesar las celdas de la rejilla
    filas, columnas = recorte.shape
    celda_x = max(columnas // (N - 2), 1)
    celda_y = max(filas // (N - 2), 1)

    # Crear una imagen para las celdas procesadas
    imagen_celdas = np.zeros_like(recorte)

    for fila in range(N - 2):
        for columna in range(N - 2):
            inicio_x = columna * celda_x
            inicio_y = fila * celda_y
            fin_x = inicio_x + celda_x
            fin_y = inicio_y + celda_y

            # Verificar límites
            fin_x = min(fin_x, columnas)
            fin_y = min(fin_y, filas)

            roi = recorte[inicio_y:fin_y, inicio_x:fin_x]
            color_medio = cv2.mean(roi)[0]
            color = 255 if color_medio > 127 else 0
            imagen_celdas[inicio_y:fin_y, inicio_x:fin_x] = color

    # Guardar la imagen con las celdas procesadas
    nombre_procesado = f"05_candidato_{index:02d}_procesado.png"
    ruta_procesado = os.path.join(carpeta_salida, nombre_procesado)
    cv2.imwrite(ruta_procesado, imagen_celdas)

    # Determinar el diccionario ArUco correspondiente
    tamano_marcador = N - 2
    if tamano_marcador == 4:
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    elif tamano_marcador == 5:
        aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_100)
    elif tamano_marcador == 6:
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    elif tamano_marcador == 7:
        aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_1000)
    else:
        print(f"No hay diccionario ArUco disponible para tamaño de rejilla {tamano_marcador}.")
        return

    # Generar secuencias binarias para cada rotación y guardarlas en un archivo de texto
    nombre_secuencias = f"05_candidato_{index:02d}_secuencias.txt"
    ruta_secuencias = os.path.join(carpeta_salida, nombre_secuencias)
    with open(ruta_secuencias, 'w', encoding='utf-8') as archivo_secuencias:
        for angulo in [0, 90, 180, 270]:
            # Rotar la imagen de celdas
            if angulo == 0:
                imagen_rotada = imagen_celdas.copy()
            else:
                num_rotaciones = angulo // 90
                imagen_rotada = np.rot90(imagen_celdas, k=num_rotaciones)

            # Extraer la secuencia binaria
            secuencia_binaria = []
            for fila in range(N - 2):
                inicio_y = fila * celda_y
                fin_y = inicio_y + celda_y
                fila_binaria = ''
                for columna in range(N - 2):
                    inicio_x = columna * celda_x
                    fin_x = inicio_x + celda_x

                    # Verificar límites
                    fin_x = min(fin_x, imagen_rotada.shape[1])
                    fin_y = min(fin_y, imagen_rotada.shape[0])

                    roi = imagen_rotada[inicio_y:fin_y, inicio_x:fin_x]
                    if roi.size == 0:
                        bit = '0'
                    else:
                        color_medio = cv2.mean(roi)[0]
                        bit = '1' if color_medio > 127 else '0'
                    fila_binaria += bit
                secuencia_binaria.append(fila_binaria)
            # Escribir la secuencia en el archivo
            archivo_secuencias.write(f"Rotación {angulo} grados:\n\n")
            for fila in secuencia_binaria:
                archivo_secuencias.write(f"{fila}\n")

            # Convertir secuencia_binaria a array numpy
            secuencia_array = np.array([[int(bit) for bit in fila] for fila in secuencia_binaria], dtype=np.uint8)
            # Comparar con marcadores ArUco
            marcador_encontrado = False
            for marker_id in range(aruco_dict.bytesList.shape[0]):
                marker_bits = decodificar_marcador(aruco_dict, marker_id)
                if np.array_equal(secuencia_array, marker_bits):
                    archivo_secuencias.write(f"\nCoincide con el marcador ArUco ID {marker_id}\n")
                    marcador_encontrado = True
                    break
            if not marcador_encontrado:
                archivo_secuencias.write("\nNo coincide con ningún marcador ArUco\n")
            archivo_secuencias.write("\n")
    print(f"Procesado del candidato {index} completado. Secuencias guardadas en '{nombre_secuencias}'.")

def procesar_imagen(nombre_imagen_entrada, carpeta_salida):
    """
    Procesa la imagen de entrada para detectar candidatos y extraer secuencias binarias.
    """
    # Cargar la imagen original en color
    imagen_original = cv2.imread(nombre_imagen_entrada)
    if imagen_original is None:
        print(f"Error: No se pudo cargar la imagen '{nombre_imagen_entrada}'.")
        return

    # Paso 1: Convertir a Escala de Grises
    imagen_grises = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)
    ruta_grises = os.path.join(carpeta_salida, "01_imagen_grises.png")
    cv2.imwrite(ruta_grises, imagen_grises)

    # Paso 2: Binarizar la Imagen
    _, imagen_binaria = cv2.threshold(imagen_grises, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ruta_binaria = os.path.join(carpeta_salida, "02_imagen_binaria.png")
    cv2.imwrite(ruta_binaria, imagen_binaria)

    # Paso 3: Umbralización Adaptativa e Invertir Colores
    umbral_adaptativo = cv2.adaptiveThreshold(
        imagen_grises, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 15, 10
    )
    contornos_invertidos = cv2.bitwise_not(umbral_adaptativo)
    ruta_contornos = os.path.join(carpeta_salida, "03_imagen_contornos.png")
    cv2.imwrite(ruta_contornos, contornos_invertidos)

    # Paso 4: Detectar y Resaltar Contornos Cerrados de 4 Vértices
    contornos, _ = cv2.findContours(
        contornos_invertidos, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    contornos_4_vertices = []
    for idx, contorno in enumerate(contornos):
        perimetro = cv2.arcLength(contorno, True)
        epsilon = 0.02 * perimetro
        aproximacion = cv2.approxPolyDP(contorno, epsilon, True)
        if len(aproximacion) == 4 and cv2.isContourConvex(aproximacion):
            area_contorno = cv2.contourArea(aproximacion)
            if area_contorno >= AREA_MINIMA_CONTORNO:
                if not es_contorno_similar(contornos_4_vertices, aproximacion):
                    contornos_4_vertices.append(aproximacion)

    # Resaltar contornos candidatos en la imagen original
    imagen_candidatos = imagen_original.copy()
    cv2.drawContours(imagen_candidatos, contornos_4_vertices, -1, (0, 255, 0), 2)
    ruta_candidatos = os.path.join(carpeta_salida, "04_imagen_candidatos.png")
    cv2.imwrite(ruta_candidatos, imagen_candidatos)

    # Procesar cada candidato
    for i, contorno in enumerate(contornos_4_vertices, start=1):
        procesar_candidato(contorno, imagen_original, i, carpeta_salida)

def main():
    # Crear y limpiar la carpeta "resultados"
    limpiar_carpeta(CARPETA_SALIDA)

    # Verificar si el archivo de imagen existe
    if not os.path.isfile(ruta_imagen):
        print(f"Error: El archivo '{ruta_imagen}' no se encontró.")
        return

    # Procesar la imagen
    procesar_imagen(ruta_imagen, CARPETA_SALIDA)

if __name__ == "__main__":
    main()