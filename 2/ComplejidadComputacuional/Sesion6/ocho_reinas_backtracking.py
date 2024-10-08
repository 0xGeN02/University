import time

def n_reinas(tablero, N, col=0, soluciones=None):
    if soluciones is None:
        soluciones = []
    if col >= N:
        soluciones.append([fila.copy() for fila in tablero])
        return soluciones
    for i in range(N):
        if es_seguro(tablero, i, col, N):
            tablero[i][col] = 1
            n_reinas(tablero, N, col + 1, soluciones)
            tablero[i][col] = 0
    return soluciones


def es_seguro(tablero, fila, col, N):
    for i in range(col):
        if tablero[fila][i] == 1:
            return False
    i, j = fila, col
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = fila, col
    while i < N and j >= 0:
        if tablero[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True



def imprimir_soluciones(soluciones):
    for solucion in soluciones:
        for fila in solucion:
            linea = ""
            for celda in fila:
                linea += "1 " if celda == 1 else "0 "
            print(linea)
        print()

n = 4
tablero = [[0 for i in range(n)] for j in range(n)]

print("Algoritmo: 8 reinas backtracking")

ini = time.time()
soluciones = n_reinas(tablero, n)
fin = time.time()

tiempo = fin-ini
print(f"Soluciones encontradas: {len(soluciones)}")
imprimir_soluciones(soluciones)
print(f'{tiempo:.20f}')