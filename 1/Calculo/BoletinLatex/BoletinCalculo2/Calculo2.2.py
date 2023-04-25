import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

x = sp.Symbol('x', real=True)

# Función a integrar
f_exp = sp.exp(x)/(sp.exp(2*x)+1) + sp.exp(-x)
f = sp.lambdify(x, f_exp)

# Límites de integración
a = 0
b = 1

# Tolerancia deseada
tol = 0.01

# Aproximación por punto medio con tolerancia
I_aprox = 0
n = 1
while True:
    h = (b - a) / n
    I_aprox_prev = I_aprox
    I_aprox = 0
    for i in range(n):
        x_i = a + h/2 + i*h
        I_aprox += f(x_i)*h
    if abs(I_aprox - I_aprox_prev) < tol:
        break
    n *= 2

print('Valor aproximado de I mediante la fórmula del punto medio con una tolerancia de', tol, '= ', I_aprox)