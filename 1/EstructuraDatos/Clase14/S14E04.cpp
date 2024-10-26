/********************************************
* Asignatura: Estructura de Datos           *
* Sesión 14 Unidad V Análisis de Algoritmos *
* Ejemplo 04: Suma n enteros positivos      *
* Rutinas:                                  *
*   Suma_Repetición  (Repetición Indexada)  *
*   Suma_Gauss       (Método de Gauss)      *
* Declarar variables de mayor tamaño        *
* Programa exclusivo para uso académico     *
* Adaptado por: Eladio Dapena Gonzalez      *
* Fecha: 23/04/2023                         *
*********************************************/
//Bibliotecas
#include <iostream>
#include <limits>
// Prototipos de Rutinas
unsigned long long int Suma_Repeticion(unsigned long long int);
unsigned long long int Suma_Gauss(unsigned long long int);
//Espacio de nombres
using namespace std;
// Programa Principal
int main()
{
 unsigned long long int N;
 cout<<"****   Suma N Primeros Enteros Positivos   ****"<<endl;
 cout<<"   Indique el valor de N <= 4835703278458516700 : ";
 cin>>N;
 if (N<=4835703278458516700)
 {
 cout<<"*** SUMA de 1 a "<<N<<endl;
 cout<<"       CON REPITA INDEXADO    : "<<Suma_Repeticion(N)<<endl;
 cout<<"       CON FORMULA DE GAUSS   : "<<Suma_Gauss(N)<<endl;
 }
 else
 cout<<"Error: N no puede superar el valor de 4835703278458516700"<<endl;
}
// Declaración de Rutinas
/*******************************************************
 * Rutina: Suma_Repetición		Tipo: unsigned long long int	
 * Parámetros:	1.- n tipo Entero  (Hasta donde sumar)
 * Descripción: Suma los primeros n enteros 
 *              Utiliza estructura Repita Indexado
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio dapena Gonzalez
 ******************************************************/
unsigned long long int Suma_Repeticion(unsigned long long int n)
{
 unsigned long long int S=0;
 unsigned long long int i;
 for (i=1;i<=n;i++)
 {
  S=S+i;
 }
  return S;
}

/*******************************************************
 * Rutina: Suma_Gauss		Tipo: unsigned long long int	
 * Parámetros:	1.- n tipo Entero  (Hasta donde sumar)
 * Descripción: Suma los primeros n enteros 
 *              Utiliza método de Gauss
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio dapena Gonzalez
 ******************************************************/
unsigned long long int Suma_Gauss(unsigned long long int n)
{
  return (n*(n+1)/2);
}