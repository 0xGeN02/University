// FICHERO CABECERA DE LA CLASE GrafoDP
#ifndef GRAFO_DP_H
#define GRAFO_DP_H
// Inclusión de Bibliotecas
#include <iostream>
#include <string>     // Biblioteca Estándar C++
#include <vector>     // Biblioteca Estándar C++
#include <queue>      // Biblioteca Estándar C++
#include <stack>      // Biblioteca Estándar C++
#include <algorithm>  // Biblioteca Estándar C++
#include <limits>     // Biblioteca Estándar C++
using namespace std;

class GrafoDP {
    // Agregar todo lo requerido para la definición de la clase
    private:
    int V;
    vector<vector<float>> MA; // Matriz de adyacencia
    public:
    // Constructor de la clase
    // Parámetro: Entero V. Número de Vértices
    GrafoDP(int);
    // Método: Agregar_Arista 
    void Agregar_Arista(int, int, float);
    // Método: Muestra_GrafoDP 
    void Muestra_GrafoDP();
    // Método Grado_Out.
    int Grado_Out(int);
    // Método Grado_In.
    int Grado_In(int);
    // Método: Caminos 
    void Caminos(int, int);
    // Método auxiliar para el método Caminos
    void Buscar_CaminosAux(int, int, vector<bool>&, vector<int>&, int&);
    // Método: Camino_Minimo_Dijkstra 
    void Camino_Minimo_Dijkstra(int, int);
    // Método: Camino_Minimo_BFS
    void Camino_Minimo_BFS(int VO, int VD);

};

#endif // GRAFO_DP_H