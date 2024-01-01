##Ejercicio 2

Precio <- cordero$Precio
Ventas <- cordero$Ventas

# Cargamos la librería necesaria
library(lmtest)

# Creamos el modelo lineal
modelo <- lm(Ventas ~ Precio, data = cordero)

# Resumen del modelo
summary(modelo)

# Verificamos la normalidad de los residuos
shapiro.test(resid(modelo))

# Verificamos la homocedasticidad
bptest(modelo)

# Verificamos la autocorrelación
dwtest(modelo)
