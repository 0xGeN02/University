/****************************************
* Asignatura: Estructura de Datos       *
* Ejemplo 05 Sesión 09                  *
* Herencia Múltiple                     *
* Clase Asignatura                      *
* Clases Base Profesor y Auxiliar       *
* Prueba Clase Asignatura               *
* Programa de uso para docencia         *
* Autor: Eladio Dapena Gonzalez         *
* Fecha: 14/03/2023                     *
*****************************************/
// Bibliotecas
#include "CPersona.h"
#include "CProfesor.h"
#include "CAuxiliar.h"
#include "CAsignatura.h"
//Principal
int main()
{
 cout<<"----   PRUEBA DE LA CLASE ASIGNATURA   ----  "<<endl;    
 // Objeto Asignatura AS1
 Asignatura AS1;  
// Objeto Asignatura AS2 invoca constructor de Inicialización
 Asignatura AS2("ALAN M. TURING","60000000F",42,"DOCTOR","CATEDRATICO","STEVE WOZNIAK","40000000D",72,"ELECTRONICA","ED01");
cout<<"Entrada de Datos del Objeto Asignatura AS1"<<endl; 
 AS1.Leer_Datos();
 cout<<endl; 
 cout<<"---------------------------------"<<endl;
 cout<<"         OBJETOS AS1 Y AS2"<<endl;
 cout<<"---------------------------------"<<endl;
 cout<<endl; 
 cout<<"DATOS OBJETO ASIGNATURA AS1"<<endl;   
 //Mostrar Datos
 AS1.Muestra_Datos();
 cout<<endl; 
 cout<<"DATOS OBJETO ASIGNATURA AS2"<<endl;   
 AS2.Muestra_Datos();
 return 0;
}