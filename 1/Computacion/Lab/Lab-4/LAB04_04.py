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

# Función Ingresa_Año
# Permite ingresar un año en un rango [0,2100]
# Parámetros
# Parámetro li Tipo Entero límite inferior permitido
# Parámetro ls Tipo Entero límite superior permitido
# Retorna un año en el rango
## Inicio de Función Ingresa_Año

def Ingresar_Año(li,ls):
    print("Indique un año en el rango [",li,",",ls,"] = ", end=" ")
    x = int (input())
    while not(Rango(x,li,ls)):
        print("Valor fuera del rango, vuelva a probar")
        print("Indique un año en el rango [",li, ",",ls,"] = ",end=" ")
        x = int(input())
    return x
#Fin Funcion

#Prueba Funcion Ingeresar_Año
print("Año = ",Ingresar_Año(0,2100))
print("Año = ",Ingresar_Año(2020,2022))