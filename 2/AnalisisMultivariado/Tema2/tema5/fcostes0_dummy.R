Producción <- fcostes0_Dummy$Producción
Costes <- fcostes0_Dummy$Costes
Empresa <- fcostes0_Dummy$Empresa
Año <- fcostes0_Dummy$Año

#grafico dispersion
library(ggplot2)
ggplot(fcostes0_Dummy, aes(x=Producción, y=Costes, col=Empresa, shape=Empresa))+geom_point(size=3)

#correlaciones
library(dplyr)
datoscor <- select(fcostes0_Dummy,Costes,Producción)
round(cor(datoscor, method='pearson'), 3)
library(corrplot)
corrplot(cor(datoscor,method='pearson'), type='lower')

#Modelo1
intercept_only <- lm(Costes~1,fcostes0_Dummy)
all<- lm(Costes~Producción+DA+DB+DC+DD+DMA+DMB+DMC+DMD, fcostes0_Dummy)
both<- step(intercept_only, direction='both', scope=formula(all), trace=0)
both$anova
both$coefficients

modelo1<-lm(Costes~Producción+DB+DD, fcostes0_Dummy)
summary(modelo1)

##Diagnosis de modelo1
resid1<-resid(modelo1)
zresid1<-rstandard(modelo1)
library(car)
Costes_estimados1 <- fitted(modelo1)
ggplot(data=fcostes0_Dummy,aes(Costes_estimados1,zresid1))+geom_point()+geom_hline(yintercept = 0)+theme_bw()
bptest(modelo1) 
dwt(modelo1,alternative="two.sided")
qqnorm(resid1)
qqline(resid1)
shapiro.test(resid1)
print(zresid1)

#Modelo2 (sin constante)
modelo2 <- lm(Costes~0+Producción+DD+DB,fcostes0_Dummy)
summary(modelo2)

#Diagnosis - Modelo2
resid2 <- resid(modelo2)
zresid2 <- rstandard(modelo2)
Costes_estimados2 <- fitted(modelo2)
ggplot(data=fcostes0_Dummy,aes(Costes_estimados2,zresid2))+geom_point()+geom_hline(yintercept = 0)+theme_bw()
bptest(modelo2) 
dwt(modelo2,alternative="two.sided") 
qqnorm(resid2)
qqline(resid2)
shapiro.test(resid2)

