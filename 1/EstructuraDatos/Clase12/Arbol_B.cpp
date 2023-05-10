/************************************************
* Asignatura: Estructura de Datos               *
* Sesión 12 Clase Arbol_B                       *
* Fichero de Declaraciones de la clase Arbol_B  *
* Utiliza Clase Nodo_AB                         *
* Adaptado por: Eladio Dapena Gonzalez          *
* Fecha: 26/03/2023                             *
*************************************************/

#include "Arbol_B.h"

/**********************************************
 *        MÉTODOS DE LA CLASE ÁRBOL BINARIO   *
 **********************************************/

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

/************************************************
 *   MÉTODOS DE RECORRIDO DE UN ÁRBOL BINARIO   *
 ************************************************/

/**   RECORRIDO POR NIVEL DE UN ÁRBOL BINARIO   **/ 
void Arbol_B::R_Nivel() 
{
 if (Raiz==nullptr) 
 {
    return;
 }
 queue<Nodo_AB *> cola;
 cola.push(Raiz);
 while (!cola.empty()) 
 {
  Nodo_AB * nodo_actual = cola.front();
  cola.pop();
  cout << nodo_actual->Valor << " ";
  if (nodo_actual->H_Izq) 
  {
    cola.push(nodo_actual->H_Izq);
  }
  if (nodo_actual->H_Der) 
  {
    cola.push(nodo_actual->H_Der);
  }
 }
}

/**   RECORRIDO PREORDEN DE UN ÁRBOL BINARIO     **/ 
void Arbol_B::R_Preorden(Nodo_AB * nodo) 
{
 if (nodo) 
 {
    cout << nodo->Valor << " ";
    R_Preorden(nodo->H_Izq);
    R_Preorden(nodo->H_Der);
 }
}

/**   RECORRIDO INORDEN DE UN ÁRBOL BINARIO     **/ 
void Arbol_B::R_Inorden(Nodo_AB * nodo) 
{
 if (nodo) 
 {
    R_Inorden(nodo->H_Izq);
    cout << nodo->Valor << " ";
    R_Inorden(nodo->H_Der);
 }
}

/**   RECORRIDO POSTORDEN DE UN ÁRBOL BINARIO   **/ 
void Arbol_B::R_Postorden(Nodo_AB * nodo) 
{
 if (nodo) 
 {
    R_Postorden(nodo->H_Izq);
    R_Postorden(nodo->H_Der);
    cout << nodo->Valor << " ";
 }
}

/**   CAMINO ENTRE DOS NODOS DE UN ÁRBOL BINARIO   **/
void Arbol_B::Muestra_Camino(Tipo valor1, Tipo valor2){
 Nodo_AB* nodo1 = Busca_Nodo(valor1);
 Nodo_AB* nodo2 = Busca_Nodo(valor2);
 if (nodo1 == nullptr || nodo2 == nullptr) 
 {
  cout << "NODO NULO" << endl;
        return;
 }
 if (nodo1 == nodo2) 
 {
  cout <<nodo1->Valor << endl;
  return;
 }
 unordered_map<Nodo_AB*, Nodo_AB*> padres;
 queue<Nodo_AB*> cola;
 cola.push(Raiz);
 while (!cola.empty()) 
 {
  Nodo_AB* actual = cola.front();
  cola.pop();
  if (actual->H_Izq != nullptr) 
  {
    padres[actual->H_Izq] = actual;
    cola.push(actual->H_Izq);
  }
  if (actual->H_Der != nullptr) 
  {
    padres[actual->H_Der] = actual;
    cola.push(actual->H_Der);
  }
  if (actual == nodo2) 
  {
    break;
  }
 }
 vector<Tipo> camino;
 Nodo_AB* actual = nodo2;
 while (actual != nodo1) 
 {
  camino.push_back(actual->Valor);
  actual = padres[actual];
  if (actual == nullptr) 
  {
    cout << "\tNO HAY CAMINO" << endl;
            return;
  }
 }
 camino.push_back(nodo1->Valor);
 //cout << "\tCAMINO : ";
 for (int i = camino.size() - 1; i >= 0; i--) 
 {
  if (i>=1)
   cout << camino[i] << "->";
  else
   cout << camino[i] << " ";
 }
    cout << endl;
}

Nodo_AB* Arbol_B::Busca_Nodo(Tipo valor) 
{
 Nodo_AB* actual = Raiz;
 while (actual != nullptr) 
 {
  if (valor == actual->Valor) 
  {
    return actual;
  } else 
  if (valor < actual->Valor) 
  {
    actual = actual->H_Izq;
  } else 
  {
    actual = actual->H_Der;
  }
 }
 return nullptr;
}