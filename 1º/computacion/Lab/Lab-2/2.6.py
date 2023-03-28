

#2.6
#Porgrama Raices Ecuación segundo grado
#Realizado por: Mateo Delgado
#Bibliotecas / Definiciones / Declaraciones
import math
#Declaraciones
#Real a,b,c,d,r1,r2,arg
#Inicio
a = float(input("Coeficiente 2 orden   "))
b = float(input("Coeficiente 1 orden   "))
c = float(input("Termino independiente  "))
arg = b**2-4*a*c
r1 = -b+math.sqrt((arg)/(2*a))
r2 = -b-math.sqrt((arg)/(2*a))
print("Raiz r1 = ",r1)
print("Raiz r2 = ",r2)
#Fin