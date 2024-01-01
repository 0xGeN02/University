#IMPORTAR LIBRERIA:
library(readxl)
name <- read_excel("C:/Users/Aleph_0/Downloads/name.xls")
View(name)


#CASO PROMOCIONES
#correlaciones
library(dplyr)
datoscomp <- select(promociones, Mayor_cantidad, Vale_descuento, Descuento_precio, Sorteo_regalo, Regalo_por_puntos, Obsequio, Concurso)
round(cor(datoscomp, method="pearson"),3)
det(cor(datoscomp, method="pearson"))
library(corrplot)
corrplot(cor(datoscomp, method="pearson"), type="lower")
#componentes principales
acp <- prcomp(datoscomp, center=TRUE, scale=TRUE)
library(factoextra)
eig_val <- get_eigenvalue(acp)
eig_val #autovalores
fviz_eig(acp, choice="eigenvalue",addlabels = T,ylim=c(0,6)) #gráfico de sedimentación
#selección de dos componentes
C2 <- cor(datoscomp, acp$x[,1:2])
apply(C2*C2, 1, sum) #comunalidades
C2 #cargos factoriales
#rotación por varimax
varimax <- varimax(C2, normalize = T)
varimax
cpv <- acp$x[,1:2]%*%varimax$rotmat #componentes rotadas por varimax
#modelo seleccionado: 2 componentes rotadas por varimax
premios_indirectos <- cpv[,1]
premios_directos <- cpv[,2]
ggplot(promociones, aes(x=premios_indirectos, y=premios_directos, col=Género, shape=Género)) + geom_point(size=3)




#CASO KLEINGOLDBERGER
ggplot(KleinGoldberger, aes(x=Salarios_no_agrícolas, y=Consumo)) + geom_point()
ggplot(KleinGoldberger, aes(x=Otros_ingresos, y=Consumo)) + geom_point()
ggplot(KleinGoldberger, aes(x=Salarios_agrícolas, y=Consumo)) + geom_point()
round(cor(KleinGoldberger, method="pearson"),3)
library(corrplot)
corrplot(cor(KleinGoldberger, method="pearson"),type="lower")
#estimación del modelo 1
modelo1 <- lm(Consumo~Salarios_no_agrícolas+Otros_ingresos+Salarios_agrícolas, data=KleinGoldberger)
summary(modelo1)
#diagnosisis de multicolinealidad
library(carData)
library(car)
vif(modelo1)
Tolerancia <- 1/vif(modelo1)
Tolerancia
library(dplyr)
datoscomp <- select(KleinGoldberger,Salarios_no_agrícolas,Otros_ingresos,Salarios_agrícolas)
round(cor(datoscomp,method="pearson"),3)
det(cor(datoscomp,method="pearson"))
acp <- prcomp(datoscomp,center=TRUE,scale=TRUE)
library(factoextra)
eig_val <- get_eigenvalue(acp)
eig_val #autovalores
fviz_eig(acp, choice="eigenvalue",addlabels=T,ylim=c(0,3)) #gráfico de sedimentación
#selección de una componente
C1 <- cor(datoscomp,acp$x[,1:1])
apply(C1*C1,1,sum) #comunalidades
C1 #cargas factoriales
#selección de dos componentes
C2 <- cor(datoscomp, acp$x[,1:2])
apply(C2*C2,1,sum) #comunalidades
C2 #cargas factoriales
#rotación por varimax
varimax <- varimax(C2, normalize = T)
varimax
#modelo seleccionado: 2 componentes
C2 #cargas factoriales
cpv <- acp$x[,1:2]%*%varimax$rotmat
ingresos_directos <- cpv[,1]
ingresos_indirectos <- cpv[,2]
#gráficos de dispersión
ggplot(data=KleinGoldberger, aes(x=ingresos_directos, y=Consumo)) + geom_point()
ggplot(data=KleinGoldberger, aes(x=ingresos_indirectos, y=Consumo)) + geom_point()
#estimacion del modelo utilizando componentes principales
modelo2 <- lm(Consumo~ingresos_directos+ingresos_indirectos, data=KleinGoldberger)
summary(modelo2)
#diagnosis modelo2
resid2 <- resid(modelo2)
zresid2 <- rstandard(modelo2)
ingresos_estimados2 <- fitted(modelo2)
ggplot(KleinGoldberger,aes(ingresos_estimados2,zresid2)) + geom_point() + geom_hline(yintercept = 0)
library(lmtest)
bptest(modelo2)
dwtest(modelo2)
qqnorm(resid2)
qqline(resid2)
shapiro.test(resid2)




