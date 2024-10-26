def f(x):
    return x**5 - 5*x + 1

def bisection_method(a, b, tol):
    if f(a)*f(b) >= 0:
        print("Error: La función no cambia de signo en el intervalo dado")
        return None
    else:
        while (b-a)/2 > tol:
            c = (a+b)/2
            if f(c) == 0:
                return c
            elif f(c)*f(a) < 0:
                b = c
            else:
                a = c
        return (a+b)/2


sol = bisection_method(1, 2, 1e-8)
print("La solución de la ecuación es:", sol)