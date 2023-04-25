// Asignatura: Estructura de Datos
// Programa: S06_Elemplo_01
// Uso de la biblioteca Nodo_Simple
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 18/02/2023        
// Inclusión de Bibliotecas
#include "Nodo_Simple.h"
// Programa principal
int main () {
// Declaración de variables
 struct Nodo *d;
 printf("Crear un nodo simple\n");
 d = Crea_Nodo();
 if (d == NULL)
  printf ("Reserva memoria fallida");
 else {
	printf("Nodo creado en %X \n",d);
	printf("Entrada de datos del Nodo\n");
	Leer_Nodo(d);
	printf("Datos del Nodo\n");
	Mostrar_Nodo(d);
	printf("Presione una tecla para finalizar");
   	fflush(stdin); // Limpia el buffer de entrada
  	getchar();
	Elimina_Nodo(d);
 }
}
