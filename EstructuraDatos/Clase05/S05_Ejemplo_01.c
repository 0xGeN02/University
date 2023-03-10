// Asignatura: Estructura de Datos
// Programa: S05_Elemplo_01
// Nodo. Crear, Leer, Mostrar y liberar memoria de un nodo
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
struct Nodo *Crea_Nodo();
void Leer_Nodo(struct Nodo *);
void Mostrar_Nodo(struct Nodo *);
// Programa principal de pruebas
int main ()
{
// Declaración de variables
 struct Nodo *d;
 printf("Solicitud de %d bytes para el nodo\n",sizeof(Data));
 // Solicitud de reserva de memoria para un nodo.   
 d = Crea_Nodo();
 if (d == NULL)
  printf ("Operacion reserva memoria fallida");
 else
 {
   Leer_Nodo(d);
   Mostrar_Nodo(d);
 }
 free (d);
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