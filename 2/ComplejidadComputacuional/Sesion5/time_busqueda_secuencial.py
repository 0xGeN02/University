import random
import time
t = 0
def busqueda_secuencial(vector, elemento):
    global t
    for i, e in enumerate(vector):
        t += 1
        if e == elemento:
            return i
    return -1

elemento = 56457432
vector = list(range(100000000))

random.shuffle(vector)
vector.reverse()

inicio = time.time()
r = busqueda_secuencial(vector, elemento)
fin = time.time()

print(fin - inicio)
print(r)

print("T(N): ", t)