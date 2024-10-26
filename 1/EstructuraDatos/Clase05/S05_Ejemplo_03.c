// Asignatura: Estructura de Datos
// Programa: S05_Elemplo_03
// Lista Simple. Operaciones 1,2,4 y 5
// Crear lista   / Agregar nodo al final 
// Mostrar lista / Vaciar Lista
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 28/01/2023        
// Inclusión de Bibliotecas
#include<stdio.h>
#include<stdlib.h>
//Definición nuevos tipos de datos
typedef struct 
{
	int Codigo;
	// Otros datos
}Data;
struct Nodo
{
	Data Inf;
	struct Nodo *sig;
};
//Definición de prototipos de funciones
struct  Nodo *Crea_Nodo();
void    Leer_Nodo(struct Nodo *);
void    Mostrar_Nodo(struct Nodo *);
struct  Nodo *Add_End(struct Nodo *, struct Nodo *);
void    Mostrar_Lista(struct Nodo *);
struct  Nodo *Vaciar_Lista(struct Nodo *);

// Programa principal de pruebas
int main ()
{
// Declaración de variables
 struct Nodo *d, *Ini;
 int op;
 Ini=NULL;  // Inicio de la lista (Vacía)
 printf("Agregar nodos 0 para finalizar : ");
 scanf("%d",&op);
 while (op!=0)
 {
  d = Crea_Nodo();
  if (d == NULL)
   printf ("Operacion reserva memoria fallida");
  else
  {
   Leer_Nodo(d);
   Ini=Add_End(Ini,d);
  }
  printf("Desea agregar otro Nodo a la lista 1->Si : ");
  scanf("%d",&op);
 }
 Mostrar_Lista(Ini);
 Ini=Vaciar_Lista(Ini);
}
// Declaración de Funciones
// Función Crea_Nodo_Vacio
struct Nodo *Crea_Nodo()
{
 return (struct Nodo *)calloc(1,sizeof(struct Nodo));
}			
// Entrada de datos de un nodo
void Leer_Nodo(struct Nodo *a)
{
 printf("CODIGO : ");
 scanf("%d",&a->Inf.Codigo);
 // Otros datos
 a->sig=NULL;
}
// Mostrar los datos de un nodo
void Mostrar_Nodo(struct Nodo *a)
{
printf("\tCODIGO : %d\n",a->Inf.Codigo);
// Otros datos
}

/***********************************************************************
 * Rutina: Add_End		Tipo: Apuntador a Nodo	
 * Parámetros:	1.- Apuntador a un tipo Nodo  (Inicio de la Lista)
 *              2.- Apuntador a el Nodo a agregar
 * Descripción: Agrega al final de la lista un nuevo nodo
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio dapena Gonzalez
 ***********************************************************************/
struct Nodo *Add_End(struct Nodo *ini, struct Nodo *N)
{
 struct Nodo *a;
 if (ini==NULL)
 	ini=N;
 else
 {
 	a=ini;
 	while (a->sig!=NULL)
	 a=a->sig;
 	a->sig=N;
 }
 return ini;
}
// Contar los nodos de la lista

// Mostrar nodos de la lista (Sólo código)
void  Mostrar_Lista(struct Nodo *a)
{
 struct Nodo *i;
 int c=0;
 i=a;
 printf("   Elementos de la lista   \n");
 while (i!=NULL)
 {
    c++;
	printf(" %d: %d\n",c,i->Inf.Codigo);
  	i=i->sig;
 }
}
// Vaciar lista y liberar memoria.
struct Nodo *Vaciar_Lista(struct Nodo *ini)
{
 struct Nodo *a;
 if (ini!=NULL)
 do
 {
  a=ini;
  ini=a->sig;
  free(a);
  }while (ini!=NULL);
 return NULL;
}