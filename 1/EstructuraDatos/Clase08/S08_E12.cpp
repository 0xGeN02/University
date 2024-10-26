/*****************************************
* Asignatura: Estructura de Datos        *
* Lenguaje C++                           *
* POO definición de Clases               *
* this, Seters y Geters                  *
* Programa exclusivo para uso académico  *
* Realizado por: Eladio Dapena Gonzalez  *
* Fecha: 02/03/2023                      *
******************************************/
#include <iostream>
#include<iomanip>
using namespace std;
// Definición de la clase
class Punto2D 
{
// Atributos
private:
float x, y;
// Métodos
public:
// Prototipos
// SETERS
void setX(float); 
void setY(float); 
// GETERS
float getX();
float getY(); // Análogo getY
// Otros métodos
};
// Programa de prueba Clase Punto2D
int main()
{
Punto2D p;
p.setX(1.0);
p.setY(2.0);
cout << fixed <<setprecision(2)<<"Punto = ["<<p.getX()<<","<<p.getY()<<"]"<<endl;
}

//Declaraciones de los métodos de la clase
void Punto2D::setX(float x){
this->x = x;
}
void Punto2D::setY(float y){
this->y = y;
}
float Punto2D::getX(){
    return this->x;
}
float Punto2D::getY(){
    return this->y;
}
