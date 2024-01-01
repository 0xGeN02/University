#Atletismo

Distancia <- atletismo$Distancia
Tiempo <- atletismo$Tiempo

plot(Distancia, Tiempo)

regresion <- lm(Tiempo~Distancia, data=atletismo)
summary(regresion)
anova(regresion)

ggplot(data=atletismo, mapping = aes(x=Distancia, y=Tiempo))+geom_point()
round(cor(atletismo, method = "pearson"), 3)
corrplot(cor(atletismo, method = "pearson"), type="lower")

modelo1 <- lm(Tiempo~Distancia, data=atletismo)
summary(modelo1)

plot(atletismo$Distancia, atletismo$Tiempo, col ="black")
abline(modelo1, col="red")

zresid1<- rstandard(modelo1)
Tiempo_estimado1 <- fitted(modelo1)
ggplot(data=atletismo, aes(Tiempo_estimado1,zresid1))+geom_point()+geom_hline(yintercept = 0)


L_Tiempo <-log(atletismo$Tiempo)
L_Distancia <- log(atletismo$Distancia)

ggplot(data=atletismo, mapping = aes(x=L_Distancia, y=L_Tiempo))+geom_point()

modelo2 <- lm(L_Tiempo~L_Distancia, data = atletismo)
summary(modelo2)

