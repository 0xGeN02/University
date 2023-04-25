/*****************************************
* Asignatura: Estructura de Datos        *
* Lenguaje C++                           *
* Extensión de ficheros                  *
* Biblioteca iostream                    *
* espacio de nombre namespace std        *
* Operadores b Incrementos (++/--)       *  
* Programa exclusivo para uso académico  *
* Realizado por: Eladio Dapena Gonzalez  *
* Fecha: 02/03/2023                      *
******************************************/
#include <iostream>
//#include <stdio.h>
using namespace std;
/* Programa principal */
int main()
{
    int a;
    a=10;    
    cout << " **** Operador: INCREMENTO ++ ****"<<endl;
    cout <<"a="<<a<<endl;
    a++;
    cout <<"a++="<<a<<endl;
    ++a;
    cout<<"++a="<<a<<endl;
    cout<<endl;
    cout << " **** Operador: DECREMENTO -- ****"<<endl;
    a=10;   
    cout <<"a="<<a<<endl;
    a--;
    cout <<"a--="<<a<<endl;
    --a;
    cout<<"--a="<<a<<endl;
}