/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 09 Ejemplo 01                  *
* Programación Orientada a Objetos POO  *
* Declaración Clase Punto2D             *
* Clases Amigas (friend)                *
* Sobrecargar el operador  <<           *
* Programa exclusivo para uso académico *
* Realizado por: Eladio Dapena Gonzalez *
* Fecha: 02/03/2023                     *
*****************************************/
#include "CPunto2D.h"
using namespace std;
//Declaraciones de los métodos de la clase
// Constructores
Punto2D::Punto2D() 
{
    this->x = 0.0;
    this->y = 0.0;
}
Punto2D::Punto2D(float x, float y) 
{
    this->x = x;
    this->y = y;
}
// Seters
void Punto2D::setX(float x)
{
    this->x = x;
}
void Punto2D::setY(float y)
{
    this->y = y;
}
//Geters
float Punto2D::getX()
{
    return this->x;
}
float Punto2D::getY()
{
    return this->y;
}
// Entrada
void Punto2D::Leer_Punto()
{
    cout<<"Indique coordenada x : ";
    cin>>this->x;
    cout<<"Indique ordenada   y : ";
    cin>>this->y;
}
// Salida
void Punto2D::Escribe_Punto()
{
    cout << fixed <<setprecision(2)<<"Punto 1 = ["<<this->x<<","<<this->y<<"]"<<endl;
}

// Definición de la sobre carga del operador <<
ostream& operator<<(ostream& Salida, const Punto2D& p) 
{
  Salida << "[" << p.x << ", " << p.y << "]";
  return Salida;
}
