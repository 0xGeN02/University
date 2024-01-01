Producción <- costes2$Producción
Coste <- costes2$Coste

# Scatter plot with ggplot2
ggplot(data = costes2, aes(x = Coste, y = Producción)) + geom_point()

# Correlation plot with corrplot
corrplot(cor(costes2, method = "pearson"), type = "lower")

       

#modelo1
modelo1 <- lm(Coste~Producción, data=costes2)
summary(modelo1)
plot(costes2$Coste, costes2$Producción, col="blue")
abline(modelo1, col="green")

zresid1 <- rstandard(modelo1)
Coste_estimado1 <- fitted(modelo1)
ggplot(data=costes2, aes(Coste_estimado1, zresid1)) + geom_point()+geom_hline(yintercept =0)

#modelo2
Producción2 <- costes2$Producción^2
modelo2 <- lm(Coste~Producción+Producción2, data=costes2)
summary(modelo2)

zresid2 <- rstandard(modelo2)
Coste_estimado2 <- fitted(modelo2)
ggplot(data = costes2, aes(Coste_estimado2, zresid2)) + geom_point() + geom_hline(yintercept = 0)

#modelo3
# Crear una nueva variable que sea el cubo de la producción
Producción3 <- costes2$Producción^3

# Ajustar el modelo 3
modelo3 <- lm(Coste ~ Producción + Producción2 + Producción3, data = costes2)

# Resumen del modelo
summary(modelo3)

# Gráfico de los residuos estandarizados frente a los valores ajustados
zresid3 <- rstandard(modelo3)
Coste_estimado3 <- fitted(modelo3)
ggplot(data = costes2, aes(Coste_estimado3, zresid3)) + geom_point() + geom_hline(yintercept = 0)

