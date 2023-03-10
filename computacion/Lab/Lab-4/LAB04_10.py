# Función Muestra_V
# Muestra los elementos de un vector
# Parámetros
# Parámetro formal v Vector
# Retorna (Sin retorno)
## Inicio de Función Muestra_V
def Muestra_V(v):
    print("[",end=" ")
    for i in range(len(v)):
        print(v[i]," ",end=" ")
    print("]")
## Fin de Función Muestra_V