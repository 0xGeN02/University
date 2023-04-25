import sympy as sp
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
x= sp.symbols('x') 
f_expr=x
f=sp.lambdify(x,f_expr)

x_ap=np.arange(-np.pi, np.pi,0.01)
fig=plt.plot(x_ap,f(x_ap))
plt.plot(x_ap,f(x_ap))
plt.show()