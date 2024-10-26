/*****************************************
* Asignatura: Estructura de Datos        *
* Lenguaje C++                           *
* Extensión de ficheros                  *
* Biblioteca iostream                    *
* espacio de nombre namespace std        *
* Operadores RELACIONALES                *  
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
int a,b,c;
a=1,b=2;c=3;    
cout << " **** Operadores: LOGICOS ****"<<endl;
cout <<"a = "<<a<<"  b = "<<b<<"  c = "<<c<<endl;
cout <<"a == b "<<(a==b)<<"  a==c = "<<(a==c)<<"  b==c = "<<(b==c)<<endl;
cout <<"a != b "<<(a!=b)<<"  a!=c = "<<(a!=c)<<"  b!=c = "<<(b!=c)<<endl;
cout <<"a < b "<<(a<b)<<"  a<c = "<<(a<c)<<"  b<c = "<<(b<c)<<endl;
cout <<"a <= b "<<(a<=b)<<"  a<=c = "<<(a<=c)<<"  b<=c = "<<(b<=c)<<endl;
cout <<"a > b "<<(a>b)<<"  a>c = "<<(a>c)<<"  b>c = "<<(b>c)<<endl;
cout <<"a >= b "<<(a>=b)<<"  a>=c = "<<(a>=c)<<"  b>=c = "<<(b>=c)<<endl;
return 0;
}