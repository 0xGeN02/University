/*****************************************
* Asignatura: Estructura de Datos        *
* Lenguaje C++                           *
* Biblioteca iostream                    *
* Declaración simplificada de estructuras*                   *
* Programa exclusivo para uso académico  *
* Realizado por: Eladio Dapena Gonzalez  *
* Fecha: 02/03/2023                      *
******************************************/
#include <iostream>
using namespace std;
// Definición de nuevo tipo estructura
//Definición nuevos tipos de datos
typedef struct 
{
	int Codigo;
	// Otros datos
}Data;
// Prototipos de rutinas
Data    Leer_Data(Data);
void    Mostrar_Data(Data);

/* Programa principal */
int main()
{
    system("cls"); //system("clear"); unix ios users
    Data D[3];
    for (int i = 0; i < 3; i++)
    {
        cout<<"Indique los datos del elemento : "<<(i+1)<<endl;
        D[i]=Leer_Data(D[i]);
    }
        cout<<"Los datos son:"<<endl;
     for (int i = 0; i < 3; i++)
    {
        cout<<"Elemento  ["<<(i+1)<<"]  ";
        Mostrar_Data(D[i]);
    }   
    return 0;
}

Data Leer_Data(Data a)
{
 printf("\tCODIGO : ");
 scanf("%d",&a.Codigo);
 return a;
 // Otros datos
}

/***********************************************************************
 * Rutina		: Mostrar_Data	Procedimiento 	Tipo: void	
 * Parámetros	:variable tipo Data
 * Retorna		:		void
 * Diseño		: Rutina para uso académico
 * Autor		: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
void Mostrar_Data(Data a)
{
printf("\tCODIGO : %d\n",a.Codigo);
// Otros datos
}