# Módulo: Modulo_Matrices
# Funciones para operaciones con matrices

# Bibliotecas
import random as r
import Modulo_Vectores as vec

# Función Crea_Matriz
### Crea una matriz de f Filas y c Columnas sin valores
## Parámetros
### Parámetro formal f Entero número de filas
### Parámetro formal c Entero número de columnas
## Retorna la matriz creada
## Inicio de Función Crea_Matriz
def Crea_Matriz(f,c):
    m = []
    for i in range(f):
        a = [None]*c
        m.append(a)
    return m
## Fin de Función Crea_Matriz  

# Función Crea_Matriz_Dato
### Crea una matriz de f Filas y c Columnas inicializada en dato
## Parámetros
### Parámetro formal f Entero número de filas
### Parámetro formal c Entero número de columnas
### Parámetro formal d Valor del dato de inicialización
## Retorna la matriz creada
## Inicio de Función CreaMatrizDato
def CreaMatrizDato(n,m,d):
    matriz = []
    for i in range(n):
        a = [d]*m
        matriz.append(a)
    return matriz 
## Fin de Función CreaMatrizDato

# Función Crea_Matriz_Letras
### Crea una matriz de f Filas y c Columnas de letras aleatoria
## Parámetros
### Parámetro formal f Entero número de filas
### Parámetro formal c Entero número de columnas
## Retorna la matriz creada
## Inicio de Función Crea_Matriz_Letras
def Crea_Matriz_Letras(n,m):
    matriz = []
    for i in range(n):
        a=[]
        for j in range(m):
            a.append(chr(r.randint(65,90))) 
        matriz.append(a)
    return matriz 
## Fin de Función Crea_Matriz_Letras
#
# FUNCIONES DE ENTRADA DE ELEMENTOS DE UNA MATRIZ
#
# Función Entrada_M
### Entrada de datos a una matriz desde teclado
## Parámetros
### Parámetro formal m Matriz
### Parámetro formal tipo Tipo de dato (float,int,str,bool)
### Parámetro formal smsF Mensaje para filas por defecto Fila
### Parámetro formal smsC Mensaje para Columna por defecto Columna
## Retorna la matriz con los datos
## Inicio de Función Entrada_M
def Entrada_M(m,tipo,smsF="Fila",smsC="Columna"):
    for i in range(len(m)):
        print("Indique elementos ",smsF," : ",i+1," : ")
        for j in range(len(m[0])):
            print("   ",smsC," : ",j+1," : ",end=" ")
            m[i][j]=tipo(input())
            print()
    return m
## Fin de Función Entrada_M

# Función Entrada_CSV
# Parámetros
##  file     Nombre del fichero .csv (debe estar en el directorio)
# Retorna Una Matriz con los datos del fichero csv
## Inicio de Función Entrada_CSV
def Entrada_CSV(file,TIPO=float):
    import csv
    with open(file) as f:
        a = [[TIPO(x) for x in row] for row in csv.reader(f)]
    f.close()
    return a
## Fin de Función Entrada_CSV

# ENTRADA DE DATOS DESDE UN FICHERO txt A UNA MATRIZ
# Función Entrada_TXT
# Entrada de datos desde u fichero .txt separados por ","
# Parámetros
##  file     Nombre del fichero .txt (debe estar en el directorio)
# Retorna Una Matriz con los datos del fichero txt
## Inicio de Función Entrada_TXT
def Entrada_TXT(file,TIPO=float):
    f = open(file)
    fila = f.read()
    f.close()
    a = [[TIPO(i) for i in k.split(",")] for k in fila.split("\n")]
    return a
