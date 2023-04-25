# Programa LAB05_04
# Uso del Modulo_Matrices Entrada desde ficheros
# Realizado por: Eladio Dapena Gonzalez
# Uso académico
# Bibliotecas
import Modulo_Matrices as mat
# Inicio del programa
# Entrada de datos desde un fichero .csv
m_csv=mat.Entrada_CSV("DATA02.csv")
mat.Muestra_M(m_csv)
print("La suma total es = {:9.2f}".format(mat.Suma_M(m_csv)))
f=3
print("La fila [",f,"] suma = {:9.2f}".format(mat.Suma_M_Fila(m_csv,f)))
c=5
print("La columna [",c,"] suma = {:9.2f}".format(mat.Suma_M_Columna(m_csv,c-1)))
MA=mat.Mayor_M(m_csv)
print("El mayor elemento en [",MA[0]+1,",",MA[0]+1,"] = ",m_csv[MA[0]][MA[1]])
ME=mat.Menor_M(m_csv)
print("El menor elemento está en [",ME[0]+1,",",ME[0]+1,"] = ",m_csv[ME[0]][ME[1]])
ele=2538.01
x=mat.Busca_M(m_csv,ele)
if not -1 in x:
    print("El elemento (",ele,") está en [",x[0]+1,",",x[1]+1,"]")
else:
    print("Elemento [",ele,"] no está en la matriz")
suma_mayor=0
Fila_mayor=0
for i in range(len(m_csv)):
    sm=mat.Suma_M_Fila(m_csv,i)
    if(suma_mayor<sm):
        suma_mayor=sm
        Fila_mayor=i
print("Suma mayor en Fila [",Fila_mayor+1,"] = {:9.2f}".format(suma_mayor))