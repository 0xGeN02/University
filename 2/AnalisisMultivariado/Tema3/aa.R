library(dplyr)
trajes<- select(trajes, Precio, Calidad, Prestigio, Exclusividad, Elegancia, Vanguardia, Complementos)
round(cor(trajes, method = "pearson"), 3)
det(cor(trajes, method = "pearson"))
library(corrplot)
corrplot(cor(trajes, method="pearson"),type = "lower")

#Componenetes Principales
acp<-prcomp(trajes,center=TRUE,scale=TRUE)
acp$x#Componentes principales

#Autovector
acp$rotation

#Autovalores
library(factoextra)
eig_aval <-get_eigenvalue(acp)
eig_aval

fviz_eig(acp, choice = "eigenvalue", addlabels = T, ylim=c(0,6))

# Selección de dos componentes
C2 <- cor(trajes, acp$x[,1:2])
apply(C2*C2, 1, sum) # Comunalidades

C2#cargas factoriales

#Rotacion por varimax

varimax<-varimax(C2,normalize=T)
varimax

cpv<-acp$x[,1:2]%*%varimax$rotmat#componentes rotadas por Varimax
#modelo seleccionado:2 componenentes rotadas por varimax
Premios_indirectos<-cpv[,1]
Premios_directos<-cpv[,2]

ggplot(trajes, aes(x=Premios_indirectos, y=Premios_directos,col=Género,shape=Género))+geom_point(size=3)