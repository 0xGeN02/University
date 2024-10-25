/********************************************
* Asignatura: Estructura de Datos           *
* Sesión 11 TDA Grafo DIRIGIDO PONDERADO    *
* Ejemplo 10. Camino Mínimo dos vértices    *
* Definición Clase GrafoDP                  *
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
// Clase GrafoDP  Grafo Dirigido Ponderado
class GrafoDP 
{
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

// Program principal
int main() 
{
// Crear un objeto tipo grafo No dirigido de 6 vértices
 GrafoDP GDP(6); 
 int vi,vf;  // Vértices inicial y final
 // Agregar Aristas
 GDP.Agregar_Arista(0, 1, 2);
 GDP.Agregar_Arista(0, 2, 5);
 GDP.Agregar_Arista(1, 2, 6);
 GDP.Agregar_Arista(1, 3, 1);
 GDP.Agregar_Arista(1, 4, 3);
 GDP.Agregar_Arista(2, 3, 3);
 GDP.Agregar_Arista(2, 4, 1);
 GDP.Agregar_Arista(2, 5, 7);
 GDP.Agregar_Arista(3, 4, 2);
 GDP.Agregar_Arista(3, 5, 4);
 GDP.Agregar_Arista(4, 5, 4);
 // Mostrar Los nodos, su grado y conexiones
 cout<<"****    GRAFO DIRIGIDO PONDERADO    ****"<<endl;
 GDP.Muestra_GrafoDP();
 cout<<endl;
 cout<<"  VERTICE ORIGEN  : ";
 cin>>vi;
 cout<<"  VERTICE DESTINO : ";
 cin>>vf;
 cout<<endl;
 cout<<"--- CAMINOS ENTRE LOS VERTICES ["<<vi<<","<<vf<<"]"<<endl;
 GDP.Caminos(vi,vf);
 cout<<endl;
 cout<<"--- CAMINO MINIMO ENTRE LOS VERTICES ["<<vi<<","<<vf<<"]"<<endl;
 GDP.Camino_Minimo_Dijkstra(vi,vf);
 cout<<endl;
 GDP.Camino_Minimo_BFS(vi,vf);
 return 0;
}

// DECLARACIONES DE LA CLASE
 // Constructor de la clase
 // Parámetro: Entero V. Número de Vértices
 GrafoDP::GrafoDP(int V) 
 {
    this->V = V;
    MA = vector<vector<float>>(V, vector<float>(V, 0));
 }
// Método: Agregar_Arista 
// Agrega una arista al grafo
// Parámetros. 
//  vs: Entero. Vértice de Salida
//  ve: Entero. Vértice de Entrada
//   p: Real. Ponderación de la arísta
 void GrafoDP::Agregar_Arista(int vs, int ve, float p) 
 {
  MA[vs][ve] = p;
 }
// Método: Muestra_GrafoD 
// Muestra.
// Vértice / Grado Salida / Grado Entrada / Adyacentes / Ponderación
// Parámetros. NO 
 void GrafoDP::Muestra_GrafoDP() 
 {
  string S;
  for (int i = 0; i < V; i++) 
  {
   cout << "VERTICE : " << i << "\tG. Out :  "<<Grado_Out(i)<< "\tG. In :  "<<Grado_In(i);
   S=" ";
   for (int j = 0; j < V; ++j)
   {
    if (MA[i][j]!=0)
    {
     S=S+to_string(j)+"("+to_string(MA[i][j])+") ";
    }
   }
   cout << "\tAdyacentes : " <<S<<endl;
 }
}
// Método Grado_Out.
// Retorna el grado de salida de un Vértice
// Parámetros.
//    n: Entero. Número del Vértice
int GrafoDP::Grado_Out(int n)
{
 int g=0;
 for (int i = 0; i < V; i++)
  if (MA[n][i]!=0) 
   g++; 
 return g;
}
// Método Grado_In.
// Retorna el grado de entrada de un Vértice
// Parámetros.
//    n: Entero. Número del Vértice
int GrafoDP::Grado_In(int n)
{
 int g=0;
 for (int i = 0; i < V; i++)
  if (MA[i][n]!=0) 
   g++; 
 return g;
}
// Método: Caminos 
// Muestra los caminos entre dos nodos y su coste
// Parámetros. 
//  VO: Entero. Vértice Origen
//  VD: Real. Ponderación de la arísta
void GrafoDP::Caminos(int VO, int VD) 
{
    vector<bool> Visto(V, false);
    vector<int> Ruta;
    int Peso_T = 0;
    Buscar_CaminosAux(VO, VD, Visto, Ruta, Peso_T);
}
// Método auxiliar para el método Caminos
void GrafoDP::Buscar_CaminosAux(int V_Actual, int VD, vector<bool>& Visto, vector<int>& Ruta, int& Peso_T) 
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
 void GrafoDP::Camino_Minimo_Dijkstra(int VO, int VD) 
 {
  vector<float> dist(V, numeric_limits<float>::max());  // Distancias mínimas
  vector<int> prev(V, -1);    // Nodos previos
  dist[VO] = 0;    // Distancia 0 del VO al VO
  // Cola de prioridad para guardar nodos no visitados
  priority_queue<pair<float, int>, vector<pair<float, int>>, greater<pair<float, int>>> pq;
  pq.push(make_pair(0, VO));   //Nodo origen a la cola de prioridad
  cout<<"  ALGORITMO DE DIJKSTRA"<<endl;
  cout<<"\tNODOS : ";
  while (!pq.empty()) 
  {
   int u = pq.top().second;  //Nodo con D Mínima no visitado
   pq.pop();
   if (u == VD)   // Si es el Destino
   {
    stack<int> camino;  // Pila para el camino
    float costo = dist[u];
    while (prev[u] != -1) 
    {
      camino.push(u);
      u = prev[u];
    }
    camino.push(VO);
    while (!camino.empty()) 
    {
      cout << camino.top();
      camino.pop();
      if (!camino.empty()) 
      {
        cout << " -> ";
      }
    }
    cout<<endl;
    cout << "\tCoste : " << costo << endl;
    return;
   }
   // Se recorren los nodos adyacentes a u
   for (int v = 0; v < V; v++) 
   {
    if (MA[u][v] != 0 && dist[u] + MA[u][v] < dist[v]) 
    {
      dist[v] = dist[u] + MA[u][v];
      prev[v] = u;
      pq.push(make_pair(dist[v], v)); // Se inserta v en la cola de prioridad
    }
   }
  }  // Fin del ciclo de recorrido 
  // Si no se ha encontrado un camino hasta el nodo destino
  cout << "\tNO HAY CAMINO" << endl;
}







// Método: Camino_Minimo_BFS 
// Encuentra el camino mínimo entre dos vértices
// ALgoritmo BFS* Modificado
// Parámetros. 
//  VO: Entero. Vértice Origen
//  VD: Entero. Vértice Destino
void GrafoDP::Camino_Minimo_BFS(int VO, int VD) 
 {
  vector<float> dist(V, numeric_limits<float>::max());
  vector<int> prev(V, -1);
  dist[VO] = 0;
  queue<int> cola;
  cola.push(VO);
  cout << "   ALGORITMO BFS*" << endl;
  cout<<"\tNODOS : ";
  while (!cola.empty()) 
  {
   int u = cola.front();
   cola.pop();
   for (int v = 0; v < V; v++) 
   {
    if (MA[u][v] != 0 && dist[u] + MA[u][v] < dist[v]) 
    {
     dist[v] = dist[u] + MA[u][v];
     prev[v] = u;
     cola.push(v);
    }
   }
  }
  stack<int> camino;
  float costo = dist[VD];
  while (prev[VD] != -1) 
  {
   camino.push(VD);
   VD = prev[VD];
  }
  camino.push(VO);
  while (!camino.empty()) 
  {
   cout << camino.top();
   camino.pop();
   if (!camino.empty()) 
   {
    cout << " -> ";
   }
  }
  cout<<endl;
  cout << "\tCOSTE : " << costo << endl;
 }