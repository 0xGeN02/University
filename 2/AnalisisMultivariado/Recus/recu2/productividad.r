#productividad

#librerias
library(readxl)
library(corrplot)
library(ggplot2)

#import de datos
data_productividad <- read_excel("C:/Users/Aleph_0/Downloads/productividad.xlsx")
View(data_productividad)

Productividad <- data_productividad$Productividad
Región <- data_productividad$Región
Sueldo <- data_productividad$Sueldo
Antigüedad <- data_productividad$Antigüedad

# Gráfico de correlación
corrplot(cor(data_productividad[,sapply(data_productividad, is.numeric)], method="pearson"), type="lower")

# Grafico dispersion por region

# Gráfico de dispersión de Productividad vs Sueldo para cada Región
g_productividad_sueldo <- ggplot(data_productividad, aes(x=Sueldo, y=Productividad, color=Región)) +
    geom_point() +
    facet_wrap(~Región) +
    labs(title="Productividad vs Sueldo por Región", x="Sueldo", y="Productividad")
ggsave(filename = "g_productividad_sueldo_region.png", plot = g_productividad_sueldo)

# Gráfico de dispersión de Productividad vs Antigüedad para cada Región
g_productividad_antiguedad <- ggplot(data_productividad, aes(x=Antigüedad, y=Productividad, color=Región)) +
    geom_point() +
    facet_wrap(~Región) +
    labs(title="Productividad vs Antigüedad por Región", x="Antigüedad", y="Productividad")
ggsave(filename = "g_productividad_antiguedad_region.png", plot = g_productividad_antiguedad)

#modelo de regresion lineal
modelo1 <- lm(Productividad ~ Sueldo + Antigüedad, data = data_productividad)
print(summary(modelo1))

#modelo de regresion lineal por region(filiales)
# Convertir la región en una variable categórica
data_productividad$Región <- as.factor(data_productividad$Región)

# Ajustar un modelo de regresión lineal que incluya la región
modelo2 <- lm(Productividad ~ Sueldo + Antigüedad + Región, data = data_productividad)

# Ver el resumen del modelo
summary(modelo2)

# Realizar una prueba ANOVA en el modelo
anova(modelo2)

# Calcular los residuos del modelo
residuos <- residuals(modelo2)

# Crear un gráfico de residuos
plot(residuos, main="Gráfico de Residuos", ylab="Residuos", xlab="Índice")

# Realizar una prueba de autocorrelación en los residuos
# Instalar y cargar el paquete 'lmtest' si aún no está instalado
# install.packages('lmtest')
library(lmtest)
test_autocorrelacion <- dwtest(modelo2)
print(test_autocorrelacion)