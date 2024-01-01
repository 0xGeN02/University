##Ejercicios

# 1. Tamaño del fichero
filesize<-file.info("airbnb2023.csv")$size
paste(filesize, "bytes")
# 2. Dimensión del fichero importado
print(dim(data))

# 3. Variables en el fichero
print(names(data))

# 4. Eliminar NA y comprobar la dimensión
data_no_na <- na.omit(data)
print(dim(data_no_na))

# 5. Resumen numérico de todas las variables
print(summary(data))

# 6. Exploración de variables continuas y categóricas
# Media y cuantil 95 de la variable "price"
mean_price <- mean(data$price, na.rm = TRUE)
quantile_price <- quantile(data$price, probs = 0.95, na.rm = TRUE)
print(mean_price)
print(quantile_price)
# Frecuencia absoluta y relativa de "room_type"
freq_abs_room_type <- table(data$room_type)
freq_rel_room_type <- prop.table(table(data$room_type))
print(freq_abs_room_type)
paste0(freq_rel_room_type*100, "%")
# 7. Exploración de la relación entre algunas variables
# Pisos ordenados por precio y número de revisiones
data_ordered_price <- data[order(data$price), ]
data_ordered_reviews <- data[order(data$number_of_reviews), ]
print(data_ordered_price)
print(data_ordered_reviews)

# Número de barrios diferentes en "Ciutat Vella"
num_neighbourhoods_ciutat_vella <- length(unique(data[data$neighbourhood_group == "Ciutat Vella", ]$neighbourhood))
paste(" La cantidad de barrios en Ciutat Vella es" , num_neighbourhoods_ciutat_vella)

# Precio medio para cada "neighbourhood_group"
mean_price_neighbourhood_group <- tapply(data$price, data$neighbourhood_group, mean, na.rm = TRUE)
paste("Precio medio por vecindario es", mean_price_neighbourhood_group)

# Precio medio, mínimo, máximo y total para cada "room_type"
mean_price_room_type <- tapply(data$price, data$room_type, mean, na.rm = TRUE)
min_price_room_type <- tapply(data$price, data$room_type, min, na.rm = TRUE)
max_price_room_type <- tapply(data$price, data$room_type, max, na.rm = TRUE)
total_price_room_type <- tapply(data$price, data$room_type, sum, na.rm = TRUE)
paste("El precio medio por habitación es:", mean_price_room_type)
paste("El precio mínimo por habitación es:", min_price_room_type)
paste("El precio máximo por habitación es:", max_price_room_type)
paste("El precio total por habitación es:", total_price_room_type)

# Precio medio, total y frecuencia relativa para cada "room_type" y "neighbourhood_group"
mean_price_room_neighbourhood <- with(data, tapply(price, list(room_type, neighbourhood_group), mean, na.rm = TRUE))
total_price_room_neighbourhood <- with(data, tapply(price, list(room_type, neighbourhood_group), sum, na.rm = TRUE))
freq_rel_room_neighbourhood <- prop.table(table(data$room_type, data$neighbourhood_group))
paste("El precio medio para cada tipo de habitación y vecindario es:", mean_price_room_neighbourhood)
paste("El precio total para cada tipo de habitación y vecindario es:", total_price_room_neighbourhood)
paste("La frecuencia relativa para cada tipo de habitación y para cada vecindario es:", freq_rel_room_neighbourhood)

# Tabla de contingencia 2x2 de "neighbourhood_group" y "room_type"
contingency_table <- table(data$neighbourhood_group, data$room_type)
paste("La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es:", contingency_table)

# 8. Visualización Univariante
# Gráficos de variables categóricas
# Gráfico de barras para una variable categórica
ggplot(airbnb2023, aes(x = room_type, y = price)) + geom_bar(stat = "identity")

# Este gráfico compara la frecuencia de los 4 diferentes tipos de habitaciones.Podemos observar como el que más frecuencia tiene es Entire home/apt Hotel seguido de Private room; la barra de los otros dos tipos apenas se puede apreciar en el gráfico ya que tienen una frecuencia mucho menor

