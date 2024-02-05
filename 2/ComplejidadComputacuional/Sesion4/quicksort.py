t = 0
def quicksort(vector):
    global t
    t += 1
    if len(vector) <= 1:
        return vector
    else:
        pivot = vector[0]
        left = [x for x in vector[1:] if x < pivot]
        right = [x for x in vector[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

vector = [5, 4, 3, 2, 1]

print("Resultado: ", quicksort(vector))
print("T(N): ", t)