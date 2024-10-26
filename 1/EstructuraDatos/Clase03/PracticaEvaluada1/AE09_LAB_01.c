// PRACTICA DE LABORATORIO EVALUADA 01
// Asignatura: Estructura de Datos
// 1 Corregir errores de sintaxix y semántica
// 2 Realizar la rutina para sumar los elementos de una columna
// 3 Realizar la rutina para sumar todos los elementos de la matriz
// Programa de uso académico
// Realizado por: Manuel Mateo Delgado
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
int  Suma_Columna(int [][C], int , int, int );  //Realizar la declaración de esta rutina
int  Suma_Matriz(int [][C], int , int);        //Realizar la declaración de esta rutina
// Programa principal
int main(void)
{
int Mat[F][C],sf,sc;
Leer_Arreglo_Bi(Mat,F,C);
Mostrar_Arreglo_Bi(Mat,F,C);
printf("  Suma de cada fila  \n");
// Sumar los elementos de cada fila
for (sf=0;sf<F;sf++)
   printf("   Fila %d = %d\n",sf+1,Suma_Fila(Mat,F,C,sf));
// Sumar los elementos de cada columna
printf("  Suma de cada columna  \n");
for (sc=0;sc<C;sc++)
   printf("   Columna %d = %d\n",sc+1,Suma_Columna(Mat,F,C,sc));
// Suma los elementos de la matriz 
   printf("  Suma de todos los elementos  \n");
   printf("      Suma = %d\n",Suma_Matriz(Mat,F,C));
return 0;
}
// Declaración de funciones y procedimientos
/*********************************************************
 * Rutina: Leer_Arreglo_Bi	Tipo: Procedimiento
 * Parámetros:	1.- Tipo Arreglo de Entero 	(Arreglo)
 *              2.- Tipo Entero (Número de Filas)
 *              3.- Tipo Entero (Número de Columnas)
 * Descripción: Entrada de datos a una matriz
 * Rutina diseñada para uso académico
 * Realizado por: Mateo Delgado
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
 *              2.- Tipo Entero (Número de Filas)
 *              3.- Tipo Entero (Número de Columnas)
 * Descripción: Muestra los elementos de una matriz
 * Rutina diseñada para uso académico
 * Realizado por: Mateo Delgado
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
 * Parámetros:	 1.- Tipo Arreglo de Entero 	(Arreglo)
 *              2.- Tipo Entero (Número de Filas)
 *              3.- Tipo Entero (Número de Columnas)
 *              4.- Tipo Entero (Fila a sumar)
 * Descripción: Suma elementos de una fila
 * Retorna    : Entero    
 * Rutina diseñada para uso académico
 * Realizado por: Mateo Delgado
 *********************************************************/
int Suma_Fila(int x[][C], int f, int c, int fila)
{
int k,s;
s=0;
for (k=0;k<c;k++)
   s += x[fila][k];
return s;
}
/*********************************************************
 * Rutina: Suma_Columna	Tipo: Entero
 * Parámetros:	 1.- Tipo Arreglo de Entero 	(Arreglo)
 *              2.- Tipo Entero (Número de Filas)
 *              3.- Tipo Entero (Número de Columnas)
 *              4.- Tipo Entero (Columna a sumar)
 * Descripción: Suma elementos de una Columna
 * Retorna    : Entero    
 * Rutina Evaluada
 * Realizado por: Mateo Delgado
 *********************************************************/

int Suma_Columna(int x[][C], int f, int c, int Col)
{
   int s=0;
  // Construya la rutina para sumar en s la columna col 3 pts.
   for (int i = 0; i < c; i++) {
      s += x[i][Col];
   }
   return s;
}
/*********************************************************
 * Rutina: Suma_Matriz	Tipo: Entero
 * Parámetros:	 1.- Tipo Arreglo de Entero 	(Arreglo)
 *              2.- Tipo Entero (Número de Filas)
 *              3.- Tipo Entero (Número de Columnas)
 * Descripción: Suma elementos de toda la matriz
 * Retorna    : Entero    
 * Rutina Evaluada
 * Realizado por: Mateo Delgado
 *********************************************************/

int Suma_Matriz(int x[][C], int f, int c)
{
   int s=0;
  // Construya la rutina para sumar todos los elementos 3 pts.
   for (int i = 0; i < f; i++){
      for(int j = 0; j < c; j++){
         s += x[i][j];
      }
   }
   return s;
}