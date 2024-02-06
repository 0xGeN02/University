t = 0
def ordenacion_burbuja(vector):
    global t
    n = len(vector)
    for i in range(n-1):
        for j in range(0, n-i-1):
            t += 1
            if vector[j] > vector[j + 1]:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
    return vector

vector = list(range(1000))
vector.reverse()
elemento = 0

print(ordenacion_burbuja(vector))
print ("T(N): ", t)