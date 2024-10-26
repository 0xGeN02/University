/*****************************************
* Asignatura: Estructura de Datos        *
* Lenguaje C++                           *
* Biblioteca iostream                    *
* Memoria Dinámica Operadores new y del  *
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
Data    *Crea_Estructura();
void     Leer_Data(Data *);
void     Mostrar_Data(Data *);

/* Programa principal */
int main()
{
    system("cls"); //system("clear"); unix ios users
    Data *d[3];
    for (int i = 0; i < 3; i++)
    {
        cout<<"Indique los datos del elemento : "<<(i+1)<<endl;
        d[i]=Crea_Estructura();
        Leer_Data(d[i]);
    }
        cout<<"Los datos son:"<<endl;
     for (int i = 0; i < 3; i++)
    {
        cout<<"Elemento  ["<<(i+1)<<"]  ";
        Mostrar_Data(d[i]);
        delete d[i]; 
    }   

    return 0;
}

Data *Crea_Estructura()
{
 return (new Data);
}
void Leer_Data(Data *a)
{
 printf("\tCODIGO : ");
 scanf("%d",&a->Codigo);
 // Otros datos
}

/***********************************************************************
 * Rutina		: Mostrar_Data	Procedimiento 	Tipo: void	
 * Parámetros	:variable tipo Data
 * Retorna		:		void
 * Diseño		: Rutina para uso académico
 * Autor		: Dr. Eladio Dapena Gonzalez
 ***********************************************************************/
void Mostrar_Data(Data *a)
{
printf("\tCODIGO : %d\n",a->Codigo);
// Otros datos
}