##Ejercicio1 

Sueño <- sueño$Sueño
Trabajo <- sueño$Trabajo
Sueldo <- sueño$Sueldo
Ordenador <- sueño$Ordenador

# Cargar la librería necesaria
library(ggplot2)

# Crear los gráficos
ggplot(sueño, aes(x=Trabajo, y=Sueño)) +
  geom_point() +
  labs(title="Horas de sueño vs. Horas de trabajo",
       x="Horas de trabajo",
       y="Horas de sueño")

ggplot(sueño, aes(x=Ordenador, y=Sueño)) +
  geom_boxplot() +
  labs(title="Horas de sueño vs. Ordenador en casa",
       x="Ordenador en casa",
       y="Horas de sueño")

ggplot(sueño, aes(x=Sueldo, y=Sueño)) +
  geom_point() +
  labs(title="Horas de sueño vs. Sueldo",
       x="Sueldo",
       y="Horas de sueño")

# Cargar la librería necesaria
library(corrplot)

# Calcular la matriz de correlación
correlaciones <- cor(sueño[, c("Sueño", "Trabajo", "Sueldo")])

# Crear el gráfico de correlación de Pearson
corrplot(correlaciones, method="circle")


# Cargar la librería necesaria
library(lmtest)

# Estimar el modelo
modelo <- lm(Sueño ~ Ordenador, data=sueño)

# Mostrar el resumen del modelo
summary(modelo)

# Realizar un contraste de hipótesis para ver si el coeficiente de Ordenador es significativamente distinto de cero
coeftest(modelo)

