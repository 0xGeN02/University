/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 12 Clase Nodo_AB               *
* Fichero Declaraciones de la Clase     *
* Declaración de la Clase Nodo_AB       *
* Clase Nodo_AB (Árbol Binario)         *
* Programa exclusivo para uso académico *
* Adaptado por: Eladio Dapena Gonzalez  *
* Fecha: 26/03/2023                     *
*****************************************/
#include "Nodo_AB.h"
//    Constructores de la clase Nodo_AB
Nodo_AB::Nodo_AB(Tipo x) 
 {
  Valor = x;
  H_Izq = nullptr;
  H_Der = nullptr;
 }

 // Agregar Hijo izquierdo
Nodo_AB* Nodo_AB::ADD_IZQ(Tipo x) 
 {
  delete H_Izq;
  H_Izq = new Nodo_AB(x);
  return H_Izq;
 }
// Agregar Hijo Derecho
Nodo_AB* Nodo_AB::ADD_DER(Tipo x) 
 {
  delete H_Der;
  H_Der = new Nodo_AB(x);
  return H_Der;
 }
 void Nodo_AB::Muestra_Nodo() const 
{
  cout<<"[";
  if (H_Izq != nullptr) 
    cout<<H_Izq->Valor;
  cout<<"]"<<" <- ["<<Valor<<"] -> [";
  if (H_Der != nullptr) 
    cout<<H_Der->Valor;
  cout<<"]"<<endl;

} 
// Pregunta si tienen hijo izquierdo
 bool Nodo_AB::Tiene_H_Izq(Nodo_AB* x) const 
 {
  bool a=true;
  if (x->H_Izq == nullptr) 
    a=false;
 return a;
 }
// Pregunta si tienen hijo derecho
bool Nodo_AB::Tiene_H_Der(Nodo_AB* x) const 
 {
  bool a=true;
  if (x->H_Der == nullptr) 
    a=false;
  return a;
 }
// Pregunta si no tienen hijos (Hoja)
 bool Nodo_AB::Es_Hoja(Nodo_AB* x) const 
 {
  bool a=true;
  if ((x->H_Der != nullptr)||(x->H_Izq != nullptr) )
    a=false;
  return a;
 }
// Muestra un nodos y sus hijos en forma de árbol
void Nodo_AB::Muestra_Nodos(int Nivel = 0) const 
{
 if (H_Der != nullptr) 
    H_Der->Muestra_Nodos(Nivel + 4);
 cout << string(Nivel, ' ') << Valor << endl;
 if (H_Izq != nullptr) 
    H_Izq->Muestra_Nodos(Nivel + 4);
} 
// Destructor de la clase
Nodo_AB::~Nodo_AB()
 {
  delete H_Izq;
  delete H_Der;
 }