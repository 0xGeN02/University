#Correlaciones
library(dplyr)

library(corrplot)
países <- select(países, Densidad, PIB, Gini, Índice)
round(cor(países, method = "pearson"),3)
det(cor(países, method = "pearson"))
corrplot(cor(países, method = "pearson"), type = "lower")

library(factoextra)
#Componentes principales
acp <- prcomp (países, center=TRUE, scale=TRUE)
acp$x #Componentes principales
acp$rotation #Autovectores
eig_val <- get_eigenvalue(acp)
eig_val #Autovalores

#Selección de tres componentes
C2 <- cor(países, acp$x[,1:2])
apply(C2*C2, 1, sum) #Comunalidades
C2 #Cargas factoriales

#Rotación por Varimax
varimax <- varimax(C2, normalize = T)
varimax
C2V <- acp$x[,1:2]%*%varimax$rotmat #Componentes rotadas por varimax

#Modelo seleccionado: 2 componentes rotadas
C2V #Cargas factoriales rotadas
Densidad2 <- C2V[,1]
Economía <- C2V[,2]
ggplot(países, aes(x=Densidad2, y=Economía, label=País)) + geom_text()

#Cluster:analisis jerárquico
datoscluster<-data.frame(Densidad2,Economía)
row.names(datoscluster)<-países$País
mat_dist<-dist(x=datoscluster,method="euclidean") #Distancias euclideas
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
fviz_nbclust(x=datoscluster,FUNcluster=kmeans,method = "wss",k.max = 8,diss=get_dist(datoscluster,method = "euclidean"),nstart=50)

#Kmc2
kmc2 <- kmeans(x=datoscluster, center=2,nstart=50)
kmc2
fviz_cluster(kmc2,data=datoscluster,ellipse.type = "convex")+theme_classic()

#Kmc3
kmc3 <- kmeans(x=datoscluster, center=3,nstart=50)
kmc3
fviz_cluster(kmc3,data=datoscluster,ellipse.type = "convex")+theme_classic()

#Kmc4
kmc4 <- kmeans(x=datoscluster, center=4,nstart=50)
kmc4
fviz_cluster(kmc4,data=datoscluster,ellipse.type = "convex")+theme_classic()

#Kmc5
kmc5 <- kmeans(x=datoscluster, center=5,nstart=50)
kmc5
fviz_cluster(kmc5,data=datoscluster,ellipse.type = "convex")+theme_classic()