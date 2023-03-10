// Asignatura: Estructura de Datos
// Programa: PRUEBA_BIBLIOTECA_LISTAS
// Actividad práctica presencial sesión 05
// Menú con opciones para operaciones con listas simples
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 28/01/2023        
// Inclusión de Bibliotecas
#include "Menu_Line.h"
#define LIMPIA "clear"   // Limpiar terminal
//PROTOTIPOS
void Muestra_Opciones();
int Menu(int, int);
struct Nodo *Hacer(int, struct Nodo *, struct Nodo * );
// Programa principal de pruebas
int main ()
{
// Declaración de variables
 struct Nodo *d, *Ini;
 int op;
 Ini=NULL;d=NULL;  // Inicio de la lista (Vacía)
  do
  {
  	op=Menu(1,6);
  	Ini=Hacer(op,Ini,d);
  	printf("Presione una tecla para continuar");
   	fflush(stdin);
  	getchar();
	}while (op!=6);
 Ini=Vaciar_Line(Ini);
 return 0;
 }
