import time

def cambio_voraz(monedas, cantidad):
    solucion = [0] * len(monedas)
    total_actual = 0
    objetivo = cantidad
    encontrada = False
    while cantidad > 0 and not encontrada:
        x = seleccionar(monedas, cantidad)
        if x is not None:
            i = monedas.index(x)
            if es_factible(total_actual, x, objetivo):
                solucion[i] += 1
                total_actual += x
                cantidad -= x
                if es_solucion(total_actual, objetivo):
                    encontrada = True
        else:
            conjunto = [] 
    return solucion

def es_factible(total_actual, moneda, objetivo):
    return total_actual + moneda <= objetivo

def es_solucion(total_actual, objetivo):
    return total_actual == objetivo

def seleccionar(monedas, cantidad):
    for moneda in reversed(monedas):
        if moneda <= cantidad:
            return moneda
    return None

monedas = [1, 2, 5, 10, 20, 50, 100, 200]
cantidad = 63

print("Algoritmo: cambio moneda voraz")

ini = time.time()
solucion = cambio_voraz(monedas, cantidad)
fin = time.time()

tiempo = fin-ini
print(solucion)
print(f'{tiempo:.20f}')