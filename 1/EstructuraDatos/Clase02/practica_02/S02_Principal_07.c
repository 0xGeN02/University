// Programa Principal Ejemplo 06
// S02_Principal_06.c
// Realizado por: Eladio Dapena Gonzalez
// Fecha 02/01/2023
/* INCLUSIÓN DE BIBLIOTECAS */
#include "S02_Funciones_07.h"
/* DECLARACIONES Y DEFINICIONES GLOBALES */ 
#define C 5
// Programa principal
int main(void)
{
    int N[C];
    Leer_Arreglo(N,C);
    Mostrar(N,C);
    printf("Media = %5.2f  \n",(float)(Suma(N,C)/(float)C));
    return 0;
}