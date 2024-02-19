import time

def cambio_recursivo(monedas, cantidad, i=0):
    if cantidad == 0:
        return [0] * len(monedas)  # No se necesita ninguna moneda.
    if i >= len(monedas):
        return None  # No es posible hacer el cambio con las monedas disponibles.
    
    mejor_solucion = None
    max = cantidad // monedas[i]
    for num_monedas in range(max + 1):
        nueva_cantidad = cantidad - num_monedas * monedas[i]
        if nueva_cantidad >= 0:
            solucion_parcial = cambio_recursivo(monedas, nueva_cantidad, i + 1)
            if solucion_parcial is not None:
                solucion_parcial[i] = num_monedas
                if mejor_solucion is None or sum(solucion_parcial) < sum(mejor_solucion):
                    mejor_solucion = solucion_parcial
    
    return mejor_solucion

monedas = [1, 2, 5, 10, 20, 50, 100, 200]
cantidad = 63

print("Algoritmo: cambio moneda recursivo")

ini = time.time()
solucion = cambio_recursivo(monedas, cantidad)
fin = time.time()

tiempo = fin-ini
print(solucion)
print(f'{tiempo:.20f}')