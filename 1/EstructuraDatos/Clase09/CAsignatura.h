/****************************************
* Asignatura: Estructura de Datos       *
* Ejemplo 05 Sesión 09                  *
* Herencia Múltiple                     *
* Clase Asignatura                      *
* Clases Base Profesor y Auxiliar       *
* Definición de la Clase                *
* Programa de uso para docencia         *
* Autor: Eladio Dapena Gonzalez         *
* Fecha: 14/03/2023                     *
*****************************************/
#ifndef ASIGNATURA_H
#define ASIGNATURA_H
#include "CPersona.h"
#include "CProfesor.h"
#include "CAuxiliar.h"
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

// Clase derivada Asignatura que hereda de Profesor y Auxiliar
class Asignatura : public Profesor,  public Auxiliar {
  private:
    string Codigo;
  public:
    Asignatura();
    Asignatura(string, string, int, string, string, string, string, int, string, string);
 //Seters
    void SetCodigo(string);
//Geters
    string GetCodigo();
// Otros métodos
    void Leer_Datos();
    void Muestra_Datos();
};
#endif // ASIGNATURA_H
