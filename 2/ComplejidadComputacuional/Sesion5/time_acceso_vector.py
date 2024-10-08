import time

t = 0
def acceso_vector(vector, indice):
    global t
    n = len(vector)
    t += 1
    if indice >= 0 and indice <= n-1:
        return vector[indice]
    else:
        return -1

vector = [1, 2, 3, 4, 5, 6, 7, 8]
indice = 8


inicio = time.time()
r = acceso_vector(vector, indice)
fin = time.time()

print(fin - inicio)
print(r)
print(acceso_vector(vector, indice))
print("T(N): ", t)