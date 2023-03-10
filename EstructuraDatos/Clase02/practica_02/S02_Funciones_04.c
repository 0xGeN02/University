// Programa S02_Funciones_04
// Asignatura: Estructura de Datos
// Parámetros por referencia
// Intercambiar el valor de dos variables tipo entero
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 02/01/2023
/* INCLUSIÓN DE BIBLIOTECAS */
#include<stdio.h>
//Definición de prototipos de funciones
void CambiaRef  ( int *, int *);  // Por referencia
// Programa Principal
int main()
{
    int a,b;     a=10;   b=20; 
    printf("      Variable a = %d        Variable b = %d  \n",a,b);
    printf("   Ejecutamos CambiaRef  \n"); 
    CambiaRef ( &a, &b );  //Direciones de las variables
    printf("   Luego de Ejecutar CambiaRef  \n"); 
    printf("     Variable a = %d        Variables b = %d  \n",a,b);  
    return 0;
}
// Declaración de funciones y procedimientos
/***********************************************************************
 * Rutina: Cambia_Var	Tipo: Procedimiento
 * Parámetros:	1.- Tipo puntero a Entero 
 *              2.- Tipo puntero a Entero 
 * Descripción: Recibe dos variables enteras e intercambia sus valores
 * Rutina diseñada para uso académico
 * Realizado por: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
void CambiaRef( int *a, int *b)
{
    int z;
    z=*a;  *a=*b;  *b=z;
}




