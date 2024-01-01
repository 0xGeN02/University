# Establecer una semilla para hacer los resultados reproducibles
set.seed(634)

# Crear un dataset ficticio
num_observaciones <- 50

# Variables
metros_cuadrados <- rnorm(num_observaciones, mean = 120, sd = 60)
random_term_habitaciones <- sample(1:3, num_observaciones, replace = TRUE)
num_habitaciones <- round(1 + metros_cuadrados/50 + random_term_habitaciones)
random_term_banos <- sample(0:1, num_observaciones, replace = TRUE)
num_banos <- pmax(1, floor(num_habitaciones / 2) + round(runif(num_observaciones, min = 0, max = 1)))
ano_construccion <- sample(1900:2022, num_observaciones, replace = TRUE)+num_banos
decadas_antes <- floor((2023 - ano_construccion) / 10)
distancia_centro_ciudad <- pmax(1, 10 - decadas_antes + rnorm(num_observaciones, mean = 0, sd = 2))+ num_banos
precio_vivienda <- 150000 + 7000 * num_habitaciones + 5000 * metros_cuadrados + 3000 * num_banos + 1500 * (2022 - ano_construccion) - 2000 * distancia_centro_ciudad

# Crear el dataframe
datos <- data.frame(
  MetrosCuadrados = metros_cuadrados,
  NumHabitaciones = num_habitaciones,
  NumBanos = num_banos,
  AnoConstruccion = ano_construccion,
  DistanciaCentroCiudad = distancia_centro_ciudad,
  Precio = precio_vivienda
)

# Visualizar las primeras filas del dataset
head(datos)

library(ggplot2)

ggplot(data=datos,
       mapping=aes(x=MetrosCuadrados, y=Precio)) +geom_point()
ggplot(data=datos,
       mapping=aes(x=NumHabitaciones, y=Precio)) +geom_point()
ggplot(data=datos,
       mapping=aes(x=NumBanos, y=Precio)) +geom_point()
ggplot(data=datos,
       mapping=aes(x=AnoConstruccion, y=Precio)) +geom_point()
ggplot(data=datos,
       mapping=aes(x=DistanciaCentroCiudad, y=Precio)) +geom_point()

round(cor(datos, method = "pearson"),3)
det(cor(datos, method = "pearson"))
library(corrplot)
corrplot(cor(datos, method = "pearson"), type = "lower")

modelo1 <- lm(Precio ~ MetrosCuadrados + NumHabitaciones + NumBanos + AnoConstruccion + DistanciaCentroCiudad, data=datos)
summary(modelo1)

library(carData)
library(car)
vif(modelo1)
Tolerancia <- 1/vif(modelo1)
Tolerancia

library(dplyr)
datoscomp <- select(datos, MetrosCuadrados, NumHabitaciones, NumBanos, AnoConstruccion, DistanciaCentroCiudad)
round(cor(datoscomp, method = "pearson"),3)
det(cor(datoscomp, method = "pearson"), 3)

acp <- prcomp(datoscomp, center=TRUE,scale=TRUE)
library(factoextra)
eig_val <- get_eigenvalue(acp)
eig_val #Autovalores

fviz_eig(acp, choice="eigenvalue",addlabels=T,ylim=c(0,3)) #Grafico sedimentacion

#3 Componentes
C3 <- cor(datoscomp, acp$x[,1:3])
apply(C3*C3, 1, sum)
C3

# Rotación
varimax <- varimax(C3,normalize=T)
varimax
C3V <- acp$x[,1:3]%*%varimax$rotmat # componentes rotadas varimax

# Grafico de componentes
C3
Dimension <- C3V[,1]
ObraNueva <- C3V[,2]
Comodidad <- C3V[,3]

ggplot(data=datos,
       mapping=aes(x=Dimension, y=Precio)) +geom_point()
ggplot(data=datos,
       mapping = aes(x=ObraNueva, y=Precio)) +geom_point()
ggplot(data=datos,
       mapping=aes(x=Comodidad, y=Precio)) +geom_point()


#Modleo2
modelo2<- lm(Precio~Dimension+Comodidad+ObraNueva, data=datos)
summary(modelo2)
vif(modelo2) # evitar si hay multicolinealidad

resid2 <- resid(modelo2)
zresid2 <-rstandard(modelo2)
datos_estimados2 <- fitted(modelo2)
ggplot(datos, aes(datos_estimados2,zresid2)) + geom_point() + geom_hline(yintercept = 0)

library(lmtest)
bptest(modelo2) #heterocelasticidad >0.05
dwtest(modelo2)
qqnorm(resid2)
qqline(resid2)
shapiro.test(resid2) #Normalidad
