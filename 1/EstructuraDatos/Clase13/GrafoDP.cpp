// FICHERO DECLARACIONES DE LA CLASE GrafoDP
/********************************************
* Clase GrafoDP  Grafo Dirigido Ponderado   *
* Asignatura: Estructura de Datos           *
* Sesión 11 TDA Grafo DIRIGIDO PONDERADO    *
* Actividad Práctica Prersencial            *
* Definición Clase GrafoDP                  *
* Referencias:                              *
* Libro: Luis Joyanes(2007) Data Structures *
* Programa de uso académico                 *
* Adaptado por: Eladio Dapena Gonzalez      *
* Fecha: 25/03/2023                         *
********************************************/
#include "GrafoDP.h"
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
  S=S+"\tCoste = "+to_string(Peso_T);
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
  //cout<<"  ALGORITMO DE DIJKSTRA"<<endl;
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