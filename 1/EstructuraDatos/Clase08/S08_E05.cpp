/****************************************
* Asignatura: Estructura de Datos       *
* Lenguaje C++                          *
* Biblioteca iostream                   *
* Funciones y manipuladores de formato  *
* Formato dec, hex, oct, uppercase      *      
* Programa exclusivo para uso académico *
* Autor: Eladio Dapena Gonzalez         *
* Fecha: 05/03/2023                     *
*****************************************/
// Bibliotecas
#include<iostream>
#include<iomanip>
// espacio de nombres
using namespace std;
/* Programa principal */
int main()
{
    system("cls"); //system("clear"); unix ios users
    int a=1024, b=58, c=64, e=64458;
    bool T=true, F=false;   // Variables booleanas
    cout<< "Salida setw(8) dec hex (MINUS./MAYUS.) y oct  "<<endl;
    cout<<"dec "<< dec << right << setw(8) << a << setw(8) << b << setw(8) << c << setw(8) << e <<endl;
    cout<<"hex "<< hex << right << setw(8) << a << setw(8) << b << setw(8) << c << setw(8) << e <<endl;
    cout<<"HEX "<<uppercase << right << setw(8) << a << setw(8) << b << setw(8) << c << setw(8) << e <<endl;    
    cout<<"oct "<< oct << right << setw(8) << a << setw(8) << b << setw(8) << c << setw(8) << e <<endl;
    cout<<endl;
    cout<< "Salida setbase(10) setbase(16) setbase(8)  "<<endl;
    cout<<"dec "<<setbase(10)<< right << setw(8) << a << setw(8) << b << setw(8) << c << setw(8) << e <<endl;
    cout<<"HEX "<<setbase(16)<< right << setw(8) << a << setw(8) << b << setw(8) << c << setw(8) << e <<endl;
    cout<<"oct "<<setbase(8) << right << setw(8) << a << setw(8) << b << setw(8) << c << setw(8) << e <<endl;
    cout<<endl;
    cout<<"Valores booleanos"<<endl;
    cout<<"T = "<<T << "\t  F= "<<F<<endl;
    cout<<"Activando bandera boolalpha"<< endl;
    cout<<boolalpha<<"T = "<<T << "\t  F= "<<F<<endl;   
    cout<<"Desactivando bandera noboolalpha "<<T << endl; 
    cout<<noboolalpha<<"T = "<<T << "\t  F= "<<F<<endl; 
    cout<<endl;
    return 0;
}