## Fin de Función Entrada_TXT
#
# MOSTRAR ELEMENTOS DE LA MATRIZ
#
# Función Muestra_M
### Entrada de datos a una matriz desde teclado
## Parámetros
### Parámetro formal m Matriz
### Parámetro formal smsT título por defecto Matriz
## Retorna No regresa valores
## Inicio de Función Muestra_M
def Muestra_M(m,smsT="  Matriz "):
    print(smsT)
    for i in range(len(m)):
        print("|",end=" ")
        for j in range(len(m[0])):
            print(m[i][j],end=" ")
        print("|")
## Fin de Función Muestra_M

#
# OPERACIONES CON FILAS Y COLUMNAS
#
# SUMA ELEMENTOS DE UNA MATRIZ
# Función Suma_M
### Suma todos los elementos de una matriz
## Parámetros
### Parámetro formal m Matriz
## Retorna La suma de los elementos
## Inicio de Función Suma_M
def Suma_M(m):
    s=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            s=s+m[i][j]
    return s
## Fin de Función Suma_M

# SUMA ELEMENTOS DE UNA FILA DE UNA MATRIZ
# Función Suma_M_Fila
### Suma los elementos de una fila de una matriz
## Parámetros
### Parámetro formal m Matriz
### Parámetro formal f Fila a sumar
## Retorna La suma de los elementos de la fila indicada
## Inicio de Función Suma_M_Fila
def Suma_M_Fila(m,f):
    return vec.Suma_V(m[f])
## Fin de Función Suma_M_Fila
    
# SUMA ELEMENTOS DE UNA COLUMNA DE UNA MATRIZ
# Función Suma_M_Col
### Suma los elementos de una coloumna de una matriz
## Parámetros
### Parámetro formal m Matriz
### Parámetro formal c columna a sumar
## Retorna La suma de los elementos de la columna indicada
## Inicio de Función Suma_M_Columna      
def Suma_M_Columna(m,c):
    return vec.Suma_V(Columa_Vector_M(m,c))
## Fin de Función Suma_M_Columna

# Función Columa_Vector_M
### Crea un vector con los elementos de una columna
## Parámetros
### Parámetro formal m Matriz
### Parámetro formal c columna
## Retorna vector con los elementos de la columna
## Inicio de Función Columna_Vector
def Columa_Vector_M(m,c):
    v=vec.Crea_Vector(len(m))
    for i in range(len(v)):
        v[i]=m[i][c]
    return v
## Fin de Función Columna_Vector

# MAYOR ELEMENTO DE UNA MATRIZ           
# Función Mayor_M
### Busca el mayor elemento de una matriz
## Parámetros
### Parámetro formal m Matriz
## Retorna una vector con la fila y columna
## Inicio de Función Mayor_M
def Mayor_M(m):
    Pos=[0,0];mayor=m[0][0]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if mayor<m[i][j]:
                Pos=[i,j]; mayor=m[i][j]
    return Pos
## Fin de Función Mayor_M

# MENOR ELEMENTO DE UNA MATRIZ  
# Función Menor_M
### Busca el menor elemento de una matriz
## Parámetros
### Parámetro formal m Matriz
## Retorna un vector con la fila y columna
## Inicio de Función Menor_M         
def Menor_M(m):
    Pos=[0,0];menor=m[0][0]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if menor>m[i][j]:
                Pos=[i,j]; menor=m[i][j]
    return Pos
## Fin de Función Menor_M

# BUSCAR UN ELEMENTO EN UNA MATRIZ
# Función Busca_M
### Busca un elemento en una matriz
## Parámetros
### Parámetro formal m Matriz
### Parámetro formal e (elemnto a buscar)
## Retorna un vector con la fila y columna
### Si no lo encuentra retorna el vector [-1,-1]
## Inicio de Función Busca_M         
def Busca_M(m,e):
    Pos=[-1,-1]
    i=0
    while (i<len(m)):
        j=0
        while (j<len(m[0])):
            if m[i][j]==e:
                Pos=[i,j]
                j=len(m[0])
                i=len(m)
            else:
                j=j+1
        i=i+1
    return Pos
## Fin de Función Busca_M 