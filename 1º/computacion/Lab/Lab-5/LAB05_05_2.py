# Programa LAB05_04
# Uso del Modulo_Matrices Entrada desde ficheros
# Realizado por: Eladio Dapena Gonzalez
# Uso académico
# Bibliotecas
import Modulo_Matrices as mat

# Inicio del programa
# Entrada de datos desde un fichero txt
m_txt=mat.Entrada_TXT("DATA01.txt")

print(" Filas = ",len(m_txt))
print("Columnas = ",len(m_txt[0]))

print()

print(m_txt)