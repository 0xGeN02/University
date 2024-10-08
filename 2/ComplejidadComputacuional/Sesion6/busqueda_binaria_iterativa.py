import time

def busqueda_binaria_iterativa(lista, elemento):
    min = 0
    max = len(lista) - 1
    while min <= max:
        medio = (min + max) // 2
        if lista[medio] == elemento:
            return medio  # Elemento encontrado
        if lista[medio] > elemento:
            max = medio - 1
        else:
            min = medio + 1
    return None  # Elemento no encontrado

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
elemento = 13

print("Algoritmo: búsqueda binaria iterativa")

ini = time.time()
solucion = busqueda_binaria_iterativa(lista, elemento)
fin = time.time()

tiempo = fin-ini
print(solucion)
print(f'{tiempo:.20f}')