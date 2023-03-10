# Modulo_Vectores
# Realizado por: Eladio Dapena Gonzalez
# Funciones para operaciones con vectores
# Uso Académico

# Función Crea_Vector
# Crea un vector del tamaño indicado sin valores.
# Parámetros
# Parámetro formal n Entero Tamaño del vector
# Retorna el vector creado
# Inicio de Función Crea_Vector
def Crea_Vector(n):
    a = [None]*n
    return a
# Fin de Función Crea_Vector

# Función Crea_Vector_Tipo
# Crea un vector del tamaño n inicializado.
# Parámetros
# Parámetro formal n Entero Tamaño del vector
# Parámetro formal Valor de inicialización del vector
# Retorna el vector creado
# Inicio de Función Crea_Vector
def Crea_Vector_Valor(n,Valor):
    a = [Valor]*n
    return a
# Fin de Función Crea_Vector de un tipo de datos

## Agregar funciones de operaciones comunes con vectores
# ENTRADA DE ELEMENTOS DE UN VECTOR
# Función Entrada_Vector
### Leer los elementos de un vector
## Parámetros
### Parámetro formal v Vector
## Retorna el vector con los datos
## Inicio de Función Entrada_Vector
def Entrada_V(v,tipo):
    for i in range(len(v)):
        print("Indique el elemento ",i+1," = ",end=" ")
        v[i]=tipo(input())
    return v
## Fin de Función Entrada_Vector

# MOSTRAR ELEMENTOS DE UN VECTOR
# Función Muestra_V
### Muestra los elementos de un vector
## Parámetros
### Parámetro formal v Vector
## Retorna (Sin retorno)
## Inicio de Función Muestra_V
def Muestra_V(v):
    print("[",end=" ")
    for i in range(len(v)):
        print(v[i]," ",end=" ")
    print("]")   
 ## Fin de Función Muestra_V


# SUMA ELEMENTOS DE UN VECTOR
# Función Suma_V
### Suma elementos de un vector
## Parámetros
### Parámetro formal v Vector
## Retorna Suma
## Inicio de Función Suma_V
def Suma_V(v):
    s=0
    for i in range(len(v)):
        s=s+v[i]
    return s
## Fin de Función Suma_V

       
# MAYOR ELEMENTO DE UN VECTOR           (ASIGNACIÓN 08)
# Función Mayor_V
### Busca el mayor elemento de un vector
## Parámetros
### Parámetro formal v Vector
## Retorna pos Posición del mayor elemento
## Inicio de Función Mayor_V
def Mayor_V(v):
    if len(v)>0:
        mayor=v[0]; pos=0
        for i in range(len(v)):
            if mayor<v[i]:
                mayor=v[i]
                pos=i
    return pos
## Inicio de Función Mayor_V

# MENOR ELEMENTO DE UN VECTOR           (ASIGNACIÓN 08)
# Función Menor_V
### Busca el menor elemento de un vector
## Parámetros
### Parámetro formal v Vector
## Retorna pos Posición del menor elemento
## Inicio de Función Menor_V
def Menor_V(v):
    if len(v)>0:
        menor=v[0]; pos=0
        for i in range(len(v)):
            if menor>v[i]:
                menor=v[i]
                pos=i
    return pos
## Fin de Función Menor_V

# BUSCAR UN ELEMENTO EN UN VECTOR       (ASIGNACIÓN 08)
# Función Busca_V
### Busca un elemento en un vector
## Parámetros
### Parámetro formal v Vector
### Parámetro formal e Elemento a buscar
## Retorna pos Posición del elemento o -1 si no lo encuentra
## Inicio de Función Busca_V
def Busca_V(a,e):
    i=0
    Encuentra=False
    while ((i<len(a)) and not(Encuentra)):
        if (a[i]==e):
            Encuentra=True
        else:
            i+=1
    if Encuentra:
        return i+1
    else:
        return -1
## Fin de Función Busca_V


# MEDIA DE LOS ELEMENTOS DE UN VECTOR   (ASIGNACIÓN 08)
def Media(x):
    return (Suma_V(x)/len(x))


# INTERCAMBIAR                          (ASIGNACIÓN 08)
def Cambia_V(v,p1,p2):
    p1-=1; p2-=1
    if ((p1 in range(len(v))) and (p2 in range(len(v)))):
        aux=v[p1]; v[p1]=v[p2]; v[p2]=aux
    return v

# ORDENAR LOS ELEMENTOS DE UN VECTOR    (RETO)
# Función Ordena_V
### Ordena los elementos de un vector
## Parámetros
### Parámetro formal v Vector
### Parámetro formal o (0:Ascendente, 1 Descendente)
## Retorna pos Posición del elemento o -1 si no lo encuentra
## Inicio de Función Busca_V
def Ordena_V(v,o):
    for i in range(len(v)-1):
        j=i+1
        for j in range(len(v)):
            if (o==0):
                if (v[i]>v[j]):
                    aux=v[i]; v[i]=v[j];v[j]=aux
            else:
                if (v[i]<v[j]):
                    aux=v[i]; v[i]=v[j];v[j]=aux
    return v