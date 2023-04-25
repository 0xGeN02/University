// Programa S02_Funciones_02
// Asignatura: Estructura de Datos
// Intercambiar el valor de dos variables tipo entero
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 02/01/2023
/* INCLUSIÓN DE BIBLIOTECAS */
#include<stdio.h>
/* DECLARACIONES Y DEFINICIONES GLOBALES */ 
//Definición de prototipos de funciones
void Intercambia_Var( int,int );     /* Prototipo */
// Programa Principal
int main()
{
    int a,b;     a=10;   b=20; 
    printf("\tVariable a = %d\t Variable b = %d\n",a,b);
    printf("\t +++++ Invocamos la rutina Cambia_Var\n"); 
    Intercambia_Var (a,b);
    printf("\tVariable a = %d\t Variable b = %d\n",a,b);  
return 0;
}
// Declaración de funciones y procedimientos
/***********************************************************************
 * Rutina: Intercambia_Var	Tipo: Procedimiento
 * Parámetros:	1.- Tipo Entero 
 *              2.- Tipo Entero 
 * Descripción: Recibe dos variables enteras e intercambia sus valores
 * Rutina diseñada para uso académico
 * Realizado por: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
void Intercambia_Var( int a, int b)
{
    int z;
    z=a; a=b; b=z;
}



