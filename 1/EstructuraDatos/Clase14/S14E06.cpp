/********************************************
* Asignatura: Estructura de Datos           *
* Sesión 14 Unidad V Análisis de Algoritmos *
* Ejemplo 06: Calcular tiempos de ejecución *
* Lenguaje C++                              *
* Rutinas:                                  *
*   Factorial                               *
*   Factorial_R                             *
* Programa exclusivo para uso académico     *
* Adaptado por: Eladio Dapena Gonzalez      *
* Fecha: 23/04/2023                         *
*********************************************/     
// Inclusión de Bibliotecas
#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

// Definición de Prototipos de funciones
unsigned long long Factorial(int);
unsigned long long Factorial_R(int);
// Función principal
int main()
{
 int n;
 cout<<"---INICIAR MEDICION DEL TIEMPO DE EJECUCION"<<endl;
 cout<<endl;
 auto startp = high_resolution_clock::now(); // Medir tiempo total del programa
 cout<<"   ***********************************"<<endl;
 cout<<"   *            FACTORIAL            *"<<endl;
 cout<<"   ***********************************"<<endl;
 cout<<endl;
 cout<<"   INDIQUE UN NUMERO ENTERO EN EL RANGO [0 < n <21] : ";
 cin>>n;
 if (n>0 && n<=20)
 {
  auto start_time = high_resolution_clock::now();
  cout<<"   --FACTORIAL           DE  "<<n<<" ES : "<<Factorial(n);
  auto end_time = high_resolution_clock::now();
  auto tiempo = duration_cast<microseconds>(end_time - start_time).count();
  cout<<"   TIEMPO = "<<tiempo<<"\tmicrosegundos" << endl;
  start_time = high_resolution_clock::now();
  cout<<"   --FACTORIAL RECURSIVO DE  "<<n<<" ES : "<<Factorial_R(n);
  end_time = high_resolution_clock::now();
  tiempo = duration_cast<microseconds>(end_time - start_time).count();
  cout<<"   TIEMPO = "<<tiempo<<"\tmicrosegundos" << endl;
 }
 else
  cout<<"   ERROR: El valor de n debe estar etre 0 y 20"<<endl;
 cout<<endl;
 cout<<"---FINALIZAR MEDICION DEL TIEMPO DE EJECUCION"<<endl;
 auto endp = high_resolution_clock::now(); // Medir tiempo total del programa
 auto tiempo1 = duration_cast<microseconds>(endp - startp).count();
  cout<<"   TIEMPO = "<<tiempo1<<"\tmicrosegundos" << endl;
return 0;
} 
// Declaración de Funciones y Procedimientos
// Rutina: Factorial  (Solución iterativa)
// Tipo: Función   Retorna: Entero
// Parámetros: Entero n
// Programa de uso académico
// Dr. Eladio Dapena Gonzalez
unsigned long long Factorial(int n)
 {
  int k;
 unsigned long long F; 
 F=1;
 /* Calcula el producto n*(n-1)*(n-2)*...*2*1 */
 for (k = n; k > 1; --k) 
  {
   F=F*k;
  }
 return F;
 } 
// Declaración de Funciones y Procedimientos
// Rutina: Factorial_R  (Solución Recursiva)
// Tipo: Función   Retorna: Entero
// Parámetros: Entero n
// Programa de uso académico
// Dr. Eladio Dapena Gonzalez
unsigned long long Factorial_R(int n)
{
 unsigned long long r;
 if (n==1)
  r = 1;
 else
  r=n*Factorial_R(n-1) ;
 return (r) ;
}
