// Asignatura: Estructura de Datos
//FICHERO CABECERA LISTA SIMPLE
// BIBLIOTECAS.
#include<stdio.h>
#include<stdlib.h>
// DEFINICIÓN DE NUEVOS TIPOS DE DATOS
// Tipo de Dato con Información en los nodos
typedef struct 
{
	int Codigo;
	// Otros datos
}Data;
// Tipo de Dato Nodo Simple
struct Nodo
{
	Data Inf;
	struct Nodo *sig;
};
//PROTOTIPOS DE RUTINAS
struct 	Nodo *Crea_Nodo();
void 	Leer_Nodo(struct Nodo *);
void 	Mostrar_Nodo(struct Nodo *);
struct 	Nodo *Add_End(struct Nodo *, struct Nodo *);
struct 	Nodo *Add_Start(struct Nodo * , struct Nodo *);
int 	Contar_Nodos(struct Nodo *);
struct 	Nodo *Vaciar_Lista(struct Nodo *);
void  	Mostrar_Lista(struct Nodo *);
struct 	Nodo *Del_Nodo(int, struct Nodo *);