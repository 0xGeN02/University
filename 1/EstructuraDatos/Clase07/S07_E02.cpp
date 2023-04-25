/****************************************
* Asignatura: Estructura de Datos       *
* Lenguaje C++                          *
* Biblioteca iostream                   *
* Espacio de nombres                    *
* Formato endl   Salto de línea         *
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
 int a=10;
 float p; 
 char x;
 char cad[50];
 cout << " **********     Entrada      **********" <<endl;
 cout << "Indique un valor tipo  entero : ";
 cin  >> a;
 cout << "Indique un valor tipo real    : ";
 cin  >> p;
 cout << "Indique un valor tipo char    : ";
 cin  >> x;
 cout << "Indique un valor tipo cadena  : ";
 cin  >> cad;
 cout << " **********     Salida      **********" <<endl;
 cout <<"\ta   = " << a   <<endl;
 cout <<"\tp   = " << p   <<endl;  
 cout <<"\tx   = " << x   <<endl;  
 cout <<"\tcad = " << cad <<endl;  
 cout <<endl;
 return 0;
}