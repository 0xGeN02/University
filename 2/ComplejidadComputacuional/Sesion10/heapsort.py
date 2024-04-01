# Implementa la operación Insertar (sift up)
def sift_up(heap, indice_nodo):
    # Halla el elemento padre del nodo a insertr
    indice_padre = (indice_nodo - 1) // 2
    # Si el padre es menor que el nodo hijo, los intercambia
    if indice_padre >= 0 and heap[indice_nodo] > heap[indice_padre]:
        heap[indice_nodo], heap[indice_padre] = heap[indice_padre], heap[indice_nodo]
        # Repite el proceso recursivamente
        sift_up(heap, indice_padre)

# Implementa la operación Hundir (sift down)
def sift_down(heap, nodo, heap_size):
    # Inicializa el valor mayor con el valor del nodo
    mayor = nodo
    # Obtiene los hijos izquierdo y derecho
    hijo_izquierdo = 2 * nodo + 1
    hijo_derecho = 2 * nodo + 2

    # Calcula cuál de los dos hijos tiene el mayor valor
    if hijo_izquierdo < heap_size and heap[hijo_izquierdo] > heap[mayor]:
        mayor = hijo_izquierdo
    if hijo_derecho < heap_size and heap[hijo_derecho] > heap[mayor]:
        mayor = hijo_derecho

    # Intercambia el nodo por el mayor de sus hijos
    if mayor != nodo:
        heap[nodo], heap[mayor] = heap[mayor], heap[nodo]
        # Repite el proceso recursivamente
        sift_down(heap, mayor, heap_size)

def heap_sort(lista):
    # Fase 1: Construye el heap máximo
    for i in range(1, len(lista)):
        sift_up(lista, i)

    # Fase 2: Extrae sucesivamente la raíz del heap
    for i in range(len(lista) - 1, 0, -1):
        # Extrae la raíz del árbol y la mueve al final del heap
        lista[0], lista[i] = lista[i], lista[0]
        # Restablece la condicion de heap máximo
        sift_down(lista, 0, i)

lista = [4,8,23,15,16,42]
print("Lista original:", lista)
heap_sort(lista)
print("Lista ordenada:", lista)