/********************************************
* Asignatura: Estructura de Datos           *
* Sesión 14 Unidad V Análisis de Algoritmos *
* Análisis Empírico                         *
* Ejemplo 08:  Casos Extremos               *
* Buscar Elemento                           *
*  Caso Aleatorio                           *
*  Peor Caso                                *
* Programa exclusivo para uso académico     *
* Adaptado por: Eladio Dapena Gonzalez      *
* Fecha: 23/04/2023                         *
*********************************************/
//Bibliotecas
#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>
#include <limits.h>
#include <stdlib.h>
using namespace std;
using namespace std::chrono;
// Prototipos de rutinas
void Num_Alea( vector<int>& ,int , int , int);
int  Busca_Elem(vector<int>&, int);
void ENTERO_ALEA(vector<int>& , int, int , int , unsigned  );
void Muestra_Vec(vector<int>&);
void MergeSort(vector<int>& );
void BubbleSort(vector<int>& ); 
void bubbleSort01(vector<int>& ); 
int  Busca_Max(vector<int>& );
// Programa principal
int main() 
{
system("cls"); // Para macOS o Linux sustituir por system("clear");  
 int n;              // número de elementos del arreglo
 int m = 0;          // Valor Mínimo
 int s = 100000000;    // Valor Máximo
 int pmax, Elemento, pos;
 cout<<"INDIQUE EL NUMERO DE ELEMENTOS DEL VECTOR A GENERAR  : ";
 cin>>n;
 vector<int> Vec1,Vec2,Vec3,Vec4; // arreglo para almacenar los números generados
 Num_Alea(Vec1, n, m, s);
 //ENTERO_ALEA(Vec1, n, m, s, 10); // Genera enteros no repetidos
 Vec2=Vec1;Vec3=Vec1;Vec4=Vec1;
 cout<<endl;

 // BUSCAR MAXIMO CASO ALEATORIO
 pmax=Busca_Max(Vec1);
 Elemento=Vec1[Busca_Max(Vec1)];

 cout<<"ELEMENTO A BUSCAR MAXIMO = "<<Vec1[pmax]<<endl; 
 cout<<"  BUSCAR ELEMENTO"<<endl; 
 //CASO ALEATORIO BUSCAR ELEMENTO EN EL VECTOR
 auto start = chrono::high_resolution_clock::now();
 pos=Busca_Elem(Vec1, Elemento);
 auto end = chrono::high_resolution_clock::now();
 //chrono::duration<double> Case_alea = end - start;
 auto Case_alea = duration_cast<microseconds>(end - start).count();
 cout<<"\tORDEN AELATORIO           ELEMENTO EN : ["<<pos<<"] = \t"<<Vec1[pos]<<endl; 
// ORDENAR EL VECTOR DE MAYOR A MENOR PARA EXPLORAR MEJOR CASO
 sort(Vec2.begin(), Vec2.end(), [](int a, int b) {return a > b;});
 start = chrono::high_resolution_clock::now();
 pos=Busca_Elem(Vec2, Elemento);
 end = chrono::high_resolution_clock::now();
 //chrono::duration<double> Case_ord_may = end - start;
  auto Case_ord_may = duration_cast<microseconds>(end - start).count();
 cout<<"\tORDENADO DE MAYOR A MENOR ELEMENTO EN : ["<<pos<<" ] = \t"<<Vec2[pos]<<endl; 
// ORDENAR EL VECTOR DE MENOR A MAYOR PARA EXPLORAR PEOR CASO
//BubbleSort(Vec3);
MergeSort(Vec3);
//bubbleSort01(Vec3); 
// BUSCAR MAXÍMO QUE ES EL ÚLTIMO ELEMENTO
 start = chrono::high_resolution_clock::now();
 pos=Busca_Elem(Vec3, Elemento);
 end   = chrono::high_resolution_clock::now();
 //chrono::duration<double> Case_ord_men = end - start;
  auto Case_ord_men = duration_cast<microseconds>(end - start).count();
 cout<<"\tORDENADO DE MENOR A MAYOR ELEMENTO EN : ["<<pos<<"] = "<<Vec3[pos]<<endl; 
 cout<<"RESULTADOS"<<endl;
 cout << "  TIEMPO DE BUSQUEDA CASO ALEATORIO  : " << (Case_alea) <<"\tmicrosegundos" << endl;
 cout << "  TIEMPO DE BUSQUEDA MEJOR CASO      : " << (Case_ord_may) <<"\tmicrosegundos" << endl;
 cout << "  TIEMPO DE BUSQUEDA PEOR  CASO      : " << (Case_ord_men) <<"\tmicrosegundos" << endl;
 return 0;
}

