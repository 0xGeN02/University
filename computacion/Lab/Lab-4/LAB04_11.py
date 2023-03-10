# Función Suma_V
# Suma elementos de un vector
# Parámetros
# Parámetro formal v Vector
# Retorna Suma
## Inicio de Función Suma_V
def Suma_V(v):
    s=0
    for i in range(len(v)):
        s=s+v[i]
    return s
## Fin de Función Suma_V