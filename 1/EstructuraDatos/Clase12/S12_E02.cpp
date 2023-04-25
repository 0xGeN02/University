/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 12 Clase Nodo_AB               *
* Ejemplo 02: S12_E02                   *
* Prueba de la clase  Nodo_AB           *
* Crear un estructura con varios nodos  *
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
    // Crear y conectar varios nodos
    Nodo_AB *Raiz = new Nodo_AB('A');
    Raiz->ADD_IZQ('B')->ADD_IZQ('D')->ADD_IZQ('G')->ADD_DER('J');
    Raiz->ADD_DER('C')->ADD_IZQ('E');
    Raiz->H_Der->ADD_DER('F')->ADD_IZQ('H');
    Raiz->H_Der->H_Der->ADD_DER('I');
    Raiz->Muestra_Nodo();
    // Mostrar el árbol
    Raiz->Muestra_Nodos(0);
    cout<<endl;
    delete Raiz->H_Der->H_Der->H_Der->H_Izq;
    delete Raiz->H_Der->H_Der->H_Der;
    delete Raiz->H_Der->H_Der;
    delete Raiz->H_Der;
    delete Raiz->H_Izq->H_Der;
    delete Raiz->H_Izq->H_Izq->H_Der;
    delete Raiz->H_Izq->H_Izq->H_Izq;  
    delete Raiz->H_Izq->H_Izq;
    delete Raiz->H_Izq;
    delete Raiz;

    return 0;
}