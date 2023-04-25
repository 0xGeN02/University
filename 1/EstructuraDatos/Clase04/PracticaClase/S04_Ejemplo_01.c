// Asignatura: Estructura de Datos
// Programa: S04_Elemplo_01
// Funciones malloc, Calloc y free
// Asignar y liberar memoria dinámica
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 28/01/2023        
// Inclusión de Bibliotecas
#include<stdio.h>
#include<stdlib.h>
//Definiciones de nuevos tipos y prototipos de funciones
// Programa Principal
int main (){
	int *pm,*pc; // Declarar punteros a enteros
	pm =(int *)malloc(sizeof(int));
	pc =(int *)calloc(1,sizeof(int));
	if (pm == NULL || pc == NULL)
		printf ("Reserva memoria fallida");
	else{
		printf("*** Memoria asignada ***\n");
		printf("  pm Dirección : %X Contenido : = %X  Apunta = %d\n",&pm,pm,*pm); 
		printf("  pc Dirección : %X Contenido : = %X  Apunta = %d\n",&pc,pc,*pc); 
		//Liberar el espacio de memoria 
		printf("*** Liberar el espacio de memoria ***\n");
		free(pm);free(pc);  // Libera el espacio asignado
		printf("  pm Dirección : %X Contenido : = %X  Apunta = %d\n",&pm,pm,*pm); 
		printf("  pc Dirección : %X Contenido : = %X  Apunta = %d\n",&pc,pc,*pc); 
		printf("*** Asignar NULL a los punteros ***\n");
		pm=NULL;pc=NULL;  // Asignar nulo a pm y pc
		printf("  pm Dirección : %X Contenido : = %X\n",&pm,pm); 
		printf("  pc Dirección : %X Contenido : = %X \n",&pc,pc); 
		printf("  pm Apunta luego de pm=NULL : %d \n",*pm); // Sin salida
		printf("  pc Apunta luego de pm=NULL : %d \n",*pc); // Sin salida
		}
	int *p; //Declaramos puntero a un entero
	p = (int *) malloc(sizeof(int));
	if (p == NULL)
		printf ("Reserva memoria fallida");
	else{
		*p = 10;
		printf("p = %d   *p = %d",p,*p);
	}
	free(p);
    printf("p = %d *p = %d",p,*p);
return 0;
}




