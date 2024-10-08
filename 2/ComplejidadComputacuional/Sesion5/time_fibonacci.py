import time

t = 0
f = []
def fibonacci(n):
    global t
    t += 1
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 50
for i in range(n):
    f.append(fibonacci(i))

print(f)
inicio = time.time()
r = fibonacci(n)
fin = time.time()

print(fin - inicio)
print ("T(N): ", t)