#CASO COCHES
correlaciones
library(dplyr)
datoscomp <- select(coches, Mecánica, Estabilidad, Habitabilidad, Comodidad, Equipamiento, Prestaciones, Consumo)
round(cor(datoscomp, method="pearson"),3)
#det = determinante
det(cor(datoscomp, method="pearson"))
library(corrplot)
corrplot(cor(datoscomp, method="pearson"), type="lower")
#componentes principales
acp <- prcomp(datoscomp, center=TRUE, scale=TRUE)
acp$x #componentes principales
acp$rotation #autovectores
library(factoextra)
eig_val <- get_eigenvalue(acp)
eig_val #autovalores
#selección de tres componentes
c3 <- cor(datoscomp, acp$x[,1:3])
apply(c3*c3, 1, sum) #comunalidades
c3 #cargas factoriales
#rotación varimáx
varimax <- varimax(c3, normalize = T)
varimax
#modelo seleccionado: 3 componentes sin rotación
c3 #cargas factoriales
CP1 <- acp$x[,1]
CP2 <- acp$x[,2]
CP3 <- acp$x[,3]
ggplot(coches, aes(x=CP1, y=CP2, label=Modelo)) + geom_text()
ggplot(coches, aes(x=CP1, y=CP3, label=Modelo)) + geom_text()


#CASO BENEFICIOS
ggplot(beneficios, aes(x=Activo, y=Beneficios)) + geom_point()
ggplot(beneficios, aes(x=Empleados, y=Beneficios)) + geom_point()
ggplot(beneficios, aes(x=Ventas, y=Beneficios)) + geom_point()
round(cor(beneficios, method="pearson"),3)
library(corrplot)
corrplot(cor(beneficios, method="pearson"),type="lower")
#estimación del modelo 1
modelo1 <- lm(Beneficios~Activo+Empleados+Ventas, data=beneficios)
summary(modelo1)
#diagnosisis de multicolinealidad
library(carData)
library(car)
vif(modelo1)
Tolerancia <- 1/vif(modelo1)
Tolerancia
library(dplyr)
datoscomp <- select(beneficios, Activo, Empleados, Ventas)
round(cor(datoscomp,method="pearson"),3)
det(cor(datoscomp,method="pearson"))
acp <- prcomp(datoscomp,center=TRUE,scale=TRUE)
library(factoextra)
eig_val <- get_eigenvalue(acp)
eig_val #autovalores
fviz_eig(acp, choice="eigenvalue",addlabels=T,ylim=c(0,3)) #gráfico de sedimentación
#selección de una componente
C1 <- cor(datoscomp,acp$x[,1:1])
apply(C1*C1,1,sum) #comunalidades
C1 #cargas factoriales
#selección de dos componentes
C2 <- cor(datoscomp, acp$x[,1:2])
apply(C2*C2,1,sum) #comunalidades
C2 #cargas factoriales
#rotación por varimax
varimax <- varimax(C2, normalize = T)
varimax
#modelo seleccionado: 1 componente
C1 #cargas factoriales
Tamaño <- acp$x[,1]
#gráficos de dispersión
ggplot(data=beneficios, mapping=aes(x=Tamaño, y=Beneficios)) + geom_point()
#estimacion del modelo utilizando componentes principales
modelo2 <- lm(Beneficios~Tamaño, data=beneficios)
summary(modelo2)
#diagnosis modelo2
resid2 <- resid(modelo2)
zresid2 <- rstandard(modelo2)
Beneficios_estimados2 <- fitted(modelo2)
ggplot(beneficios,aes(Beneficios_estimados2,zresid2)) + geom_point() + geom_hline(yintercept = 0)
library(lmtest)
bptest(modelo2)
dwtest(modelo2)
qqnorm(resid2)
qqline(resid2)
shapiro.test(resid2)




