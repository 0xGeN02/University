/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 12 Clase Arbol_B               *
* Fichero S12_E04.cpp                   *
* Utiliza Clase Nodo_AB                 *
* Métodos Básicos:                      *
*  Constructor y Desctructor            *
*  Mostrar Árbol, Eliminar Nodo         * 
^ Métodos PROPIEDADES DEL ÁRBOL         *
*  GradO, Peso, Altura,                 *
*  Factor de Equilibrio Lleno, Completo *
* Programa exclusivo para uso académico *
* Adaptado por: Eladio Dapena Gonzalez  *
* Fecha: 26/03/2023                     *
*****************************************/
// BIBLIOTECAS DE LA CLASE Arbol_B
#include "Nodo_AB.h"
#include <vector>
#include <queue>
//BIBLIOTECA DE USO EN PROGRAMA PRINCIPAL
#include <conio.h>
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
};

//  RUTINA DE USO POR EL PROGRAMA PRINCIPAL
void Pausa() 
{
 cout << "Presione una tecla para continuar...";
 _getch(); 
 cout << endl; 
}
// PROGRAMA PRINCIPAL DE PRUEBA DE LOS MÉTODOS
int main() 
{
 int i;
 Arbol_B* AB=new Arbol_B();
 vector<int> Nodos = {50,40,60,35,45,55,65,30,38,42,48,70,62,52,58,61,43};
 for (i = 0; i < Nodos.size(); ++i) 
 {
    AB->Agrega_Nodo(Nodos[i]);
 }
 cout<<"***   ARBOL BINARIO   ***"<<endl;
 cout << "\t REPRESENTACION " << endl;
 AB->Muestra_Arbol(AB->Raiz, 0);
 AB->Propiedades_AB(AB);
 Pausa();
 cout<<"ELIMINAR NODO 43 "<<endl;
 AB->Elimina_Nodo(AB->Raiz,43);
 cout << "\t REPRESENTACION " << endl;
 AB->Muestra_Arbol(AB->Raiz, 0);
 AB->Propiedades_AB(AB);
 Pausa();
 cout<<"ELIMINAR NODO 61 "<<endl;
 AB->Elimina_Nodo(AB->Raiz,61);
 cout << "\t REPRESENTACION " << endl;
 AB->Muestra_Arbol(AB->Raiz, 0);
 AB->Propiedades_AB(AB);
 Pausa();
 cout<<"ELIMINAR NODOS 62 y 70"<<endl;
 AB->Elimina_Nodo(AB->Raiz,62);
 AB->Elimina_Nodo(AB->Raiz,70);
 cout << "\t REPRESENTACION " << endl;
 AB->Muestra_Arbol(AB->Raiz, 0);
 AB->Propiedades_AB(AB);
 Pausa();
 cout<<"ELIMINAR NODOS 30 y 38"<<endl;
 AB->Elimina_Nodo(AB->Raiz,30);
 AB->Elimina_Nodo(AB->Raiz,38);
 cout << "\t REPRESENTACION " << endl;
 AB->Muestra_Arbol(AB->Raiz, 0);
 AB->Propiedades_AB(AB);
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

/************************************************
 *   MÉTODOS PROPIEDADES DE UN ÁRBOL BINARIO    *
 ************************************************/

//**   MUESTRA PROPIESDADES DEL ÁRBOL BINARIO  **/
void Arbol_B::Propiedades_AB(Arbol_B * R)
{
 cout<<" PROPIEDADES"<<endl;
 cout<<"\tGrado        = "<<R->Grado(R->Raiz); 
 cout<<endl;
 cout<<"\tPeso         = "<<R->Peso(R->Raiz); 
 cout<<endl;
 cout<<"\tAltura       = "<<R->Altura(R->Raiz); 
 cout<<endl;
 cout<<"\tFactor Eq    = "<<R->Factor_Eq(R->Raiz); 
 cout<<endl;
 cout<<"\tEs Completo  = ";
 if (R->EsCompleto(R->Raiz))
   cout<<"SI"<<endl;
  else
   cout<<"NO"<<endl;
 cout<<"\tEs Lleno     = ";
 if (R->EsLleno(R->Raiz))
   cout<<"SI"<<endl;
  else
   cout<<"NO"<<endl;
}

/**   GRADO DE UN ÁRBOL BINARIO  **/ 
int Arbol_B::Grado(Nodo_AB* raiz) const
{
 int grado = 0;
 if (raiz != nullptr) 
 {
  grado = max(Grado(raiz->H_Izq), Grado(raiz->H_Der));
  if (raiz->H_Izq != nullptr && raiz->H_Der != nullptr) 
  {
    grado = max(grado, 2);
  }
  else 
  if (raiz->H_Izq != nullptr || raiz->H_Der != nullptr) 
  {
    grado = max(grado, 1);
  }
 }
 return grado;
}

/**   PESO DE UN ÁRBOL BINARIO  **/ 
int Arbol_B::Peso(Nodo_AB* raiz) const
{
 if (raiz == nullptr) 
 {
    return 0;
 }
 int peso_izq = 0;
 int peso_der = 0;
 if (raiz->H_Izq != nullptr) 
 {
  peso_izq = Peso(raiz->H_Izq);
 }
 if (raiz->H_Der != nullptr) 
 {
  peso_der = Peso(raiz->H_Der);
 }
 return peso_izq + peso_der + 1;
}

/**   ALTURA DE UN  DE UN ÁRBOL BINARIO   **/ 
int Arbol_B::Altura(Nodo_AB* raiz) const
{
 if (raiz == nullptr) 
 {
  return -1;
 }
 int altura_izq = Altura(raiz->H_Izq);
 int altura_der = Altura(raiz->H_Der);
 return 1 + max(altura_izq, altura_der);
}
/**   FACTOR DE EQUILIBRIO DE UN ÁRBOL BINARIO   **/ 
int Arbol_B::Factor_Eq(Nodo_AB* raiz) const 
{
 return Altura(raiz->H_Izq) - Altura(raiz->H_Der);
}

/**   PROPIEDAD COMPLETO DE UN ÁRBOL BINARIO **/ 
bool Arbol_B::EsCompleto(Nodo_AB* raiz) const 
{
 if (raiz == nullptr) 
 {
  return true;
 }
 queue<Nodo_AB*> q;
 q.push(raiz);
 bool ultimoNivel = false;
 while (!q.empty()) 
 {
  Nodo_AB* nodo = q.front();
  q.pop();
  // Verificar si este es el último nivel
  if (nodo->H_Izq == nullptr && nodo->H_Der == nullptr) 
  {
    ultimoNivel = true;
  } else 
  if (nodo->H_Izq == nullptr || nodo->H_Der == nullptr) 
  {
   // Si un nodo tiene solo un hijo, entonces no es completo
   return false;
  } else 
  {
    // Agregar los hijos del nodo a la cola
    q.push(nodo->H_Izq);
    q.push(nodo->H_Der);
  }
  // Verificar si todos los nodos del último nivel están lo más a la izquierda posible
  if (ultimoNivel) 
  {
    if (nodo->H_Izq != nullptr || nodo->H_Der != nullptr) 
    {
      return false;
    }
  }
 }
 return true;
}
/**   PROPIEDAD LLENO DE UN ÁRBOL BINARIO  **/ 
bool Arbol_B::EsLleno(Nodo_AB* raiz) const 
{
 if (raiz == nullptr) 
 {
  return true;
 }
 // Si el nodo raíz es una hoja ÁRBOL LLENO
 if (raiz->H_Izq == nullptr && raiz->H_Der == nullptr) 
 {
  return true;
 }
  // Si un nodo tiene dos hijos, verificar que ambos subárboles sean llenos 
 if (raiz->H_Izq != nullptr && raiz->H_Der != nullptr) 
 {
  return EsLleno(raiz->H_Izq) && EsLleno(raiz->H_Der);
 }
 // Si no cumple ninguna anterior el árbol NO ESTÁ LLENO
 return false;
}