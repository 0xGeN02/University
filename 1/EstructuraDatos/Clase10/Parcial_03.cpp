// Asignatura: Estructura de Datos
// Clase Estudiante
// Inclusión de Bibliotecas
#include <iostream>
#include<iomanip>
#include <string>
using namespace std;
// Clase base Persona
class Estudiante {
  // Atributos   NO MODIFICAR
  private:
    string Name;
    float P1,P2,P3;
  public:
  //Constructores   NO MODIFICAR
    Estudiante(){
      Name="";P1=P2=P3=0;
    };

    Estudiante(string N, float p1, float p2 , float p3){
      Name=N;P1=p1;P2=p2;P3=p3;
    };

/************************************************************/

//Entrada de Datos Name, P1, P2, P3         

  float Leer_Datos(){
      cout << "Ingrese el nombre del estudiante: ";
      getline(cin, Name);
      cout << "Ingrese la nota del primer parcial: ";
      cin >> P1;
      cout << "Ingrese la nota del segundo parcial: ";
      cin >> P2;
      cout << "Ingrese la nota del tercer parcial: ";
      cin >> P3;
      return 0;
  }
//Método Media
  float Media(){   // Media de los parciales
    return (P1 + P2 + P3) / 3.0;
  };
  


  // Definición de la sobre carga del operador <<
  friend ostream& operator<<(ostream& Salida, Estudiante& e)  {
  
    Salida << "Nombre : "<<e.Name<<"["<< e.P1<<","<< e.P2 << ","<< e.P3 <<"]"<<"  Media = "<<e.Media()<<endl;
    return Salida;
  }
};

// Programa principal

int main (){

  // Declaración de variables
  Estudiante E1("Carlos Perdomo",4,7,6);
  Estudiante E2;
  E2.Leer_Datos();
  cout<<endl,
  cout<<"Estudiantes"<<endl;
  cout << fixed << setprecision(2)<<E1<<endl;
  cout << fixed << setprecision(2)<<E2<<endl;
  return 0;
}