ggplot(airbnb2023, aes(x = "", fill = neighbourhood_group)) +
  geom_bar(width = 1, color = "white") +
  coord_polar("y") +
  theme_minimal() +
  labs(title = "Distribución de Barrios", fill = "Barrio")

# Este es un gráfico de queso que muestra la cantidad de veces que se repite un barrio, es decir, cuántas viviendas hay de cada barrio

#Gráficos de variables continuas, en la mayoría de estos gráficos tuve que poner límite porque había datos extremos que si los recogía en las gráficas no podía observar la tendencia de la mayoría de datos

# Gráfico de histograma mejorado
ggplot(airbnb2023, aes(x = price, fill = cut(price, breaks = 5))) +
  geom_histogram(binwidth = 30, color = "black", position = "identity") +
  scale_fill_brewer(palette = "Blues") +
  labs(title = "Distribución de Precios en Airbnb", x = "Precio", y = "Frecuencia") +
  xlim(0, 800)
# Este histograma recoged la distribución de precios. Podemos observar como la mayoría son precios bajos y a medida que aumenta el precio disminuye la frecuencia

# Diagrama de cajas para una variable continua:
boxplot(airbnb2023$price, col = "yellow", ylim = c(0, 1500))
# En este diagrama de caja se puede observar que la caja, que es en la que hay información del primer al segundo cuartil tiene un precio bastante bajo, sin embargo, hay muchos puntos atípicos y extremos de viviendas mucho más caras. Tuve que dejar algunos elementos sin representar para que la caja se pueda apreciar.

# Gráfico de densidad para una variable continua
ggplot(airbnb2023, aes(x = number_of_reviews)) +
  geom_density(fill = "blue") +
  theme_minimal() +
  labs(title = "Gráfico de densidad de price", x = "Reviews", y = "Densidad") + xlim(0, 300)
# Este gráfico de densidad recoge la distribución de la variable number_reviews. Podemos observar como con las reviews sucede lo mismo que con el precio, la mayoría viviendas tienen reviews muy bajas, pero hay viviendas con muchas reviews

# 9. Visualización Multivariante
# Distribución de una variable continua y una variable categórica (por ejemplo, "price" y "room_type")
ggplot(data, aes(x = room_type, y = price)) +
  geom_boxplot() +
  theme_minimal() +
  labs(title = "Distribución de price por room_type", x = "Tipo de habitación", y = "Precio")

# Relación entre dos variables continuas: "price" y "number_of_reviews"
ggplot(data, aes(x = price, y = number_of_reviews)) +
  geom_point() +
  theme_minimal() +
  labs(title = "Relación entre price y number_of_reviews", x = "Precio", y = "Número de revisiones")

# 10. Mapa de los pisos del data set con leaflet
leaflet(data) %>%
  addTiles() %>%
  addMarkers(~longitude, ~latitude, popup = paste("Host:", data$host_name, "<br>",
                                                  "Name:", data$name, "<br>",
                                                  "Neighbourhood Group:", data$neighbourhood_group))
##Solucion
> ##Ejercicios
  > 
  > # 1. Tamaño del fichero
  > filesize<-file.info("airbnb2023.csv")$size
> paste(filesize, "bytes")
[1] "3683059 bytes"
> # 2. Dimensión del fichero importado
  > print(dim(data))
[1] 18086    18
> 
  > # 3. Variables en el fichero
  > print(names(data))
[1] "id"                             "name"                           "host_id"                        "host_name"                     
[5] "neighbourhood_group"            "neighbourhood"                  "latitude"                       "longitude"                     
[9] "room_type"                      "price"                          "minimum_nights"                 "number_of_reviews"             
[13] "last_review"                    "reviews_per_month"              "calculated_host_listings_count" "availability_365"              
[17] "number_of_reviews_ltm"          "license"                       
> 
  > # 4. Eliminar NA y comprobar la dimensión
  > data_no_na <- na.omit(data)
> print(dim(data_no_na))
[1] 10380    18
> 
  > # 5. Resumen numérico de todas las variables
  > print(summary(data))
