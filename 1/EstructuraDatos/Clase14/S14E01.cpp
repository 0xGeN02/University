/********************************************
* Asignatura: Estructura de Datos           *
* Sesión 14 Unidad V Análisis de Algoritmos *
* Ejemplo 01: Suma n enteros positivos      *
* Rutinas:                                  *
*   Suma_Repetición  (Repetición Indexada)  *
* Programa exclusivo para uso académico     *
* Adaptado por: Eladio Dapena Gonzalez      *
* Fecha: 23/04/2023                         *
*********************************************/
//Bibliotecas
#include <iostream>
// Prototipos de Rutinas
int Suma_Repeticion(int);
//Espacio de nombres
using namespace std;
// Programa Principal
int main()
{
 int N;
 cout<<"****   Suma N Primeros Enteros Positivos   ****"<<endl;
 cout<<"   Indique el valor de N : ";
 cin>>N;
 cout<<"*** SUMA de 1 a "<<N<<endl;
 cout<<"       CON REPITA INDEXADO    : "<<Suma_Repeticion(N)<<endl;
}
/******************************************
 *        Rutinas Utilizadas              *
 ******************************************/
//
/*******************************************************
 * Rutina: Suma_Repetición		Tipo: Entero	
 * Parámetros:	1.- n tipo Entero  (Hasta donde sumar)
 * Descripción: Suma los primeros n enteros 
 *              Utiliza estructura Repita Indexado
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio dapena Gonzalez
 ******************************************************/
int Suma_Repeticion(int n)
{
 int S=0,i;
 for (i=1;i<=n;i++)
 {
  S=S+i;
 }
  return S;
}