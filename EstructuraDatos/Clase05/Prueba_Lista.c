// Asignatura: Estructura de Datos
// Programa: PRUEBA_BIBLIOTECA_LISTAS
// Actividad práctica presencial sesión 05
// Menú con opciones para operaciones con listas simples
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 28/01/2023        
// Inclusión de Bibliotecas
#include "Lista_Simple.h"
#define LIMPIA "clear"   // Limpiar terminal
//PROTOTIPOS
void Muestra_Opciones();
int Menu(int, int);
struct Nodo *Hacer(int, struct Nodo *, struct Nodo * );
// Programa principal de pruebas
int main (){
// Declaración de variables
 struct Nodo *d, *Ini;
 int op;
 Ini=NULL;d=NULL;  // Inicio de la lista (Vacía)
  do
  {
  	op=Menu(1,7);
  	Ini=Hacer(op,Ini,d);
  	printf("Presione una tecla para continuar");
   	fflush(stdin);
  	getchar();
	}while (op!=7);
 Ini=Vaciar_Lista(Ini);
 return 0;
 }
// Declaraciones de rutinas
// Mostrar un menú con opciones de gestión de una lista
void Muestra_Opciones()
{
	system(LIMPIA);  // Limpia terminal 
    printf("\033[2J"); // Limpia terminal códigos de escape (ANSI X3.64) 
	printf("***************  GESTION DE UNA LISTA   ******************\n");
	printf("*                                                        *\n");
	printf("*      Agregar Nodo al Final  .................   1      *\n");
	printf("*      Agregar Nodo al Inicio .................   2      *\n");
	printf("*      Contar Nodos           .................   3      *\n");
	printf("*      Mostrar Lista          .................   4      *\n");
    printf("*      Eliminar Nodo          .................   5      *\n");
 	printf("*      Vaciar Lista           .................   6      *\n");
	printf("*      Finalizar              .................   7      *\n");
	printf("*                                                        *\n");
	printf("**********************************************************\n");
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
struct Nodo *Hacer(int o, struct Nodo *Ini, struct Nodo *Ele)
{
	int c,ne;
	switch (o)
	{
	 	case 1:
			Ele=Crea_Nodo();
			if (Ele!=NULL)
			{
				Leer_Nodo(Ele);
				Ini=Add_End(Ini,Ele);
			}
			else
				printf("Falla en la creación del Nodo\n");
			break;
		case 2:
			Ele=Crea_Nodo();
			if (Ele!=NULL)
			{
				Leer_Nodo(Ele);
				Ini=Add_Start(Ini,Ele);
			}
			else
				printf("Falla en la creación del Nodo\n");
			break;
		case 3:
			printf("Cantidad de Nodos = %d\n",Contar_Nodos(Ini));
			break;
		case 4:
			Mostrar_Lista(Ini);
			break;
		case 5:
            c=Contar_Nodos(Ini);
			if (c>0)
			 {
			  printf("Indique nodo a eliminar [1,%d] : ",c);scanf("%d",&ne);
			  if (ne>0 && ne<=c)
				Ini=Del_Nodo(ne,Ini);
			  else
			   	printf("No se puede Eliminar nodo no existe\n");
			 }
			 else
			  	printf("NO se puede eliminar Lista vacia \n");
			break;
		case 6:
			Ini=Vaciar_Lista(Ini);
			break;
	}
	return Ini;
}
