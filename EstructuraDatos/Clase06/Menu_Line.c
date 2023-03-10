// Inclusión de Bibliotecas
#include "Menu_Line.h"
// Mostrar un menú con opciones de gestión de una Fila
void Muestra_Opciones()
{
	//system(LIMPIA);  // Limpia terminal 
    printf("\033[2J"); // Limpia terminal códigos de escape (ANSI X3.64) 
	printf("***************  GESTION DE UNA FILA   *************\n");
	printf("*                                                  *\n");
	printf("*      Agregar          .................   1      *\n");
	printf("*      Contar           .................   2      *\n");
	printf("*      Mostrar Fila     .................   3      *\n");
    printf("*      Eliminar         .................   4      *\n");
 	printf("*      Vaciar Fila      .................   5      *\n");
	printf("*      Finalizar        .................   6      *\n");
	printf("*                                                  *\n");
	printf("****************************************************\n");
}
// Rutina que retorna una opción válida del menu
int Menu(int n1, int n2)
{
	int o;
  do
  {
	 	Muestra_Opciones();
		printf("                 Indique su opcion : ");
		scanf("%d",&o);
	}while (o<n1 || o>n2);
	return o;
}
// Rutina que ejecuta las acciones según la opción 
/***********************************************************************
 * Rutina: Hacer		Tipo: Apuntador a Nodo retorna un puntero a nodo
 * Parámetros:	1.- Entero o  Acción a ejecutar
 *							2.- Nodo  Puntero a un dato tipo Nodo (inicio de lista)
 *							3.- Nodo  Puntero a un dato tipo Nodo
 * Descripción: Ejecuta la acción seleccionada por el usuario
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
struct Nodo *Hacer(int o, struct Nodo *Ini, struct Nodo * Ele)
{
	int c,ne;
	switch (o)
	{
	 case 1:
		Ele=Crea_Nodo();
		if (Ele!=NULL)
		{
			Leer_Nodo(Ele);
			Ini=Line_Add(Ini,Ele);
		}
		else
			printf("Falla en la creación del Nodo\n");
		break;
		case 2:
			printf("Cantidad de Nodos = %d\n",Nodos_Line(Ini));
			break;
		case 3:
			Mostrar_Line(Ini);
			break;
		case 4:
            if (Ini!=NULL)
			   Ini=Line_Del(Ini);
			 else
			  printf("No hay elementos en la fila \n");
			break;
		case 5:
			Ini=Vaciar_Line(Ini);
			break;
	}
	return Ini;
}