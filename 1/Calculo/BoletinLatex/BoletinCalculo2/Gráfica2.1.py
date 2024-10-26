import numpy as np
import matplotlib.pyplot as plt

# Función f(x)
def f(x):
    return 2 + 1/x

# Polinomio de Taylor P2,1,f(x)
def P(x):
    return 0.5 * (x**2 - 2*x + 4)

# Intervalo de representación
a, b = -2, 3

# Puntos para la representación de f(x)
x = np.linspace(a, b, 100)
y = f(x)

# Puntos para la representación de P2,1,f(x)
x_p = np.linspace(a, b, 100)
y_p = P(x_p)

# Representación gráfica
plt.plot(x, y, label='f(x)')
plt.plot(x_p, y_p, label='P2,1,f(x)')
plt.legend()
plt.show()
