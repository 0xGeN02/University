library(ggplot2)

ggplot(data=baloncesto,
       mapping=aes(x=Altura, y=Puntos)) +geom_point()
ggplot(data=baloncesto,
       mapping=aes(x=Minutos, y=Puntos)) +geom_point()
ggplot(data=baloncesto,
       mapping=aes(x=Balones_perdidos, y=Puntos))+geom_point()
ggplot(data=baloncesto,
       mapping=aes(x=Faltas, y=Puntos))+geom_point()


round(cor(baloncesto, method = "pearson"),3)
library(corrplot)
corrplot(cor(baloncesto, method = "pearson"), type = "lower")

modelo1 <- lm(Puntos ~ Altura + Minutos + Balones_perdidos + Faltas, data=baloncesto)
summary(modelo1)

library(carData)
library(car)
vif(modelo1)
Tolerancia <- 1/vif(modelo1)
Tolerancia

library(dplyr)
datoscomp <- select(baloncesto, Altura, Minutos, Balones_perdidos, Faltas)
round(cor(datoscomp, method = "pearson"),3)
det(cor(datoscomp, method = "pearson"), 3)

acp <- prcomp(datoscomp, center=TRUE,scale=TRUE)
library(factoextra)
eig_val <- get_eigenvalue(acp)
eig_val #Autovalores

fviz_eig(acp, choice="eigenvalue",addlabels=T,ylim=c(0,3)) #Grafico sedimentacion

#Selececion 1 componente
C1 <- cor(datoscomp, acp$x[,1:1])
apply(C1*C1, 1, sum) # Comunalidades -> % de informacion de las variables empleada. NO PUEDEN SER INFERIORES A 0.5
C1 # Cargas factoriales -> Correlacion entre componentes y variables. NO VALORES INTERMEDIOS. CERCA DE 0 NO INFLUYE. CERCA DE 1 INFLUYE MAS 
#2 Componentes
C2 <- cor(datoscomp, acp$x[,1:2])
apply(C2*C2, 1, sum)
C2

# Rotación
varimax <- varimax(C2,normalize=T)
varimax
C2V <- acp$x[,1:2]%*%varimax$rotmat # componentes rotadas varimax

#Modelo seleccionado: 2 
C2
Rendimiento_fisico <- C2V[,1]
Estrategia_juego <- C2V[,2]

ggplot(data=baloncesto,
       mapping=aes(x=Rendimiento_fisico, y=Puntos)) +geom_point()
ggplot(data=baloncesto,
       mapping=aes(x=Estrategia_juego, y=Puntos)) +geom_point()

#Modleo2
modelo2<- lm(Puntos~Rendimiento_fisico+Estrategia_juego, data=baloncesto)
summary(modelo2)
vif(modelo2) # evitar si hay multicolinealidad

resid2 <- resid(modelo2)
zresid2 <-rstandard(modelo2)
baloncesto_estimados2 <- fitted(modelo2)
ggplot(baloncesto, aes(baloncesto_estimados2,zresid2)) + geom_point() + geom_hline(yintercept = 0)

library(lmtest)
bptest(modelo2) #heterocelasticidad >0.05
dwtest(modelo2)
qqnorm(resid2)
qqline(resid2)
shapiro.test(resid2) #Normalidad

