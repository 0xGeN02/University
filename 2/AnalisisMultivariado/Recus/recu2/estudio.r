#caso bonus

#librerias
library(readxl)
library(corrplot)
library(ggplot2)

#import de datos
bonus <- read_excel("C:/Users/Aleph_0/Downloads/bonus (2).xlsx")
View(bonus)

Bonus <- bonus$Bonus
Rentabilidad <- bonus$Rentabilidad

# Ajustar el modelo de regresión lineal
modelo <- lm(Bonus ~ Rentabilidad, data = bonus)

# Ver el resumen del modelo
summary(modelo)

# Matriz de correlación
correlacion <- cor(bonus)
print(correlacion)

# Gráfica de correlación
correlaciones <- cor(bonus, method="pearson")

# Crear un nuevo archivo de imagen
png(filename = "correlaciones.png")

# Dibujar la gráfica en el archivo
corrplot(correlaciones, type="lower")

# Cerrar el archivo y guardar la gráfica
dev.off()

# Gráfica de dispersión con línea de regresión
g_rentabilidad_bonus <- ggplot(data=bonus, mapping=aes(x=Rentabilidad, y=Bonus)) + geom_point() + geom_smooth(method="lm", se=FALSE)
ggsave(filename = "g_rentabilidad_bonus.png", plot = g_rentabilidad_bonus)

# Calcular el IQR de Bonus
IQR_Bonus <- IQR(bonus$Bonus)

# Calcular Q1 y Q3 de Bonus
Q1_Bonus <- quantile(bonus$Bonus, 0.25)
Q3_Bonus <- quantile(bonus$Bonus, 0.75)

# Identificar los datos atípicos
bonus_atipico <- bonus$Bonus < (Q1_Bonus - 1.5 * IQR_Bonus) | bonus$Bonus > (Q3_Bonus + 1.5 * IQR_Bonus)

# Imprimir los datos atípicos
print(bonus[bonus_atipico, ])