// Asignatura: Estructura de Datos
//FICHERO DE DECLARACIONES LISTA SIMPLE
// Biblioteca
//#include<stdio.h>
//#include<stdlib.h>
#include "Lista_Simple.h"
// Declaración de Funciones
// Función Crea_Nodo_Vacio
struct Nodo *Crea_Nodo()
{
 return (struct Nodo *)calloc(1,sizeof(struct Nodo));
}			
// Entrada de datos de un nodo
void Leer_Nodo(struct Nodo *a)
{
 printf("CODIGO : ");
 scanf("%d",&a->Inf.Codigo);
 // Otros datos
 a->sig=NULL;
}
// Mostrar los datos de un nodo
void Mostrar_Nodo(struct Nodo *a)
{
printf("\tCODIGO : %d\n",a->Inf.Codigo);
// Otros datos
}
/***********************************************************************
 * Rutina: Add_End		Tipo: Apuntador a Nodo	
 * Parámetros:	1.- Apuntador a un tipo Nodo  (Inicio de la Lista)
 *              2.- Apuntador a el Nodo a agregar
 * Descripción: Agrega al final de la lista un nuevo nodo
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio dapena Gonzalez
 ***********************************************************************/
// Agregar un nodo al final de la lista
struct Nodo *Add_End(struct Nodo *ini, struct Nodo *N)
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

/***********************************************************************
 * Rutina: Add_Start		Tipo: Apuntador a Nodo	
 * Parámetros:	1.- Apuntador a un tipo Nodo  (Inicio de la Lista)
 *              2.- Apuntador a el Nodo a agregar
 * Descripción: Agrega al inicio de la lista un nuevo nodo
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio dapena Gonzalez
 ***********************************************************************/
struct Nodo *Add_Start(struct Nodo *ini, struct Nodo *N)
{
 struct Nodo *a;
 if (ini==NULL)
  	ini=N;
  else
 {
 	a=N;
 	N->sig=ini;
	ini=a;
 }
 return ini;
}

// Contar los nodos de la lista
/*******************************************************************
 * Rutina: Contar nodos		Tipo: Entero	
 * Parámetros:	1.- Apuntador a un tipo Nodo  (Inicio de la Lista)
 * Descripción: Contar la cantidad de nodos en la lista
 * Retorna : Cantidad de nodos
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio dapena Gonzalez
 ******************************************************************/
int Contar_Nodos(struct Nodo *ini)
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
// Vaciar lista y liberar memoria.
/*******************************************************************
 * Rutina: Vaciar_Lista		Tipo: Apuntador a Nodo	
 * Parámetros:	1.- Apuntador a un tipo Nodo  (Inicio de la Lista)
 * Descripción: Libera la memoria utilizada por los nodos de la lista
 * Rutina diseñada para docencia
 * Retorna un puntero con el valor NULL.
 * Realizado por: Dr. Eladio dapena Gonzalez
 ******************************************************************/
struct Nodo *Vaciar_Lista(struct Nodo *ini)
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
/*******************************************************************
 * Rutina: Mostrar_Lista		Tipo: Procedimiento	
 * Parámetros:	1.- Apuntador a un tipo Nodo  (Inicio de la Lista)
 * Descripción: Muestra el código de cada nodo. 
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio dapena Gonzalez
 ******************************************************************/
void  Mostrar_Lista(struct Nodo *a)
{
 struct Nodo *i;
 int c=0;
 i=a;
 printf("   Elementos de la lista   \n");
 while (i!=NULL)
 {
    c++;
	printf("   %d: %d\n",c,i->Inf.Codigo);
  	i=i->sig;
 }
}
/***********************************************************************
 * Rutina: Del_Nodo		Tipo: Apuntador a Nodo
 * Parámetros: 1.- Nodo a eliminar
 *             2.- Apuntador a un tipo Nodo  (Inicio de la Lista)
 * Descripción: Elimina un nodo de la lista
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio dapena Gonzalez
 ***********************************************************************/
struct 	Nodo *Del_Nodo(int n, struct Nodo *ini)
{
	struct Nodo *ni,*ne;
	int k;
	ni=ini;
	if (n==1)
	{
		ini=ini->sig;
		free(ni);
	}
	else
	{
	 for (k=1;k<(n-1);k++)
   {
		ni=ni->sig;
	 }
	 ne=ni->sig;
	 ni->sig=ne->sig;
	 free(ne);
 }
return ini;
}