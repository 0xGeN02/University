import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def Simpson(a,b,fa,fpm,fb):
    aprox_S = (b-a) /6 * (fa + 4*fpm + fb)
    return aprox_S

a = 0
b = np.pi
pm = (a+b)/2
fa = np.sin(a)
fb = np.sin(b)
fpm = np.sin(pm)
aproximacion_Simpson = Simpson(a,b,fa,fpm,fb)
print('Valor aproximado de la integral por Simpson = ', aproximacion_Simpson)

X = np.array([a,(a+b)/2,b]) 
Y = np.sin(X)
print('Valor aproximado de I mediante la fórmula de Simpson = ', integrate.simpson(Y, X))

def pmc(a, b, f, n):
    h = float((b-a)/n)
    valor = 0
    for i in range(n):
        valor += f((a + h/2.0) + i*h)
    valor *= h
    return valor    

a = 0
b = np.pi
f = np.sin
n = 100
aprox_pmc = pmc(a,b,f,n)
print('Valor aproximado por punto medio compuesto = ',aprox_pmc)

