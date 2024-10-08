def quicksort(lista, primero, ultimo):
    if primero < ultimo:
        # Dividimos la lista y obtenemos el pivote
        pivote = dividir_lista(lista, primero, ultimo)
        # Ordenamos recursivamente cada una de las dos sublistas
        quicksort(lista, primero, pivote - 1)
        quicksort(lista, pivote + 1, ultimo)

def dividir_lista(lista, primero, ultimo):  
    # Tomamos como pivote el último elemento de la lista
    pivote = lista[ultimo]

    # Inicializamos el apuntador
    i = primero - 1

    # Recorremos la lista desde el primer hasta el último elemento
    for j in range(primero, ultimo):
        # Comprobamos si el elemento es menor o igual que el pivote
        if lista[j] <= pivote:
            # En caso afirmativo, incrementamos el apuntador
            i = i + 1
            # E intercambiamos los elementos
            lista[i], lista[j] = lista[j], lista[i]

    # Intercambiamos el pivote con el siguiente elemento indicado por el apuntador.
    lista[i + 1], lista[ultimo] = lista[ultimo], lista[i + 1]

    # Devolvemos la posición del pivote
    return i + 1

lista = [8, 4, 23, 15, 42, 16]
primero = 0
ultimo = len(lista) - 1
print(lista)
quicksort(lista, primero, ultimo)
print(lista)