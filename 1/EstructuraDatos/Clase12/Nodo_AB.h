/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 12 Clase Nodo_AB               *
* Fichero Cabecera de la Clase          *
* Definición de la Clase Nodo_AB        *
* Clase Nodo_AB (Árbol Binario)         *
* Programa exclusivo para uso académico *
* Adaptado por: Eladio Dapena Gonzalez  *
* Fecha: 26/03/2023                     *
*****************************************/
#include <iostream>
using namespace std;
// Definir el tipo de dato del Nodo
typedef int Tipo;

class Nodo_AB 
{
public:
// Atributos
    Tipo         Valor;
    Nodo_AB*     H_Izq;
    Nodo_AB*     H_Der;

//    Constructores de la clase Nodo_AB
 Nodo_AB( Tipo );
 Nodo_AB( Tipo, Nodo_AB*, Nodo_AB* );
 // Muestra nodo
 void Muestra_Nodo() const;
 // Agregar Hijo izquierdo
 Nodo_AB* ADD_IZQ( Tipo );
// Agregar Hijo Derecho
 Nodo_AB* ADD_DER( Tipo );
// Pregunta si tienen hijo izquierdo
 bool Tiene_H_Izq(Nodo_AB * ) const;
// Pregunta si tienen hijo derecho
 bool Tiene_H_Der(Nodo_AB * ) const;
// Pregunta si no tienen hijos (Hoja)
 bool Es_Hoja(Nodo_AB * ) const;
// Muestra un nodos y sus hijos en forma de árbol
 void Muestra_Nodos(int) const;
// Destructor de la clase
~Nodo_AB(); 
};