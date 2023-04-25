/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 11 TDA Grafo DIRIGIDO          *
* Ejemplo 02. Clase GrafoD              *
* Definición Clase GrafoD               *
* Representación Matriz de Adyacencia   *
* Programa de uso académico             *
* Realizado por: Eladio Dapena Gonzalez *
* Fecha: 25/03/2023                     *
****************************************/
#include <iostream>
#include <string>
#include <vector>         // Biblioteca Estándar C++
using namespace std;
// Clase GrafoD  Grafo Dirigido  
class GrafoD 
{
 private:
  int V;
  vector<vector<int>> MA; // Matriz de adyacencia
 public:
// Constructor de la clase
  GrafoD(int);
 // Método: Agregar_Arista 
 void Agregar_Arista(int,int);
 // Método: Muestra_GrafoD 
 void Muestra_GrafoD();
 // Método Grado_Out.
 int Grado_Out(int);
 // Método Grado_In.
 int Grado_In(int);
}; 

// Program principal
int main() 
{
// Crear un objeto tipo grafo No dirigido de 6 vértices
 GrafoD GD(6); 
 // Agregar Aristas
 GD.Agregar_Arista(0, 1);
 GD.Agregar_Arista(0, 2);
 GD.Agregar_Arista(1, 2);
 GD.Agregar_Arista(1, 3);
 GD.Agregar_Arista(1, 4);
 GD.Agregar_Arista(2, 3);
 GD.Agregar_Arista(2, 4);
 GD.Agregar_Arista(2, 5);
 GD.Agregar_Arista(3, 4);
 GD.Agregar_Arista(3, 5);
 GD.Agregar_Arista(4, 5);
 // Mostrar Los nodos, su grado y conexiones
 cout<<"***   Grafo Dirigido   ***"<<endl;
 GD.Muestra_GrafoD();
 return 0;
}

// DECLARACIONES DE LA CLASE GrafoD
 // Constructor de la clase
 // Parámetro: Entero V. Número de Vértices
 GrafoD::GrafoD(int V) 
  {
    this->V = V;
    MA = vector<vector<int>>(V, vector<int>(V, 0));
  }

// Método: Agregar_Arista 
// Agrega una arista al grafo
// Parámetros. 
//  vs: Entero. Vértice de Salida
//  ve: Entero. Vértice de Entrada
 void GrafoD::Agregar_Arista(int vs, int ve) 
 {
  MA[vs][ve] = 1;
 }
// Método: Muestra_GrafoD 
// Muestra.
// Vértice/Grado Salida/Grado Entrada/Adyacentes
// Parámetros. NO 
 void GrafoD::Muestra_GrafoD() 
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
     S=S+to_string(j)+ " ";
    }
   }
   cout << "\tAdyacentes : " <<S<<endl;
 }
}
// Método Grado_Out.
// Retorna el grado de salida de un Vértice
// Parámetros.
//    n: Entero. Número del Vértice
int GrafoD::Grado_Out(int n)
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
int GrafoD::Grado_In(int n)
{
 int g=0;
 for (int i = 0; i < V; i++)
  if (MA[i][n]!=0) 
   g++; 
 return g;
}

