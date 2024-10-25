/****************************************
* Asignatura: Estructura de Datos       *
* Lenguaje C++                          *
* Biblioteca iostream. Clase ostream    *
* Funciones y manipuladores de formato  *
* Formato width, fill y flush           *
* Programa exclusivo para uso académico *
* Autor: Eladio Dapena Gonzalez         *
* Fecha: 05/03/2023                     *
*****************************************/
// Bibliotecas
#include <iostream>
// espacio de nombres
using namespace std;
/* Programa principal */
int main()
{
int NE = 36;
cout.width(8); // Sólo afecta la salida siguiente y se desactiva
cout << NE << endl;
cout << NE << endl;
cout.fill('*'); // Afecta todas las salidas a partir de su invocación
cout.width(8);
cout << NE << endl;
cout.width(8);
cout << NE << endl;
cout.fill(' ');
cout.width(8);
cout << "Hola C++" << endl;
cout << "Hola C++" << flush; // La siguiente salida se realiza en la misma línea
cout << "Hola C++" << endl; 
return 0;
}