# Asigna el valor 1 a la variable 'var1'
var1 <- 1

# Imprime el valor de 'var1'
cat("Valor de var1:", var1, "\n")

# Crea un vector 'vector1' con valores 1, 2 y 3
vector1 <- c(1, 2, 3)

# Imprime el vector 'vector1'
cat("Vector vector1:", vector1, "\n")

# Crea un vector 'medallas' con valores "oro", "oro", "plata", "plata", "bronce"
medallas <- c("oro", "oro", "plata", "plata", "bronce")

# Imprime el vector 'medallas'
cat("Vector medallas:", medallas, "\n")

# Crea un gráfico de barras de la frecuencia de los factores en 'medallas'
barplot(table(medallas), main="Gráfico de Medallas", xlab="Medallas", ylab="Frecuencia")

# Convierte el vector 'medallas' en un factor
medallas_factor <- factor(medallas)

# Imprime el factor 'medallas_factor'
cat("Factor medallas_factor:", levels(medallas_factor), "\n")

# Crea un gráfico de barras de la frecuencia de los factores en 'medallas_factor'
barplot(table(medallas_factor), main="Gráfico de Medallas (Factor)", xlab="Medallas", ylab="Frecuencia")

# Crea una matriz 'matriz' a partir de 'vector1' y 'vector2'
vector2 <- c(4, 5, 6)
matriz <- matrix(c(vector1, vector2), nrow=3, ncol=2)

# Imprime la matriz 'matriz'
cat("Matriz matriz:\n")
print(matriz)

# Crea un vector 'vector3' con valores "oro", "plata", "bronce"
vector3 <- c("oro", "plata", "bronce")

# Imprime el vector 'vector3'
cat("Vector vector3:", vector3, "\n")

# Crea un vector lógico 'vector4' con valores TRUE, FALSE, TRUE
vector4 <- c(TRUE, FALSE, TRUE)

# Imprime el vector lógico 'vector4'
cat("Vector lógico vector4:", vector4, "\n")

# Crea un data frame 'df' a partir de varios vectores
df <- data.frame(var1, vector1, vector3, vector4)

# Imprime el data frame 'df'
cat("Data frame df:\n")
print(df)

# Crea una lista 'lista' que contiene varias variables y estructuras de datos
lista <- list(var1, vector1, medallas, matriz, df)

# Imprime la lista 'lista'
cat("Lista lista:\n")
print(lista)
