def merge(lista, primero, medio, ultimo):
    # Calcula el tamaño de cada mitad
    n_izquierda = medio - primero + 1
    n_derecha = ultimo - medio

    # Crea dos listas temporales, una para cada mitad
    izquierda = [0] * (n_izquierda)
    derecha = [0] * (n_derecha)

    # Copia los elementos de cada mitad a las listas temporales
    for i in range(0, n_izquierda):
        izquierda[i] = lista[primero + i]

    for j in range(0, n_derecha):
        derecha[j] = lista[medio + 1 + j]

    # Mezcla ambas mitades en la lista original
    i = 0	 # Índice de la lista izquierda
    j = 0	 # Índice de la lista derecha
    k = primero	 # Índice de la lista mezcla

    while i < n_izquierda and j < n_derecha:
        if izquierda[i] <= derecha[j]:
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    # Copia los elementos restantes de la lista izquierda
    while i < n_izquierda:
        lista[k] = izquierda[i]
        i += 1
        k += 1

    # Copia los elementos restantes de la lista derecha
    while j < n_derecha:
        lista[k] = derecha[j]
        j += 1
        k += 1


def mergesort(lista, primero, ultimo):
    if primero < ultimo:
        # Halla el medio de la lista
        medio = (primero + ultimo) // 2
        # Divide la lista en dos mitadas y las ordena recursivamente
        mergesort(lista, primero, medio)
        mergesort(lista, medio+1, ultimo)
        # Mezcla las listas
        merge(lista, primero, medio, ultimo)


# Driver code to test above
lista = [4,8,23,15,16,42]
n = len(lista)
print("Lista original:", lista)
mergesort(lista, 0, n-1)
print("Lista ordenada:", lista)
