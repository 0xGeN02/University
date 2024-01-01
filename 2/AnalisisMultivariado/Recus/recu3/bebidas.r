#librerias
library(readxl)
library(corrplot)
library(ggplot2)
library(car)
library(lmtest)
library(factoextra)

#import de datos
data_bebidas <- read_excel("C:/Users/Aleph_0/Downloads/bebidas.xlsx")
print(data_bebidas)

# Selecciona solo las columnas numéricas (consumo de bebidas)
datos_bebidas_num <- data_bebidas[, -1]

# Calcula las componentes principales
pca_bebidas <- prcomp(datos_bebidas_num, scale = TRUE)

# Imprime un resumen de los resultados
print(summary(pca_bebidas))

# Visualiza las componentes principales
print(fviz_eig(pca_bebidas))

# Obtiene las cargas de las componentes principales
cargas_pca <- pca_bebidas$rotation
print(cargas_pca)

# Calcula las componentes principales rotadas por varimax
pca_rot <- pca_bebidas$x[,1:3] %*% varimax(pca_bebidas$rotation[,1:3])$rotmat

# Asigna nombres a las componentes principales
colnames(pca_rot) <- c("Bebidas_Alcohólicas", "Vino", "Agua")

# Asigna las componentes a nuevas variables
Bebidas_Alcohólicas <- pca_rot[, "Bebidas_Alcohólicas"]
Vino <- pca_rot[, "Vino"]
Agua <- pca_rot[, "Agua"]

# Clúster: análisis jerárquico
datoscluster <- data.frame(Bebidas_Alcohólicas, Vino, Agua)
row.names(datoscluster) <- data_bebidas$Países

# Con el método se efectúa la agrupación en base a la distancia máxima entre los puntos
mat_dist <- dist(x=datoscluster, method="euclidean") # distancia euclídea
hc_euclidea_complete <- hclust(d=mat_dist, method="complete")
plot(as.dendrogram(hc_euclidea_complete), main="Método de la distancia euclídea")

hc_euclidea_complete$merge
hc_euclidea_complete$height
rect.hclust(hc_euclidea_complete, k=4)

# Distancia media de todos los objetos de un grupo contra todos los objetos de otro grupo
hc_euclidea_complete <- hclust(d=mat_dist, method="average")
plot(as.dendrogram(hc_euclidea_complete), main="Método de la media (inter-grupo)")

# Con este método los grupos se hacen en base a la distancia mínima entre los puntos, método de Ward
hc_euclidea_ward.D2 <- hclust(d=mat_dist, method="ward.D2")
plot(as.dendrogram(hc_euclidea_ward.D2), main="Método de Ward")

# kmeans
library(factoextra)
fviz_nbclust(x=datoscluster, FUNcluster = kmeans, method="wss", k.max=8,
             diss=get_dist(datoscluster, method="euclidean"), nstart=50)

kmc3 <- kmeans(x=datoscluster, centers=3, nstart=50)
kmc3
fviz_cluster(kmc3, data=datoscluster, ellipse.type = "convex") + theme_classic()

kmc4 <- kmeans(x=datoscluster, centers=4, nstart=50)
kmc4
fviz_cluster(kmc4, data=datoscluster, ellipse.type = "convex") + theme_classic()

kmc5 <- kmeans(x=datoscluster, centers=5, nstart=50)
kmc5
fviz_cluster(kmc5, data=datoscluster, ellipse.type = "convex") + theme_classic()