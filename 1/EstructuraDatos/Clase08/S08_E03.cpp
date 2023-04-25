/****************************************
* Asignatura: Estructura de Datos       *
* Lenguaje C++                          *
* Biblioteca iostream. Clase ostream    *
* Funciones y manipuladores de formato  *
* Formato setprecision, fixed, unsetf   *
*         showpoint, noshowpoint        *
* Programa exclusivo para uso académico *
* Autor: Eladio Dapena Gonzalez         *
* Fecha: 05/03/2023                     *
*****************************************/
// Bibliotecas
#include <iostream>
#include<iomanip>
// espacio de nombres
using namespace std;
/* Programa principal */
int main()
{
double NE = 3.141516, x=3.0;
cout << fixed << setprecision(3)<<NE<<endl; 
cout.unsetf(ios::fixed);            // Desactivar fixed
cout << showpoint << x << endl; 	//Muestra "3.10000"
cout << noshowpoint << x << endl; 	//Muestra "3"
return 0;
}