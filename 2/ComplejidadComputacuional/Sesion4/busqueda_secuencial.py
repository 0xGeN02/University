import random
t = 0
def busqueda_secuencial(vector, elemento):
    global t
    for i, e in enumerate(vector):
        t += 1
        if e == elemento:
            return i
    return -1

elemento = 1000
vector = list(range(10000))

random.shuffle(vector)
vector.reverse()

print(vector)
print(busqueda_secuencial(vector, elemento))
print("T(N): ", t)