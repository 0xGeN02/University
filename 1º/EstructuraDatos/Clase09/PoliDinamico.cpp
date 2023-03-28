/****************************************
* Asignatura: Estructura de Datos       *
* Ejemplo 09 Sesión 09                  *
* Polimorfismo Dinámico                 *
* Clase Base Figura                     *
*    Método virtual Area                *
* Herencia Simple                       *
*   Clase Triangulo                     *
*   Clase Cuadrado                      *
*   Clase Rectangulo                    *
*   Clase Circulo                       *
* Programa de uso para docencia         *
* Autor: Eladio Dapena Gonzalez         *
* Fecha: 14/03/2023                     *
*****************************************/
#include <iostream>
#include <math.h>
using namespace std;
const double PI=3.14159265;
// Declaraciones de las Clases
class Figura 
{
 public:
 // Método virtual para el área
   virtual double Area() = 0;
   virtual        ~Figura() {}
};

class Triangulo : public Figura 
{
 private:
  double BASE, ALTURA;
 public:
 Triangulo(double b, double a){this->BASE=b;this->ALTURA=a;}
 virtual ~Triangulo() {}
 double Area() {return ((BASE * ALTURA) / 2.0);}
};

class Cuadrado : public Figura 
{
 private:
  double L;    
 public:
  Cuadrado(double l){this->L = l;}
  virtual ~Cuadrado() {}
  double Area() {return (pow(L,2.0));}
};

class Rectangulo : public Figura 
{
 private:
  double L1,L2;
 public:
  Rectangulo(double a, double b) {this->L1 = a;this->L2 = b;}
  virtual ~Rectangulo() {}
  double Area() {return(L1 * L2);}
};

class Circulo : public Figura 
{
 private:
  double R;
 public:
  Circulo(double r) {this->R = r;}
  virtual ~Circulo() {}
  double  Area(){return(PI*pow(R,2));}
};

int main() 
{
 // Crear objetos de las distintas figuras
    Figura* F1 = new Triangulo(4.0, 3.0);
    Figura* F2 = new Cuadrado(5.0);
    Figura* F3 = new Rectangulo(10.0, 5.0);
    Figura* F4 = new Circulo(2.0);
 // Mostrar el área de cada figura
    cout<< "AREAS DE LAS FIGURAS" <<endl;
    cout<<" TRIANGULO  = "<<F1->Area()<<endl;
    cout<<" CUADRADO   = "<<F2->Area()<<endl;
    cout<<" RECTANGULO = "<<F3->Area()<<endl;
    cout<<" CIRCULO    = "<<F4->Area()<<endl;
 // Liberar memoria
   delete F1;delete F2; delete F3; delete F4;
   return 0;
}


