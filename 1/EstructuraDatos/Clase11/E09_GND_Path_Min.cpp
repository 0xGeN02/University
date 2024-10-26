/********************************************
* Asignatura: Estructura de Datos           *
* Sesión 11 TDA Grafo NO DIRIGIDO           *
* Ejemplo 09. Camino Mínimo dos vértices    *
* Definición Clase GrafoND                  *
* Representación: Matriz de Adyacencia      *
*  Métodos   Camino Mínimo                  *
*    Algoritmo de Dijkstra                  *
*    Algoritmo BFS* (Modificado)            * 
* Referencias:                              *
* Libro: Luis Joyanes(2007) Data Structures *
* Programa de uso académico                 *
* Adaptado por: Eladio Dapena Gonzalez      *
* Fecha: 25/03/2023                         *
********************************************/
// Inclusión de Bibliotecas
#include <iostream>
#include <string>     // Biblioteca Estándar C++
#include <vector>     // Biblioteca Estándar C++
#include <queue>      // Biblioteca Estándar C++
#include <stack>      // Biblioteca Estándar C++
#include <algorithm>  // Biblioteca Estándar C++
#include <limits>     // Biblioteca Estándar C++
using namespace std;
// Clase GrafoND  Grafo No Dirigido Ponderado
class GrafoND 
{
 private:
  int V;
  vector<vector<int>> MA; // Matriz de adyacencia
 public:
 // Constructor de la clase
 // Parámetro: Entero V. Número de Vértices
 GrafoND(int);
// Método: Agregar_Arista 
 void Agregar_Arista(int, int);
// Método: Muestra_GrafoND 
 void Muestra_GrafoND();
// Método Grado.
int Grado(int);
// Método: Caminos 
void Caminos(int, int);
// Método auxiliar para el método Caminos
void Buscar_CaminosAux(int, int, vector<bool>&, vector<int>&, int&);
// Método: Camino_Minimo_Dijkstra 
float Camino_Minimo_Dijkstra(int, int);
// Método: Camino_Minimo_BFS 
void Camino_Minimo_BFS(int, int);
};

// Program principal
int main() 
{
// Crear un objeto tipo grafo No dirigido de 6 vértices
 GrafoND GND(6);
 int vi,vf;  // Vértices inicial y final 
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
 cout<<endl;
 cout<<"  VERTICE ORIGEN  : ";
 cin>>vi;
 cout<<"  VERTICE DESTINO : ";
 cin>>vf;
 cout<<endl;
 cout<<"--- CAMINOS ENTRE LOS VERTICES ["<<vi<<","<<vf<<"]"<<endl;
 GND.Caminos(vi,vf);
 cout<<endl;
 cout<<"--- CAMINO MINIMO ENTRE LOS VERTICES ["<<vi<<","<<vf<<"]"<<endl;
 GND.Camino_Minimo_Dijkstra(vi,vf);
 cout<<endl;
 GND.Camino_Minimo_BFS(vi,vf);
 return 0;
}

// DECLARACIONES DE LA CLASE
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
//   p: Real. Ponderación de la arísta
 void GrafoND::Agregar_Arista(int vs, int ve) 
 {
  MA[vs][ve] = 1;
  MA[ve][vs] = 1;
 }
// Método: Muestra_GrafoND 
// Muestra.
// Vértice/Grado/Adyacentes
// Parámetros. NO 
 void GrafoND::Muestra_GrafoND() 
 {
  string S;
  for (int i = 0; i < V; i++) 
  {
   cout << "  VERTICE " << i << ": ";
   S=" ";
   for (int j = 0; j < V; ++j)
   {
    if (MA[i][j]!=0)
    {
     //S=S+to_string(j)+ " ";
     S=S+to_string(j)+"("+to_string(MA[i][j])+") ";
    }
   }
   cout << "\tGrado : "<< Grado(i) << "\tAdyacentes : " <<S<<endl;
  }
 }
