import sympy as sp
from IPython.display import display
#Var Indep
t = sp.Symbol ('t')

#Var Dep
x = sp.Function('x')

#Escribinos EDO
eq= sp.Eq(x(t).diff(t), 2*t)

#Sol general
s_general = sp.dsolve(eq)
display(s_general)

#Sol particular
s_particular = sp.dsolve ( eq,ics={x(0):1})
display(s_particular)
