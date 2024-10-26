/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 09 Ejemplo 03                  *
* Programación Orientada a Objetos POO  *
* Declaraciones Clase Derivada Auxiliar *
* Clase Base Persona                    *
* Programa exclusivo para uso académico *
* Realizado por: Eladio Dapena Gonzalez *
* Fecha: 14/03/2023                     *
*****************************************/
#include "CAuxiliar.h"
// Clase Auxiliar derivada de clase Base Persona
 //Constructores
  Auxiliar::Auxiliar()
  {
    Especialidad="";
  }
  Auxiliar::Auxiliar(string N, string D, int E, string Esp) : Persona(N, D, E)
  {
    Especialidad=Esp;
  }

void Auxiliar::Leer_Datos() 
{
// Método de la clase base Persona
    cout<<"  DATOS DEL AUXILIAR"<<endl;
    Persona::Leer_Datos();
    cin.ignore();
    cout<<"    ESPECIALIDAD : ";
    getline(cin,Especialidad);

}
void Auxiliar::Muestra_Datos() 
{
      // Método de la clase base
      cout<<left<<"  AUXILIAR"<<endl;
      Persona::Muestra_Datos();
      cout<<left<<"    ESPECIALIDAD : "<<setw(20)<<this->Especialidad<<endl;
}
