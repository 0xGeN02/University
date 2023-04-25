/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 09 Ejemplo 03                  *
* Programación Orientada a Objetos POO  *
* Definición Clase Derivada Profesor    *
* Clase Base Persona                    *
* Programa exclusivo para uso académico *
* Realizado por: Eladio Dapena Gonzalez *
* Fecha: 14/03/2023                     *
*****************************************/
#ifndef PROFESOR_H
#define PROFESOR_H
#include "CPersona.h"  //Clase Base
// Clase Profesor derivada de clase Base Persona
class Profesor : public Persona 
{
  private:
    string Titulo;
    string Cargo;
  public:
 //Constructores
  Profesor();
  Profesor(string, string, int, string, string);
//Seters
    void SetTitulo(string);
    void SetCargo(string);

//Geters
    string GetTitulo();
    string GetCargo();
// Otros métodos
    void Leer_Datos();
    void Muestra_Datos();
};
#endif // PROFESOR_H