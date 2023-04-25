/*****************************************
* Asignatura: Estructura de Datos        *
* Lenguaje C++                           *
* Biblioteca iostream                    *
* Entrada de datos Cadenas getline()     *
* Programa exclusivo para uso académico  *
* Realizado por: Eladio Dapena Gonzalez  *
* Fecha: 02/03/2023                      *
******************************************/
#include <iostream>
#include <string>
//#include <stdio.h>
using namespace std;
/* Programa principal */
int main()
{
    system("cls"); //system("clear"); unix ios users
    string  Nombre;

    cout << " **** Entrada de cadenas con espacios ****"<<endl;
    cout<< "Indique nombre y apellido : ";
    getline(cin,Nombre);
    cout << " **** Salida de Datos ****"<<endl;    
    cout <<"      Nombre Apellido     : "<<Nombre<<endl; // Observe esta salida
    return 0;
}