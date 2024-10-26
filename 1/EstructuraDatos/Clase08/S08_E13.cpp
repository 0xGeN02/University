/*****************************************
* Asignatura: Estructura de Datos        *
* Lenguaje C++                           *
* POO definición de Clases               *
* Métodos constructores y destructores   *
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
// Métdos constructores
Punto2D();
Punto2D(float, float);
// Punto2D(float =0.0, float =0.0);  // Agrupa las dos anteriores
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
Punto2D p1,p2(10,10),p3(20,20);
cout << fixed <<setprecision(2)<<"Punto 1 = ["<<p1.getX()<<","<<p1.getY()<<"]"<<endl;
cout << fixed <<setprecision(2)<<"Punto 2 = ["<<p2.getX()<<","<<p2.getY()<<"]"<<endl;
cout << fixed <<setprecision(2)<<"Punto 3 = ["<<p3.getX()<<","<<p3.getY()<<"]"<<endl;
}

//Declaraciones de los métodos de la clase
// Constructores
Punto2D::Punto2D() {
this->x = 0.0;
this->y = 0.0;
}
Punto2D::Punto2D(float x, float y) {
this->x = x;
this->y = y;
}
// Seters
void Punto2D::setX(float x){
this->x = x;
}
void Punto2D::setY(float y){
this->y = y;
}
//Geters
float Punto2D::getX(){
    return this->x;
}
float Punto2D::getY(){
    return this->y;
}

