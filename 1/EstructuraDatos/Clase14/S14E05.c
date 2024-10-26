/********************************************
* Asignatura: Estructura de Datos           *
* Sesión 14 Unidad V Análisis de Algoritmos *
* Ejemplo 05: Calcular tiempos de ejecución *
* Lenguaje C
* Rutinas:                                  *
*   Factorial                               *
*   Factorial_R                             *
* Programa exclusivo para uso académico     *
* Adaptado por: Eladio Dapena Gonzalez      *
* Fecha: 23/04/2023                         *
*********************************************/  
// Inclusión de Bibliotecas
#include <stdio.h>
#include <stdlib.h>
#include <time.h>   // Medir tiempo
// Definición de nuevos tipos de datos

// Definición de Prototipos de funciones
unsigned long long Factorial(int);
unsigned long long Factorial_R(int);
// Función principal
int main()
{
 int n;
 clock_t startp,endp,start_time, end_time;
 double total_time;
 printf("---INICIAR MEDICION DEL TIEMPO DE EJECUCION\n " ) ;
 startp = clock(); // Medir tiempo total del programa
 printf("   ***********************************\n" ) ;
 printf("   *            FACTORIAL            *\n " ) ;
 printf("   ***********************************\n" ) ;
 printf("\n" ) ;
 printf("   INDIQUE UN NUMERO ENTERO EN EL RANGO [0 < n <21] : " ) ;
 scanf("%d",&n ) ;
 if (n>0 && n<=20)
 {
  start_time = clock();
  printf("   --FACTORIAL           DE  %d ES : %llu ",n,Factorial(n)) ;
  end_time = clock();
  total_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;
  printf("   TIEMPO = %.6f  segundos\n",total_time);
  start_time = clock();
  printf("   --FACTORIAL RECURSIVO DE  %d ES : %llu",n,Factorial_R(n)) ;
  end_time = clock();
  total_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;
  printf("    TIEMPO = %.6f  segundos\n",total_time);
 }
 else
  printf("   ERROR: El valor de n debe estar etre 0 y 20\n");
 endp = clock();
 printf("\n");
 printf("---FINALIZAR MEDICION DEL TIEMPO DE EJECUCION\n " ) ;
   total_time = (double)(endp - startp) / CLOCKS_PER_SEC;
  printf("  TIEMPO TOTAL  = %.6f  segundos\n",total_time);

return 0;
} 
// Declaración de Funciones y Procedimientos
// Rutina: Factorial  (Solución iterativa)
// Tipo: Función   Retorna: Entero
// Parámetros: Entero n
// Programa de uso académico
// Dr. Eladio Dapena Gonzalez
unsigned long long Factorial(int n)
 {
  int k;
 unsigned long long F; 
 F=1;
 /* Calcula el producto n*(n-1)*(n-2)*...*2*1 */
 for (k = n; k > 1; --k) 
  {
   F=F*k;
  }
 return F;
 } 
// Declaración de Funciones y Procedimientos
// Rutina: Factorial_R  (Solución Recursiva)
// Tipo: Función   Retorna: Entero
// Parámetros: Entero n
// Programa de uso académico
// Dr. Eladio Dapena Gonzalez
unsigned long long Factorial_R(int n)
{
 unsigned long long r;
 if (n==1)
  r = 1;
 else
  r=n*Factorial_R(n-1) ;
 return (r) ;
}
