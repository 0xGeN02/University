import numpy as np
import sympy as sp

x = sp.symbols('x', real=True) #Definir variable
f_expr = x-sp.cos(x) #Definimos la expresion de f(x)
f  = sp.Lambda(x,f_expr)

a = 0.1
b = 1.
ext_izq = a # Extremo izquierdo del intervalo inicial
ext_der = b# Extremos derecho del intervalo inicial
N_max = 35 # Número máximo de iteraciones
tol = 1.e-10 # Tolerancia: diferencia relativa entre aproximaciones que consideramos aceptable

x_aprox = np.zeros(N_max)

for k in range(0,N_max):
    x_aprox[k] = (a+b) / 2

    if f(x_aprox[k]) == 0: break
      
    if f(a) * f(x_aprox[k]) < 0:
        b = x_aprox[k]
    else:
       a = x_aprox[k]

    if ( (k > 0) and (np.abs(x_aprox[k]-x_aprox[k-1]) / np.abs(x_aprox[k]) < tol) ): break

print('MÉTODO DE DICOTOMÍA PARA LA FUNCIÓN F(x)= ',f_expr)
print('Número de iteraciones realizadas: ', k+1) # Empezamos a contar en 0
print('Aproximación de la raíz: ', x_aprox[k])
print('Cota del error cometido: ', (ext_der-ext_izq)/2**k)
print('Valor de la función en la aproximación de la raíz', f(x_aprox[k]))