#CASO TRAJES
library(dplyr)
datoscomp <- select(trajes, Precio, Calidad, Prestigio, Exclusividad, Elegancia, Vanguardia, Complementos)
round(cor(datoscomp, method="pearson"),3)
det(cor(datoscomp, method="pearson"))
library(corrplot)
corrplot(cor(datoscomp, method="pearson"), type="lower")
#componentes principales
acp <- prcomp(datoscomp, center=TRUE, scale=TRUE)
library(factoextra)
eig_val <- get_eigenvalue(acp)
eig_val #autovalores
fviz_eig(acp, choice="eigenvalue",addlabels = T,ylim=c(0,6)) #gráfico de sedimentación
#selección de dos componentes
C2 <- cor(datoscomp, acp$x[,1:2])
apply(C2*C2, 1, sum) #comunalidades
C2 #cargos factoriales
#rotación por varimax
varimax <- varimax(C2, normalize = T)
varimax
acp <- prcomp(datoscomp, center=TRUE, scale=TRUE)
#selección de tres componentes
C3 <- cor(datoscomp, acp$x[,1:3])
apply(C3*C3, 1, sum) #comunalidades
C3 #cargos factoriales
valoracion_global <- acp$x[,1]*(-1)
elegancia_versus_vanguardia <- acp$x[,2]
valoracion_precio <- acp$x[,3]
library(ggplot2)
ggplot(trajes, aes(x=valoracion_global,y=elegancia_versus_vanguardia,label=Marca)) + geom_text()
ggplot(trajes, aes(x=valoracion_global,y=valoracion_precio,label=Marca)) + geom_text()

#clúster:análisis jerárquico
datoscluster <- data.frame(valoracion_global,elegancia_versus_vanguardia,valoracion_precio)
row.names(datoscluster) <- trajes$Marca

mat_dist <- dist(x=datoscluster,method="euclidean") #distancia euclídea
hc_euclidea_complete <- hclust(d=mat_dist,method="complete")
plot(as.dendrogram(hc_euclidea_complete),main="Método de la distancia euclídea")

hc_euclidea_complete$merge
hc_euclidea_complete$height
rect.hclust(hc_euclidea_complete,k=3)

hc_euclidea_complete <- hclust(d=mat_dist,method="average")
plot(as.dendrogram(hc_euclidea_complete),main="Método de la media(inter-grupo")

hc_euclidea_ward.D2 <- hclust(d=mat_dist,method="ward.D2")
plot(as.dendrogram(hc_euclidea_ward.D2),main="Método de Ward")

#kmeans
library(factoextra)
fviz_nbclust(x=datoscluster,FUNcluster = kmeans,method="wss",k.max=15,
             diss=get_dist(datoscluster, method="euclidean"),nstart=50)

kmc3 <- kmeans(x=datoscluster,centers=3,nstart=50)
kmc3
fviz_cluster(kmc3,data=datoscluster,ellipse.type = "convex")+theme_classic()

kmc4 <- kmeans(x=datoscluster,centers=4,nstart=50)
kmc4
fviz_cluster(kmc4,data=datoscluster,ellipse.type = "convex")+theme_classic()

kmc5 <- kmeans(x=datoscluster,centers=5,nstart=50)
kmc5
fviz_cluster(kmc5,data=datoscluster,ellipse.type = "convex")+theme_classic()




#CASO PAÍSES
library(dplyr)
datoscomp <- select(países, Densidad, PIB, Gini, Índice)
round(cor(datoscomp, method="pearson"),3)
det(cor(datoscomp, method="pearson"))
library(corrplot)
corrplot(cor(datoscomp, method="pearson"), type="lower")
#componentes principales
acp <- prcomp(datoscomp, center=TRUE, scale=TRUE)
library(factoextra)
eig_val <- get_eigenvalue(acp)
eig_val #autovalores
fviz_eig(acp, choice="eigenvalue",addlabels = T,ylim=c(0,6)) #gráfico de sedimentación
#selección de dos componentes
C2 <- cor(datoscomp, acp$x[,1:2])
apply(C2*C2, 1, sum) #comunalidades
C2 #cargos factoriales
#rotación por varimax
varimax <- varimax(C2, normalize = T)
varimax
CV2 <- acp$x[,1:2]%*%varimax$rotmat
View(CV2)

desarrollo <- CV2[,1]
poblacion <- CV2[,2]
ggplot(países, aes(x=desarrollo,y=poblacion,label =País)) + geom_text()
#clúster:análisis jerárquico
datoscluster <- data.frame(desarrollo,poblacion)
row.names(datoscluster) <- países$País

#Con el método se efectúa la agrupación en base a la distancia máxima entre los puntos
mat_dist <- dist(x=datoscluster,method="euclidean") #distancia euclídea
hc_euclidea_complete <- hclust(d=mat_dist,method="complete")
plot(as.dendrogram(hc_euclidea_complete),main="Método de la distancia euclídea")

