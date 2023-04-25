// Asignatura: Estructura de Datos
// Programa: S04_Elemplo_02
// Funciones malloc y free
// Asignar memoria dinámica y guardar valores
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 28/01/2023        
// Inclusión de Bibliotecas
#include<stdio.h>
#include<stdlib.h>
//Definiciones de tipo

//Definición de prototipos de funciones
// Programa Principal
int main ()
{
	int *pm,*pc; // Declarar puntero a un entero
	pm =(int *)malloc(sizeof(int));
	pc =(int *)calloc(1,sizeof(int));
	if (pm == NULL || pc == NULL)
		printf ("Reserva memoria fallida");
	else {
		printf("*** Memoria asignada ***\n");
		printf("  pm Dirección : %X Contenido : = %X  Apunta = %d\n",&pm,pm,*pm); 
		printf("  pc Dirección : %X Contenido : = %X  Apunta = %d\n",&pc,pc,*pc); 
		//Asignar  valores en el espacio dinámico
		printf("*** Entrada de Datos ***\n");
		printf("  Indique un número entero : ");
		scanf("%d",pm); // Sin &
		printf("  Indique un número entero : ");
		scanf("%d",pc); // Sin &
		// mostrar el contenido de la memoria dinámica
		printf("*** Salida de Datos ***\n");
		printf("  pm Dirección : %X Contenido : = %X  Apunta = %d\n",&pm,pm,*pm); 
		printf("  pc Dirección : %X Contenido : = %X  Apunta = %d\n",&pc,pc,*pc); 
		// Liberar memoria
		free(pm);free(pc);  // Liberar el espacio asignado
	}
	return 0;
	//Definiciones del nuevo tipo de dato
	typedef struct{
		int DNI,Edad;
		float Peso,Estatura;
	}Data;

	
}
