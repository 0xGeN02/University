/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 12 Clase Arbol_B               *
* Fichero S12_E03.cpp                   *
* Utiliza Clase Nodo_AB                 *
* Métodos Básicos:                              *
*  Constructor y Desctructor            *
*  Mostrar Árbol, Eliminar Nodo         * 
* Programa exclusivo para uso académico *
* Adaptado por: Eladio Dapena Gonzalez  *
* Fecha: 26/03/2023                     *
*****************************************/
// BIBLIOTECAS DE LA CLASE Arbol_B
#include "Nodo_AB.h"
#include <vector>
#include <queue>
#include <string>
#include <math.h>

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
};
//  RUTINA DE USO POR EL PROGRAMA PRINCIPAL
// RREMPLAZAR POR OTRA PARA macOS con Intel y/o M1
void Pausa() 
{
 cout << "Presione una tecla para continuar...";
 cin.get();
 cout << endl; 
}
// PROGRAMA PRINCIPAL DE PRUEBA DE LOS MÉTODOS
int main() 
{
 int i;
 Arbol_B* AB = new Arbol_B();
 vector<int> Nodos = {50,40,60,35,45,55,65,30,38,42,48,70,62,52,58,61,43};
 for (i = 0; i < Nodos.size(); ++i) 
 {
    AB->Agrega_Nodo(Nodos[i]);
 }
 cout << "\t REPRESENTACION " << endl;
 AB->Muestra_Arbol(AB->Raiz, 0);
 Pausa();
 cout << "\t ELIMINAR NODO 45 " << endl;
 AB->Elimina_Nodo(AB->Raiz,45);
 AB->Muestra_Arbol(AB->Raiz, 0);
 Pausa();
 cout << "\t AGREGAR NODO 45 " << endl;
 AB->Agrega_Nodo(45);
 AB->Muestra_Arbol(AB->Raiz, 0);
 Pausa();
 delete AB;
} 

/******************************************
 *        MÉTODOS BÁSICOS ÁRBOL BINARIO   *
 ******************************************/

/**   CONSTRUCTORES  DE UN ÁRBOL BINARIO **/
 Arbol_B::Arbol_B() 
 {
   Raiz = nullptr;
 }
 Arbol_B::Arbol_B(Tipo x) 
 {
   Raiz->Valor=x;
   Raiz->H_Izq = nullptr;
   Raiz->H_Der = nullptr;
 }

/**   DESTRUCTOR  DE UN ÁRBOL BINARIO **/
Arbol_B::~Arbol_B()
{
   DestruirArbol(Raiz);
}

/**   AGREGA NODO A UN ÁRBOL BINARIO  **/
void Arbol_B::Agrega_Nodo(Tipo valor) 
{
 if (Raiz==nullptr)
 { 
    Raiz = new Nodo_AB(valor);
    Raiz->H_Izq = nullptr;
    Raiz->H_Der = nullptr;   
 }
 else  
 {
  Nodo_AB * nodo_actual = Raiz;
  while (nodo_actual) 
  {
   if (valor < nodo_actual->Valor) 
   {
    if (!nodo_actual->H_Izq) 
    {
     nodo_actual->ADD_IZQ(valor);
     break;
    }
    else 
    {
     nodo_actual = nodo_actual->H_Izq;
    }
   }
   else 
   {
    if (!nodo_actual->H_Der)  
    {
     nodo_actual->ADD_DER(valor);
     break;
    }
    else 
    {
     nodo_actual = nodo_actual->H_Der;
    }
   }
  }
 }
}

/**   ELIMINAR UN NODO DE UN ÁRBOL BINARIO **/
Nodo_AB * Arbol_B::Elimina_Nodo(Nodo_AB * nodo, Tipo valor) 
{
 if (nodo == nullptr) 
 {
    return nullptr;
 }
 if (valor < nodo->Valor) 
 {
    nodo->H_Izq = Elimina_Nodo(nodo->H_Izq, valor);
 } 
 else 
 if (valor > nodo->Valor) 
  {
    nodo->H_Der = Elimina_Nodo(nodo->H_Der, valor);
  } 
 else 
 {
  if (nodo->H_Izq == nullptr) 
  {
    Nodo_AB * temp = nodo->H_Der;
    delete nodo;
    return temp;
  } 
  else 
   if (nodo->H_Der == nullptr) 
    {
      Nodo_AB * temp = nodo->H_Izq;
      delete nodo;
      return temp;
    }
   Nodo_AB * temp = Nodo_Mas_Izquierdo(nodo->H_Der);
   nodo->Valor = temp->Valor;
   nodo->H_Der = Elimina_Nodo(nodo->H_Der, temp->Valor);
 }
  return nodo;
}

/**   MÉTODO AUXILIAR DE ELIMINA NODO  **/
Nodo_AB * Arbol_B::Nodo_Mas_Izquierdo(Nodo_AB * nodo) 
{
 Nodo_AB * actual = nodo;
 while (actual->H_Izq != nullptr) 
 {
   actual = actual->H_Izq;
 }
 return actual;
}

/**   MUESTRA ÁRBOL BINARIO  **/
void Arbol_B::Muestra_Arbol(Nodo_AB *nodo, int nivel = 0) 
{
 if (nodo) 
 {
  Muestra_Arbol(nodo->H_Der, nivel + 1);
  for (int i = 0; i < nivel; i++) 
  {
   cout << "   ";
  }
  cout << nodo->Valor << endl;
  Muestra_Arbol(nodo->H_Izq, nivel + 1);
 }
}

/**   DESTRUIR UN ÁRBOL BINARIO **/
void Arbol_B::DestruirArbol(Nodo_AB * raiz)
{
    if (raiz != nullptr) 
    {
        DestruirArbol(raiz->H_Izq);
        DestruirArbol(raiz->H_Der);
    }
    delete raiz;
}