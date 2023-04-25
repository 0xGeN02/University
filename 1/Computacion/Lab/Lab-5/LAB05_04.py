#Programa LAB05_04
import Modulo_Matrices as mat
#Inicio_Programa
m=mat.Crea_Matriz(2,3)
print("Filas   = ",len(m))
print("Columnas   = ",len(m[0]))
mat.Muestra_M(m)
mat.Entrada_M(m,int)
mat.Muestra_M(m)
m2=mat.CreaMatrizDato(4,4,0.0)
mat.Muestra_M(m2)

