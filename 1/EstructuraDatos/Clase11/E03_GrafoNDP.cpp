/********************************************
* Asignatura: Estructura de Datos           *
* Sesión 11 TDA Grafo NO DIRIGIDO PONDERADO *       *
* Ejemplo 03. Clase GrafoNDP                *
* Definición Clase GrafoNDP                 *
* Representación Matriz de Adyacencia       *
* Programa de uso académico                 *
* Realizado por: Eladio Dapena Gonzalez     *
* Fecha: 25/03/2023                         *
********************************************/
#include <iostream>
#include <string>
#include <vector> // Biblioteca Estándar C++
using namespace std;
// Clase GrafoND  Grafo No Dirigido
class GrafoNDP 
{
 // Atributos
 private:
  int V;
  vector<vector<float>> MA; // Clase vector. Matriz de adyacencia
 public:
 // Constructor de la clase
 GrafoNDP(int);
 // Método: Agregar_Arista 
 void Agregar_Arista(int, int, float);
 // Método: Muestra_GrafoND 
 void Muestra_GrafoNDP();
 // Método Grado.
 int Grado(int n);
};

// Program principal
int main() 
{
// Crear un objeto tipo grafo No dirigido de 6 vértices
 GrafoNDP GNDP(6); 
 // Agregar Aristas
 GNDP.Agregar_Arista(0, 1, 2);
 GNDP.Agregar_Arista(0, 2, 5);
 GNDP.Agregar_Arista(1, 2, 6);
 GNDP.Agregar_Arista(1, 3, 1);
 GNDP.Agregar_Arista(1, 4, 3);
 GNDP.Agregar_Arista(2, 3, 3);
 GNDP.Agregar_Arista(2, 4, 1);
 GNDP.Agregar_Arista(2, 5, 7);
 GNDP.Agregar_Arista(3, 4, 2);
 GNDP.Agregar_Arista(3, 5, 4);
 GNDP.Agregar_Arista(4, 5, 4);
 // Mostrar Los nodos, su grado y conexiones
 cout<<"***   Grafo No Dirigido Ponderado   ***"<<endl;
 GNDP.Muestra_GrafoNDP();
 return 0;
}

// DECLARACIONES DE LA CLASE GNDP
 // Constructor de la clase
 // Parámetro: Entero V. Número de Vértices
 GrafoNDP::GrafoNDP(int V) 
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
 void GrafoNDP::Agregar_Arista(int vs, int ve, float p) 
 {
  MA[vs][ve] = p;
  MA[ve][vs] = p;
 }
// Método: Muestra_GrafoND 
// Muestra.
// Vértice/Grado/Adyacentes/Ponderación
// Parámetros. NO 
 void GrafoNDP::Muestra_GrafoNDP() 
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
int GrafoNDP::Grado(int n)
{
 int g=0;
 for (int i = 0; i < V; i++)
  if (MA[n][i]!=0) 
   g++; 
 return g;
}
