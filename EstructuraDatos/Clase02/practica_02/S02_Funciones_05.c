// Programa S02_Funciones_05
// Asignatura: Estructura de Datos
// Funciones y arreglos unidimensionales como parámetros
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 02/01/2023
/* INCLUSIÓN DE BIBLIOTECAS */
#include<stdio.h>
/* DECLARACIONES Y DEFINICIONES GLOBALES */ 
#define C 5
//Definición de prototipos de funciones
void Leer_Arreglo  (int [], int);
int  Suma(int *, int);
void Mostrar  (int [], int);
// Programa principal
int main(void)
{
	int N[C];
	Leer_Arreglo(N,C);
	Mostrar(N,C);
	printf("Media = %5.2f  \n",(float)(Suma(N,C)/(float)C));
	return 0;
}
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
 * Descripción: Suma los elementos de un arreglo
 * Retorna    : Entero con la suma
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


