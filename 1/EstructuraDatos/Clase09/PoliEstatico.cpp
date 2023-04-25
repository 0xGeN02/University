/****************************************
* Asignatura: Estructura de Datos       *
* Ejemplo 08 Sesión 09                  *
* Polimorfismo Estático                 *
* Sobrecarga Procedimiento Imprime      *
* Programa de uso para docencia         *
* Autor: Eladio Dapena Gonzalez         *
* Fecha: 14/03/2023                     *
*****************************************/
// Encabezado
#include <iostream>
using namespace std;
// Prototipos de funciones y procedimientos
void Imprime(int);          // Comportamiento 1
void Imprime(double);       // Comportamiento 2   
void Imprime(int,double);   // Comportamiento 3
// Programa Principal
int main() 
{
 int    E = 10;
 double D = 3.1416;
 cout<<"   PROCEDIMIENTO CON DIFERENTES PARAMETROS   "<<endl;
 Imprime(E);    // Imprime "Entero : 10"
 Imprime(D);    // Imprime "Real   : 3.1416"
 Imprime(E,D);  // Imprime "Entero : 10   Real   : 3.1416""
 return 0; 
}
// Declaraciones de funciones y procedimientos
// Procedimiento Imprime Entero
void Imprime(int num) 
{
 cout << " Entero : " << num << endl;
}
// Procedimiento Imprime Real (double)
void Imprime(double num) 
{
 cout << " Real   : " << num << endl;
}
// Procedimiento Imprime Entero y Real (double)
void Imprime(int num1, double num2) 
{
 cout << " Entero : " << num1 <<"    Real : " << num2 << endl;
}
