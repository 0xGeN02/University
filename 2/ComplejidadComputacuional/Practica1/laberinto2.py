# Resuelve el camino mediante backtracking
def resolver_laberinto(laberinto, x, y, solucion, visitado):
    # Si ha llegado al final, termina
    if x == len(laberinto) - 1 and y == len(laberinto[0]) - 1:
        solucion[x][y] = 2
        return True

    if es_valido(laberinto, x, y, visitado):
        solucion[x][y] = 2  # Marcar el camino como parte de la solución
        visitado[x][y] = True

        # Si es posible, nos movemos hacia abajo
        if resolver_laberinto(laberinto, x + 1, y, solucion, visitado):
            return True

        # En caso contrario, si es posible, nos movemos hacia la derecha
        if resolver_laberinto(laberinto, x, y + 1, solucion, visitado):
            return True

        # En caso contrario, si es posible, nos movemos hacia arriba
        # COD05
        if resolver_laberinto(laberinto, x - 1, y, solucion, visitado):
            return True
        # En caso contrario, si es posible, nos movemos hacia la izquierda
        # COD06
        if resolver_laberinto(laberinto, x, y - 1, solucion, visitado):
            return True
        # Si no es posible moverse en ninguna direcciòn, desmarcamos la posición actual (backtrack)
        solucion[x][y] = 0
        visitado[x][y] = False
        return False

    return False

# Comprueba que la posición x,y está dentro del laberinto, es decir, que la posición:
# - Se encuentra dentro del laberinto
# - Forma parte de un camino
# - No ha sido visitado antes
def es_valido(laberinto, x, y, visitado):
    return (0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and
            laberinto[x][y] == 1 and not visitado[x][y])

# Imprime la solución
def imprimir_solucion(solucion):
    for i in solucion:
        for j in i:
            print(str(j) + " ", end="")
        print()


laberinto = [
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1]
]

# Inicializa las matrices con la solución y celdas visitadas.
solucion = [[0 for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]
visitado = [[False for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]

if resolver_laberinto(laberinto, 0, 0, solucion, visitado):
    imprimir_solucion(solucion)
else:
    print("No es posible resolver el laberinto.")