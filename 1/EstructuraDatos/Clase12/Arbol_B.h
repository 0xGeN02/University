/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 12 Clase Arbol_B               *
* Fichero Cabecera de la clase Arbol_B  *
* Utiliza Clase Nodo_AB                 *
* Adaptado por: Eladio Dapena Gonzalez  *
* Fecha: 26/03/2023                     *
*****************************************/
// BIBLIOTECAS DE LA CLASE Arbol_B
#include "Nodo_AB.h"
#include <iostream>
#include <vector>
#include <queue>
#include <iomanip>
#include <unordered_map>

/*************************************
 * DEFINICIÓN DE LA CLASE  Arbol_B   *
 *************************************/
class Arbol_B 
{
public:
// ATRIBUTOS DE UN AB
  Nodo_AB * Raiz;
// CONSTRUCTOR DE UN AB
    Arbol_B();
    Arbol_B(Tipo);
// DESTRUCTOR DE UN AB
   ~Arbol_B();
// MÉTODOS BÁSICOS DE UN AB
 void       Agrega_Nodo(Tipo);
 Nodo_AB   *Elimina_Nodo(Nodo_AB * , Tipo );
 Nodo_AB   *Nodo_Mas_Izquierdo(Nodo_AB *);  // Rutina auxiliar de Elimina_Nodo
 void       Muestra_Arbol(Nodo_AB *, int ); 
 void       DestruirArbol(Nodo_AB*);
 // MÉTODOS PROPIEDADES DE UN AB
 void       Propiedades_AB(Arbol_B *);
 int        Grado(Nodo_AB * )  const;
 int        Peso(Nodo_AB * )   const;
 int        Altura(Nodo_AB * ) const;
 int        Factor_Eq(Nodo_AB * ) const;
 bool       EsCompleto(Nodo_AB* ) const; 
 bool       EsLleno(Nodo_AB* ) const;   
 // MÉTODOS RECORRIDO DE UN AB
 void       R_Nivel();
 void       R_Preorden(Nodo_AB * );
 void       R_Inorden(Nodo_AB * );
 void       R_Postorden(Nodo_AB * );
 // MÉTODOS CAMINO ENTRE DOS NODOS EN UN AB
 void       Muestra_Camino(Tipo , Tipo ); 
 Nodo_AB*   Busca_Nodo(Tipo );
};