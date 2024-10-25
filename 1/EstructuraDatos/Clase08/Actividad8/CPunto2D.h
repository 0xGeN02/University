/*****************************************
* Asignatura: Estructura de Datos        *
* Lenguaje C++                           *
* POO definición de Clases               *
* Método de lectura con cin de atributos *
* Programa exclusivo para uso académico  *
* Realizado por: Mateo Delgado           *
* Fecha: 02/03/2023                      *
******************************************/
#include <iostream>
#include<iomanip>
#include <cmath>

using namespace std;
// Definición de la clase
class Punto2D{
    // Atributos
    private:
    float x, y;
    int num_punto;
    // Métodos
    public:
    // Métodos constructores
    Punto2D();
    Punto2D(float, float);
    // Punto2D(float =0.0, float =0.0);  // Agrupa las dos anteriores
    // Prototipos
    // SETERS
    void setX(float); 
    void setY(float); 
    // GETERS
    float getX();
    float getY(); // Análogo getY
    // Otros métodos
    void Leer_Punto();
    //Parte 2:

    //Mostrar
    void Mostrar_Punto(int);

    //Parte 3:

    //Cuadrante
    void Cuadrante(int);
    //Distancia P-2P
    void DistanciaP_2P(int);
};