t = 0
def busqueda_secuencial(vector, elemento):
    global t
    for i, e in enumerate(vector):
        t += 1
        if e == elemento:
            return i
    return -1

vector = [1, 2, 3, 4, 5]
elemento = 3
print(busqueda_secuencial(vector, elemento))
print("T(N): ", t)