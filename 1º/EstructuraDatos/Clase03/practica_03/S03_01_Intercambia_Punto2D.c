// Asignatura: Estructura de Datos
// Registros como parámetros por referencia
// Prueba rutina intercambia dos puntos
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 20/01/2023        
// Inclusión de Bibliotecas
#include <stdio.h>
// Definicion del tipo de dato Punto2D
  typedef struct
  {
    float x; // Coordenada sobre el eje de las abscisas
    float y; // Coordenada sobre el eje de las ordenadas
  }Punto2D;
// Prototipo
void Intercambia(Punto2D *, Punto2D *);  
 // Programa principal
int main()
{
  Punto2D P1,P2;
  P1.x=10.0;P1.y=10.0;
  P2.x=20.0;P2.y=20.0;
  printf("Punto 1 :[%5.2f,%5.2f]    ",P1.x,P1.y);
  printf("Punto 2 :[%5.2f,%5.2f]\n",P2.x,P2.y);
  printf("Intercambiar\n");
  Intercambia(&P1,&P2);
  printf("Punto 1 :[%5.2f,%5.2f]    ",P1.x,P1.y);
  printf("Punto 2 :[%5.2f,%5.2f]\n",P2.x,P2.y);
} 
// Declaraciones de rutinas
/* Funcion: Intercambia    Tipo: void (Procedimiento)
    Parametros :  1  Tipo: Punto2D  Identificador : P1  Forma: Referencia
                  2  Tipo: Punto2D  Identificador : P2  Forma: Referencia
    Comentario: Intercambia los valores de dos puntos
*/
 void  Intercambia(Punto2D *P1, Punto2D *P2)
  {
  Punto2D Paux;
  Paux=*P1;
  P1->x=P2->x; P1->y=P2->y;
  P2->x=Paux.x; P2->y=Paux.y;
  }
