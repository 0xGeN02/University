/********************************************
* Asignatura: Estructura de Datos           *
* Sesión 14 Unidad V Análisis de Algoritmos *
* Análisis Empírico                         *
* Ejemplo 07:  Benchmarking                 *
* Ordenar Vecotres                          *
* Comparación Métodos                       *
* BubbleSort, MergeSort y SelectionSort     *
* Uso de Tipo más grandes                   *
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

//void Num_Normal(int , int , int , vector<int>& );
void Num_Alea(vector<int>& ,int , int , int );
void Muestra_Vec(vector<int>&);
void BubbleSort(vector<int>& ); 
void MergeSort(vector<int>& );
void SelectionSort(vector<int>& );

int main() 
{
 system("cls");   // Para macOS o Linux sustituir por system("clear");  
 cout<<"*****    ANALISIS DE ALGORITMOS    *****"<<endl;
 cout<<"----CASOS BENCHMARKING"<<endl;
 int n;              // número de elementos del arreglo
 int m = 0;          // Valor Mínimo
 int s = 100000000;    // Valor Máximo
 vector<int> Vec1,Vec2,Vec3,Vec4;   // arreglo para almacenar los números generados
 cout<<"INDIQUE EL NUMERO DE ELEMENTOS DEL VECTOR A GENERAR  < 500000 : ";
 cin>>n;
 //
 Num_Alea(Vec1,n, m, s);
 Vec2=Vec1;
 Vec3=Vec1;
 Vec4=Vec1;
// Benchmarking BubbleSort
    auto start = high_resolution_clock::now();
    BubbleSort(Vec2);
    auto end = high_resolution_clock::now();
    auto timeBubbleSort = duration_cast<microseconds>(end - start).count();
  
// Benchmarking merge sort
 start = high_resolution_clock::now();
 MergeSort(Vec3);
 end = high_resolution_clock::now();
 auto timeMergeSort = duration_cast<microseconds>(end - start).count();

// Benchmarking selection sort
 start = high_resolution_clock::now();
 SelectionSort(Vec4);
 end = high_resolution_clock::now();
 auto timeSelecSort = duration_cast<microseconds>(end - start).count();
 /*Muestra_Vec(Vec1);cout<<endl;
 Muestra_Vec(Vec2);cout<<endl;
 Muestra_Vec(Vec3);cout<<endl;
 Muestra_Vec(Vec4);cout<<endl;*/

 cout<<"***   COMPARACION DE TIEMPOS DE CADA METODO"<<endl;
 cout << "\tBubble    Sort Tiempo : " << (timeBubbleSort/1000) <<"\tmilisegundos" << endl;
 cout << "\tMerge     Sort Tiempo : " << (timeMergeSort/1000) << "\tmilisegundos" << endl;
 cout << "\tSelection Sort Tiempo : " << (timeSelecSort/1000) << "\tmilisegundos" << endl;   
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
// Rutina Ordenación por Selección
void SelectionSort(vector<int>& arr) 
{
 int n = (int)arr.size();
 int i, j, min_idx;
 for (i = 0; i < n-1; i++) 
 {
  min_idx = i;
  for (j = i+1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;
        swap(arr[min_idx], arr[i]);
    }
}


int Busca_Max(vector<int>& arr) 
{
    int maxPos = -1;
    int maxVal = INT_MIN;
    for (unsigned i = 0; i < arr.size(); i++) {
        if (arr[i] > maxVal) {
            maxVal = arr[i];
            maxPos = i;
        }
    }
    return maxPos;
}