id                name              host_id           host_name         neighbourhood_group neighbourhood         latitude    
Min.   :1.867e+04   Length:18086       Min.   :     3073   Length:18086       Length:18086        Length:18086       Min.   :41.35  
1st Qu.:2.172e+07   Class :character   1st Qu.:  9919300   Class :character   Class :character    Class :character   1st Qu.:41.38  
Median :4.435e+07   Mode  :character   Median : 96299106   Mode  :character   Mode  :character    Mode  :character   Median :41.39  
Mean   :2.997e+17                      Mean   :166184865                                                             Mean   :41.39  
3rd Qu.:7.450e+17                      3rd Qu.:310348791                                                             3rd Qu.:41.40  
Max.   :9.740e+17                      Max.   :535400790                                                             Max.   :41.46  

longitude      room_type             price         minimum_nights    number_of_reviews  last_review         reviews_per_month
Min.   :2.092   Length:18086       Min.   :    8.0   Min.   :   1.00   Min.   :   0.00   Min.   :2011-06-23   Min.   : 0.010   
1st Qu.:2.157   Class :character   1st Qu.:   52.0   1st Qu.:   1.00   1st Qu.:   1.00   1st Qu.:2023-01-31   1st Qu.: 0.240   
Median :2.168   Mode  :character   Median :  100.0   Median :   3.00   Median :   6.00   Median :2023-08-02   Median : 0.850   
Mean   :2.167                      Mean   :  162.8   Mean   :  14.76   Mean   :  42.22   Mean   :2022-10-26   Mean   : 1.436   
3rd Qu.:2.177                      3rd Qu.:  185.0   3rd Qu.:  31.00   3rd Qu.:  42.00   3rd Qu.:2023-08-22   3rd Qu.: 2.100   
Max.   :2.228                      Max.   :90000.0   Max.   :1125.00   Max.   :1817.00   Max.   :2023-09-06   Max.   :55.020   
NA's   :4466         NA's   :4466     
calculated_host_listings_count availability_365 number_of_reviews_ltm   license         
Min.   :  1.00                 Min.   :  0.0    Min.   :  0.00        Length:18086      
1st Qu.:  1.00                 1st Qu.: 47.0    1st Qu.:  0.00        Class :character  
Median :  5.00                 Median :175.0    Median :  2.00        Mode  :character  
Mean   : 31.63                 Mean   :171.8    Mean   : 11.44                          
3rd Qu.: 28.00                 3rd Qu.:302.0    3rd Qu.: 15.00                          
Max.   :294.00                 Max.   :365.0    Max.   :836.00                          

> 
  > # 6. Exploración de variables continuas y categóricas
  > # Media y cuantil 95 de la variable "price"
  > mean_price <- mean(data$price, na.rm = TRUE)
> quantile_price <- quantile(data$price, probs = 0.95, na.rm = TRUE)
> print(mean_price)
[1] 162.8024
> print(quantile_price)
95% 
357 
> # Frecuencia absoluta y relativa de "room_type"
  > freq_abs_room_type <- table(data$room_type)
> freq_rel_room_type <- prop.table(table(data$room_type))
> print(freq_abs_room_type)

Entire home/apt      Hotel room    Private room     Shared room 
10622             134            7173             157 
> paste0(freq_rel_room_type*100, "%")
[1] "58.7305097865752%"  "0.740904567068451%" "39.660510892403%"   "0.868074753953334%"
> # 7. Exploración de la relación entre algunas variables
  > # Pisos ordenados por precio y número de revisiones
  > data_ordered_price <- data[order(data$price), ]
> data_ordered_reviews <- data[order(data$number_of_reviews), ]
> print(data_ordered_price)
# A tibble: 18,086 × 18
id name   host_id host_name neighbourhood_group neighbourhood latitude longitude room_type price minimum_nights number_of_reviews
<dbl> <chr>    <dbl> <chr>     <chr>               <chr>            <dbl>     <dbl> <chr>     <dbl>          <dbl>             <dbl>
  1 8.72e17 Home …  8.78e7 Max       Eixample            la Nova Esqu…     41.4      2.15 Private …     8             31                 0
