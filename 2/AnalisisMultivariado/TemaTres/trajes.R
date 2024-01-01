#Correlaciones
datoscomp<- select(trajes, Precio, Calidad, Prestigio, Exclusividad, Elegancia, Vanguardia, Complementos)
round(cor(datoscomp, method = "pearson"),3)
det(cor(datoscomp, method="pearson"))
corrplot(cor(datoscomp, method="pearson"), type = "lower")

#Componentes Principales
acp<-prcomp (datoscomp,center=TRUE, scale=TRUE)
acp$x #Componetes principales 

#Autovectores 
acp$rotation

eig_val<- get_eigenvalue(acp)
eig_val # Autovalores 

#Gráfica de sedimentación
fviz_eig(acp, choice = "eigenvalue", addlabels = T, ylim=c(0,6))

#Selección de dos componentes
C2 <- cor(datoscomp, acp$x[,1:2])
apply(C2*C2, 1, sum) # Comunalidades

C2 # Cargas factoriales

#Rotación varimax
varimax<- varimax (C2, normalize = T)
varimax

#Selección de tres componentes
C3 <- cor(datoscomp, acp$x[,1:3])
apply(C3*C3, 1, sum) # Comunalidades

C3 # Cargas factoriales

#Rotación varimax
varimax2<- varimax (C3, normalize = T)
varimax2

#Gráficas
CP1 <- acp$x[,1]
CP2 <- acp$x[,2]
CP3 <- acp$x[,3]

ggplot(trajes, aes(x=CP1, y=CP2, label=Marca)) + geom_text()
ggplot(trajes, aes(x=CP1, y=CP3, label=Marca)) + geom_text()
ggplot(trajes, aes(x=CP2, y=CP3, label=Marca)) + geom_text()