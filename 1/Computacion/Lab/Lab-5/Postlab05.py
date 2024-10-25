Lista_Sucursales = [Santiago, Vigo, COruña, Ponteverda, Orense, Lugo, Ferrol, Rianxo, Monforte]
Lista_Productos = [Lacon, Bacon, Raxo, Chorizo, Jamon, Lomo, Calamares]

import Modulo_Matrices as mat
import Modulo_Vectores as vec

#1-Ingresos semana total
#2-Ingresos semana sucursal
#3-Ingresos semana producto
#4-Mayor ingreso semana, mat 3D(cantidad, sucursal, producto)
#5-Menor ingreso semana, mat 3D(cantidad, sucursal, producto)
#6-Mejor Sucursal
#R1-Reorganizar fichero y menu opciones
#R2-Producto genera mas ingresos
#R3-Producto genera menos ingresos

#1-Ingresos Semana Total

m_csv = mat.Entrada_CSV("DATA03.csv")
print("Filas    = ", len(m_csv))
print("Columnas = ", len(m_csv[0]))
mat.Muestra_M(m_csv)

def Ingresos_Totales(Lista_Sucursal, Lista_Producto):
    sum 

