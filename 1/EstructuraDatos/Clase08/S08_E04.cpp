/****************************************
* Asignatura: Estructura de Datos       *
* Lenguaje C++                          *
* Biblioteca iostream                   *
* Funciones y manipuladores de formato  *
* Formato setw, left y right            *
* Programa exclusivo para uso académico *
* Autor: Eladio Dapena Gonzalez         *
* Fecha: 05/03/2023                     *
*****************************************/
// Bibliotecas
#include<iostream>
#include<iomanip>
// espacio de nombres
using namespace std;
/* Programa principal */
int main()
{
    system("cls"); //system("clear"); unix ios users
    int a=1024, b=512, c=64;
    cout<< "  Salida  "<<endl;
    cout<<"a  = "<<a<<endl;  
    cout<<"b  = "<<b<<endl;  
    cout<<"c  = "<<c<<endl; 
    cout<< "  Salida a,b,c con setw(12)"<<endl;
    cout<< setw(12) << a << setw(12) << b << setw(12) << c << endl;
    cout<< "  Salida a,b,c  con setw(12)"<<endl;
    cout<< left << setw(12) << a << setw(12) << b << setw(12) << c << endl;
    cout<< "  Salida a,b,c con setw(12) right"<<endl;
    cout<< right << setw(12) << a << setw(12) << b << setw(12) << c << endl;
    cout<<endl;
    return 0;
}