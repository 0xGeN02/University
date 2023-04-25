// FICHERO CABECERA DE LA CLASE GrafoND
#ifndef GRAFO_ND_H
#define GRAFO_ND_H
// Inclusión de Bibliotecas
#include <iostream>
#include <string>     // Biblioteca Estándar C++
#include <vector>     // Biblioteca Estándar C++
#include <queue>      // Biblioteca Estándar C++
#include <stack>      // Biblioteca Estándar C++
#include <algorithm>  // Biblioteca Estándar C++
#include <limits>     // Biblioteca Estándar C++
using namespace std;
// Clase GrafoND  Grafo No Dirigido
class GrafoND 
{
 private:
  int V;
  vector<vector<float>> MA; // Matriz de adyacencia simétrica
 public:
  // Constructor de la clase
  // Parámetro: Entero V. Número de Vértices
  GrafoND(int);
  
  // Método: Agregar_Arista 
  void Agregar_Arista(int, int, float);
  
  // Método: Muestra_GrafoND 
  void Muestra_GrafoND();
  
  // Método Grado
  int Grado(int);
  
  // Método: Caminos 
  void Caminos(int, int);
  
  // Método auxiliar para el método Caminos
  void Buscar_CaminosAux(int, int, vector<bool>&, vector<int>&, int&);
  
  // Método: Camino_Minimo_Dijkstra 
  void Camino_Minimo_Dijkstra(int, int);
  
  // Método: Camino_Minimo_BFS
  void Camino_Minimo_BFS(int, int);
};

#endif // GRAFO_ND_H