2 5.87e 5 Renta…  2.90e6 Cristina  Sant Martí          el Poblenou       41.4      2.20 Private …     9             31               155
3 8.99e 6 Renta…  4.70e7 Simo      Horta-Guinardó      la Font d'en…     41.4      2.16 Private …     9              1                 1
 4 1.39e 7 Renta…  5.34e7 Guido     Eixample            la Sagrada F…     41.4      2.18 Private …     9              1                 1
 5 1.71e 7 Renta…  6.97e7 Maria     Sants-Montjuïc      Sants             41.4      2.14 Private …     9              1                 0
 6 2.22e 7 Floor…  1.62e8 Andrea    Sants-Montjuïc      Sants - Badal     41.4      2.13 Private …     9              1                 1
 7 5.00e 7 Condo…  4.03e8 Alber     Horta-Guinardó      Can Baró          41.4      2.16 Shared r…     9              1                 0
 8 4.78e 6 Renta…  5.73e6 Barcelona Sant Martí          la Vila Olím…     41.4      2.20 Entire h…    10              1                21
 9 1.06e 7 Renta…  5.73e6 Barcelona Eixample            la Dreta de …     41.4      2.18 Entire h…    10              1                26
10 1.17e 7 Renta…  6.19e7 Hanni     Eixample            el Fort Pienc     41.4      2.18 Private …    10              1                 0
# ℹ 18,076 more rows
# ℹ 6 more variables: last_review <date>, reviews_per_month <dbl>, calculated_host_listings_count <dbl>, availability_365 <dbl>,
#   number_of_reviews_ltm <dbl>, license <chr>
# ℹ Use `print(n = ...)` to see more rows
> print(data_ordered_reviews)
# A tibble: 18,086 × 18
        id name   host_id host_name neighbourhood_group neighbourhood latitude longitude room_type price minimum_nights number_of_reviews
     <dbl> <chr>    <dbl> <chr>     <chr>               <chr>            <dbl>     <dbl> <chr>     <dbl>          <dbl>             <dbl>
 1  480975 Loft … 2272146 Javi      Sants-Montjuïc      el Poble Sec      41.4      2.17 Private …    50              1                 0
 2  663655 Renta… 1447144 Acomodis… Eixample            la Dreta de …     41.4      2.17 Entire h…   831              2                 0
 3  675175 Floor… 3429484 Pamela    Nou Barris          la Prosperit…     41.4      2.18 Private …    25             90                 0
 4  684639 Renta… 3297466 Rosa Leni Eixample            la Nova Esqu…     41.4      2.14 Private …    35             31                 0
 5  849035 Renta… 1432736 Inaki     Eixample            la Dreta de …     41.4      2.18 Entire h…   135              3                 0
 6 1140144 Renta… 3376710 Maria St… Sant Martí          el Camp de l…     41.4      2.18 Entire h…    49             32                 0
 7 1506324 Loft … 8046825 Luis      Horta-Guinardó      el Baix Guin…     41.4      2.17 Entire h…   125             31                 0
 8 1608746 Renta… 8568339 Leonardo  Eixample            la Dreta de …     41.4      2.17 Private …    48             60                 0
 9 1735838 Renta… 4396451 Pilar     Gràcia              el Camp d'en…     41.4      2.16 Private …    26             60                 0
10 1978145 Renta… 7496141 Aav       Eixample            la Dreta de …     41.4      2.17 Private …    79              1                 0
# ℹ 18,076 more rows
# ℹ 6 more variables: last_review <date>, reviews_per_month <dbl>, calculated_host_listings_count <dbl>, availability_365 <dbl>,
#   number_of_reviews_ltm <dbl>, license <chr>
# ℹ Use `print(n = ...)` to see more rows
> 
  > # Número de barrios diferentes en "Ciutat Vella"
  > num_neighbourhoods_ciutat_vella <- length(unique(data[data$neighbourhood_group == "Ciutat Vella", ]$neighbourhood))
