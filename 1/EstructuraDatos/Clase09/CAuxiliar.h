/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 09 Ejemplo 04                  *
* Programación Orientada a Objetos POO  *
* Definición Clase Derivada Auxiliar    *
* Clase Base Persona                    *
* Programa exclusivo para uso académico *
* Realizado por: Eladio Dapena Gonzalez *
* Fecha: 14/03/2023                     *
*****************************************/
#ifndef AUXILIAR_H
#define AUXILIAR_H
#include "CPersona.h"
// Clase derivada 2
class Auxiliar : public Persona 
{
  private:
    string Especialidad;
  public:
 //Constructores
  Auxiliar();
  Auxiliar(string, string, int, string);
//Seters
    void SetEspecialidad(string);
//Geters
    string GetEspecialidad();
// Otros métodos
    void Leer_Datos();
    void Muestra_Datos();
};
#endif // AUXILIAR_H