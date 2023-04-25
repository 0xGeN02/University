// Asignatura: Estructura de Datos
// Programa: S04_Elemplo_06
// Crear nodos dinámicos
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 28/01/2023        
// Inclusión de Bibliotecas
#include<stdio.h>
#include<stdlib.h>
//Definición nuevos tipos de datos
typedef struct 
{
	int DNI,Edad;
	float Peso,Estatura;
}Data;
struct Nodo
{
	Data Inf;
	struct Nodo *sig;
};
//Definición de prototipos de funciones
struct Nodo *Crea_Nodo_Vacio();

int main ()
{
	// declaramos un puntero a un entero
	struct Nodo *d,X;
	printf("Tamano de INF : %d \n",sizeof(Data));
	printf("Tamano de datos : %d \n",sizeof(X));
	// Reservamos memoria para un nodo.   
	d = Crea_Nodo_Vacio();
	if (d == NULL)
		printf ("Operacion reserva memoria fallida");
	else
	{
	 printf("Direccion de d : %p \n",&d);
	 printf("Contenido de d : %p \n",d);
	 printf("Indique DNI sin letra   : ");
	 scanf("%d",&d->Inf.DNI);
	 printf("Indique su Edad         : ");
	 scanf("%d",&d->Inf.Edad);
	 printf("Indique su Peso         : ");
	 scanf("%f",&d->Inf.Peso);
	 printf("Indique estatura        : ");
	 scanf("%f",&d->Inf.Estatura);
	 d->sig=NULL;
	 printf("Cedula   : %d \n",d->Inf.DNI);
	 printf("Edad     : %d \n",d->Inf.Edad);
	 printf("Peso     : %2.2f \n",d->Inf.Peso);
	 printf("Estatura : %1.2f \n",d->Inf.Estatura);
	// No necesito el dato y libero el espacio de memoria
	free (d);
	}
}
// Declaración de Funciones
// Función Crea_Nodo_Vacio
struct Nodo *Crea_Nodo_Vacio()
{
 return (struct Nodo *)calloc(1,sizeof(struct Nodo));
}			