> paste(" La cantidad de barrios en Ciutat Vella es" , num_neighbourhoods_ciutat_vella)
[1] " La cantidad de barrios en Ciutat Vella es 4"
> 
  > # Precio medio para cada "neighbourhood_group"
  > mean_price_neighbourhood_group <- tapply(data$price, data$neighbourhood_group, mean, na.rm = TRUE)
> paste("Precio medio por vecindario es", mean_price_neighbourhood_group)
[1] "Precio medio por vecindario es 128.554765291607" "Precio medio por vecindario es 204.485237285516"
[3] "Precio medio por vecindario es 142.532369578881" "Precio medio por vecindario es 203.398181818182"
[5] "Precio medio por vecindario es 165.27094972067"  "Precio medio por vecindario es 69.0392156862745"
[7] "Precio medio por vecindario es 72.8735632183908" "Precio medio por vecindario es 153.734055354994"
[9] "Precio medio por vecindario es 131.584705257568" "Precio medio por vecindario es 163.141573033708"
> 
  > # Precio medio, mínimo, máximo y total para cada "room_type"
  > mean_price_room_type <- tapply(data$price, data$room_type, mean, na.rm = TRUE)
> min_price_room_type <- tapply(data$price, data$room_type, min, na.rm = TRUE)
> max_price_room_type <- tapply(data$price, data$room_type, max, na.rm = TRUE)
> total_price_room_type <- tapply(data$price, data$room_type, sum, na.rm = TRUE)
> paste("El precio medio por habitación es:", mean_price_room_type)
[1] "El precio medio por habitación es: 195.31105253248"  "El precio medio por habitación es: 230.94776119403" 
[3] "El precio medio por habitación es: 114.856684790185" "El precio medio por habitación es: 95.7707006369427"
> paste("El precio mínimo por habitación es:", min_price_room_type)
[1] "El precio mínimo por habitación es: 10" "El precio mínimo por habitación es: 10" "El precio mínimo por habitación es: 8" 
[4] "El precio mínimo por habitación es: 9" 
> paste("El precio máximo por habitación es:", max_price_room_type)
[1] "El precio máximo por habitación es: 84999" "El precio máximo por habitación es: 2000"  "El precio máximo por habitación es: 90000"
[4] "El precio máximo por habitación es: 985"  
> paste("El precio total por habitación es:", total_price_room_type)
[1] "El precio total por habitación es: 2074594" "El precio total por habitación es: 30947"  
[3] "El precio total por habitación es: 823867"  "El precio total por habitación es: 15036"  
> 
  > # Precio medio, total y frecuencia relativa para cada "room_type" y "neighbourhood_group"
  > mean_price_room_neighbourhood <- with(data, tapply(price, list(room_type, neighbourhood_group), mean, na.rm = TRUE))
