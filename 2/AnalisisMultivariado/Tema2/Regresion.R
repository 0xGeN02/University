##Medios de comunicación
Ventas <- medios_comunicación$Ventas
Televisión <- medios_comunicación$Televisión
Prensa <- medios_comunicación$Prensa
Radio <- medios_comunicación$Radio

#Análisis de los datos(Televisión)
regresión_televisión <- lm(Ventas~Televisión, data=medios_comunicación)
summary(regresión_televisión)
#Gráfica con recta (Televisión)
plot(Televisión, Ventas)
abline(regresión_televisión)

#Análisis de los datos(Prensa)
regresión_prensa <- lm(Ventas~Prensa, data=medios_comunicación)
summary(regresión_prensa)
#Gráfica con recta (Prensa)
plot(Prensa, Ventas)
abline(regresión_prensa)

#Análisis de los datos(Televisión)
regresión_radio <- lm(Ventas~Radio, data=medios_comunicación)
summary(regresión_radio)
#Gráfica con recta (Televisión)
plot(Radio, Ventas)
abline(regresión_radio)

# Correlaciones
round(cor(medios_comunicación, method="pearson"),3)
corrplot(cor(medios_comunicación,method = "pearson"), type="lower")

#Regresion
modelo1<-lm(Ventas~Televisión+Prensa+Radio,data=medios_comunicación)
summary(modelo1)

modelo2<- lm(Ventas~Prensa, data=medios_comunicación)
summary(modelo2)

modelo3<- lm(Ventas~0+Prensa, data=medios_comunicación)
summary(modelo3)
