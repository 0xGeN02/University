/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 11 TDA Grafo NO DIRIGIDO       *
* Ejemplo 01. Clase GrafoND             *
* Definición Clase GrafoND              *
* Representación Matriz de Adyacencia   *
* Programa de uso académico             *
* Realizado por: Eladio Dapena Gonzalez *
* Fecha: 25/03/2023                     *
****************************************/
#include <iostream>
#include <string>
#include <vector> // Biblioteca Estándar C++
using namespace std;
// Clase GrafoND  Grafo No Dirigido
class GrafoND 
{
 // Atributos
 private:
  int V;
  vector<vector<int>> MA; // Clase vector. Matriz de adyacencia
 public:
 // Constructor de la clase
 // Parámetro: Entero V. Número de Vértices
 GrafoND(int ); 
 // Método: Agregar_Arista 
 void Agregar_Arista(int , int ); 
 // Método: Muestra_GrafoND 
 void Muestra_GrafoND(); 
 // Método Grado de un Vértice.
int Grado(int );
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
int GrafoND::Grado(int n)
{
 int g=0;
 for (int i = 0; i < V; i++)
  if (MA[n][i]!=0) 
   g++; 
 return g;
}
