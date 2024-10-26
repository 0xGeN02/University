/*****************************************
* Asignatura: Estructura de Datos        *
* Sesión 11 TDA Grafo NO DIRIGIDO        *
* Ejemplo 05. RECORRIDO GrafoND          *
* Definición Clase GrafoND               *
* Representación: Matriz de Adyacencia   *
*   Métodos    BFS y DFS                 *
* Programa de uso académico              *
* Adaptado por: Eladio Dapena Gonzalez   *
* Fecha: 25/03/2023                      *
*****************************************/
#include <iostream>
#include <string> // Biblioteca Estándar C++
#include <vector> // Biblioteca Estándar C++
#include <queue>  // Biblioteca Estándar C++
using namespace std;
// Clase GrafoND  Grafo No Dirigido
class GrafoND 
{
 private:
  int V;
  vector<vector<int>> MA; // Matriz de adyacencia
 public:
 // Constructor de la clase
 GrafoND(int);
// Método: Agregar_Arista 
 void Agregar_Arista(int,int);
// Método: Muestra_GrafoND 
 void Muestra_GrafoND();
// Método Grado.
int Grado(int);
// Método BFS. Recorrido en Amplitud
void BFS(int);
// Método DFS. Recorrido en Profundidad
 void DFS(int);
// Método Auxilir Recursivo DFS_AUX.
 void  DFS_AUX(int, vector<bool>&);
};

// Program principal
int main() 
{
// Crear un objeto tipo grafo No dirigido de 6 vértices
 GrafoND GND(6); 
 // Agregar Aristas
 GND.Agregar_Arista(0, 1);
 GND.Agregar_Arista(0, 2);
 GND.Agregar_Arista(1, 2);
 GND.Agregar_Arista(1, 3);
 GND.Agregar_Arista(1, 4);
 GND.Agregar_Arista(2, 3);
 GND.Agregar_Arista(2, 4);
 GND.Agregar_Arista(2, 5);
 GND.Agregar_Arista(3, 4);
 GND.Agregar_Arista(3, 5);
 GND.Agregar_Arista(4, 5);
 // Mostrar Los nodos, su grado y conexiones
 cout<<"***   Grafo No Dirigido   ***"<<endl;
 GND.Muestra_GrafoND();
  cout<< "--- BFS RECORRIDO EN ANCHURA. VI = 0"<<endl;
  for (int k=0;k<6;k++)
 {
    cout<<"\tVERTICE "<<k<<" : ";
    GND.BFS(k);
 //   cout<<endl;
 }
 cout<< "--- DFS RECORRIDO EN PROFUNDIDAD. VI = 0"<<endl;
  for (int k=0;k<6;k++)
 {
    cout<<"\tVERTICE "<<k<<" : ";
    GND.DFS(k);
//    cout<<endl;
 }
 return 0;
}

// DECLARACIONES DE LA CLASE GrafoND
 // Constructor de la clase
 // Parámetro: Entero V. Número de Vértices
 GrafoND::GrafoND(int V) 
  {
    this->V = V;
    MA = vector<vector<int>>(V, vector<int>(V, 0));
  }

// Método: Agregar_Arista 
// Agrega una arista al grafo
// Parámetros. 
//  vs: Entero. Vértice de Salida
//  ve: Entero. Vértice de Entrada
 void  GrafoND::Agregar_Arista(int v, int w) 
 {
  MA[v][w] = 1;
  MA[w][v] = 1;
 }

// Método: Muestra_GrafoND 
// Muestra.
// Vértice/Grado/Adyacentes
// Parámetros. NO 
 void  GrafoND::Muestra_GrafoND() 
 {
  string S;
  for (int i = 0; i < V; i++) 
  {
   cout << "\tVERTICE " << i << ": ";
   S=" ";
   for (int j = 0; j < V; ++j)
   {
    if (MA[i][j]!=0)
    {
     S=S+to_string(j)+ " ";
    }
   }
   cout << "\tGrado : "<< Grado(i) << "\tAdyacentes : " <<S<<endl;
 }
}

// Método Grado.
// Retorna el grado de un Vértice
// Parámetros.
//    n: Entero. Número del Vértice
int  GrafoND::Grado(int n)
{
 int g=0;
 for (int i = 0; i < V; i++)
  if (MA[n][i]!=0) 
   g++; 
 return g;
}

// Recorrido en anchura
// Método BFS.
// Recorrido en amplitud de un grafo
// Parámetros.
//    n: Entero. Vértice
void  GrafoND::BFS(int VI) 
{
 vector<bool> visitado(V, false);
 queue<int> fila;
 visitado[VI] = true;
 fila.push(VI);
 while (!fila.empty()) 
 {
  int actual = fila.front();
  cout << actual << " ";
  fila.pop();
  for (int i = 0; i < V; i++) 
  {
   if (MA[actual][i] == 1 && !visitado[i]) 
   {
    visitado[i] = true;
    fila.push(i);
   }
  }
 }
  cout << endl;
}

// Recorrido en Profundidad
// Método DFS.
// Recorrido en profundidad de un grafo
// Implementación recursiva
// Parámetros.
//    n: Entero. Vértice
 void  GrafoND::DFS(int VI) 
 {
  vector<bool> visitado(V, false);
  DFS_AUX(VI, visitado);
  cout << endl;
 }
 // Rutina recursiva que complementa DFS
 void  GrafoND::DFS_AUX(int v, vector<bool>& visitado) 
 {
  visitado[v] = true;
  cout << v << " ";
  for (int i = 0; i < V; i++) 
  {
   if (MA[v][i] == 1 && !visitado[i]) 
   {
     DFS_AUX(i, visitado);
   }
  }
 }

