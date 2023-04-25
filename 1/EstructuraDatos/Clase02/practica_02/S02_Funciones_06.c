// Programa S02_Funciones_06
// Asignatura: Estructura de Datos
// Funciones y arreglos bidimensionales como parámetros
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 02/01/2023
/* INCLUSIÓN DE BIBLIOTECAS */
#include<stdio.h>
/* DECLARACIONES Y DEFINICIONES GLOBALES */ 
#define F 3
#define C 3
//Definición de prototipos de funciones
void Leer_Arreglo_Bi(int [F][C], int, int);
void Mostrar_Arreglo_Bi(int [][C], int, int);
int  Suma_Fila(int [][C], int , int, int );
// Programa principal
int main(void)
{
   int Mat[F][C],sf;
   Leer_Arreglo_Bi(Mat,F,C);
   Mostrar_Arreglo_Bi(Mat,F,C);
   printf("  Suma de cada fila  \n");
   for (sf=0;sf<C;sf++)
   printf("   Fila %d = %d\n",sf+1,Suma_Fila(Mat,F,C,sf));
   return 0;
}
// Declaración de funciones y procedimientos
/*********************************************************
 * Rutina: Leer_Arreglo_Bi	Tipo: Procedimiento
 * Parámetros:	1.- Tipo Arreglo de Entero 	(Arreglo)
 *              2.- Tipo Entero (Filas)
 *              3.- Tipo Entero (Columnas)
 * Descripción: Entrada de datos a una matriz
 * Rutina diseñada para uso académico
 * Realizado por: Dr. Eladio Dapena Gonzalez
 *********************************************************/
void Leer_Arreglo_Bi( int x[F][C], int f, int c)
{
   int k,j;
   for (k=0;k<f;k++)
   {
      for (j=0;j<c;j++)
      {
      printf("Indique el elemento [%d,%d]   :  ",k+1,j+1);
      scanf("%d",&x[k][j]);
      }
   }
}
/*********************************************************
 * Rutina: Mostrar_Arreglo_Bi	Tipo: Procedimiento
 * Parámetros:	1.- Tipo Arreglo de Entero 	(Arreglo)
 *              2.- Tipo Entero (Filas)
 *              3.- Tipo Entero (Columnas)
 * Descripción: Muestra los elementos de una matriz
 * Rutina diseñada para uso académico
 * Realizado por: Dr. Eladio Dapena Gonzalez
 *********************************************************/
void Mostrar_Arreglo_Bi( int x[][C], int f, int c)
{
   int k,j;
   for (k=0;k<f;k++)
   {
      printf("\t|");
      for (j=0;j<c;j++)
      {
      printf(" %d ",x[k][j]);
      }
      printf(" |\n");
   }
}
/*********************************************************
 * Rutina: Suma_Fila	Tipo: Entero
 * Parámetros:	1.- Tipo Arreglo de Entero 	(Arreglo)
 *              2.- Tipo Entero (Filas)
 *              3.- Tipo Entero (Columnas)
 *              4.- Tipo Entero (Fila a sumar)
 * Descripción: Suma elementos de una fila
 * Retorna    : Entero    
 * Rutina diseñada para uso académico
 * Realizado por: Dr. Eladio Dapena Gonzalez
 *********************************************************/
int Suma_Fila(int x[][C], int f, int c, int fila)
{
   int k,s;
   s=0;
   for (k=0;k<c;k++)
      s=s+x[fila][k];
   return s;
}