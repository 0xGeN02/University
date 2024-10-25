/*****************************************
* Asignatura: Estructura de Datos        *
* Sesión 11 TDA Grafo DIRIGIDO PONDERADO *
* Ejemplo 04. Clase GrafoDP              *
* Definición Clase GrafoDP               *
* Representación:                        *
*      Matriz de Adyacencia              *
*      Matriz Ponderada                  *
* Programa de uso académico              *
* Realizado por: Eladio Dapena Gonzalez  *
* Fecha: 25/03/2023                      *
*****************************************/
#include <iostream>
#include <string>
#include <vector>     // Biblioteca Estándar C++
using namespace std;
// Clase GrafoDP  Grafo Dirigido Ponderado
class GrafoDP 
{
 private:
  int V;
  vector<vector<int>>   MA; // Matriz de adyacencia
  vector<vector<float>> MP; // Matriz de Ponderada
 public:
 // Constructor de la clase
 GrafoDP(int);

// Método: Agregar_Arista 
// Agrega una arista al grafo
 void Agregar_Arista(int, int, float);
// Método: Muestra_GrafoD 
 void Muestra_GrafoDP();
// Método Grado_Out.
int Grado_Out(int n);
// Método Grado_In.
int Grado_In(int n);
};
// Program principal
int main() 
{
// Crear un objeto tipo grafo No dirigido de 6 vértices
 GrafoDP GDP(6); 
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
 cout<<"***   Grafo Dirigido Ponderado   ***"<<endl;
 GDP.Muestra_GrafoDP();
 return 0;
}

// DECLARACIONES DE LA CLASE GrafoDP
 // Constructor de la clase
 GrafoDP::GrafoDP(int V) 
  {
    this->V = V;
    MA = vector<vector<int>>(V, vector<int>(V, 0));
    MP = vector<vector<float>>(V, vector<float>(V, 0.0));
  }

// Método: Agregar_Arista 
// Agrega una arista al grafo
// Parámetros. 
//  vs: Entero. Vértice de Salida
//  ve: Entero. Vértice de Entrada
//   p: Real.   Ponderación de la arísta
 void GrafoDP::Agregar_Arista(int vs, int ve, float p) 
 {
  MA[vs][ve] = 1;
  MP[vs][ve] = p;
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
     S=S+to_string(j)+"("+to_string(MP[i][j])+") ";
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
