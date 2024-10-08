t = 1
def busqueda_binaria(vector, elemento):
    global t
    min = 0
    max = len(vector) - 1
    while min <= max:
        t += 1
        medio = (min + max) // 2
        if vector[medio] > elemento:
            max = medio - 1
        elif vector[medio] < elemento:
            min = medio + 1
        else:
            return medio
    return -1

vector = [1, 2, 3, 4, 5] # El vector debe estar ordenado
elemento = 3
print(busqueda_binaria(vector, elemento))
print ("T(N): ", t)