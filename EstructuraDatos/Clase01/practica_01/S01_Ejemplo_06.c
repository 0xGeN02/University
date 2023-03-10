// Fecha 02/01/2023
/* INCLUSIÓN DE BIBLIOTECAS */
#include <stdio.h>      // Biblioteca estándar de entrada salida
/* DECLARACIONES Y DEFINICIONES GLOBALES */ 
int main(void)              // Función principal
{
// Declaración de variables 
int op;        //Declaracion de variables y constantes locales
printf("Indique una opci%cn [1,2,3,4] : ",162, op);
scanf("%d",&op);              
switch (op)
{
case 1:
    printf("\tOpci%cn  seleccionada = %d",162, op);
       // Acciones de la opción 1
    break;
case 2:
    printf("\tOpci%cn  seleccionada = %d",162, op);      
       // Acciones de la opción 2
    break;
case 3:
    printf("\tOpci%cn  seleccionada = %d",162,op);  
       // Acciones de la opción 3
    break;
case 4:
    printf("\tOpci%cn  seleccionada = %d",162,op);  
        // Acciones de la opción 4
    break;
default:
    printf("\tOpci%cn  otros casos",162);  
       // Acciones de la opción otros casos
}
return 0;
}


