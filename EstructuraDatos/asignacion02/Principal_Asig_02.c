
//Grupo 5: Hugo Iglesias; Manuel Menendez; Laura Vazquez; Manuel Mateo Delgado; Juan Ramon Pazo
//Programa hecho por: Manuel Mateo Delgado
//Asignación 2 Estructura de Datos
//Universidad Intercontinental de la Empresa

//Include
#include "Bliblio_Asig_02.h"

//Muestra menu de opciones 
void Menu_Opciones(){

	system(Limpiar);
    printf("\033[2J"); // Limpia terminal códigos de escape (ANSI X3.64) 
	printf("***************  GESTION DE UNA LISTA   ******************\n");
	printf("*                                                        *\n");
	printf("*      Agregar un Tren al Origen    ...........   1      *\n");
	printf("*      Modiificar Estado del Tren   ...........   2      *\n");
	printf("*      Mostrar Ubicación del Tren   ...........   3      *\n");
	printf("*      Lista Orden Ubicación        ...........   4      *\n");
    printf("*      Mostrar Tren y Yuxtapuestos  ...........   5      *\n");
 	printf("*      Retirar Nodo                 ...........   6      *\n");
    printf("*      Angulo Azimuth               ...........   7      *\n");
	printf("*      Finalizar                    ...........   8      *\n");
	printf("*                                                        *\n");
	printf("**********************************************************\n");
}

// Rutina que retorna una opción válida del menu
int Menu(int n1, int n2)
{
	int o;
  do
  {
	 	Menu_Opciones();
		printf("                 Indique su opcion : ");
		scanf("%d",&o);
	}while (o<n1 || o>n2);
	return o;
}