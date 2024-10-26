# Modulo_Vectores
## Contienen operaciones comunes con vectores
import numpy as np

# Función Crea_Vector

## Inicio de Función Crea_Vector
def Vector_Valor(n,Valor):
    a = [Valor]*n
    return a
## Fin de Función Crea_Vector de un tipo de datos

# FUNCION ENTRADA DE ELEMENTOS DE UN VECTOR

## Inicio de Función Entrada_V 
def Entrada_V(v,tipo):
    for i in range(len(v)):
        print("Indique el elemento ",i+1," = ",end=" ")
        v[i]=tipo(input())
    return v
## Fin de Función entrada_V

# FUNCION MOSTRAR ELEMENTOS DE UN VECTOR

## Inicio de Función Muestra_V
def Muestra_V(v):
    print("[",end=" ")
    for i in range(len(v)):
        print(v[i]," ",end=" ")
    print("]")
## Fin de Función Muestra_V

# FUNCION SUMA ELEMENTOS DE UN VECTOR

# Función Suma_V

## Inicio de Función Suma_V
def Suma_V(v):
    s=0
    for i in range(len(v)):
        s=s+v[i]
    return s
## Fin de Función Suma_V

# FUNCION MAYOR ELEMENTO DE UN VECTOR           (ASIGNACIÓN 08)

print("El elemento de mayor valor del vector es:", np.amax(Vector_Valor))

# FUNCION MENOR ELEMENTO DE UN VECTOR           (ASIGNACIÓN 08)

print("El elemento de menor valor del vector es:", np.amin(Vector_Valor))

# FUNCION BUSCAR UN ELEMENTO EN UN VECTOR       (ASIGNACIÓN 08)

x = print("Indique el elemento a buscar:")
try:
    Position_Vector = Vector_Valor.index(x)
    print("El elemento se encuentra en la posición", Position_Vector)
except:
    print("El elemento no pertenece al vector")

# FUNCION MEDIA DE LOS ELEMENTOS DE UN VECTOR   (ASIGNACIÓN 08)

print("La media aritmetica del vector es:", np.mean(Vector_Valor))  

# FUNCION INTERCAMBIAR                          (ASIGNACIÓN 08)

pos1 = print("Indique la posición del primer número a cambiar")
pos2 = print("Indique la posición del segundo número a cambiar")

def SwapPosition(Vector, pos1, pos2):
    get = Vector[pos1], Vector[pos2]
    Vector_Valor[pos2], Vector_Valor[pos1] = get, get
    return Vector_Valor
print(SwapPosition(Vector_Valor,pos1-1,pos2-1))


# FUNCION ORDENAR LOS ELEMENTOS DE UN VECTOR    (RETO)

print("Orden de mayor a menor",Ordered_Vector = sorted(Vector_Valor))
print("Orden de menor a mayor",Ordered_Vector = sorted(Vector_Valor, reverse= True))
