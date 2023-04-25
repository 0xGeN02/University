import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

x = sp.Symbol('x', real = True)

#Aproximación por punto medio
a = 0
b = np.pi
pm = (a+b)/2

f_exp = sp.sin(x)
f = sp.lambdify(x,f_exp)

fpm = f(pm)
I_aprox = (b-a) * fpm
print('Valor aproximado de I mediante la fórmula del punto medio = ', I_aprox)

def trapecio(a,b,fa,fb):
    aprox_tr = (b-a) * (fa + fb)/2
    return aprox_tr
x = sp.Symbol('x', real = True)

a = 0
b = np.pi
pm = (a+b)/2

f_exp = sp.sin(x)
f = sp.lambdify(x,f_exp)

fa = f(a)
fb = f(b)
aproximacion_trapecio = trapecio(a,b,fa,fb)
print('Valor aproximado de la integral por trapecio simple = ', aproximacion_trapecio)

X = np.array([a,b])
Y = np.sin(X)
print('Valor aproximado de I mediante la fórmula del trapecio = ', np.trapz(Y,X))