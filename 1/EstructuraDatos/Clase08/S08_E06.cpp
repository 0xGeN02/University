/*****************************************
* Asignatura: Estructura de Datos        *
* Lenguaje C++                           *
* Biblioteca iostream                    *
* Entrada de datos cin >>                *
* Programa exclusivo para uso académico  *
* Realizado por: Eladio Dapena Gonzalez  *
* Fecha: 02/03/2023                      *
******************************************/
#include <iostream>
#include <string>
using namespace std;
/* Programa principal */
int main()
{
    system("cls"); //system("clear"); unix ios users
    int     Entero;
    float   Peso;
    char    Letra;
    bool    Logico;
    string  Nombre;

    cout << " **** Entrada de Datos ****"<<endl;
    cout << "Indique un entero y un real separados por espacios :";
    cin>> Entero >> Peso;
    cout << "Indique un char                                    : ";
    cin>>Letra;
    cout << "Indique booleano 0/1                               : ";
    cin>>Logico;
    cout<< "Indique nombre y apellido                          : ";
    cin>>Nombre;
    cout << " **** Salida de Datos ****"<<endl;    
    cout <<"Entero   = "<<Entero<<"\t Real = "<<Peso<<endl;
    cout <<"Caracter = "<<Letra<<boolalpha<<"\t  Bool = "<<Logico<<endl;
    cout <<"Cadena Nombre Apellido = "<<Nombre<<endl; // Observe esta salida
    return 0;
}