#Programa Suma_enteros
#Suma los 5 primeros números enteros positivos
#Realizado por: Manuel Mateo Delgado
#Fecha: 16/11/2022
#Bibliotecas
#Declaraciones
#Entero i,s
#Inicio
n=int(input("Indique hasta donde sumar :"))
s=0
for i in range(n):
    s=s+i
print("la suma es = ", s)
#Fin