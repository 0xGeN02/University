// Programa S01_EJEMPLO_07
// Norma 6 Ciclos 
// Repetición indexada
// Leer n temperaturas sin almacenarlas y obtener su promedio
// La cantidad n de temperaturas debe ser solicitada al usuario
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 02/01/2023
/* INCLUSIÓN DE BIBLIOTECAS */
#include <stdio.h>      // Biblioteca estándar de entrada salida
/* DECLARACIONES Y DEFINICIONES GLOBALES */ 
int main(void)              // Función principal
{
// Declaración de variables locales
float T,S,M;       
int n,i;
printf("Indique la cantidad de temperaturas a sumar = ");
scanf("%d",n);
S=0;
for (i=1; i<=n; i++)
    printf("Indicar la temperatura  = ");
    scanf("%f",&T);
    S=S+T;
    if (n>0)
{
    M=S/n;
    printf("La media de las %d temperaturas es = %5.2f",n,M);
}
else
    printf("*** No hay temperaturas ***");
return 0;
}