#include <stdio.h>      // Biblioteca estándar de entrada salida
/* DECLARACIONES Y DEFINICIONES GLOBALES */ 
int main(void)              // Función principal
{
// Declaración de variables locales
float T,S,M;       
int n;
n=0;
S=0;

S=0;
do
{
printf("Indique la temperatura %d : ",n+1);
scanf("%f",&T);
if (T>0)
{
    n++;
    S=S+T;
}
} while (T>0);
if (n>0)
{
    M=S/n;
    printf("La media de las %d temperaturas es = %5.2f",n,M);
}
else
    printf("*** No hay temperaturas ***");
return 0;
}
