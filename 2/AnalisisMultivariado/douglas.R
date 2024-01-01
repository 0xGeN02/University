L_Produccion <- log(Cobb_Douglas$Producción)
L_Trabajo <- log(Cobb_Douglas$Trabajo)
L_Inversion <- log(Cobb_Douglas$Inversión)

Logaritmos <- data.frame(L_Produccion, L_Trabajo, L_Inversion)
ggplot(data = Logaritmos, mapping = aes(x = L_Trabajo, y = L_Produccion)) + geom_point()
ggplot(data = Logaritmos, mapping = aes(x = L_Inversion, y = L_Produccion)) + geom_point()


round(cor(Logaritmos, method="pearson"), 3)
corrplot(cor(Logaritmos, method = "pearson"), type="lower")

modelo <- lm(L_Produccion ~ L_Inversion + L_Trabajo, data = Logaritmos)
summary(modelo)
confint(modelo)
