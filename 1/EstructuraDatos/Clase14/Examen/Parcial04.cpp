// Asignatura: Estructura de Datos
// PRUEBA_PARCIAL 04 PARTE 2
// REALIZADO POR:   mateo Delgado
#include "Arbol_B.h"                         // NO MODIFICAR                 
int main()                                   // NO MODIFICAR
{                                            // NO MODIFICAR
 Arbol_B* AB = new Arbol_B();                // NO MODIFICAR
 vector<int> Nodos;                          // NO MODIFICAR
 NUM_ALEA_P4(Nodos, 50, 2, 98, 10);          // NO MODIFICAR
 for (unsigned i = 0; i < Nodos.size(); ++i) // NO MODIFICAR
 {                                           // NO MODIFICAR
  AB->Agrega_Nodo(Nodos[i]);                 // NO MODIFICAR
 }                                           // NO MODIFICAR
// PARTE EVALUADA
/*** APARTADO 01  MOSTRAR EL ÁRBOL ***/
 cout << "******   ARBOL BINARIO   ****** " << endl; // NO MODIFICAR
// ESCRIBA ABAJO EL MÉTODO PARA MOSTRAR EL ÁRBOL
    AB->Muestra_Arbol(AB->Raiz, 0); 

 Pausa();        // NO MODIFICAR
/*** APARTADO 02  PROPIEDADES DEL ÁRBOL ***/
// ESCRIBA ABAJO EL MÉTODO PARA MOSTRAR LAS PROPIEDADES DEL ÁRBOL
    AB->Propiedades_AB(AB);

 Pausa();        // NO MODIFICAR
/*** APARTADO 03  RECORRIDOS DEL ÁRBOL ***/
 cout<<"---RECORRIDOS"<<endl;               // NO MODIFICAR
 cout <<"   Nivel     : ";                  // NO MODIFICAR
 // ESCRIBA ABAJO EL MÉTODO PARA RECORRIDO POR NIVEL
    AB->R_Nivel();

 cout << endl;                             // NO MODIFICAR
 cout <<"   Preorden  : ";                 // NO MODIFICAR  
 // ESCRIBA ABAJO EL MÉTODO PARA RECORRIDO EN PREORDEN
    AB->R_Preorden(AB->Raiz);

 cout << endl;                             // NO MODIFICAR
 cout <<"   Inorden   : ";  
 // ESCRIBA ABAJO EL MÉTODO PARA RECORRIDO EN INORDEN
    AB->R_Inorden(AB->Raiz);
 cout << endl;                              // NO MODIFICAR
 cout <<"   Postorden : ";                  // NO MODIFICAR 
 // ESCRIBA ABAJO EL MÉTODO PARA RECORRIDO EN POSTORDEN
    AB->R_Postorden( AB->Raiz);

 cout << endl;                              // NO MODIFICAR
 Pausa();        // NO MODIFICAR
/*** APARTADO 04  CAMINOS ***/
 cout<<"---CAMINOS"<<endl;                  // NO MODIFICAR
 cout << "\tDel Nodo [50]  al Nodo [ 1]   : ";  // NO MODIFICAR
 // ESCRIBA ABAJO EL MÉTODO PARA MOSTRAR CAMINO ENTRE NODOS [50] Y [1]
    AB->Muestra_Camino( 50 ,  1 );

 cout << "\tDel Nodo [75]  al Nodo [ 1]   : ";  // NO MODIFICAR
 // ESCRIBA ABAJO EL MÉTODO PARA MOSTRAR CAMINO ENTRE NODOS [75] Y [1]
    AB->Muestra_Camino( 75 ,  1 );

 cout << "\tDel Nodo [50]  al Nodo [99]   : ";  // NO MODIFICAR
 // ESCRIBA ABAJO EL MÉTODO PARA MOSTRAR CAMINO ENTRE NODOS [50] Y [99]
    AB->Muestra_Camino( 50 ,  99 );

 cout << "\tDel Nodo [25]  al Nodo [99]   : ";  // NO MODIFICAR
 // ESCRIBA ABAJO EL MÉTODO PARA MOSTRAR CAMINO ENTRE NODOS [50] Y [99]
    AB->Muestra_Camino( 25 ,  99 );

 Pausa();        // NO MODIFICAR
 delete AB;      // NO MODIFICAR

 cout << "Fin del programa" << endl;
 
}