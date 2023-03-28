/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 09 Ejemplo 02                  *
* Programación Orientada a Objetos POO  *
* Prueba Clase Base Persona             *
* Programa exclusivo para uso académico *
* Realizado por: Eladio Dapena Gonzalez *
* Fecha: 14/03/2023                     *
*****************************************/
// Bibliotecas
#include "CPersona.h"
//Principal
int main()
{
 cout<<"----   PRUEBA DE LA CLASE BASE PERSONA   ----  "<<endl;
 // Objeto Persona P1
 Persona P1;
 // Objeto Persona P2 invoca constructor de Inicialización
 Persona P2("Alan M. Turing","20000000B",42);
 // Entrada de Datos del Objeto P1
 cout<<"Entrada de Datos del Objeto Persona P1"<<endl;
 P1.Leer_Datos();
 cout<<endl;
 //Mostrar Datos
 cout<<"Datos Objeto Persona P1"<<endl;
 P1.Muestra_Datos();
 cout<<"Datos Objeto Persona P2"<<endl;
 P2.Muestra_Datos();
return 0;
}
