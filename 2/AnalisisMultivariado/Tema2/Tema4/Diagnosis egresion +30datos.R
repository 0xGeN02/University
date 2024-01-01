Inversiones <- pescas_sur$Inversiones
Temperatura <- pescas_sur$Temperatura
Horas <- pescas_sur$Horas

#grafico dispersion
ggplot(data = pescas_sur, mapping = aes(x=Inversiones, y=Capturas))+geom_point()
ggplot(data = pescas_sur, mapping = aes(x=Temperatura, y=Capturas))+geom_point()
ggplot(data = pescas_sur, mapping = aes(x=Horas, y=Capturas))+geom_point()

#Correlaciones
round(cor(pescas_sur,method="pearson"),3)
corrplot::corrplot(cor(pescas_sur, method="pearson"), type="lower")

#Estimacion modelo1
modelo1<- lm(Capturas~Inversiones+Temperatura+Horas, data= pescas_sur)
summary(modelo1)

#Diagnosis modelo1

resid1 <-resid(modelo1)
zresid1 <- rstandard(modelo1)
capturas_estimadas1 <- fitted(modelo1)
ggplot(data = pescas_sur, aes(capturas_estimadas1, zresid1))+geom_point()+geom_hline(yintercept = 0)+theme_bw()
lmtest::bptest(modelo1)
car::dwt(modelo1,alternative="two.sided")
qqnorm(resid1)
qqline(resid1)
shapiro.test(resid1)

#Eliminacion dato atipico
pescas <- subset(pescas_sur, zresid1 > -2)

#modelo2
modelo2 <-lm(Capturas~Inversiones+Temperatura+Horas, data= pescas)

#Diagnosis modelo2
resid2 <-resid(modelo2)
zresid2 <- rstandard(modelo2)
capturas_estimadas2 <- fitted(modelo2)
ggplot(data = pescas, aes(capturas_estimadas2, zresid2))+geom_point()+geom_hline(yintercept = 0)+theme_bw()
lmtest::bptest(modelo2)
car::dwt(modelo2,alternative="two.sided")
qqnorm(resid2)
qqline(resid2)
shapiro.test(resid2)

#modelo3
modelo3 <-lm(Capturas~0+Inversiones+Temperatura+Horas, data= pescas)

#Diagnosis modelo2
resid3 <-resid(modelo3)
zresid3 <- rstandard(modelo3)
capturas_estimadas3 <- fitted(modelo3)
ggplot(data = pescas, aes(capturas_estimadas3, zresid3))+geom_point()+geom_hline(yintercept = 0)+theme_bw()
lmtest::bptest(modelo3)
car::dwt(modelo3,alternative="two.sided")
qqnorm(resid3)
qqline(resid3)
shapiro.test(resid3)