> total_price_room_neighbourhood <- with(data, tapply(price, list(room_type, neighbourhood_group), sum, na.rm = TRUE))
> freq_rel_room_neighbourhood <- prop.table(table(data$room_type, data$neighbourhood_group))
> paste("El precio medio para cada tipo de habitación y vecindario es:", mean_price_room_neighbourhood)
[1] "El precio medio para cada tipo de habitación y vecindario es: 153.864347826087"
[2] "El precio medio para cada tipo de habitación y vecindario es: 295.384615384615"
[3] "El precio medio para cada tipo de habitación y vecindario es: 95.5740053050398"
[4] "El precio medio para cada tipo de habitación y vecindario es: 74.1428571428571"
[5] "El precio medio para cada tipo de habitación y vecindario es: 240.502096177559"
[6] "El precio medio para cada tipo de habitación y vecindario es: 237.084337349398"
[7] "El precio medio para cada tipo de habitación y vecindario es: 141.320888888889"
[8] "El precio medio para cada tipo de habitación y vecindario es: 122.58024691358" 
[9] "El precio medio para cada tipo de habitación y vecindario es: 186.114141414141"
[10] "El precio medio para cada tipo de habitación y vecindario es: 167.727272727273"
[11] "El precio medio para cada tipo de habitación y vecindario es: 70.0490367775832"
[12] "El precio medio para cada tipo de habitación y vecindario es: 35.4210526315789"
[13] "El precio medio para cada tipo de habitación y vecindario es: 143.979253112033"
[14] "El precio medio para cada tipo de habitación y vecindario es: NA"              
[15] "El precio medio para cada tipo de habitación y vecindario es: 248.86319218241" 
[16] "El precio medio para cada tipo de habitación y vecindario es: 384.5"           
[17] "El precio medio para cada tipo de habitación y vecindario es: 155.965957446809"
[18] "El precio medio para cada tipo de habitación y vecindario es: NA"              
[19] "El precio medio para cada tipo de habitación y vecindario es: 186.533333333333"
[20] "El precio medio para cada tipo de habitación y vecindario es: 43.6666666666667"
[21] "El precio medio para cada tipo de habitación y vecindario es: 134.807692307692"
[22] "El precio medio para cada tipo de habitación y vecindario es: NA"              
[23] "El precio medio para cada tipo de habitación y vecindario es: 46.7"            
[24] "El precio medio para cada tipo de habitación y vecindario es: 34.5"            
[25] "El precio medio para cada tipo de habitación y vecindario es: 106.223214285714"
[26] "El precio medio para cada tipo de habitación y vecindario es: NA"              
[27] "El precio medio para cada tipo de habitación y vecindario es: 47.4236111111111"
[28] "El precio medio para cada tipo de habitación y vecindario es: 58.8"            
[29] "El precio medio para cada tipo de habitación y vecindario es: 189.357142857143"
[30] "El precio medio para cada tipo de habitación y vecindario es: 232.666666666667"
[31] "El precio medio para cada tipo de habitación y vecindario es: 99.2492113564669"
[32] "El precio medio para cada tipo de habitación y vecindario es: 59.5294117647059"
[33] "El precio medio para cada tipo de habitación y vecindario es: 158.245746691871"
[34] "El precio medio para cada tipo de habitación y vecindario es: 98.6"            
[35] "El precio medio para cada tipo de habitación y vecindario es: 98.1795511221945"
[36] "El precio medio para cada tipo de habitación y vecindario es: 48"              
[37] "El precio medio para cada tipo de habitación y vecindario es: 197.30823117338" 
[38] "El precio medio para cada tipo de habitación y vecindario es: 60"              
[39] "El precio medio para cada tipo de habitación y vecindario es: 101.474193548387"
[40] "El precio medio para cada tipo de habitación y vecindario es: 127"             
> paste("El precio total para cada tipo de habitación y vecindario es:", total_price_room_neighbourhood)
[1] "El precio total para cada tipo de habitación y vecindario es: 353888"
[2] "El precio total para cada tipo de habitación y vecindario es: 7680"  
[3] "El precio total para cada tipo de habitación y vecindario es: 180157"
[4] "El precio total para cada tipo de habitación y vecindario es: 519"   
[5] "El precio total para cada tipo de habitación y vecindario es: 975236"
[6] "El precio total para cada tipo de habitación y vecindario es: 19678" 
[7] "El precio total para cada tipo de habitación y vecindario es: 317972"
[8] "El precio total para cada tipo de habitación y vecindario es: 9929"  
[9] "El precio total para cada tipo de habitación y vecindario es: 184253"
[10] "El precio total para cada tipo de habitación y vecindario es: 1845"  
[11] "El precio total para cada tipo de habitación y vecindario es: 39998" 
[12] "El precio total para cada tipo de habitación y vecindario es: 673"   
[13] "El precio total para cada tipo de habitación y vecindario es: 34699" 
[14] "El precio total para cada tipo de habitación y vecindario es: NA"    
[15] "El precio total para cada tipo de habitación y vecindario es: 76401" 
[16] "El precio total para cada tipo de habitación y vecindario es: 769"   
[17] "El precio total para cada tipo de habitación y vecindario es: 36652" 
[18] "El precio total para cada tipo de habitación y vecindario es: NA"    
[19] "El precio total para cada tipo de habitación y vecindario es: 22384" 
[20] "El precio total para cada tipo de habitación y vecindario es: 131"   
[21] "El precio total para cada tipo de habitación y vecindario es: 7010"  
[22] "El precio total para cada tipo de habitación y vecindario es: NA"    
[23] "El precio total para cada tipo de habitación y vecindario es: 7005"  
[24] "El precio total para cada tipo de habitación y vecindario es: 69"    
[25] "El precio total para cada tipo de habitación y vecindario es: 11897" 
[26] "El precio total para cada tipo de habitación y vecindario es: NA"    
[27] "El precio total para cada tipo de habitación y vecindario es: 6829"  
[28] "El precio total para cada tipo de habitación y vecindario es: 294"   
[29] "El precio total para cada tipo de habitación y vecindario es: 190872"
[30] "El precio total para cada tipo de habitación y vecindario es: 698"   
[31] "El precio total para cada tipo de habitación y vecindario es: 62924" 
[32] "El precio total para cada tipo de habitación y vecindario es: 1012"  
[33] "El precio total para cada tipo de habitación y vecindario es: 167424"
[34] "El precio total para cada tipo de habitación y vecindario es: 986"   
[35] "El precio total para cada tipo de habitación y vecindario es: 78740" 
[36] "El precio total para cada tipo de habitación y vecindario es: 624"   
[37] "El precio total para cada tipo de habitación y vecindario es: 112663"
[38] "El precio total para cada tipo de habitación y vecindario es: 60"    
[39] "El precio total para cada tipo de habitación y vecindario es: 31457" 
[40] "El precio total para cada tipo de habitación y vecindario es: 1016"  
> paste("La frecuencia relativa para cada tipo de habitación y para cada vecindario es:", freq_rel_room_neighbourhood)
[1] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.127170186884883"   
[2] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.0014375760256552"  
[3] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.104224261860002"   
[4] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.000387039699214862"
[5] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.22420656861661"    
[6] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.00458918500497623" 
[7] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.124405617604777"   
[8] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.00447860223377198" 
[9] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.054738471746102"   
[10] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.000608205241623355"
[11] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.0315713811788123"  
[12] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.00105053632644034" 
[13] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.0133252239301117"  
[14] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0"                   
[15] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.0169744553798518"  
[16] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.000110582771204246"
[17] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.0129934756164989"  
[18] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0"                   
[19] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.00663496627225478" 
[20] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.00016587415680637" 
[21] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.00287515205131041" 
[22] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0"                   
[23] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.00829370784031848" 
[24] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.000110582771204246"
[25] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.0061926351874378"  
[26] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0"                   
[27] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.00796195952670574" 
[28] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.000276456928010616"
[29] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.0557337166869402"  
[30] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.00016587415680637" 
[31] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.0350547384717461"  
[32] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.000939953555236094"
[33] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.0584982859670463"  
[34] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.000552913856021232"
[35] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.0443436912529028"  
[36] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.000718788012827601"
[37] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.0315713811788123"  
[38] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 5.52913856021232e-05"
[39] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.0171403295366582"  
[40] "La frecuencia relativa para cada tipo de habitación y para cada vecindario es: 0.000442331084816986"
> 
  > # Tabla de contingencia 2x2 de "neighbourhood_group" y "room_type"
  > contingency_table <- table(data$neighbourhood_group, data$room_type)
