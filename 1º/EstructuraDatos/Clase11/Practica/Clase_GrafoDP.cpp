// FICHERO DECLARACIONES DE LA CLASE GrafoDP

#include "Clase_GrafoDP.h"

// Constructor de la clase
GrafoDP::GrafoDP(int V) {
    this->V = V;
    MA.resize(V, vector<float>(V, std::numeric_limits<float>::infinity()));
}

// Método: Agregar_Arista 
void GrafoDP::Agregar_Arista(int origen, int destino, float peso) {
    MA[origen][destino] = peso;
}

// Método: Muestra_GrafoDP 
void GrafoDP::Muestra_GrafoDP() {
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (MA[i][j] == std::numeric_limits<float>::infinity()) {
                std::cout << "INF ";
            }
            else {
                std::cout << MA[i][j] << " ";
            }
        }
        std::cout << std::endl;
    }
}

// Método Grado_Out.
int GrafoDP::Grado_Out(int v) {
    int grado = 0;
    for (int j = 0; j < V; j++) {
        if (MA[v][j] != std::numeric_limits<float>::infinity()) {
            grado++;
        }
    }
    return grado;
}

// Método Grado_In.
int GrafoDP::Grado_In(int v) {
    int grado = 0;
    for (int i = 0; i < V; i++) {
        if (MA[i][v] != std::numeric_limits<float>::infinity()) {
            grado++;
        }
    }
    return grado;
}

// Método: Caminos 
void GrafoDP::Caminos(int origen, int destino) {
    vector<bool> visitado(V, false);
    vector<int> camino;
    int num_caminos = 0;
    Buscar_CaminosAux(origen, destino, visitado, camino, num_caminos);
    if (num_caminos == 0) {
        std::cout << "No se encontraron caminos entre " << origen << " y " << destino << std::endl;
    }
}

// Método auxiliar para el método Caminos
void GrafoDP::Buscar_CaminosAux(int actual, int destino, vector<bool>& visitado, vector<int>& camino, int& num_caminos) {
    visitado[actual] = true;
    camino.push_back(actual);
    if (actual == destino) {
        for (auto v : camino) {
            std::cout << v << " ";
        }
        std::cout << std::endl;
        num_caminos++;
    }
    else {
        for (int j = 0; j < V; j++) {
            if (MA[actual][j] != std::numeric_limits<float>::infinity() && !visitado[j]) {
                Buscar_CaminosAux(j, destino, visitado, camino, num_caminos);
            }
        }
    }
    camino.pop_back();
    visitado[actual] = false;
}

// Método: Camino_Minimo_Dijkstra
// Parámetros: Enteros VO, VD. Vértices de Origen y Destino.
// Devuelve: Nada
void GrafoDP::Camino_Minimo_Dijkstra(int VO, int VD)
{
    // Vector para almacenar la distancia más corta desde el vértice origen hasta cada vértice
    vector<float> dist(V, numeric_limits<float>::max());
    // Vector para marcar si un vértice ya fue visitado
    vector<bool> visitado(V, false);
    // Vector para almacenar el camino más corto desde el vértice origen hasta cada vértice
    vector<int> camino(V, -1);
    
    // La distancia al vértice origen es cero
    dist[VO] = 0;
    
    // Se recorre todo el grafo
    for (int i = 0; i < V; i++) {
        // Se busca el vértice no visitado con menor distancia
        int v_actual = -1;
        for (int j = 0; j < V; j++) {
            if (!visitado[j] && (v_actual == -1 || dist[j] < dist[v_actual])) {
                v_actual = j;
            }
        }
        
        // Si no se encontró vértice disponible se sale del ciclo
        if (dist[v_actual] == numeric_limits<float>::max()) {
            break;
        }
        
        // Se marca el vértice actual como visitado
        visitado[v_actual] = true;
        
        // Se actualizan las distancias y los caminos de los vértices adyacentes al vértice actual
        for (int j = 0; j < V; j++) {
            if (MA[v_actual][j] != 0 && !visitado[j]) {
                float distancia = dist[v_actual] + MA[v_actual][j];
                if (distancia < dist[j]) {
                    dist[j] = distancia;
                    camino[j] = v_actual;
                }
            }
        }
    }
    
    // Si no se encontró un camino desde VO hasta VD se informa
    if (dist[VD] == numeric_limits<float>::max()) {
        cout << "No existe un camino desde " << VO << " hasta " << VD << endl;
    } else {
        // Se almacena el camino encontrado en un vector
        vector<int> recorrido;
        for (int v = VD; v != -1; v = camino[v]) {
            recorrido.push_back(v);
        }
        reverse(recorrido.begin(), recorrido.end());
        
        // Se muestra la distancia y el camino encontrado
        cout << "Distancia mínima desde " << VO << " hasta " << VD << ": " << dist[VD] << endl;
        cout << "Camino encontrado: ";
        for (int v : recorrido) {
            cout << v << " ";
        }
        cout << endl;
    }
}

//Camino_Minimo_BFS
void GrafoDP::Camino_Minimo_BFS(int VO, int VD) {
    vector<int> dist(V, INT_MAX); // Vector para almacenar las distancias mínimas desde el origen
    vector<int> previo(V, -1); // Vector para almacenar el nodo anterior en el camino mínimo
    
    queue<int> cola; // Cola para implementar el algoritmo BFS
    dist[VO] = 0; // La distancia del origen a sí mismo es 0
    cola.push(VO); // Insertamos el origen a la cola
    
    // Algoritmo BFS para recorrer el grafo y encontrar los caminos mínimos desde el origen
    while (!cola.empty()) {
        int actual = cola.front();
        cola.pop();
        
        // Iteramos sobre los nodos adyacentes al actual
        for (int i = 0; i < V; i++) {
            if (MA[actual][i] != 0) { // Si existe una arista entre el actual y el nodo i
                // Calculamos la distancia acumulada desde el origen al nodo i
                int distancia = dist[actual] + MA[actual][i];
                // Si encontramos una distancia menor que la previamente almacenada para i, la actualizamos
                if (distancia < dist[i]) {
                    dist[i] = distancia;
                    previo[i] = actual;
                    cola.push(i);
                }
            }
        }
    }
    
    // Imprimimos el camino mínimo encontrado, si existe
    if (dist[VD] != INT_MAX) {
        cout << "Camino mínimo desde " << VO << " a " << VD << ": " << endl;
        int actual = VD;
        stack<int> pila; // Utilizamos una pila para almacenar el camino mínimo
        while (actual != -1) {
            pila.push(actual);
            actual = previo[actual];
        }
        while (!pila.empty()) {
            cout << pila.top() << " ";
            pila.pop();
        }
        cout << endl;
        cout << "Distancia mínima: " << dist[VD] << endl;
    } else {
        cout << "No existe camino mínimo desde " << VO << " a " << VD << endl;
    }
}
