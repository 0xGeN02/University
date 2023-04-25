# Función Bisiesto
# Verifica si un año es bisiesto. Retorna Verdadero si es bisiesto
# Parámetros
# Parámetro formal  a  Tipo Entero año para verificar
# Retorna Verdadero si el año es bisiesto
## Inicio de Función Bisiesto

def Bisiesto(a):
    if ((a%4 == 0) and ((a%100 != 0) or (a%400 == 0))):
        return True
    else:
        return False
# Fin Funcion BIsiesto