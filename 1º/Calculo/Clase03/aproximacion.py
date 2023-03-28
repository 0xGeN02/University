import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


#Definir la función f(x)
x = sp.symbols('x')
f_expr = x
f = sp.lambdify(x, f_expr)


sumandos = 50
pol_trig_expr = 0

coefs_sin = np.zeros(sumandos+1)

for k in range(1,sumandos+1):
    coefs_sin[k] = sp.integrate(f_expr*sp.sin(k*x), (x,-sp.pi,sp.pi))/sp.pi 
    pol_trig_expr = pol_trig_expr + coefs_sin[k] * sp.sin(k*x)

print(coefs_sin)
print(pol_trig_expr)
pol_trig_expr = sp.lambdify(x, pol_trig_expr)


#Gráfica
x_ap = np.arange(-np.pi, np.pi, 0.01)
plt.plot(x_ap, f(x_ap), x_ap, pol_trig_expr(x_ap), 'r')
plt.show()