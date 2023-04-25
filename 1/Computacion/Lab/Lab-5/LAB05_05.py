# Programa LAB05_04
# Uso del Modulo_Matrices Entrada desde ficheros
# Realizado por: Mateo Delgado
# Uso académico
# Bibliotecas
import Modulo_Matrices as mat
# Inicio del programa
# Entrada de datos desde un fichero txt
m_txt=mat.Entrada_TXT("DATA01.txt")
print("Filas    = ",len(m_txt))
print("Columnas = ",len(m_txt[0]))
mat.Muestra_M(m_txt)
# Entrada de datos desde fichero .csv
m_csv=mat.Entrada_CSV("DATA02.csv")
print("Filas    = ",len(m_csv))
print("Columnas = ",len(m_csv[0]))
mat.Muestra_M(m_csv)
