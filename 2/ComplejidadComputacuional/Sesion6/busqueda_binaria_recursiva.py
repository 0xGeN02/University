import time

def busqueda_binaria_recursiva(lista, elemento, min = 0, max = None):
    if max is None:
        max = len(lista) - 1
    if min > max:
        return None  # Elemento no encontrado
    medio = (min + max) // 2
    if lista[medio] == elemento:
        return medio  # Elemento encontrado
    elif lista[medio] > elemento:
        max = medio - 1
    else:
        min = medio + 1
    return busqueda_binaria_recursiva(lista, elemento, min, max)

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
elemento = 13

print("Algoritmo: búsqueda binaria recursiva")

ini = time.time()
solucion = busqueda_binaria_recursiva(lista, elemento)
fin = time.time()

tiempo = fin-ini
print(solucion)
print(f'{tiempo:.20f}')