library(dplyr)
datoscomp<- select(coches, Mecánica, Estabilidad, Habitabilidad, Comodidad, Equipamiento, Prestaciones, Consumo)
round(cor(datoscomp, method = "pearson"), 3)
det(cor(datoscomp, method = "pearson"))
library(corrplot)
corrplot(cor(datoscomp, method="pearson"),type = "lower")

#Componenetes Principales
acp<-prcomp(datoscomp,center=TRUE,scale=TRUE)
acp$x#Componentes principales

#Autovector
acp$rotation

#Autovalor
library(factoextra)
eig_aval <-get_eigenvalue(acp)
eig_aval

#Comunalidad
C3<-cor(datoscomp,acp$x[,1:3])
apply(C3*C3,1,sum)
C3

CP1 <- acp$x[,1]
CP2 <- acp$x[,2]
CP3 <- acp$x[,3]

ggplot(coches, aes(x=CP1, y=CP2, label=Modelo)) + geom_text()
ggplot(coches, aes(x=CP1, y=CP3, label=Modelo)) + geom_text()