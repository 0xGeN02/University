// Asignatura: Estructura de Datos
// Biblioteca para nodos simples
// Fichero de declaraciones Nodo_Simple.c
// Declaraciones de Operaciones Nodo Simple: Crear Nodo, Leer Nodo, Mostrar Nodo
// Programa exclusivo para uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha: 18/02/2023        
// Inclusión del Fichero Cabecera de la Biblioteca
#include "Nodo_Simple.h"
//
// Declaración de Funciones y procedimientos de la biblioteca
//
//
/***********************************************************************
 * Rutina		: *Crea_Nodo	Función		Tipo: Apuntador a Nodo	
 * Parámetros	:	
 * Descripción	: Crea un nuevo dato del tipo nodod simple
 * Retorna		: Un puntero con la dirección de memoria del nodo creado.
 * Diseño		: Rutina para uso académico
 * Autor		: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
struct Nodo *Crea_Nodo()
{
 return (struct Nodo *)calloc(1,sizeof(struct Nodo));
}			
// 
/***********************************************************************
 * Rutina		: Leer_Nodo	Procedimiento 	Tipo: void	
 * Parámetros	:	1.- Apuntador a un tipo Nodo 
 *              	2.- Apuntador a el Nodo a agregar
 * Descripción	: Entrada de la información del nodo
 * Retorna		:		void
 * Diseño		: Rutina para uso académico
 * Autor		: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
void Leer_Nodo(struct Nodo *a)
{
 printf("\tCODIGO : ");
 scanf("%d",&a->Inf.Codigo);
 // Otros datos
 a->sig=NULL;
}

/***********************************************************************
 * Rutina		: Mostrar_Nodo	Procedimiento 	Tipo: void	
 * Parámetros	:	1.- Apuntador a un tipo Nodo 
 * Descripción	: Muestra la información del nodo indicado
 * Retorna		:		void
 * Diseño		: Rutina para uso académico
 * Autor		: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
void Mostrar_Nodo(struct Nodo *a)
{
printf("\tCODIGO : %d\n",a->Inf.Codigo);
// Otros datos
}

/***********************************************************************
 * Rutina		: Elimina_Nodo	Función 	Tipo: Apuntador a Nodo		
 * Parámetros	:	1.- Apuntador a un tipo Nodo 
 * Descripción	: Libera la memoria asignada a un nodo
 * Retorna		: Puntero con valor NULL.
 * Diseño		: Rutina para uso académico
 * Autor		: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
struct Nodo *Elimina_Nodo(struct Nodo *a)
{
 free(a);
 return (NULL);
}