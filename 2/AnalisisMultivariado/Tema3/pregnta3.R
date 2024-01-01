##Ejercicio3

Tamaño <- pisos$Tamaño
Precio <- pisos$Precio

ggplot(data=pisos, mapping=aes(x=Tamaño, y=Precio)) + geom_point()

# Gráfico de correlación  (paquete corrplot)

round(cor(pisos, method = "pearson"), 3)
corrplot(cor(pisos, method = "pearson"), type = "lower")

#Modelo1

# Para hacer una regresión por pasos se utilizan las 5 órdenes anteriores y vemos cuales nos quedan 
# en la orden both$coefficients. Estas las meteremos en el nuevo modelo tal que:

modelo1 <- lm(Precio~Tamaño, data = pisos)
summary(modelo1)


# Análisis de la validez del modelo:

resid_1 <- resid(modelo1)           # e = y - y' -> Unidades de medida
zresid_1 <- rstandard(modelo1)      # Residuos estadrizados -> z = (e - media)/desviación
precioEstimado <- fitted(modelo1)    # Representa la recta estimada reultante de sustituir los valores dados en el enunciado en el modelo
ggplot(data = pisos, aes(precioEstimado, zresid_1)) + geom_point() + geom_hline(yintercept = 0) + theme_bw()
# Activar paquete lmtest
bptest(modelo1)                     # H0 = Homocedaticidad H1: Heterocedasticidad
dwtest(modelo1)                     # H0 = No autorrelación (independecia linear) H1: autocorrelación (dependecia linear)
shapiro.test(resid_1)               # H0 = Normalidad H1 = No normalidad
qqnorm(resid_1)                     # Representación de los residuos en una gráfica. Si es una linea son normales
qqline(resid_1)                     # Recta que representa la normalidad de los datos 

# Detección de valores atípicos (outliers)
dummy <- which(abs(zresid_1) > 2)  # Usamos zresid_1 para identificar los valores atípicos

# Visualización de los valores atípicos en el gráfico de dispersión
ggplot(data = pisos, aes(x = Tamaño, y = Precio)) +
  geom_point() +
  geom_point(data = pisos[dummy, ], aes(x = Tamaño, y = Precio), color = "red", size = 3) +
  theme_bw()

# Lista de índices de los valores atípicos
dummy


#Crear una variable dummy:
pisos$dummy <- ifelse(rownames(pisos) %in% dummy, 1, 0)

# Incluir la variable dummy en el modelo de regresión:
modelo_con_dummy <- lm(Precio ~ Tamaño + dummy, data = pisos)

#Ver el resumen de los resultados:
summary(modelo_con_dummy)
