/********************************************
* Asignatura: Estructura de Datos           *
* Sesión 14 Unidad V Análisis de Algoritmos *
* Ejemplo 03: Suma n enteros positivos      *
* Rutinas:                                  *
*   Suma_Repetición  (Repetición Indexada)  *
*   Suma_Gauss       (Método de Gauss)      *
* Limita el tamaño del datos de entrada     *
* Programa exclusivo para uso académico     *
* Adaptado por: Eladio Dapena Gonzalez      *
* Fecha: 23/04/2023                         *
*********************************************/
//Bibliotecas
#include <iostream>
#include <limits>
// Prototipos de Rutinas
int Suma_Repeticion(int);
int Suma_Gauss(int);
//Espacio de nombres
using namespace std;
// Programa Principal
int main()
{
 int N;
 cout<<"max int                    : "<<numeric_limits<int>::max()<<endl;
 cout<<"max unsigned int           : "<<numeric_limits<unsigned int>::max()<<endl;
 cout<<"max long int               : "<<numeric_limits<long int>::max()<<endl;
 cout<<"max unsigned long int      : "<<numeric_limits<unsigned long int >::max()<<endl;
 cout<<"max long long int          : "<<numeric_limits<long long int>::max()<<endl;
 cout<<"max unsigned long long int : "<<numeric_limits<unsigned long long int>::max()<<endl;
 cout<<"****   Suma N Primeros Enteros Positivos   ****"<<endl;
 cout<<"   Indique el valor de N <= 46340 : ";
 cin>>N;
 if (N<=46340)
 {
 cout<<"*** SUMA de 1 a "<<N<<endl;
 cout<<"       CON REPITA INDEXADO    : "<<Suma_Repeticion(N)<<endl;
 cout<<"       CON FORMULA DE GAUSS   : "<<Suma_Gauss(N)<<endl;
 }
 else
 cout<<"Error: N no puede superar el valor de 46340"<<endl;
}
// Declaración de Rutinas
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

/*******************************************************
 * Rutina: Suma_Gauss		Tipo: Entero	
 * Parámetros:	1.- n tipo Entero  (Hasta donde sumar)
 * Descripción: Suma los primeros n enteros 
 *              Utiliza método de Gauss
 * Rutina diseñada para docencia
 * Realizado por: Dr. Eladio dapena Gonzalez
 ******************************************************/
int Suma_Gauss(int n)
{
  return (n*(n+1)/2);
}