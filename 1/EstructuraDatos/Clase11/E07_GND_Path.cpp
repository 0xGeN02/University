/********************************************
* Asignatura: Estructura de Datos           *
* Sesión 11 TDA Grafo NO DIRIGIDO PONDERADO *       
* Ejemplo 07. CAMINOS ENTRE DOS VÉRTICES    *
* Definición Clase GrafoNDP                 *
* Representación: Matriz de Adyacencia      *
*   Métodos    Caminos BFS*                 *
*   Luis Joyanes(2007) Data Structures      *
* Programa de uso académico                 *
* Adaptado por: Eladio Dapena Gonzalez      *
* Fecha: 25/03/2023                         *
********************************************/
// Inclusión de Bibliotecas
#include <iostream>
#include <string>   // Biblioteca Estándar C++
#include <vector>   // Biblioteca Estándar C++
#include <queue>    // Biblioteca Estándar C++
#include <stack>    // Biblioteca Estándar C++
#include <limits>   // Biblioteca Estándar C++
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
