def f(x):
    return x**5 - 5*x + 1

def df(x):
    return 5*x**4 - 5

def newton_raphson(x0, tol):
    xn = x0
    while abs(f(xn)) > tol:
        xn = xn - f(xn)/df(xn)
    return xn

solucion = newton_raphson(1.4, 1e-8)
print(solucion)
