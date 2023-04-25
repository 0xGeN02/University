// Asignatura: Estructura de Datos
// Biblioteca para nodos simples
// Fichero Cabecera Nodo_Simple.h
// Estructura de datos de información del nodo
// Estructura de datos del tipo Nodo
// Operaciones Nodo Simple: Crear Nodo, Leer Nodo, Mostrar Nodo
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha: 18/02/2023        
// Inclusión de Bibliotecas del sistema
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
struct  Nodo *Elimina_Nodo(struct Nodo *);
