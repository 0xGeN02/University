// Fichero de declaraciones de rutinas
// Ejemplo 06 Sesión 02
// Realizado por: Eladio Dapena Gonzalez
// Fecha 02/01/2023
// Inclusión del fichero cabecera de la biblioteca
#include "S02_Funciones_07.h"
// Declaración de funciones y procedimientos
/***********************************************************************
 * Rutina: Leer_Arreglo	Tipo: Procedimiento
 * Parámetros:	1.- Tipo Apuntador Entero 	(Arreglo)
 *              2.- Tipo Entero 			(Tamaño del Arreglo)
 * Descripción: Entrada de datos a un arreglo
 * Rutina diseñada para uso académico
 * Realizado por: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
void Leer_Arreglo( int *x, int t)
{
	int k;
	for (k=0;k<t;k++)
	{
		printf("Indique el elemento %d   :  ",k+1);
		scanf("%d",&x[k]);
	}
}

/***********************************************************************
 * Rutina: Suma	Tipo: Entero
 * Parámetros:	1.- Tipo Apuntador Entero 	(Arreglo)
 *              2.- Tipo Entero 			(Tamaño del Arreglo)
 * Descripción: Suma y retorna los elementos de un arreglo
* Rutina diseñada para uso académico
 * Realizado por: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
int Suma( int *x, int t)
{
	int k,s=0;
	for (k=0;k<t;k++)
		s=s+x[k];
	return s;
}

/***********************************************************************
 * Rutina: Mostrar	Tipo: Procedimiento
 * Parámetros:	1.- Tipo Apuntador Entero 	(Arreglo)
 *              2.- Tipo Entero 			(Tamaño del Arreglo)
 * Descripción: Muestra elementos de un arreglo
 * Rutina diseñada para uso académico
 * Realizado por: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
void Mostrar( int *x, int t)
{
	int k;
	printf("Elementos [");
	for (k=0;k<t;k++) 
	{
	printf(" %d ",x[k]);
	}
	printf("]\n");
}


