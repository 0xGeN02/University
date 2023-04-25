/*****************************************
* Asignatura: Estructura de Datos        *
* Lenguaje C++                           *
* POO definición de Clases               *
* Definición de Clase Punto2D            *
* Programa exclusivo para uso académico  *
* Realizado por: Eladio Dapena Gonzalez  *
* Fecha: 02/03/2023                      *
******************************************/
#include <iostream>
using namespace std;
class Punto2D {
float x, y;
}; 
int main()
{
Punto2D p;
p.x=10.0;
p.y=5.0;
cout <<"Punto = ["<<p.x<<","<<p.y<<"]"<<endl;
}

