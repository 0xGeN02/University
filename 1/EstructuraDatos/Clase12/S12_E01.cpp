/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 12 Clase Nodo_AB               *
* Ejemplo 01: S12_E01                   *
* Prueba de la clase  Nodo_AB           *
* Programa exclusivo para uso académico *
* Adaptado por: Eladio Dapena Gonzalez  *
* Fecha: 26/03/2023                     *
*****************************************/
#include <iostream>
#include "Nodo_AB.h"
using namespace std;
// Prueba de la clase Nodo_AB
int main() 
{
    // Crear Nodos
    Nodo_AB *N1 = new Nodo_AB('A');
    N1->Muestra_Nodo();
    Nodo_AB *N2 = new Nodo_AB('B');
    N2->Muestra_Nodo();
    Nodo_AB *N3 = new Nodo_AB('C');
    N3->Muestra_Nodo();    
    cout<<endl;
    delete N1;
    delete N2;
    delete N3;
    return 0;
}