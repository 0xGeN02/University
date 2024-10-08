# Implementa la operación Insertar (sift up)
# heap: lista que representa el heap o montículo.
# indice_nodo: índice del nodo que se desea insertar.
def sift_up(heap, indice_nodo):
    # Halla el índice del elemento padre del nodo a insertar
    indice_padre = (indice_nodo - 1) // 2
    # Si el padre es menor que el nodo hijo, los intercambia
    if (indice_padre >= 0) and (heap[indice_nodo] > heap[indice_padre]):
        heap[indice_nodo], heap[indice_padre] = heap[indice_padre], heap[indice_nodo]
        print("Sift up:", heap)
        # Repite el proceso
        sift_up(heap, indice_padre)

# Implementa la operación Hundir (sift down)
# heap: lista que representa el heap o montículo.
# indice_nodo: índice del nodo que se desea insertar.
# heap_size: tamaño del heap.
def sift_down(heap, indice_nodo, heap_size):
    # Inicializa el valor mayor con el valor del nodo actual
    indice_mayor = indice_nodo
    # Obtiene los hijos izquierdo y derecho
    indice_hijo_izquierdo = 2 * indice_nodo + 1
    indice_hijo_derecho = 2 * indice_nodo + 2

    # Calcula cuál de los dos hijos tiene el mayor valor
    if (indice_hijo_izquierdo < heap_size) and (heap[indice_hijo_izquierdo] > heap[indice_mayor]):
        indice_mayor = indice_hijo_izquierdo
    if (indice_hijo_derecho < heap_size) and (heap[indice_hijo_derecho] > heap[indice_mayor]):
        indice_mayor = indice_hijo_derecho

    # Intercambia el nodo por el mayor de sus hijos
    if indice_mayor != indice_nodo:
        heap[indice_nodo], heap[indice_mayor] = heap[indice_mayor], heap[indice_nodo]
        print("Sift down:", heap)
        # Repite el proceso
        sift_down(heap, indice_mayor, heap_size)

# Implementa el algoritmo heapsort
# lista: lista a ordenar.
def heapsort(lista):
    # Fase 1: Construye el heap
    print()
    print("Construcción del heap:")
    print()
    for i in range(1, len(lista)):
        sift_up(lista, i)

    # Fase 2: Extrae sucesivamente la raíz del heap
    print()
    print("Extracción sucesiva de la raíz del heap:")
    print()
    for i in range(len(lista) - 1, 0, -1):
        # Extrae la raíz del árbol y la mueve al final del heap
        lista[0], lista[i] = lista[i], lista[0]
        print("Elemento extraido:", lista[i])
        # Restablece la condicion de heap
        sift_down(lista, 0, i)

# Punto de inicio del programa
lista = [8,4,23,15,42,16]
print("Lista original:", lista)
heapsort(lista)
print("Lista ordenada:", lista)