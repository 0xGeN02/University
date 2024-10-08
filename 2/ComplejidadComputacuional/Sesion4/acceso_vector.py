t = 0
def acceso_vector(vector, indice):
    global t
    n = len(vector)
    t += 1
    if indice >= 0 and indice <= n-1:
        return vector[indice]
    else:
        return -1

vector = [1, 2, 3, 4, 5]
indice = 3
print(acceso_vector(vector, indice))
print("T(N): ", t)