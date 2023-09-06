# Crea una tabla de datos con tus valores editados
datos <- data.frame(
  Autonomía = c(
    "Cantabria", "Castilla y León", "Castilla - La Mancha", "Cataluña",
    "Comunitat Valenciana", "Extremadura", "Galicia", "Comunidad de Madrid",
    "Región de Murcia", "Comunidad Foral deNavarra", "País Vasco", "La Rioja",
    "Andalucía", "Aragón", "Principado de Asturias", "Illes Balears",
    "Canarias", "Cantabria", "Castilla y León", "Castilla - La Mancha",
    "Cataluña", "Comunitat Valenciana", "Extremadura", "Galicia", "Comunidad de Madrid",
    "Región de Murcia", "Comunidad Foral deNavarra", "País Vasco", "La Rioja"
  ),
  Precio = c(
    128.109, 133.728, 130.011, 153.446, 135.769, 133.709, 136.273, 152.477,
    142.847, 124.117, 140.758, 140.242, 123.310, 123.266, 117.392, 143.408,
    124.877, 123.838, 116.874, 108.262, 140.490, 119.815, 106.888, 116.769,
    145.718, 117.235, 113.979, 120.384, 119.168
  ),
  Tipo = c(
    "Nueva", "Nueva", "Nueva", "Nueva", "Nueva", "Nueva", "Nueva", "Nueva",
    "Nueva", "Nueva", "Nueva", "Nueva", "Segunda mano", "Segunda mano", "Segunda mano",
    "Segunda mano", "Segunda mano", "Segunda mano", "Segunda mano", "Segunda mano",
    "Segunda mano", "Segunda mano", "Segunda mano", "Segunda mano", "Segunda mano",
    "Segunda mano", "Segunda mano", "Segunda mano", "Segunda mano"
  ),
  Cliente = c(
    "Cliente A", "Cliente B", "Cliente C", "Cliente D", "Cliente E",
    "Cliente F", "Cliente G", "Cliente H", "Cliente I", "Cliente J",
    "Cliente K", "Cliente L", "Cliente M", "Cliente N", "Cliente O",
    "Cliente P", "Cliente Q", "Cliente R", "Cliente S", "Cliente T",
    "Cliente U", "Cliente V", "Cliente W", "Cliente X", "Cliente Y",
    "Cliente Z", "Cliente AA", "Cliente BB", "Cliente CC"
  )
)

# Utiliza la función summary() para obtener un resumen estadístico de la columna "Precio"
resumen_precio <- summary(datos$Precio)
print(resumen_precio)

# Calcula y muestra el valor mínimo de la columna "Precio" en datos_excel
min_precio <- min(datos$Precio)
print(paste("Mínimo de Precio:", min_precio))

# Calcula y muestra el valor máximo de la columna "Precio" en datos_excel
max_precio <- max(datos$Precio)
print(paste("Máximo de Precio:", max_precio))

# Calcula y muestra el rango de la columna "Precio" en datos_excel
rango_precio <- range(datos$Precio)
print(paste("Rango de Precio:", rango_precio[1], " - ", rango_precio[2]))

# Calcula y muestra la media aritmética de la columna "Precio" en datos_excel
media_precio <- mean(datos$Precio)
print(paste("Media de Precio:", media_precio))

# Calcula y muestra la mediana de la columna "Precio" en datos_excel
mediana_precio <- median(datos$Precio)
print(paste("Mediana de Precio:", mediana_precio))

# Calcula y muestra la longitud de la columna "Precio" en datos_excel
longitud_precio <- length(datos$Precio)
print(paste("Longitud de Precio:", longitud_precio))

# Calcula y muestra la desviación estándar de la columna "Precio" en datos_excel
desviacion_precio <- sd(datos$Precio)
print(paste("Desviación Estándar de Precio:", desviacion_precio))

# Calcula y muestra la varianza de la columna "Precio" en datos_excel
varianza_precio <- var(datos$Precio)
print(paste("Varianza de Precio:", varianza_precio))

# Calcula y muestra el primer cuartil (percentil 25) de la columna "Precio" en datos_excel
cuartil_25 <- quantile(datos$Precio, 0.25)
print(paste("Cuartil 25 de Precio:", cuartil_25))

# Calcula y muestra el tercer cuartil (percentil 75) de la columna "Precio" en datos_excel
cuartil_75 <- quantile(datos$Precio, 0.75)
print(paste("Cuartil 75 de Precio:", cuartil_75))

# Calcula y muestra el rango intercuartil (IQR) de la columna "Precio" en datos_excel
iqr_precio <- IQR(datos$Precio)
print(paste("Rango Intercuartil (IQR) de Precio:", iqr_precio))

# Calcula el coeficiente de variación (CV) de la columna "Precio" en datos_excel
cv_precio <- desviacion_precio / media_precio
print(paste("Coeficiente de Variación (CV) de Precio:", cv_precio))

# Tabla de frecuencias de la columna "Cliente"
table_cliente <- table(datos$Cliente)
print("Tabla de frecuencias de la columna Cliente:")
print(table_cliente)

# Gráfico de barras de la columna "Cliente"
barplot(table_cliente, main="Frecuencia de Clientes", xlab="Cliente", ylab="Frecuencia")

# Histograma de la columna "Precio"
hist(datos$Precio, main="Histograma de Precios", xlab="Precio", ylab="Frecuencia")

# Diagrama de tallo y hojas (stem-and-leaf plot) de la columna "Precio"
stem(datos$Precio)

# Diagrama de caja (boxplot) de la columna "Precio"
boxplot(datos$Precio, main="Diagrama de Caja de Precios", ylab="Precio")

# Instala y carga la librería ggplot2 si aún no está instalada
if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}
library(ggplot2)