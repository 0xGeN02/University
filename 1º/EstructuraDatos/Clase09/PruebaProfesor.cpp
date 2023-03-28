/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 09 Ejemplo 03                  *
* Programación Orientada a Objetos POO  *
* Prueba de Clase Derivada Profesor     *
* Clase Base Persona                    *
* Programa exclusivo para uso académico *
* Realizado por: Eladio Dapena Gonzalez *
* Fecha: 14/03/2023                     *
*****************************************/
// Bibliotecas
#include "CProfesor.h"
//Principal
int main()
{
 cout<<"----   PRUEBA DE LA CLASE DERIVADA PROFESOR   ----  "<<endl;
// Objeto Profesor P1   
 Profesor P1;
// Objeto Profesor P2 invoca constructor de Inicialización
 Profesor P2("ALAN M. TURING","20000000B",42,"DOCTOR","CATEDRATICO");
// Entrada de Datos del Objeto P1
 cout<<"Entrada de Datos del Objeto Profesor P1"<<endl;
 P1.Leer_Datos();
 cout<<endl;
 //Mostrar Datos
 cout<<"Datos Objeto Profesor P1"<<endl;
 P1.Muestra_Datos();
 cout<<"Datos Objeto Profesor P2"<<endl;
 P2.Muestra_Datos();
 return 0;
}
