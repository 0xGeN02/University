/****************************************
* Asignatura: Estructura de Datos       *
* Lenguaje C++                          *
* Extensión de ficheros                 *
* Biblioteca iostream                   *
* std::cin  para Entrada                *
* std::cout para Salida                 *
* Programa exclusivo para uso académico *
* Autor: Eladio Dapena Gonzalez         *
* Fecha: 05/03/2023                     *
*****************************************/
// Bibliotecas
#include <iostream>
/* Programa principal */
int main()
{
 int a=10;
 float p; 
 char x;
 char cad[50];
 std::cout << " **********     Entrada      **********\n";
 std::cout << "Indique un valor tipo  entero : ";
 std::cin >> a;
 std::cout << "Indique un valor tipo real    : ";
 std::cin >> p;
 std::cout << "Indique un valor tipo char    : ";
 std::cin >> x;
 std::cout << "Indique un valor tipo cadena  : ";
 std::cin >> cad;
 std::cout << " **********     Salida      **********\n";
 std::cout<<"\ta   = "<<a<<"\n";
 std::cout<<"\tp   = "<<p<<"\n";  
 std::cout<<"\tx   = "<<x<<"\n";  
 std::cout<<"\tcad = "<<cad<<"\n";  
 std::cout<<"\n";
 return 0;
}