// Método Grado.
// Retorna el grado de un Vértice
// Parámetros.
//    n: Entero. Número del Vértice
int GrafoND::Grado(int n)
{
 int g=0;
 for (int i = 0; i < V; i++)
  if (MA[n][i]!=0) 
   g++; 
 return g;
}
// Método: Caminos 
// Muestra los caminos entre dos nodos y su coste
// Parámetros. 
//  VO: Entero. Vértice Origen
//  VD: Real. Ponderación de la arísta
void GrafoND::Caminos(int VO, int VD) 
{
    vector<bool> Visto(V, false);
    vector<int> Ruta;
    int Peso_T = 0;
    Buscar_CaminosAux(VO, VD, Visto, Ruta, Peso_T);
}
// Método auxiliar para el método Caminos
void GrafoND::Buscar_CaminosAux(int V_Actual, int VD, vector<bool>& Visto, vector<int>& Ruta, int& Peso_T) 
{
 string C,S;
 Visto[V_Actual] = true;
 Ruta.push_back(V_Actual);
 if (V_Actual == VD) 
 {
  C="CAMINO : ";
  for (unsigned i = 0; i < Ruta.size(); i++) 
  {
   C=C+to_string(Ruta[i])+" ";
  }
  S=C;  
  for (int l=C.size();l<(V*3);l++)
    S=S+" "; // Completa con espación la cadena de salida
  S=S+"\tAristas = "+to_string(Peso_T);
  cout<<"\t"<<S<<endl;
 }
 else 
 {
  for (int i = 0; i < V; i++) 
  {
  if (MA[V_Actual][i] != 0 && !Visto[i]) 
   {
    Peso_T += MA[V_Actual][i];
    Buscar_CaminosAux(i, VD, Visto, Ruta, Peso_T);
    Peso_T -= MA[V_Actual][i];
   }
  }
 }
 Visto[V_Actual] = false;
 Ruta.pop_back();
}
// Método: Camino_Minimo_Dijkstra 
// Encuentra el camino mínimo entre dos vértices
// Añgoritmo de Dijkstra
// Parámetros. 
//  VO: Entero. Vértice Origen
//  VD: Entero. Vértice Destino
float GrafoND::Camino_Minimo_Dijkstra(int VO, int VD) 
{
 string S;
 vector<double> distancias(V, numeric_limits<double>::infinity());
 vector<int> padres(V, -1);
 distancias[VO] = 0;
 priority_queue<pair<double, int>, vector<pair<double, int>>, greater<pair<double, int>>> cola_prioridad;
 cola_prioridad.push(make_pair(0, VO));
 while (!cola_prioridad.empty()) 
 {
  int V_Actual = cola_prioridad.top().second;
  cola_prioridad.pop();
  for (int i = 0; i < V; i++) 
  {
   if (MA[V_Actual][i] != 0) 
   {
    int distancia_nueva = distancias[V_Actual] + MA[V_Actual][i];
    if (distancia_nueva < distancias[i]) 
    {
     distancias[i] = distancia_nueva;
     padres[i] = V_Actual;
     cola_prioridad.push(make_pair(distancia_nueva, i));
    }
   }
  }
 }
 cout<<"  ALGORITMO DE DIJKSTRA"<<endl;
 cout<<"\tNODOS : ";
    stack<int> camino;
    int V_Actual = VD;
    while (V_Actual != -1) 
    {
        camino.push(V_Actual);
        V_Actual = padres[V_Actual];
    }
    int aristas=0;
    while (!camino.empty()) 
    {
        aristas++;
        cout << camino.top(); // Muestra nodo del camino
        camino.pop();
        if (!camino.empty())
         cout<<" -> ";
    }
//    cout<<"  Longitud : "<<distancias[VO]<<endl;
cout<<"  Longitud : "<<(aristas-1)<<endl;
    return distancias[VO];
}

// Método: Camino_Minimo_BFS 
// Encuentra el camino mínimo entre dos vértices
// ALgoritmo BFS* Modificado
// Parámetros. 
//  VO: Entero. Vértice Origen
//  VD: Entero. Vértice Destino
void GrafoND::Camino_Minimo_BFS(int VO, int VD) 
{
 queue<int> q;
 vector<bool> visited(V, false);
 vector<int> parent(V, -1);
 q.push(VO);
 visited[VO] = true;
 while (!q.empty()) 
 {
  int curr = q.front();
  q.pop();
  if (curr == VD) 
  {
    break;
  }
  for (int neigh = 0; neigh < V; neigh++) 
  {
   if (MA[curr][neigh] != 0 && !visited[neigh]) 
   {
    q.push(neigh);
    visited[neigh] = true;
    parent[neigh] = curr;
   }
  }
 }
 cout << "   ALGORITMO BFS*" << endl;
 cout<<"\tNODOS : ";
 if (visited[VD]) 
 {
  vector<int> path;
  int curr = VD;
  while (curr != VO) 
  {
   path.push_back(curr);
   curr = parent[curr];
  }
  path.push_back(VO);
  reverse(path.begin(), path.end());

  for (unsigned j=0;j<path.size();j++)
  {
   cout << path[j];
   if (j<(path.size()-1))
    cout<<" -> ";
  }
  cout<<"  Longitud : "<<(path.size()-1)<<endl;
 }
 else
 {
  cout << "   NO HAY CAMINO "<< endl;
 }
}
