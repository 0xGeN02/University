# Leer los elementos de un vector
# Parámetros
# Parámetro formal v Vector
# Parámetro formal tipo  (tipo entrada float,int,str,bool)
# Retorna el vector con los datos del tipo indicado
## Inicio de Función Entrada_V 
def Entrada_V(v,tipo):
    for i in range(len(v)):
        print("Indique el elemento ",i+1," = ",end=" ")
        v[i]=tipo(input())
    return v
## Fin de Función entrada_V
