/*****************************************
* Asignatura: Estructura de Datos        *
* Lenguaje C++                           *
* Extensión de ficheros                  *
* Biblioteca iostream                    *
* espacio de nombre namespace std        *
* Operadores Lógicos                     *  
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
bool a,b,c;
a=true,b=false;c=true;    
cout << " **** Operadores: LOGICOS ****"<<endl;
cout <<"a = "<<a<<"  b = "<<b<<"  c = "<<c<<endl;
cout <<"!a = "<<!a<<"  !b = "<<!b<<"  !c = "<<!c<<endl;
cout <<"a&&b = "<<(a&&b)<<"  a&&c = "<<(a&&c)<<"  b&&c = "<<(b&&c)<<endl;
cout <<"a||b = "<<(a||b)<<"  a||c = "<<(a||c)<<"  b||c = "<<(b||c)<<endl;
return 0;
}