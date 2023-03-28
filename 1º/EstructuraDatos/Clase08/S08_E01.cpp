/****************************************
* Asignatura: Estructura de Datos       *
* Lenguaje C++                          *
* Biblioteca iostream. Clase ostream    *
* Funciones y manipuladores de formato  *
* Formato cout.precison()               *
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
double PI = 3.14159265;
cout << "PI = 3.14159265  sin formato  PI : " << PI << endl;
cout.precision(2);
cout << "cout.precision(2)             PI : " << PI << endl;
cout.precision(4);
cout << "cout.precision(4)             PI : " << PI << endl;
cout.precision(8);
cout << "cout.precision(8)             PI : " << PI << endl;
cout.precision(12);
cout << "cout.precision(12)            PI : " << PI << endl;
return 0;
}