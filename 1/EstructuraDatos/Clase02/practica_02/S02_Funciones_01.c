// Programa S02_Funciones_01
// Asignatura: Estructura de Datos
// Definición de prototipos y Declaración de rutinas
// Sumar dos números
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 02/01/2023
/* INCLUSIÓN DE BIBLIOTECAS */
#include<stdio.h>
/* DECLARACIONES Y DEFINICIONES GLOBALES */ 
//Definición de prototipos de funciones
int Suma(int, int);     	/* Prototipo */
// Programa Principal
int main()
{
    int N1,N2;
    printf("Indique el valor de Numero 1 : ");
    scanf("%d",&N1); 
    printf("Indique el valor de Numero 2 : ");
    scanf("%d",&N2); 
    printf("La suma de %d  +  %d  es : %d \n",N1,N2,Suma(N1,N2) );  /* Llamado */
    return 0;  	  
}
// Declaración de funciones y procedimientos
/***********************************************************************
 * Función: Sumar	Tipo: Función (Entero)
 * Parámetros:	1.- Tipo Entero Num1
 *              2.- Tipo Entero Num2
 * Descripción: Recibe dos enteros y retorna la suma
 * Rutina diseñada para uso académico
 * Realizado por: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
int Suma( int Num1, int Num2 )	/* Declaración */
{
    return (Num1+Num2);
}
