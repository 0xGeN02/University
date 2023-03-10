#include <stdio.h>      // Biblioteca estándar de entrada salida
/* DECLARACIONES Y DEFINICIONES GLOBALES */ 
int main(void)              // Función principal
{
// Declaración de variables locales
float T,S,M,TE;       
int n;
n=0;
S=0;
printf("Indique la temperatura %d : ",n+1);
scanf("%f",&T);
S=0;
while (T>0)
{
    n++;
    S=S+TE;
    printf("Indique la temperatura %d : ",n+1);
    scanf("%f",&T);
}

if (n>0)
{
    M=S/n;
    printf("La media de las %d temperaturas es = ",n,M);
}
else
    printf("*** No hay temperaturas ***");
return 0;
}