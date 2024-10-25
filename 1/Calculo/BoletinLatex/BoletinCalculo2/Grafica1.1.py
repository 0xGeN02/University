from matplotlib import pyplot
# Función
def f(x):
    return x**5 -5*x +1

# Valores del eje X que toma el gráfico.
x = range(-5, 5)
# Graficar funcion.
pyplot.plot(x, [f(i) for i in x])

# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(-10, 10)
pyplot.ylim(-10, 10)
# Guardar gráfico como imágen PNG.
pyplot.savefig("output.png")
# Mostrarlo.
pyplot.show()

