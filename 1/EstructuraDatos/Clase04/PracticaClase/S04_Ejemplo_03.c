// Asignatura: Estructura de Datos
// Programa: S04_Elemplo_03
// Funciones malloc y free
// Creación dinámica de registros (struct)
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 28/01/2023        
// Inclusión de Bibliotecas
#include<stdio.h>
#include<stdlib.h>
//Definiciones de nuevos tipos de datos
typedef struct 
{
	int DNI,Edad;
	float Peso,Estatura;
}Data;
//Definición de prototipos de funciones
// Programa Principal
int main ()
{
	// declarar un puntero a un tipo Data
	Data *d;
	printf("Tamaño de la estructura Data : %d \n",sizeof(Data));
	printf("Tamaño de la variable      d : %d \n",sizeof(d));
	// Asignar memoria para un tipo Data.   
	d = (Data *)malloc (sizeof(Data));
	if (d == NULL)
		printf ("Reserva memoria fallida");
	else
	{
	printf("Dirección de d : %X \n",&d);
	printf("Contenido de d : %X \n",d);
	printf("Indique DNI      : ");
	scanf("%d",&d->DNI);
	printf("Indique Edad     : ");
	scanf("%d",&d->Edad);
	printf("Indique peso     : ");
	scanf("%f",&d->Peso);
	printf("Indique estatura : ");
	scanf("%f",&d->Estatura);
	printf("**** Los datos almacenados ****\n");
	printf("DNI      : %d \n",d->DNI);
	printf("Edad     : %d \n",d->Edad);
	printf("Peso     : %3.2f \n",d->Peso);
	printf("Estatura : %3.2f \n",d->Estatura);
	// liberar el espacio de memoria
	free (d);
	}
return 0;
}



