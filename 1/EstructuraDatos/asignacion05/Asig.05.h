
#ifndef ASIG_05
#define ASIG_05

/****************************************
* Asignatura: Estructura de Datos       *
* Clase Arbol_B                         *
* Fichero Cabecera de la clase Arbol_B  *
* Define  Clase Nodo_AB                 *
* Adaptado por: Mateo Delgado-Gambino   *
* Fecha: 08/05/2023                     *
*****************************************/

using namespace std;

#include <vector>
#include <algorithm>
#include <random>
#include <iostream>

class Arbol_B {
public:
    Arbol_B();
    ~Arbol_B();
    void insertar(int valor);
    bool buscar(int valor) const;

private:
    struct Nodo {
        int valor;
        Nodo* izquierdo;
        Nodo* derecho;
    };
    Nodo* raiz;
    void insertar(Nodo*& nodo, int valor);
    bool buscar(Nodo* nodo, int valor) const;
};

void NUM_ALEA_P4(vector<int>& , int , int , int , unsigned  );



#endif