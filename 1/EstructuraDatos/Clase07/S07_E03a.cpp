/*****************************************
* Asignatura: Estructura de Datos        *
* Lenguaje C++                           *
* Extensión de ficheros                  *
* Biblioteca iostream                    *
* espacio de nombre namespace std        *
* Operadores 1 Asignación                *  
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
    int a, b, c;
    cout << " **** Operadores: ASIGNACION ****"<<endl;
    a=10; b=2; c=0;
    cout << " a = "<<a <<"    b = "<<b <<"    c= "<<c<<endl;
    a+=b;
    cout << " a+=b   a = "<<a<<endl;
    a-=b;
    cout << " a-=b   a = "<<a<<endl;
    a*=b;
    cout << " a*=b   a = "<<a<<endl;
    a/=b;
    cout << " a/=b   a = "<<a<<endl;
    a%=b;
    cout << " a%=b   a = "<<a<<endl;
    c=a;
    a&=b;
    cout << " a&=b   a = "<<a<<endl;
    a=c;a|=b;
    cout << " a|=b   a = "<<a<<endl;
    a=c;a^=b;
    cout << " a^=b   a = "<<a<<endl;
    a=c;a<<=b;
    cout << " a<<=b  a = "<<a<<endl;
    a=c;a>>=b;
    cout << " a>>=b  a = "<<a<<endl;
}