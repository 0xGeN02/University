import sympy as sp
import numpy as np

x = sp.symbols('x', real = True)
f_exp = sp.sin(x)
f = sp.Lambda(x, f_exp)
#f_exp = sp.exp(-x**2)

a = 0
b = np.pi
trozos = 5000

x_aprox =  np.linspace(a,b, trozos+1)
print(x_aprox)

I_aprox = 0
 
for k in range(1, trozos + 1):
    I_aprox = I_aprox + f(x_aprox[k] - x_aprox[k-1])*f((x_aprox[k] + x_aprox[k-1])/2)


print('Una aproximacion del area de la curva y = sen(x) entre 0 y pi es A = ',I_aprox)
