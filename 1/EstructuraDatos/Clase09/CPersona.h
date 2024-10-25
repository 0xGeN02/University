/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 09 Ejemplo 02                  *
* Programación Orientada a Objetos POO  *
* Definición Clase Base Persona         *
* Programa exclusivo para uso académico *
* Realizado por: Eladio Dapena Gonzalez *
* Fecha: 14/03/2023                     *
*****************************************/
#ifndef PERSONA_H
#define PERSONA_H
// Bibliotecas
#include <iostream>
#include<iomanip>
#include <string>
using namespace std;
// Clase base Persona
class Persona 
{
// Atributos
protected:
  string Nombre,DNI;
  int Edad;
 public:
 //Constructores
  Persona();
  Persona(string, string, int);
//Seters
    void SetNombre(string);
    void SetDNI(string);
    void SetEdad(int);
//Geters
    string GetNombre();
    string GetDNI();
    int GetEdad();
// Métodos Adicionales
  void Leer_Datos();
  void Muestra_Datos();
};
#endif // PERSONA_H