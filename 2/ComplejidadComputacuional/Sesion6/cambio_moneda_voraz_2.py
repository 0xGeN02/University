import time

def cambio_voraz(monedas, cambio):
    solucion = [0] * len(monedas)
    while cambio > 0:
        x = seleccionar(monedas, cambio)
        solucion[monedas.index(x)] += 1
        cambio -= x
    return solucion

def seleccionar(monedas, cambio):
    for moneda in reversed(monedas):
        if moneda <= cambio:
            return moneda

monedas = [1, 2, 5, 10, 20, 50, 100, 200]
cantidad = 63

print("Algoritmo: cambio moneda voraz 2")

ini = time.time()
solucion = cambio_voraz(monedas, cantidad)
fin = time.time()

tiempo = fin-ini
print(solucion)
print(f'{tiempo:.20f}')