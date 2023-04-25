// Asignatura: Estructura de Datos
// Práctica Evaluada 03
// Clase Punto2D Reducida 
// Evaluación:
//    Agregar el métdodO cuadrante a la clase Punto2D 
// Realizado por: Eladio Dapena Gonzalez && Manuel Delgado
// Fecha 24/03/2023        
// Inclusión de Bibliotecas
#include <iostream>
#include<iomanip>
using namespace std;
// Definición de la clase y prototipos
//******************************************
//   NO MODIFICAR LA DEFINICIÓN DE LA CLASE
//******************************************
class Punto2D 
{
// Atributos
private:
 float x, y;
// Métodos
public:
// Método constructor
 Punto2D(float, float);
//PROTOTIPO DEL MÉTODO A REALIZAR

 char Cuadrante() const;   //Debe mantener el prototipo

//Función friend operator << (Inserción)
  friend ostream& operator<<(ostream& salida, const Punto2D& p); 
};
//*************************************
//  NO MODIFICAR EL PROGRAMA PRINCIPAL
//*************************************
int main(){
  Punto2D P1(4,2),P2(-4,2),P3(-4,-2),P4(4,-2),P5(0,4),P6(4,0);
  cout<<"Punto 1 "<<P1<<"  Cuadrante : "<<P1.Cuadrante()<<endl;
  cout<<"Punto 2 "<<P2<<"  Cuadrante : "<<P2.Cuadrante()<<endl;
  cout<<"Punto 3 "<<P3<<"  Cuadrante : "<<P3.Cuadrante()<<endl;
  cout<<"Punto 4 "<<P4<<"  Cuadrante : "<<P4.Cuadrante()<<endl;
  cout<<"Punto 5 "<<P5<<"  Cuadrante : "<<P5.Cuadrante()<<endl;
  cout<<"Punto 6 "<<P6<<"  Cuadrante : "<<P6.Cuadrante()<<endl;
}
//Declaraciones de la clase
//****************************************
//   ESCRIBIR EL MÉTDODO DEL CUADRANTE
//****************************************
char Punto2D::Cuadrante() const   {

  // SU CÓDIGO PROPUESTO PARA EL MÉTODO
  if (x == 0 && y == 0) { // está en el origen (0,0)
      return '0';
  } 
  else if (x > 0 && y > 0) { // cuadrante 1
      return '1';
  } 
  else if (x < 0 && y > 0) { // cuadrante 2
      return '2';
  } 
  else if (x < 0 && y < 0) { // cuadrante 3
      return '3';
  }
  if (x==0 or y==0){
    return '0';
  }
  else { // cuadrante 4
      return '4';
  }
  return ' '; // ELIMINAR UNA VEZ COMPLETE SU CÓDIGO    
}
//*********************************************************
//    NO MODIFICAR NINGUNA DE LAS DECLARACIONES SIGUIENTES
//**********************************************************
// Constructor
Punto2D::Punto2D(float x, float y) {
    this->x = x;    this->y = y;
}
// Definición de la sobrecarga del operador <<
ostream& operator<<(ostream& Salida, const Punto2D& p) {
  // Construimos el stream de salida
  Salida <<right<< "["<<setw(3) << p.x << ", "<<setw(3) << p.y << "]";
  return Salida;
}
