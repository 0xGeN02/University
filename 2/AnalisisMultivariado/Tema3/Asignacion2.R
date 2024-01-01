#Caso 2: Pescado

# Gráfico de dispersión para Inversiones vs Capturas
plot(pescas_sur$Inversiones, pescas_sur$Capturas, main="Inversiones vs Capturas", xlab="Inversiones", ylab="Capturas")

# Gráfico de dispersión para Temperatura vs Capturas
plot(pescas_sur$Temperatura, pescas_sur$Capturas, main="Temperatura vs Capturas", xlab="Temperatura", ylab="Capturas")

# Gráfico de dispersión para Horas vs Capturas
plot(pescas_sur$Horas, pescas_sur$Capturas, main="Horas vs Capturas", xlab="Horas", ylab="Capturas")

# Gráfico de dispersión para Mes vs Capturas
plot(pescas_sur$Mes, pescas_sur$Capturas, main="Mes vs Capturas", xlab="Mes", ylab="Capturas")


# Cargar la biblioteca
library(corrplot)

# Calcular la matriz de correlación
correlaciones <- cor(pescas_sur, method="pearson")

# Redondear los valores
correlaciones_redondeadas <- round(correlaciones, 3)

# Imprimir las correlaciones redondeadas
print(correlaciones_redondeadas)

# Crear el gráfico de correlación
corrplot(correlaciones_redondeadas, type="lower")

# Ajustar modelos de regresión lineal
modelo_inversiones <- lm(Capturas ~ Inversiones, data = pescas_sur)
modelo_temperatura <- lm(Capturas ~ Temperatura, data = pescas_sur)
modelo_horas <- lm(Capturas ~ Horas, data = pescas_sur)
modelo_mes <- lm(Capturas ~ Mes, data = pescas_sur)

# Realizar pruebas de hipótesis para los coeficientes beta
summary(modelo_inversiones)
summary(modelo_temperatura)
summary(modelo_horas)
summary(modelo_mes)

# Crear un nuevo dataframe con los valores medios de las variables
valores_medios <- data.frame(Inversiones = mean(pescas_sur$Inversiones, na.rm = TRUE),
                             Horas = mean(pescas_sur$Horas, na.rm = TRUE),
                             Mes = mean(pescas_sur$Mes, na.rm = TRUE))

# Calcular las capturas estimadas
capturas_estimadas <- 1.0821 * valores_medios$Inversiones + 0.5747 * valores_medios$Horas + 1.5129 * valores_medios$Mes

# Imprimir las capturas estimadas
print(capturas_estimadas)
