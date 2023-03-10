# Modulo_Fecha
## Funciones para la validación de ingreso de fechas
# Funciones
#   Rango(n,li,ls)
#   Bisiesto(a)
#   Dias_Mes(m,b)
#   Ingresa_Año(li,ls)
#   Ingresa_Mes()
#   Ingresa_Dia(nd)

# FUNCIÓN RANGO
def Rango(n,li,ls):
    if ((n>=li) and (n<=ls)):
       return True
    else:
        return False

# FUNCIÓN BISIESTO
def Bisiesto(a):
    if((a%4==0) and ((a%100!=0) or (a%400==0))):
        return True
    else:
        return False
     
# FUNCIÓN MÁXIMO DE DÍAS PARA UN MES
def Dias_Mes(m,b):
    if m in (1,3,5,7,8,10,12):
        return 31
    else:
        if m in (4,6,9,11):
            return 30
        else:
            if(b):
                return 29
            else:
                return 28

# FUNCIÓN INGRESA UN AÑO VÁLIDO
def Ingresa_Año(li,ls):
    print("Indique un año en el rango [",li,",",ls,"] = ", end=" ")
    x=int(input())
    while not(Rango(x,li,ls)):
        print("Valor fuera del rango intente nuevamente")
        print("Indique un año en el rango [",li,",",ls,"] = ", end=" ")
        x=int(input())
    return x  

# FUNCIÓN INGRESA UN MES VÁLIDO
def Ingresa_Mes():
    print("Indique un mes en el rango [1,12] = ", end=" ")
    x=int(input())
    while not(Rango(x,1,12)):
        print("Valor del mes fuera del rango intente nuevamente")
        print("Indique un mes en el rango [1,12] = ",end=" ")
        x=int(input())
    return x
 
# FUNCIÓN INGRESA UN DÍA VÁLIDO 
def Ingresa_Dia(nd):
    print("Indique un día en el rango [1,",nd,"] = ",end=" ")
    d=int(input())
    while not(Rango(d,1,nd)):
        print("Valor del día fuera del rango intente nuevamente")
        print("Indique un día en el rango [1,",nd,"] = ",end=" ")
        d=int(input())
    return d