#Biblioteca randon
import random as r
#Inicio
import random
r.seed(10)
print("9 números en rango [0,50] con paso 5")
for i in range(10):
    print(random.randrange(0, 51, 5), end=' ')
#Fin