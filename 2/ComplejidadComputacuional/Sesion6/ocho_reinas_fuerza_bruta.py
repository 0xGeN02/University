import time

def es_solucion_valida(tablero, N):
    for i in range(N):
        for j in range(N):
            # Si encontramos una reina en [i, j]
            if tablero[i][j] == 1:
                # Revisar si hay otra reina en la misma columna
                for k in range(N):
                    if k != i and tablero[k][j] == 1:
                        return False

                # Revisar diagonales
                for k in range(1, N):
                    if i+k < N and j+k < N and tablero[i+k][j+k] == 1:
                        return False
                    if i+k < N and j-k >= 0 and tablero[i+k][j-k] == 1:
                        return False
                    if i-k >= 0 and j+k < N and tablero[i-k][j+k] == 1:
                        return False
                    if i-k >= 0 and j-k >= 0 and tablero[i-k][j-k] == 1:
                        return False
    return True

def n_reinas(N):
    soluciones = []
    # Generar todas las posibles combinaciones de posiciones de las reinas
    # Usamos un número entero para representar la columna de la reina en cada fila
    for combinacion in range(N**N):
        tablero = [[0 for i in range(N)] for j in range(N)]
        temp = combinacion
        valido = True
        for fila in range(N):
            col = temp % N
            temp //= N
            # Si dos reinas se colocan en la misma columna, descartar esta combinación
            if any(tablero[f][col] == 1 for f in range(N)):
                valido = False
                break
            tablero[fila][col] = 1
        if valido and es_solucion_valida(tablero, N):
            soluciones.append(tablero)
    return soluciones

def imprimir_solucion(tablero):
    for fila in tablero:
        print(" ".join(str(x) for x in fila))
    print()

n = 4

print("Algoritmo: 8 reinas fuerza bruta")

ini = time.time()
soluciones = n_reinas(n)
fin = time.time()

tiempo = fin-ini
print(f"Soluciones encontradas: {len(soluciones)}")
for solucion in soluciones:
    imprimir_solucion(solucion)
print(f'{tiempo:.20f}')