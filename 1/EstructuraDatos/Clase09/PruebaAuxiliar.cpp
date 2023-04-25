/****************************************
* Asignatura: Estructura de Datos       *
* Ejemplo 04 Sesión 09                  *
* Prueba Clase Auxiliar                 *
* Programa de uso para docencia         *
* Autor: Eladio Dapena Gonzalez         *
* Fecha: 14/03/2023                     *
*****************************************/
// Bibliotecas
#include "CAuxiliar.h"
//Principal
int main()
{
 cout<<"----   PRUEBA DE LA CLASE DERIVADA AUXILIAR   ----  "<<endl;
 // Objeto Auxiliar A1  
 Auxiliar A1;    
 // Objeto Auxiliar A2 invoca constructor de Inicialización
 Auxiliar A2("STEVE WOZNIAK","40000000D",72,"ELECTRONICA");
 // Entrada de Datos del Objeto A1
 cout<<"Entrada de Datos del Objeto Auxiliar A1"<<endl;
 A1.Leer_Datos();
 cout<<endl;
 //Mostrar Datos
 cout<<"Datos Objeto Auxiliar A1"<<endl;
 A1.Muestra_Datos();
 cout<<"Datos Objeto Auxiliar A2"<<endl;
 cout<<endl;
 A2.Muestra_Datos();
 return 0;
}