> paste("La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es:", contingency_table)
[1] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 2300"
[2] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 4055"
[3] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 990" 
[4] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 241" 
[5] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 235" 
[6] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 52"  
[7] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 112" 
[8] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 1008"
[9] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 1058"
[10] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 571" 
[11] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 26"  
[12] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 83"  
[13] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 11"  
[14] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 0"   
[15] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 0"   
[16] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 0"   
[17] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 0"   
[18] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 3"   
[19] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 10"  
[20] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 1"   
[21] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 1885"
[22] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 2250"
[23] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 571" 
[24] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 307" 
[25] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 120" 
[26] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 150" 
[27] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 144" 
[28] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 634" 
[29] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 802" 
[30] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 310" 
[31] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 7"   
[32] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 81"  
[33] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 19"  
[34] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 2"   
[35] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 3"   
[36] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 2"   
[37] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 5"   
[38] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 17"  
[39] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 13"  
[40] "La tabla de contingencia 2*2 de cada tipo de habitación y vecindario es: 8"   
> 
  # 8. Visualización Univariante
  # Gráficos de variables categóricas
  # Gráfico de barras para una variable categórica
  ggplot(airbnb2023, aes(x = room_type, y = price)) + geom_bar(stat = "identity")

# Este gráfico compara la frecuencia de los 4 diferentes tipos de habitaciones.Podemos observar como el que más frecuencia tiene es Entire home/apt Hotel seguido de Private room; la barra de los otros dos tipos apenas se puede apreciar en el gráfico ya que tienen una frecuencia mucho menor

