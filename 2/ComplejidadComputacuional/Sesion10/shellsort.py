def ordenamiento_insercion(lista, salto):
    # Calcula el tamaño de la lista
    n = len(lista)
    # Recorre la lista desde el primer salto hasta el final
    for i in range(salto,n):
        # Toma el elemento a insertar
        nuevo_elemento = lista[i]
        indice = i
        # Si los elementos a la izquierda del elemento a insertar
        # son mayores que este, los desplaza hacia la derecha.
        while indice >= salto and lista[indice-salto] > nuevo_elemento:
            lista[indice] = lista[indice-salto]
            indice -= salto
        # Finalmente, inserta el elemento
        lista[indice] = nuevo_elemento
    return lista
    

def shellsort(lista):
    # Calcula el tamaño de la lista
    n = len(lista)
    # Calcula el tamaño del salto
    salto = n//2
    # Inicializa las pasadas
    pasada = 1
    # Mientras el salto no sea 0, ejecuta una pasada
    while salto > 0:
        print("Pasada: ", pasada)
        # Ordena la sublista por inserción
        lista = ordenamiento_insercion(lista, salto)
        print(lista)
        # Divide el salto a la mitad
        salto //= 2
        # Incrementa las pasadas
        pasada += 1

lista = [16,7,10,1,13,11,3,8,14,4,2,12,6,5,9,15]
print("Lista desordenada:")
print (lista)
print()

shellsort(lista)

print ()
print("Lista ordenada:")
print (lista)