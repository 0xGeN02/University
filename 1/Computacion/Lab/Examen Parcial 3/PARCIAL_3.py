# PRUEBA PARCIAL 3
# PARTE 2 PRÁCTICA
# Nombre y apellido:     
# Bibliotecas / Definiciones / Declaraciones
import Modulo_Vectores as vec
import Modulo_Matrices as mat
# PARCIAL 3 PARTE 2

# APARTADO 01
M=mat.Entrada_TXT("DATACORUÑAA.txt")
print("Filas    : ",len(M))
print("Columnas : ",len(M))



# APARTADO 02
print("Fila 35 suma : {:2.2f}".format(mat.Suma_M_Fila(M,34)))
print("Fila 28 suma : {:2.2f}".format(mat.Suma_M_Fila(M,27)))



# APARTADO 03
print("Columna 4 suma : {:2.2f}".format(mat.Suma_M_Columna(M,3)))
print("Columna 13 suma : {:2.2f}".format(mat.Suma_M_Columna(M,12)))



# APARTADO 04
MEN=mat.Menor_M(M)
print("El menor elemento está en : [",MEN[0]+1,",",MEN[1]+1,"]")
print("El valor del menor es     : {:2.2f}".format(M[MEN[0]][MEN[1]]))



# APARTADO 05
print("La Suma de la matriz M es : {:2.2f}".format(mat.Suma_M(M)))