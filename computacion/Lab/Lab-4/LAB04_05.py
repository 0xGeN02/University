# Función Rango
# Verificar si un valor está dentro de un rango
# Parámetros
# Parámetro formal n   Número a verificar
# Parámetro formal li   Límite inferior
# Parámetro formal ls   Límite superior
# Retorna Verdadero si el valor n está dentro del rango
# Inicio de Función Rango

def Rango(n,li,ls):
    if ((n>=li) and (n<=ls)):
        return True
    else:
        return False
#Fin Funcion Rango

# Función Ingresa_Mes
# Valida el ingreso de un mes en rango [1,12]
# Parámetros (No tiene)
# Retorna un mes en el rango [1,12]
# Inicio de Función Ingresa_Mes

def Ingresar_Mes():
    print("Indique un mes en el rango [1,12] = ",end=" ")
    X = int(input())
    while not(Rango(X,1,12)):
        print("Valor fuera del rango, vuelva a probar")
        print("Indique un año en el rango [1,12] = ",end=" ")
        X = int(input()) 
    return X
##Fin Funcion Ingresar_mes

##Prueba Ingresar_Mes
print("Mes = ",Ingresar_Mes())