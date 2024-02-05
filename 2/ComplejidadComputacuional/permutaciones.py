t = 0
def permutar(vector):
    global t
    t += 1
    if len(vector) > 1:
        permutaciones = []
        for i in range(0, len(vector)):
            for permutacion in permutar(vector[:i] + vector[i + 1:]):
                permutacion.insert(0,vector[i])
                permutaciones.append(permutacion)
        return permutaciones
    else:
        return [vector]

vector = [1,2,3,4,5]
permutaciones = permutar(vector)
for permutacion in permutaciones:
    print(permutacion)
print("T(N): ", t)

