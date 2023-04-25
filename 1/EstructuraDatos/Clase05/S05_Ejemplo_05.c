// Asignatura: Estructura de Datos
// Programa: S05_Elemplo_04
// Lista Simple. Contar nodos
// Programa de uso académico
// Realizado por: Mateo Delgado
// Fecha 28/01/2023        
// Inclusión de Bibliotecas
#include<stdio.h>
#include<stdlib.h>
//DefInición nuevos tipos de datos
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
//DefInición de prototipos de funciones
struct 	Nodo *Crea_Nodo();
void 	Leer_Nodo(struct Nodo *);
void 	Mostrar_Nodo(struct Nodo *);
struct 	Nodo *Add_End(struct Nodo *, struct Nodo *);
int 	Contar_Nodos(struct Nodo *);
void  	Mostrar_Lista(struct Nodo *);
struct 	Nodo *Vaciar_Lista(struct Nodo *);

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
 printf("Total de nodos : %d\n",Contar_Nodos(Ini));
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
struct Nodo *Add_End(struct Nodo *Ini, struct Nodo *N)
{
 struct Nodo *a;
 if (Ini==NULL)
 	Ini=N;
 else
 {
 	a=Ini;
 	while (a->sig!=NULL)
	 a=a->sig;
 	a->sig=N;
 }
 return Ini;
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
struct Nodo *Vaciar_Lista(struct Nodo *Ini)
{
 struct Nodo *a;
 if (Ini!=NULL)
 do
 {
  a=Ini;
  Ini=a->sig;
  free(a);
  }while (Ini!=NULL);
 return NULL;
}
// Contar los nodos de la lista
/*******************************************************************
 * Rutina: Contar nodos		Tipo: Entero	
 * Parámetros:	1.- Apuntador a un tipo Nodo  (Inicio de la Lista)
 * Descripción: Contar la cantidad de nodos en la lista
 * Retorna : Cantidad de nodos
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio dapena Gonzalez
 ******************************************************************/
int Contar_Nodos(struct Nodo *Ini)
{
 struct Nodo *a;  // Nodo auxiliar local
 int c=0;	// Contador de Nodos
 a=Ini;
 while (a!=NULL)
 {
 	 a=a->sig;	
 	 c++;
 }
 return c;  // Cantidad de Nodos
}

/***********************************************************************
 * Rutina: Add_End		Tipo: Apuntador a Nodo	
 * Parámetros:	1.- Apuntador a un tipo Nodo  (Inicio de la Lista)
 *              2.- Apuntador a el Nodo a agregar
 * Descripción: Agrega al final de la lista un nuevo nodo
 * Rutina diseñada para docencia
 * Realizado por: Dra. Mateo Delgado
 ***********************************************************************/

struct Nodo *Add_Start(struct Nodo *Ini, struct Nodo *N){
    N->sig = Ini;
    Ini = N;
    return Ini;
}


/***********************************************************************
 * Rutina: Add_End		Tipo: Apuntador a Nodo	
 * Parámetros:	1.- Apuntador a un tipo Nodo  (Inicio de la Lista)
 *              2.- Apuntador a el Nodo a agregar
 * Descripción: Agrega al final de la lista un nuevo nodo
 * Rutina diseñada para docencia
 * Realizado por: Dra. Mateo Delgado
 ***********************************************************************/

struct Nodo *Del_Nodo(int pos, struct Nodo *Ini)
{
    if (Ini == NULL) {
        // Lista vacía
        return NULL;
    }
    if (pos == 1) {
        // Eliminar el primer nodo de la lista
        struct Nodo *nodoAEliminar = Ini;
        Ini = Ini->sig;
        free(nodoAEliminar);
        return Ini;
    }
    // Buscar el nodo anterior al que se quiere eliminar
    struct Nodo *anterior = Ini;
    for (int i = 1; i < pos - 1 && anterior->sig != NULL; i++) {
        anterior = anterior->sig;
    }
    if (anterior->sig == NULL) {
        // La posición es mayor que la cantidad de nodos en la lista
        return Ini;
    }
    // Eliminar el nodo
    struct Nodo *nodoAEliminar = anterior->sig;
    anterior->sig = nodoAEliminar->sig;
    free(nodoAEliminar);
    return Ini;
}