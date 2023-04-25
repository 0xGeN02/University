/****************************************
* Asignatura: Estructura de Datos       *
* Sesión 09 Ejemplo 02                  *
* Programación Orientada a Objetos POO  *
* Declaraciones Clase Base Persona      *
* Programa exclusivo para uso académico *
* Realizado por: Eladio Dapena Gonzalez *
* Fecha: 14/03/2023                     *
*****************************************/
// Bibliotecas
#include "CPersona.h"
// Declaraciones de métodos de la Clase base Persona
 //Constructores
Persona::Persona()
{
    Nombre="";DNI="";Edad=0; 
}
Persona::Persona(string A, string B, int C)
{
   Nombre=A;DNI=B;Edad=C;
}
//Seters
void Persona::SetNombre(string A)
{
    Nombre=A;
}
void Persona::SetDNI(string A)
{
    DNI=A;
}
void Persona::SetEdad(int A)
{
    Edad=A;
}
//Geters
string Persona::GetNombre()
{
    return Nombre;
}
string Persona::GetDNI()
{
    return DNI;
}
int Persona::GetEdad()
{
    return Edad;
}
 // Métodos Adicionales
void Persona::Leer_Datos()
{
   cout<<"    NOMBRE Y APELLIDO : ";getline(cin,this->Nombre);
   cout<<"    DNI               : ";getline(cin,this->DNI);
   cout<<"    EDAD              : ";cin>>this->Edad;
}
  void Persona::Muestra_Datos() {
   cout.fill(' ');
   cout<<left<<"    NOMBRE : "<<setw(20)<<Nombre<<"  DNI : "<<setw(10)<<DNI<<" EDAD : "<<Edad<<endl;
 }