ggplot(airbnb2023, aes(x = "", fill = neighbourhood_group)) +
  geom_bar(width = 1, color = "white") +
  coord_polar("y") +
  theme_minimal() +
  labs(title = "Distribución de Barrios", fill = "Barrio")

# Este es un gráfico de queso que muestra la cantidad de veces que se repite un barrio, es decir, cuántas viviendas hay de cada barrio

#Gráficos de variables continuas, en la mayoría de estos gráficos tuve que poner límite porque había datos extremos que si los recogía en las gráficas no podía observar la tendencia de la mayoría de datos

# Gráfico de histograma mejorado
ggplot(airbnb2023, aes(x = price, fill = cut(price, breaks = 5))) +
  geom_histogram(binwidth = 30, color = "black", position = "identity") +
  scale_fill_brewer(palette = "Blues") +
  labs(title = "Distribución de Precios en Airbnb", x = "Precio", y = "Frecuencia") +
  xlim(0, 800)
# Este histograma recoged la distribución de precios. Podemos observar como la mayoría son precios bajos y a medida que aumenta el precio disminuye la frecuencia

# Diagrama de cajas para una variable continua:
boxplot(airbnb2023$price, col = "yellow", ylim = c(0, 1500))
# En este diagrama de caja se puede observar que la caja, que es en la que hay información del primer al segundo cuartil tiene un precio bastante bajo, sin embargo, hay muchos puntos atípicos y extremos de viviendas mucho más caras. Tuve que dejar algunos elementos sin representar para que la caja se pueda apreciar.

# Gráfico de densidad para una variable continua
ggplot(airbnb2023, aes(x = number_of_reviews)) +
  geom_density(fill = "blue") +
  theme_minimal() +
  labs(title = "Gráfico de densidad de price", x = "Reviews", y = "Densidad") + xlim(0, 300)
# Este gráfico de densidad recoge la distribución de la variable number_reviews. Podemos observar como con las reviews sucede lo mismo que con el precio, la mayoría viviendas tienen reviews muy bajas, pero hay viviendas con muchas reviews
> 
  > # 9. Visualización Multivariante
  > # Distribución de una variable continua y una variable categórica (por ejemplo, "price" y "room_type")
  > ggplot(data, aes(x = room_type, y = price)) +
  +   geom_boxplot() +
  +   theme_minimal() +
  +   labs(title = "Distribución de price por room_type", x = "Tipo de habitación", y = "Precio")
> 
  > # Relación entre dos variables continuas: "price" y "number_of_reviews"
  > ggplot(data, aes(x = price, y = number_of_reviews)) +
  +   geom_point() +
  +   theme_minimal() +
  +   labs(title = "Relación entre price y number_of_reviews", x = "Precio", y = "Número de revisiones")
> 
  > # 10. Mapa de los pisos del data set con leaflet
  > leaflet(data) %>%
  +   addTiles() %>%
  +   addMarkers(~longitude, ~latitude, popup = paste("Host:", data$host_name, "<br>",
                                                      +                                                   "Name:", data$name, "<br>",
                                                      +                                                   "Neighbourhood Group:", data$neighbourhood_group))
