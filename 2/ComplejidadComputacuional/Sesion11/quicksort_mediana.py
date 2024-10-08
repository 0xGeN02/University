def quicksort(lista, primero, ultimo):
    if primero < ultimo:
        # Dividimos la lista y obtenemos el pivote
        pivote = dividir_lista(lista, primero, ultimo)
        # Ordenamos recursivamente cada una de las dos sublistas
        quicksort(lista, primero, pivote - 1)
        quicksort(lista, pivote + 1, ultimo)

def mediana_de_tres(lista, primero, ultimo):
    medio = (primero + ultimo) // 2
    if lista[primero] > lista[medio]:
        lista[primero], lista[medio] = lista[medio], lista[primero]
    if lista[primero] > lista[ultimo]:
        lista[primero], lista[ultimo] = lista[ultimo], lista[primero]
    if lista[medio] > lista[ultimo]:
        lista[medio], lista[ultimo] = lista[ultimo], lista[medio]
    # Ahora el de en medio es el pivote, lo intercambiamos con el último para utilizar la misma lógica de partición
    lista[medio], lista[ultimo] = lista[ultimo], lista[medio]
    return lista[ultimo]

def dividir_lista(lista, primero, ultimo):
    # Utilizamos mediana de tres para elegir el pivote
    pivote = mediana_de_tres(lista, primero, ultimo)

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