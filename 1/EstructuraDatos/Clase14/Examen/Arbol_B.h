/****************************************
* Asignatura: Estructura de Datos       *
* Clase Arbol_B                         *
* Fichero Cabecera de la clase Arbol_B  *
* Define  Clase Nodo_AB                 *
* Adaptado por: Eladio Dapena Gonzalez  *
* Fecha: 26/03/2023                     *
*****************************************/
#include  <iostream>
#include  <vector>
#include  <queue>
#include  <iomanip>
#include  <unordered_map>
#include  <algorithm>
#include  <random>
using namespace std;
/*************************************
 * DEFINICIÓN DE LA CLASE  Nodo_AB   *
 *************************************/
// Definir el tipo de dato del Nodo
typedef unsigned Tipo;
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

// RUTINA DE SOPORTE PARA GENERAR NÚMEROS ALEATORIOS
void Pausa();
void NUM_ALEA_P4(vector<int>& , int , int , int , unsigned  );
