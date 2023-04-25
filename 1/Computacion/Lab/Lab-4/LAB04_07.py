# Programa Fecha
# Realizado por: Manuel Mateo
# Fecha: 19/11/2022
# Bibliotecas / Definiciones / Declaraciones
import Modulo_Fecha as f
# Declaraciones
# Entero Año, Mes, Día

#Inicio Programa Principal
Año=f.Ingresa_Año(2000,2022)
Mes=f.Ingresa_Mes()
Dia=f.Ingresa_Dia(f.Dias_Mes(Mes,f.Bisiesto(Año)))
print("Fecha",Dia,"/",Mes,"/",Año)
#Fin Principal