// DECLARACIONES DE LAS RUTINAS

void Num_Alea(vector<int>& V, int n, int li, int ls) 
{
 srand(time(NULL));
 for (int i = 0; i<n; i++) 
 {
  int num = (rand() % (ls - li + 1)) + li;
  V.push_back(num);
 }
}

void Muestra_Vec(vector<int>& V)
{
 for (unsigned i = 0; i < V.size(); i++) 
 {
  cout << " " << V[i];
 }
}

// Rutina Ordenación por Burbuja
void BubbleSort(vector<int>& a) 
{
    int n,aux;
    n = a.size();
    for (int i = 0; i < n-2; i++) 
    {
        for (int j = i; j < n-1; j++) 
        {
            if (a[j] < a[i]) 
            {
                aux=a[i];a[i]=a[j];a[j]=aux;
            }
        }
    }
}

void bubbleSort01(vector<int>& arr) 
{
    int n = arr.size();
    for (int i = 0; i < n-1; i++) 
    {
        for (int j = 0; j < n-i-1; j++) 
        {
            if (arr[j] > arr[j+1]) 
            {
                swap(arr[j], arr[j+1]);
            }
        }
    }
}
// Rutina Ordenación por Mezcla
void MergeSort(vector<int>& arr) 
{
 if (arr.size() > 1) 
 {
  vector<int>::iterator mid = arr.begin() + arr.size()/2;
  vector<int> left(arr.begin(), mid);
  vector<int> right(mid, arr.end());
  MergeSort(left);
  MergeSort(right);
  merge(left.begin(), left.end(), right.begin(), right.end(), arr.begin());
 }
}

int Busca_Max(vector<int>& arr) 
{
 int maxPos = -1;
 int maxVal = INT_MIN;
 for (unsigned i = 0; i < arr.size(); i++) 
 {
  if (arr[i] >= maxVal) 
  {
   maxVal = arr[i];
   maxPos = i;
  }
 }
 return maxPos;
}

int Busca_Elem(vector<int>& v, int e)
{
 int Pos = -1;
 unsigned int i=0;
 while ((i<(v.size())))
 {
  if (v[i] == e)
  {
   Pos=i;
   i=v.size();
  }
  else
   i++;
 }
 return Pos;
}

//RUTINA DE SOPORTE PARA GENERAR NÚMEROS ENTEROS
void ENTERO_ALEA(vector<int>& Vec, int N, int LI, int LS, unsigned semilla )
{
 Vec.clear();
 Vec.push_back(50); Vec.push_back(25); Vec.push_back(75);
 // Verifica si es posible generar N enteros distintos en el rango [LI, LS]
 if (N > LS - LI + 1) 
 {
  cerr << "No es posible generar " << N << " enteros distintos en el rango [" << LI << "," << LS << "].\n";
  return;
 }
// Genera los números aleatorios no repetidos
 mt19937 generator(semilla);
 uniform_int_distribution<int> distribution(LI, LS);
 while (Vec.size() < (unsigned)N) 
 {
  int numero = distribution(generator);
  if (find(Vec.begin(), Vec.end(), numero) == Vec.end()) 
  {
   Vec.push_back(numero);
  }
 }
  Vec.push_back(1); Vec.push_back(99); 
}
