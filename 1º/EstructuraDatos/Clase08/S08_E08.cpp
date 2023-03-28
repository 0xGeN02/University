/*****************************************
* Asignatura: Estructura de Datos        *
* Lenguaje C++                           *
* Biblioteca iostream                    *
* Resolución de ámbito                   *
* Programa exclusivo para uso académico  *
* Realizado por: Eladio Dapena Gonzalez  *
* Fecha: 02/03/2023                      *
******************************************/
#include <iostream>
using namespace std;
int E=10;                   // variable global
/* Programa principal */
int main()
{
    system("cls"); //system("clear"); unix ios users
    cout<<" Varibale Global E=10   : "<<E<<endl;
    cout<<" Declarar Varibale local  E=20"<<endl;
    int E=20;               // variable local
    cout << "Local    E = "<<E<<endl;
    cout << "Global ::E = "<<::E<<endl;
    return 0;
}