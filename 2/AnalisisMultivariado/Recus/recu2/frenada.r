#caso frenada

#librerias
library(readxl)
library(corrplot)
library(ggplot2)

#import de datos
data_frenada <- read_excel("C:/Users/Aleph_0/Downloads/frenada.xlsx")
View(data_frenada)

Velocidad <- data_frenada$Velocidad
Distancia <- data_frenada$Distancia

# Crear el modelo de regresión lineal
modelo_frenada <- lm(Distancia ~ Velocidad, data = data_frenada)

# Imprimir el resumen del modelo
print(summary(modelo_frenada))

# Gráfico de dispersión con línea de regresión
g_velocidad_distancia <- ggplot(data=data_frenada, mapping=aes(x=Velocidad, y=Distancia)) + geom_point() + geom_smooth(method="lm", se=FALSE)
ggsave(filename = "g_velocidad_distancia.png", plot = g_velocidad_distancia)

#grafico de correlacion
corrplot(cor(data_frenada[,sapply(data_frenada, is.numeric)], method="pearson"), type="lower")

# Cargar el paquete necesario
library(car)


# Cargar el paquete necesario
library(ggplot2)

# Gráfico de dispersión para verificar la linealidad
ggplot(data_frenada, aes(x = Velocidad, y = Distancia)) +
  geom_point() +
  geom_smooth(method = lm)

# Gráfico de residuos vs valores ajustados para verificar la homocedasticidad
ggplot(data_frenada, aes(x = modelo_frenada$fitted.values, y = modelo_frenada$residuals)) +
  geom_point() +
  geom_hline(yintercept = 0, color = "red")
ggsave(filename = "residuos_ajustados.png", plot = g_velocidad_distancia)
# Histograma de los residuos para verificar la normalidad
ggplot(data_frenada, aes(x = modelo_frenada$residuals)) +
  geom_histogram(binwidth = 1)
ggsave(filename = "histograma_residuos.png", plot = g_velocidad_distancia)
# También puedes usar una gráfica Q-Q para verificar la normalidad
qqnorm(modelo_frenada$residuals)

# Transformar la variable dependiente
data_frenada$Distancia_log = log(data_frenada$Distancia)

# Crear el nuevo modelo de regresión lineal
modelo_frenada_log = lm(Distancia_log ~ Velocidad, data = data_frenada)

# Imprimir el resumen del nuevo modelo
print(summary(modelo_frenada_log))