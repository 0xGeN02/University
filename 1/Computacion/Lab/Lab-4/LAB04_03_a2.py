# Función Dias_Mes
# Regresa el máximo de días para un mes
# Parámetros
# Parámetro formal m mes Tipo Entero [1,12] (Validado)
# Parámetro formal b Tipo Lógico Verdadero si es año bisiesto
# Retorna el número de días del mes cosidera bisiesto
## Inicio de Función Dias_Mes
def Dias_Mes(m,b):
    if m in (1,3,5,7,8,10,12):
        return 31
    else:
        if m in(4,6,9,11):
            return 30
        else:
            if (b):
                return 29
            else:
                return 28
            
## Prueba Funcion
print("Mayo del 2022 tiene ", Dias_Mes(5,False), " días")
print("Febrero del 2020 tiene ", Dias_Mes(2,True), " días")