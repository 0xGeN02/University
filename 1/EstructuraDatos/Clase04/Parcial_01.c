// Evaluación Parcial Parte II
// Realizado por: Manuel Mateo Delgado Gambino López
// Fecha 09/02/2023

/* INCLUSIÓN DE BIBLIOTECAS */
#include<stdio.h>

//Prototipos de funciones
void Triangulo(int);
int Fibonacci_R (int);

//Programa Principal
int main()   // NO MODIFICAR EL PROGRAMA PRINCIPAL
{
  int n,k;
  printf("Indique un numero entero : ");
  scanf("%d",&n);
  printf("   TRIANGULO \n");
  Triangulo(n);
  printf("\n");
  printf("   FIBONACCI RECURSIVO \n");
  for (k=0;k<=n;k++)
    printf(" %d ",Fibonacci_R(k));
  printf("\n");
}

// DECLARACIONES DE RUTINA
// PROCEDIMIENTO TRIÁNGULO
void Triangulo(int a){
  // ESCRIBA EL CÓDIGO DE LA RUTINA
  int n;
  printf("Ingrese la altura entre el 2 y el 10:\n");
  scanf("%d", &n);
  if(n <= 10 && n >= 2){
    const char* bricks = "**********";
    const char* space = "          ";
    for(int i=1; i<n+1; ++i)
    {
      printf("%*.*s      %.*s\n", n,i,bricks, i,space);
    }
  }
  else{
    printf("Vuelve a ingresar los datos en el rango [2,10]\n");
  }
}

//FUNCIÓN RECURSIVA FIBONACCI
int Fibonacci_R (int b) 
{
  int fb=0;
  if (b < 0) {
      printf("Entrada inválida. Debe ser un número positivo.\n");
      return -1;
  } 
  else if (b == 0 || b == 1) {
      return b;
  } 
  else {
      return Fibonacci_R(b - 1) + Fibonacci_R(b - 2);
  }
}
