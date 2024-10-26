/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 09 Ejemplo 03                  *
* Programación Orientada a Objetos POO  *
* Declaraciones Clase Derivada Profesor *
* Clase Base Persona                    *
* Programa exclusivo para uso académico *
* Realizado por: Eladio Dapena Gonzalez *
* Fecha: 14/03/2023                     *
*****************************************/
#include "CProfesor.h"
// Clase derivada 1
 //Constructores
  Profesor::Profesor()
  {
    Titulo=" ";
    Cargo=" ";
  }
  Profesor::Profesor(string N, string D, int E, string T, string C) : Persona(N, D, E)
  {
    Titulo=T;
    Cargo=C;
  }

void Profesor::Leer_Datos() 
{
// Método de la clase base Persona
    cout<<"  DATOS DEL PROFESOR"<<endl;
    Persona::Leer_Datos();
    cin.ignore();
    cout<<"    TITULO : ";
    getline(cin,Titulo);
    cout<<"    CARGO  : ";
    getline(cin,Cargo);

}
void Profesor::Muestra_Datos() 
{
      // Método de la clase base
      cout<<left<<"  PROFESOR"<<endl;
      Persona::Muestra_Datos();
      cout<<left<<"    TITULO : "<<setw(20)<<this->Titulo<<"  CARGO : "<<setw(10)<<this->Cargo<<endl;
}
