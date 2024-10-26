//Programa prueba clase Arbol binario

#include "Arbol_B.h"

void Pausa() 
{
 cout << "Presione una tecla para continuar...";
 cin.get();
 cout << endl; 
}

int main() {

 Arbol_B* AB = new Arbol_B();
 vector<char> Nodos = {'M','T','G','P','W','N','Y','X','Z','D','K','E','B','Q','C','A','O','U','V','J'};

 for (int i = 0; i < Nodos.size(); ++i) {
    AB->Agrega_Nodo(Nodos[i]);
 }

 cout << "\t REPRESENTACION " << endl;
 AB->Muestra_Arbol(AB->Raiz, 0);

 
 AB->Propiedades_AB(AB); cout<<""<<endl;

 // Recorrido por Nivel
 cout<<"El recorrido por nivel es: "<<endl;
 AB->R_Nivel(); cout<<""<<endl;

 // Recorrido por Preorden
 cout<<"EL recorrido por preorden es: "<<endl;
 AB->R_Preorden(AB->Raiz); cout<<""<<endl;

 // Recorrido por Orden
 cout<<"EL recorrido por orden es:"<<endl;
 AB->R_Inorden(AB->Raiz); cout<<""<<endl;

 // Recorrido por Posorden
 cout<< "El recorrido por postorden es: "<<endl;
 AB->R_Postorden(AB->Raiz); cout<<""<<endl;


 cout<<""<<endl;
 cout<<" CAMINOS "<<endl;
 cout << "\tDel Nodo 'M'  al Nodo 'A'   : ";
 AB->Muestra_Camino( 'M' ,  'A' );
 cout << "\tDel Nodo 'G'  al Nodo 'C'   : ";
 AB->Muestra_Camino( 60 ,  61 );
 cout << "\tDel Nodo 'T'  al Nodo 'X'   : ";
 AB->Muestra_Camino( 'T' ,  'X' );

}

