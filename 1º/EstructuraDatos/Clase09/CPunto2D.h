/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 09 Ejemplo 01                  *
* Programación Orientada a Objetos POO  *
* Definición Clase Punto2D              *
* Clases Amigas (friend)                *
* Sobrecargar el operador  <<           *
* Programa exclusivo para uso académico *
* Realizado por: Eladio Dapena Gonzalez *
* Fecha: 02/03/2023                     *
*****************************************/
#include <iostream>
#include<iomanip>
#include <cmath>
using namespace std;
// Definición de la clase
class Punto2D 
{
// Atributos
private:
 float x, y;
// Métodos
public:
// Métodos constructores
  Punto2D();
Punto2D(float, float);
// Prototipos
// SETERS
  void setX(float); 
  void setY(float); 
// GETERS
  float getX();
  float getY(); // Análogo getY
// Otros métodos
  void Leer_Punto();
  void Escribe_Punto();
  char Cuadrante() const;
  float Distancia_A(const Punto2D& A) const;
// Función AMIGA friend operator << (Inserción)
  friend ostream& operator << (ostream& , const Punto2D& ); 
};