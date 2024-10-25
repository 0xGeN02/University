// Asignatura: Estructura de Datos
//FICHERO DE DECLARACIONES Line/Cola/Line
// Biblioteca
//#include<stdio.h>
//#include<stdlib.h>
#include "Line.h"
/***********************************************************************
 * Rutina: Line_Add		Tipo: Apuntador a Nodo	
 * Parámetros:	1.- Apuntador a un tipo Nodo  (Top. Inicio de la Line)
 *              2.- Apuntador a el Nodo a agregar
 * Descripción: Agrega al final de la Line un nuevo nodo
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
// Agregar un nodo al final de la lista
struct Nodo *Line_Add(struct Nodo *ini, struct Nodo *N)
{
 struct Nodo *a;
 if (ini==NULL)
 	ini=N;
 else
 {
 	a=ini;
 	while (a->sig!=NULL)
	 a=a->sig;
 	a->sig=N;
 }
 return ini;
}


// Contar los nodos de la Line
/*******************************************************************
 * Rutina: Contar nodos		Tipo: Entero	
 * Parámetros:	1.- Apuntador a un tipo Nodo  (Inicio de la Lista)
 * Descripción: Contar la cantidad de nodos en la lista
 * Retorna : Cantidad de nodos
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio dapena Gonzalez
 ******************************************************************/
int Nodos_Line(struct Nodo *ini)
{
 struct Nodo *a;  // Nodo auxiliar local
 int c=0;	// Contador de Nodos
 a=ini;
 while (a!=NULL)
 {
 	 a=a->sig;	
 	 c++;
 }
 return c;  // Cantidad de Nodos
}
/*******************************************************************
 * Rutina: Mostrar_Line		Tipo: Procedimiento	
 * Parámetros:	1.- Apuntador a un tipo Nodo  (Inicio de la Lista)
 * Descripción: Muestra el código de cada elemento en la Line. 
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio Dapena Gonzalez
 ******************************************************************/
void  Mostrar_Line(struct Nodo *a)
{
 struct Nodo *i;
 int c=0;
 i=a;
 printf("   Elementos en la Line   \n");
 while (i!=NULL)
 {
    c++;
	printf(" [ %d ] ",i->Inf.Codigo);
	if (i->sig!=NULL)
	  printf("->");
  	i=i->sig;
 }
 printf("\n");
}
// Vaciar Line y liberar memoria.
/*******************************************************************
 * Rutina: Vaciar_Line		Tipo: Apuntador a Nodo	
 * Parámetros:	1.- Apuntador a un tipo Nodo  (Top. Inicio de la Line)
 * Descripción: Libera la memoria utilizada por los nodos de la Line
 * Rutina diseñada para docencia
 * Retorna un puntero con el valor NULL.
 * Realizado por: Dr. Eladio dapena Gonzalez
 ******************************************************************/
struct Nodo *Vaciar_Line(struct Nodo *ini)
{
 struct Nodo *a;
 if (ini!=NULL)
 do
 {
  a=ini;
  ini=a->sig;
  free(a);
  }while (ini!=NULL);
 return NULL;
}
/***********************************************************************
 * Rutina: Line_Del		Tipo: Apuntador a Nodo
 * Parámetros: 1.- Apuntador al un tipo Nodo  (Top. Inicio de la Line)
 * Descripción: Elimina el Tope de la Line
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio dapena Gonzalez
 ***********************************************************************/
struct 	Nodo *Line_Del(struct Nodo *ini)
{
	struct Nodo *aux;
	int k;
	if (ini!=NULL)
	{
        aux=ini;
		ini=ini->sig;
		Elimina_Nodo(aux);
	}
return ini;
}