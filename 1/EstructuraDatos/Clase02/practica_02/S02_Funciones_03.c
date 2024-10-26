// Programa S02_Funciones_03
// Asignatura: Estructura de Datos
// Tema Funciones 
// Descripción :    Manejo de punteros      
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 02/01/2023
/* INCLUSIÓN DE BIBLIOTECAS */
#include <stdio.h>	/* Punteros */
int main()
{
    char a,*pa,**ppa;
    a='X';		// Asigna el valor X a la variable a
    pa=&a;		// Asigna la dirección de a a la variable puntero pa
    ppa=&pa;	// Asigna la dirección del puntero pa a la variable puntero ppa
    printf("El contenido de la variable    \ta\t: %c\n",a);
    printf("La direcci%cn de la variable    \ta\t: %X\n",162,&a);
    printf("El contenido de la variable    \tpa\t: %X\n",pa);
    printf("La direcci%cn de la variable    \tpa\t: %X\n",162,&pa);
    printf("El contenido de lo que apunta  \t*pa\t: %c\n",*pa);
    printf("El contenido de la variable    \tppa\t: %X\n",ppa);
    printf("La direcci%cn de la variable    \tppa\t: %X\n",162,&ppa);
    printf("El contenido de lo que apunta  \t*ppa\t: %X\n",*ppa);
    printf("El contenido de lo que apunta  \t**ppa\t: %c\n",**ppa);
    return 0;
}

