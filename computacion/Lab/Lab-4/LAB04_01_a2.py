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
#Fin Funcio Rango

P1 = Rango(15,1,12)
print("P1 = ",P1)
a = 100; b = 0; c = 1000
P2 = Rango(a,b,c)
print("P2 =",P2)