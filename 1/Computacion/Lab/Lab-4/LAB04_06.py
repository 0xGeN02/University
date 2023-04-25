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

# Función Ingresa_Dia
# Permite ingresar un mes en el rango [1,12]
# Parámetros
# Dias n Tipo Entero máximo de días
# Retorna d Tipo Entero con un día válido
## Inicio de Función Ingresa_Dia

def Ingresar_Día(nd):
    print("Indique un día en el rango [1,",nd,"] ", end=" ")
    d = int(input())
    while not(Rango(d,1,nd)):
        print("Indique un día en el rango [1,",nd,"] ", end=" ")
        print("Indique un día en el rango [1,",nd,"] = ",end=" ")
        d = int(input())
    return d
##Fin de Función Ingresar_Día
print("Día = ",Ingresar_Día(31))