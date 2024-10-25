import math

def f(x):
    return math.exp(-x) * math.sin(4 * math.pi * x)

a = 0
b = 1
n = 100
h = (b - a) / n

sumatoria = 0
for i in range(1, n + 1):
    xi = a + i * h
    xm = (a + (i - 1) * h + xi) / 2
    sumatoria += f(xm)

area = h * sumatoria
print(area)
