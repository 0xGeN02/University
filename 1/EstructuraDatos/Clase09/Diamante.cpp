/****************************************
* Asignatura: Estructura de Datos       *
* Ejemplo 06 Sesión 09                  *
* Problema del Diamante                 *
* Clase Base Coche                      *
* Herencia Simple                       *
*   Clases Electrico y Gasolina         *
* Herencia Múltiple                     *
*   Clase Híbrido                       *
* Programa de uso para docencia         *
* Autor: Eladio Dapena Gonzalez         *
* Fecha: 14/03/2023                     *
*****************************************/
#include <iostream>
using namespace std;

class Coche_Citroen 
{
public:
// Constructor
  Coche_Citroen() 
  {
    cout << "Objeto Coche Citroen" << endl;
  }
};

class Citroen_Electrico : public Coche_Citroen 
{
// Constructor
public:
  Citroen_Electrico() 
  {
// Constructor    
    cout << "Objeto Coche Electrico Citroen Oli" << endl;
  }
};

class Citroen_Gasolina : public Coche_Citroen 
{
public:
  Citroen_Gasolina() 
  {
    cout << "Objeto Coche Gasolina Citroen C3" << endl;
  }
};

class Citroen_Hibrido : public Citroen_Electrico, public Citroen_Gasolina 
{
public:
// Constructor
  Citroen_Hibrido()
 // Constructor  
  {
    cout << "Objeto Coche Hibrido Citroen C5 Aircross" << endl;
  }
};
// Programa principal
int main() 
{
// Declara Objeto
  Citroen_Hibrido Coche; // Se invoca el constructor de la clase.
  return 0;
}