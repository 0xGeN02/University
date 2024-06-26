// Asignatura: Estructura de Datos
// Programa: S04_Elemplo_05
// Funciones calloc, relloac() y free
// Redimensionar vectores en tiempo de ejecución
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 28/01/2023        
// Inclusión de Bibliotecas
#include<stdio.h>
#include<stdlib.h>
//Definiciones prototipos
//Definición de prototipos de funciones
void Leer_Arreglo(int [], int); // S02_Funciones_07.h
void Mostrar(int [], int);	// S02_Funciones_07.h
void Entrada_add(int [], int, int); // Agregar nuevos elementos
// Programa Principal
int main (){
	int *Vec;
	int num_elem=0;
	int mas;  
	printf("Indique numero de elementos del vector de enteros : ");
	scanf("%d",&num_elem);
// Reserva Memoria Dinámica (en Heap) para el Vector   
	Vec=(int *)calloc(num_elem,sizeof(int));
	if (Vec==NULL)
		printf ("Operacion reserva memoria fallida");
	else{
	// Ingreso los elementos del vector
		printf("Ingresar los elementos (números enteros) del vector\n");
		Leer_Arreglo(Vec,num_elem); // S02_Funciones_07.h
	// Mostrar los Elementos del vector
		Mostrar(Vec,num_elem);	  // S02_Funciones_07.h
	// Agregar más elementos al vector realloc()
		printf ("Elementos a agregar al vector ? :");
		scanf ("%d",&mas);
	// Cambiar el tamaño del Vector
		Vec =(int *)realloc(Vec,(num_elem+mas)*sizeof(int));
		Entrada_add(Vec, num_elem, mas); 
		Mostrar(Vec,num_elem+mas);	  // S02_Funciones_07.h  
	// liberar el espacio de memoria
		free (Vec);
	}
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
void Leer_Arreglo( int *x, int t) // S02_Funciones_07.c
{
	int k;
	for (k=0;k<t;k++)
	{
		printf("Indique el elemento %d   :  ",k+1);
		scanf("%d",&x[k]);
	}
}
/***********************************************************************
 * Rutina: Mostrar	Tipo: Procedimiento
 * Parámetros:	1.- Tipo Apuntador Entero 	(Arreglo)
 *              2.- Tipo Entero 			(Tamaño del Arreglo)
 * Descripción: Muestra elementos de un arreglo
 * Rutina diseñada para uso académico
 * Realizado por: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
void Mostrar( int *x, int t)	// S02_Funciones_07.c
{
	int k;
	printf("Elementos del vector [");
	for (k=0;k<t;k++) 
	{
	printf(" %d ",x[k]);
	}
	printf("]\n");
}
/*
 * Rutina: Entrada_add	Tipo: Procedimiento
 * Parámetros:	1.- Tipo Apuntador Entero 	(Arreglo)
 *              2.- Tipo Entero 	(Tamaño original del Arreglo)
 *              3.- Tipo Entero     (Nuevos elementos)
 * Descripción: Entrada de datos agregados al arreglo
 * Rutina diseñada para uso académico
 * Realizado por: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
void Entrada_add(int *x, int n, int m)
{
	int i;
		for (i=n; i<n+m; i++)
		{
			printf ("Escribe el elemento %d : ",i+1);
			scanf ("%d",&x[i]);
		}	
	
}