hc_euclidea_complete$merge
hc_euclidea_complete$height
rect.hclust(hc_euclidea_complete,k=4)

#distancia media de todos los objetos de un grupo contra todos los objetos de otro grupo
hc_euclidea_complete <- hclust(d=mat_dist,method="average")
plot(as.dendrogram(hc_euclidea_complete),main="Método de la media(inter-grupo)")

#con este método los grupos se hacen en base a la distancia mínima entre los puntos, método de Ward
hc_euclidea_ward.D2 <- hclust(d=mat_dist,method="ward.D2")
plot(as.dendrogram(hc_euclidea_ward.D2),main="Método de Ward")

#La conclusión del nº de clusters llega de la mano de los dendrogramas, porque con el
#gráfico del nº óptimo de clusters, se observa una caída significativa hasta k = 3.
#Por tanto, si solo se usase el gráfico del número óptimo de clusters,
#se podría llegar a la conclusión errónea de realizar únicamente 3 grupos

#kmeans
library(factoextra)
fviz_nbclust(x=datoscluster,FUNcluster = kmeans,method="wss",k.max=8,
             diss=get_dist(datoscluster, method="euclidean"),nstart=50)

kmc3 <- kmeans(x=datoscluster,centers=3,nstart=50)
kmc3
fviz_cluster(kmc3,data=datoscluster,ellipse.type = "convex")+theme_classic()

kmc4 <- kmeans(x=datoscluster,centers=4,nstart=50)
kmc4
fviz_cluster(kmc4,data=datoscluster,ellipse.type = "convex")+theme_classic()

kmc5 <- kmeans(x=datoscluster,centers=5,nstart=50)
kmc5
fviz_cluster(kmc5,data=datoscluster,ellipse.type = "convex")+theme_classic()


#CASO COCHES U3
library(dplyr)
datoscomp <- select(coches, Mecánica, Estabilidad, Habitabilidad, Comodidad, Equipamiento, Prestaciones, Consumo)
round(cor(datoscomp, method="pearson"),3)
#det = determinante
det(cor(datoscomp, method="pearson"))
library(corrplot)
corrplot(cor(datoscomp, method="pearson"), type="lower")
#componentes principales
acp <- prcomp(datoscomp, center=TRUE, scale=TRUE)
acp$x #componentes principales
acp$rotation #autovectores
library(factoextra)
eig_val <- get_eigenvalue(acp)
eig_val #autovalores
#selección de tres componentes
c3 <- cor(datoscomp, acp$x[,1:3])
apply(c3*c3, 1, sum) #comunalidades
c3 #cargas factoriales
comfort_versus_funcionamiento <- acp$x[,1]
equipacion_y_estabilidad <- acp$x[,2]
consumo <- acp$x[,3]
library(ggplot2)
ggplot(coches, aes(x=comfort_versus_funcionamiento,y=equipacion_y_estabilidad,label=Modelo)) + geom_text()
ggplot(coches, aes(x=comfort_versus_funcionamiento,y=consumo,label=Modelo)) + geom_text()

#clúster:análisis jerárquico
datoscluster <- data.frame(comfort_versus_funcionamiento,equipacion_y_estabilidad,consumo)
row.names(datoscluster) <- coches$Marca

mat_dist <- dist(x=datoscluster,method="euclidean") #distancia euclídea
hc_euclidea_complete <- hclust(d=mat_dist,method="complete")
plot(as.dendrogram(hc_euclidea_complete),main="Método de la distancia euclídea")

hc_euclidea_complete$merge
hc_euclidea_complete$height
rect.hclust(hc_euclidea_complete,k=3)

hc_euclidea_complete <- hclust(d=mat_dist,method="average")
plot(as.dendrogram(hc_euclidea_complete),main="Método de la media(inter-grupo")

hc_euclidea_ward.D2 <- hclust(d=mat_dist,method="ward.D2")
plot(as.dendrogram(hc_euclidea_ward.D2),main="Método de Ward")

#kmeans
library(factoextra)
fviz_nbclust(x=datoscluster,FUNcluster = kmeans,method="wss",k.max=15,
             diss=get_dist(datoscluster, method="euclidean"),nstart=50)

kmc3 <- kmeans(x=datoscluster,centers=3,nstart=50)
kmc3
fviz_cluster(kmc3,data=datoscluster,ellipse.type = "convex") + theme_classic()

