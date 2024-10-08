#Biblioteca randon
import random as r
#Inicio
r.seed(50)
print("9 números en rango [0,100]")
for i in range(9):
    print("Número ",i+1, " valor = ",r.randint(0,100))
    #Fin