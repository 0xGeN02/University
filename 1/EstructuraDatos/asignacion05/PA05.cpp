#include "Asig05.h"

int NUM_ALEA_P4(){
    return rand() % 100001;
}

int main() {
    srand(time(0));

    // Crear las estructuras de datos
    vector<int> numeros;
    list<int> lista;
    BinarySearchTree bst;

    // Generar 50.000 números aleatorios y agregarlos a las estructuras de datos
    for (int i = 0; i < 50000; i++) {
        int num = NUM_ALEA_P4();
        numeros.push_back(num);
        lista.push_back(num);
        bst.insert(num);
    }

    // Elemento a buscar
    int search_element = numeros[0]; // Mejor caso para la lista y el vector.
    int non_existent_element = 100001; // Peor caso.

    // Medición de tiempo para la búsqueda en el vector
    auto start = chrono::high_resolution_clock::now();
    linear_search(numeros, search_element);
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> diff = end-start;
    cout << "Vector search time: " << diff.count() << " s\n";

    // Medición de tiempo para la búsqueda en la lista
    start = chrono::high_resolution_clock::now();
    linear_search(lista, search_element);
    end = chrono::high_resolution_clock::now();
    diff = end-start;
    cout << "List search time: " << diff.count() << " s\n";

    // Medición de tiempo para la búsqueda en el árbol binario
    start = chrono::high_resolution_clock::now();
    bst.search(search_element);
    end = chrono::high_resolution_clock::now();
    diff = end-start;
    cout << "Binary tree search time: " << diff.count() << " s\n";

    // Medición de tiempo para el peor caso en el vector
    start = chrono::high_resolution_clock::now();
    linear_search(numeros, non_existent_element);
    end = chrono::high_resolution_clock::now();
    diff = end-start;
    cout << "Vector worst case search time: " << diff.count() << " s\n";

    // Medición de tiempo para el peor caso en la lista
    start = chrono::high_resolution_clock::now();
    linear_search(lista, non_existent_element);
    end = chrono::high_resolution_clock::now();
    diff = end-start;
    cout << "List worst case search time: " << diff.count() << " s\n";

    // Medición de tiempo para el peor caso en el árbol binario
    start = chrono::high_resolution_clock::now();
    bst.search(non_existent_element);
    end = chrono::high_resolution_clock::now();
    diff = end-start;
    cout << "Binary tree worst case search time: " << diff.count() << " s\n";

    return 0;
}