kmc4 <- kmeans(x=datoscluster,centers=4,nstart=50)
kmc4
fviz_cluster(kmc4,data=datoscluster,ellipse.type = "convex")+theme_classic()

kmc5 <- kmeans(x=datoscluster,centers=5,nstart=50)
kmc5
fviz_cluster(kmc5,data=datoscluster,ellipse.type = "convex")+theme_classic()



#CASO 05: BALONCESTO
library(ggplot2)
ggplot(baloncesto, aes(x=Altura, y=Puntos)) + geom_point()
ggplot(baloncesto, aes(x=Minutos, y=Puntos)) + geom_point()
ggplot(baloncesto, aes(x=Balones_perdidos, y=Puntos)) + geom_point()
ggplot(baloncesto, aes(x=Faltas, y=Puntos)) + geom_point()
#se puede observar un comportamiento similar entre ellas, pero con un poco más de dispersión
#en el caso de la altura y las faltas (1º indicio de multicolinealidad).

#estimación del modelo 1
modelo1 <- lm(Puntos~Altura + Minutos + Balones_perdidos + Faltas, data=baloncesto)
summary(modelo1)
#resultados t-test sin sentido = 3º indicio multicolinealidad

library(corrplot)
corrplot(cor(baloncesto, method="pearson"),type="lower")
library(dplyr)
datoscomp <- select(baloncesto,Altura,Minutos,Balones_perdidos,Faltas)
round(cor(datoscomp,method="pearson"),3)
det(cor(datoscomp,method="pearson"))
#matriz correlaciones muestra que la variable dependiente está relacionada linealmente con las cuatro
#variables independientes, pero también, muestra una fuerte relación entre las independientes (2º indicio)


#ANOVA indica que los coeficientes son difertentes de cero, pero los t- test indican que solo dos
# son distintos de cero =  contradicción entre contraste conjunto e individual (4º indicio)
#diagnosisis de multicolinealidad
library(carData)
library(car)
vif(modelo1)
Tolerancia <- 1/vif(modelo1)
Tolerancia
#valores del FIV  elevados y  tolerancias bajas (5º indicio)

#autovalores indican la varianza explicada por componentes principales. Si solo 1ª CP, que autovalor mayor que 1, trabajamos con el %
acp <- prcomp(datoscomp,center=TRUE,scale=TRUE)
library(factoextra)
eig_val <- get_eigenvalue(acp)
eig_val #autovalores

fviz_eig(acp, choice="eigenvalue",addlabels=T,ylim=c(0,3)) #gráfico de sedimentación

#selección de una componente
C1 <- cor(datoscomp,acp$x[,1:1])
apply(C1*C1,1,sum) #comunalidades
C1 #cargas factoriales
#las cargas factoriales cuando se trabaja con una componente, muestra que todas las variables entran con fuerza 

#selección de dos componentes
C2 <- cor(datoscomp, acp$x[,1:2])
apply(C2*C2,1,sum) #comunalidades
C2 #cargas factoriales
#rotación por varimax
varimax <- varimax(C2, normalize = T)
varimax
#rotación varimax mantiene ortogonalidad de las componentes, pero trata de que las cargas se acerquen más a cero o a uno.

cpv <- acp$x[,1:2]%*%varimax$rotmat
condicion_fisica <- cpv[,1]
resumen_jugador <- cpv[,2]

#pasamos de tener 4 independientes relacionadas a dos independientes que contienen el 83,47% de las 4 independientes iniciales y que no tienen problema de multicolinealidad.
#gráficos de dispersión
ggplot(data=baloncesto, aes(x=condicion_fisica, y=Puntos)) + geom_point()
ggplot(data=baloncesto, aes(x=resumen_jugador, y=Puntos)) + geom_point()

#estimacion del modelo utilizando componentes principales
modelo2 <- lm(Puntos~condicion_fisica + resumen_jugador, data=baloncesto)
summary(modelo2)

#diagnosis modelo2
resid2 <- resid(modelo2)
zresid2 <- rstandard(modelo2)
juego_estimado <- fitted(modelo2)
ggplot(baloncesto,aes(juego_estimado,zresid2)) + geom_point() + geom_hline(yintercept = 0)
library(lmtest)
bptest(modelo2)
dwtest(modelo2)
qqnorm(resid2)
qqline(resid2)
shapiro.test(resid2)