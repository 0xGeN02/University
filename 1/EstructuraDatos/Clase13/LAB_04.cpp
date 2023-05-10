// Asignatura: Estructura de Datos
// Práctica Evaluada 04
// Clase Grafo Dirigido Ponderado
// Evaluación: Manuel Mateo Delgado
//    Crear y Mostrar el Grafo de la Práctica (2 pts.)
//    Mostrar Caminos entre Nodos 0 y 7       (2 pts.)
//    Mostrar Camino mínimo entre Nodos 0 y 7 (2 pts.)
//    Mostrar Caminos entre Nodos 7 y 0       (2 pts.)
//    Mostrar Camino mínimo entre Nodos 7 y 0 (2 pts.)
// Realizado por: INDIQUE SU NOMBRE
// Fecha 28/03/2023        
// Inclusión de Bibliotecas
#include "GrafoDP.h"
int main() {
//  CREACIÓN DE LA VARIABLE GDO TIPO GrafoDP
 GrafoDP GDP(8);   // LA VARIABLE DEL GRAFO ES GDP

 //
 // Utilice el método Agregar_Aristas de la clase GrafoDP
 // CONSTRUIR EL GRAFO DE LA PRÁCTICA EVALUADA AGREGANDO TODAS LAS ARÍSTAS
 // EJEMPLO : GDP.Agregar_Arista(0, 1, 2);  primera arísta del nodo 0
GDP.Agregar_Arista(0,1,2);
GDP.Agregar_Arista(0,2,6);
GDP.Agregar_Arista(1,0,1);
GDP.Agregar_Arista(1,2,2);
GDP.Agregar_Arista(2,4,4);
GDP.Agregar_Arista(4,1,4);
GDP.Agregar_Arista(4,3,4);
GDP.Agregar_Arista(3,0,5);
GDP.Agregar_Arista(4,6,7);
GDP.Agregar_Arista(6,7,3);
GDP.Agregar_Arista(7,5,2);
GDP.Agregar_Arista(5,4,4);
GDP.Agregar_Arista(3,5,3);

 cout<<"****    GRAFO DIRIGIDO PONDERADO    ****"<<endl;


// INVOCAR EL MÉTODO PARA MOSTRAR EL GRAFO
 GDP.Muestra_GrafoDP();
 
 cout<<endl;
 cout<<"--- CAMINOS ENTRE LOS VERTICES [0,7]"<<endl;


 // INVOCAR EL MÉTODO PARA MOSTRAR LOS CAMINOS ENTRE LOS NODOS 0 y 7
 GDP.Caminos(0,7);

 cout<<"  - CAMINO MINIMO ENTRE LOS VERTICES [0,7]"<<endl;


 // INVOCAR EL MÉTODO PARA MOSTRAR LOS CAMINOS ENTRE LOS NODOS 0 y 7
 // Camino_Minimo_Dijkstra
 GDP.Camino_Minimo_Dijkstra(0,7);

 cout<<endl;

 cout<<"--- CAMINOS ENTRE LOS VERTICES [7,0]"<<endl;


 // INVOCAR EL MÉTODO PARA MOSTRAR LOS CAMINOS ENTRE LOS NODOS 0 y 7
GDP.Caminos(7,0);

cout<<"  - CAMINO MINIMO "<<endl;


 // INVOCAR EL MÉTODO PARA MOSTRAR LOS CAMINOS ENTRE LOS NODOS 0 y 7
 // Camino_Minimo_Dijkstra
 GDP.Camino_Minimo_Dijkstra(7,0);


 cout<<endl;
 return 0;

}