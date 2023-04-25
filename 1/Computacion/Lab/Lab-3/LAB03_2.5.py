#Programa Siete Gana
#Realizado por: Manuel Mateo Delgado
#Fecha: 16/11/2022
#Bibliotecas
import random
#Declaraciones
#Entero (int) Fichas, Total, Juegos
#Caracter   (str) Jugar
#Inicio
print('Juego de Dados Siete Gana')
random.seed(10)
Fichas=int(input("Cuantas fichas compra 1 euro c/u = "))
Total=Fichas
Jugar="S"
Juegos=0
Jugar=input("Si quieres jugar marque S : ")
#Comenzar ciclo para jugar
while ((Fichas>0)and ((Jugar=="S")or (Jugar =="s"))):
    Juegos+=1
    Dado1 = random.randint(1,6)
    Dado2 = random.randint(1,6)
    print(" Dado1 = ", Dado1," Dado2 = ",Dado2)
    print("Tus dados suman = ",Dado1+Dado2)
    if((Dado1+Dado2)==7):
        print("Enhorabuena ganaste")
        Fichas+=1
    else:
        print("Pierdes una ficha")
        Fichas-=1
    if(Fichas>0):
        print("Tienes ",Fichas," fichas para jugar")
        Jugar=input("Para seguir jugando marque S : ")
#Fin del Juego y resumen
print("Fin del Juego")
print()
print("**************************")
print("Apuestas realizadas =",Juegos)
if(Fichas>Total):
    print("Felicidades ganaste ",Fichas-Total)
else:
    if(Fichas==Total):
        print("Ni ganas ni pierdes")
    else:
        print("Perdiste ", Total-Fichas," Fichas")
        print("Tienes ",Fichas," Fichas para cambiar")
#Fin