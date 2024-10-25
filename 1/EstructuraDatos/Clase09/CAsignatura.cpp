/****************************************
* Asignatura: Estructura de Datos       *
* Ejemplo 05 Sesión 09                  *
* Herencia Múltiple                     *
* Clase Asignatura                      *
* Clases Base Profesor y Auxiliar       *
* Declaración de la Clase               *
* Programa de uso para docencia         *
* Autor: Eladio Dapena Gonzalez         *
* Fecha: 14/03/2023                     *
*****************************************/
#include "CAsignatura.h"
// Clase Asignatura derivada de clases Profesor y Auxiliar
 //Constructores
     Asignatura::Asignatura()
     {
        Codigo="";
     }
    Asignatura::Asignatura(string PN, string PDNI, int PE, string PT, string PC, string AN, string ADNI,int AE, string AESP, string ASIG) : Profesor(PN, PDNI, PE, PT, PC), Auxiliar(AN,ADNI, AE, AESP)
    {
        Codigo=ASIG;
    }
void Asignatura::Leer_Datos() 
{
    cout<<"DATOS DE LA ASIGNATURA"<<endl;
    cout<<"  CODIGO : ";
    getline(cin,Codigo);
    Profesor::Leer_Datos();
    Auxiliar::Leer_Datos();
}
void Asignatura::Muestra_Datos() 
{
      // Método de la clase base
      cout << left<<"DATOS DE LA ASIGNATURA"<<endl;
      cout << left<<"    CODIGO : "<<setw(20)<<this->Codigo<<endl;
      Profesor::Muestra_Datos();
      Auxiliar::Muestra_Datos();
}
