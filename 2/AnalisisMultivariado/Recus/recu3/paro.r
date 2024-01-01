#librerias
library(readxl)
library(corrplot)
library(ggplot2)
library(car)
library(lmtest)
library(factoextra)

#import de datos
data_paro <- read_excel("C:/Users/Aleph_0/Downloads/paro.xlsx")
print(data_paro)

Comunidad_Autónoma <- data_paro$Comunidad_Autónoma
Tasa_Paro <- data_paro$Tasa_Paro
Analfabetos <- data_paro$Analfabetos
EducacionSuperior <- data_paro$EducacionSuperior
Gini <- data_paro$Gini
Distribución <- data_paro$Distribución

# Gráfico de dispersión para Analfabetos
g_analfabetos_paro <- ggplot(data_paro, aes(x = Analfabetos, y = Tasa_Paro)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(title = "Tasa de Paro vs Analfabetos")
ggsave(filename = "g_analfabetos_paro.png", plot = g_analfabetos_paro)

# Gráfico de dispersión para EducacionSuperior
g_educacionsuperior_paro <- ggplot(data_paro, aes(x = EducacionSuperior, y = Tasa_Paro)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(title = "Tasa de Paro vs Educacion Superior")
ggsave(filename = "g_educacionsuperior_paro.png", plot = g_educacionsuperior_paro)

# Gráfico de dispersión para Gini
g_gini_paro <- ggplot(data_paro, aes(x = Gini, y = Tasa_Paro)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(title = "Tasa de Paro vs Gini")
ggsave(filename = "g_gini_paro.png", plot = g_gini_paro)

# Gráfico de dispersión para Distribución
g_distribucion_paro <- ggplot(data_paro, aes(x = Distribución, y = Tasa_Paro)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(title = "Tasa de Paro vs Distribución")
ggsave(filename = "g_distribucion_paro.png", plot = g_distribucion_paro)

# Ajustar el modelo de regresión lineal
modelo1 <- lm(Tasa_Paro ~ Analfabetos + EducacionSuperior + Gini + Distribución, data = data_paro)

# Resumir los resultados del modelo
print(summary(modelo1))

# Calcular el VIF
print(vif(modelo1))

# Realizar la prueba de Breusch-Pagan
print(bptest(modelo1))

# Realizar la prueba de Shapiro-Wilk
print(shapiro.test(resid(modelo1)))

# Calcular el estadístico de Durbin-Watson
print(dwtest(modelo1))

#Analisis de componentes principales
data_paro_numeric <- data_paro[sapply(data_paro, is.numeric)]
acp <- prcomp(data_paro_numeric, center=TRUE, scale=TRUE)
eig_val <- get_eigenvalue(acp)
#autovalores
print(eig_val) 
#gráfico de sedimentación
print(fviz_eig(acp, choice="eigenvalue",addlabels = T,ylim=c(0,6))) 

# Ajustar un modelo de regresión con el primer componente principal
modelo_pca1 <- lm(Tasa_Paro ~ acp$x[,1], data = data_paro)

# Ajustar un modelo de regresión con los dos primeros componentes principales
modelo_pca2 <- lm(Tasa_Paro ~ acp$x[,1] + acp$x[,2], data = data_paro)

# Ajustar un modelo de regresión con los tres primeros componentes principales
modelo_pca3 <- lm(Tasa_Paro ~ acp$x[,1] + acp$x[,2] + acp$x[,3], data = data_paro)

# Comparar los modelos
print(summary(modelo_pca1))
print(summary(modelo_pca2))
print(summary(modelo_pca3))

# Obtener las cargas del primer componente principal
cargas_pca1 <- acp$rotation[,1]

# Imprimir las cargas
print(cargas_pca1)

# Crear un gráfico de dispersión con una línea de regresión
plot(data_paro$Tasa_Paro ~ acp$x[,1], xlab = "Factores_Socioeconomicos", ylab = "Tasa de Paro")
abline(lm(data_paro$Tasa_Paro ~ acp$x[,1]), col = "red")

# Agregar un título al gráfico
title("Influencia de los Factores Socioeconómicos en la Tasa de Paro")

#Nuevo mdelo sin el problema
modelo2<- lm(Tasa_Paro ~ acp$x[,1], data = data_paro)
print(summary(modelo2))

# Calcular los residuos del modelo
residuos <- residuals(modelo2)

# Realizar la prueba de Durbin-Watson
dwtest <- car::durbinWatsonTest(residuos)

print(dwtest)

# Generar un gráfico QQ de los residuos
qqnorm(residuos)
qqline(residuos, col = "red")