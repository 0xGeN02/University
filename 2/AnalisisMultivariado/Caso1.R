##Caso1

Velocidad <- Caso1$`Velocidad M/S`
VelocidadCuadrado <- Caso1$VelocidadCuadrado
DistanciaFrenado <- Caso1$DistanciaFrenado
Aceleracion <- Caso1$Aceleracion
# Primero, creamos un dataframe con los datos
datos <- data.frame(
  Velocidad = Velocidad,
  VelocidadCuadrado = VelocidadCuadrado,
  DistanciaFrenado = DistanciaFrenado,
  Aceleracion = Aceleracion
  
)

library(ggplot2)

# Creamos el gráfico de dispersión para Velocidad y Distancia de Frenado
ggplot(datos) +
  geom_point(aes(x=Velocidad,y=DistanciaFrenado)) +
  labs(x="Velocidad", y="Distancia de Frenado")

# Creamos el gráfico de dispersión para Aceleracion y Distancia de Frenado
ggplot(datos) +
  geom_point(aes(x=Aceleracion,y=DistanciaFrenado)) +
  labs(x="Aceleracion", y="Distancia de Frenado")

# Creamos el gráfico de dispersión para Velocidad al Cuadrado y Distancia de Frenado
ggplot(datos) +
  geom_point(aes(x=Velocidad^2, y=DistanciaFrenado)) +
  labs(x="Velocidad al Cuadrado", y="Distancia de Frenado")

# Calculamos la correlación de Pearson para ambas relaciones
correlacion1 <- cor(Velocidad , DistanciaFrenado)
print(paste("La correlación de Pearson entre Velocidad y Distancia de Frenado es:", correlacion1))

correlacion2 <- cor(Velocidad^2 , DistanciaFrenado)
print(paste("La correlación de Pearson entre Velocidad al Cuadrado y Distancia de Frenado es:", correlacion2))

# Grafica correlacion
library(dplyr)
datoscor<-select(Caso1, Velocidad, VelocidadCuadrado, DistanciaFrenado, Aceleracion)
round(cor(datoscor,method="pearson"),3)
library(corrplot)
corrplot(cor(datoscor,method="pearson"),type="lower")

# Estimación del modelo 1

modelo1 <- lm(DistanciaFrenado ~ Velocidad + Aceleracion, data = Caso1)
summary(modelo1)

# Diagnosis del modelo 1

resid1 <- resid(modelo1)
zresid1 <- rstandard(modelo1)
DIstancia_Estimada1 <- fitted(modelo1)
ggplot(data = Caso1, aes(DIstancia_Estimada1, zresid1)) + geom_point() + geom_hline(yintercept = 0) + theme_bw()
lmtest::bptest(modelo1)
car::dwt(modelo1, alternative = "two.sided")
qqnorm(resid1)
qqline(resid1)
shapiro.test(resid1)

# Estimación del modelo 2

modelo2 <- lm(DistanciaFrenado ~ Velocidad +Aceleracion + VelocidadCuadrado, data = Caso1)
summary(modelo2)

# Diagnosis del modelo 2

resid2 <- resid(modelo2)
zresid2 <- rstandard(modelo2)
DIstancia_Estimada2 <- fitted(modelo2)
ggplot(data = Caso1, aes(DIstancia_Estimada2, zresid2)) + geom_point() + geom_hline(yintercept = 0) + theme_bw()
lmtest::bptest(modelo2)
car::dwt(modelo2, alternative = "two.sided")
qqnorm(resid2)
qqline(resid2)
shapiro.test(resid2)



