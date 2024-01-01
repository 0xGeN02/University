# Correlaciones
library(dplyr)
datoscomp<- select(trajes, Precio, Calidad, Prestigio, Exclusividad, Elegancia, Vanguardia, Complementos)
round(cor(datoscomp, method = "pearson"),3)
det(cor(datoscomp, method="pearson"))
library(corrplot)
corrplot(cor(datoscomp, method="pearson"), type = "lower")

# Componentes Principales
acp<-prcomp (datoscomp,center=TRUE, scale=TRUE)
acp$x # Componetes principales 

acp$rotation #Autovectores 

library(factoextra)
eig_val<- get_eigenvalue(acp)
eig_val # Autovalores 

# Gráfica de sedimentación
fviz_eig(acp, choice = "eigenvalue", addlabels = T, ylim=c(0,6))

# Selección de dos componentes
C2 <- cor(datoscomp, acp$x[,1:2])
apply(C2*C2, 1, sum) # Comunalidades

C2 # Cargas factoriales

# Rotación varimax
varimax<- varimax (C2, normalize = T)
varimax

# Selección de tres componentes
C3 <- cor(datoscomp, acp$x[,1:3])
apply(C3*C3, 1, sum) # Comunalidades

C3 # Cargas factoriales

# Rotación varimax
varimax2<- varimax (C3, normalize = T)
varimax2

# Modelo seleccionado: 3 componentes sin rotación
C3 # Cargas factoriales

Valoración_global<- acp$x[,1]*(-1)
Elegancia_versus_Vanguardia<- acp$x[,2]
Valoración_precio<- acp$x[,3]

ggplot(trajes, aes(x=CP1, y=CP2, label=Marca)) + geom_text()
ggplot(trajes, aes(x=CP1, y=CP3, label=Marca)) + geom_text()

#Cluster:analisis jerargico
datoscluster<-data.frame(Valoración_global,Elegancia_versus_Vanguardia,Valoración_precio)
row.names(datoscluster)<-trajes$Marca
mat_dist<-dist(x=datoscluster,method="euclidean")#Distancias euclideas
hc_euclidea_complete<-hclust(d=mat_dist,method = "complete")
plot(as.dendrogram(hc_euclidea_complete),main="Metodo de la distancia maxima")
hc_euclidea_complete$merge
hc_euclidea_complete$height
rect.hclust(hc_euclidea_complete, k=4)
hc_euclidea_average<- hclust(d=mat_dist, method = "average")
plot(as.dendrogram(hc_euclidea_average), main = "Método de la media (inter-grupo)")
hc_euclidea_ward.D2<-hclust(d=mat_dist, method = "ward.D2")
plot(as.dendrogram(hc_euclidea_ward.D2), main = "Método de ward")
#Kmeans
library(factoextra)
fviz_nbclust(x=datoscluster,FUNcluster=kmeans,method = "wss",k.max = 15,diss=get_dist(datoscluster,method = "euclidean"),nstart=50)

kmc3 <- kmeans(x=datoscluster, center=3,nstart=50)
kmc3
fviz_cluster(kmc3,data=datoscluster,ellipse.type = "convex")+theme_classic()

kmc4 <- kmeans(x=datoscluster, center=4,nstart=50)
kmc4
fviz_cluster(kmc4,data=datoscluster,ellipse.type = "convex")+theme_classic()