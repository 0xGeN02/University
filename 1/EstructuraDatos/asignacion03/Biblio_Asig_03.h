//Estructura de datos
//Asignacion 03

//Bibliotecas
#include <cmath>
#include <iostream>
#include <iomanip>

//Class Nodo
class NodoSimple{

    private:
    int codigo; //Identificador del nodo
    NodoSimple* siguiente; //Puntero al siguiente nodo en la lista enlazada

    public:
    NodoSimple(int c){ codigo = c; siguiente = nullptr;} //Inicializador del atributo
    int getCodigo() const {return codigo;} //Obtener atributo 
    void setCodigo(int c){codigo = c;} //Modificar atributo
    void setSiguiente(NodoSimple* nodo){siguiente = nodo;} //Establecer el siguiente nodo en la lista
    NodoSimple* getSiguiente() const {return siguiente;} //Obtener el siguiente nodo en la lista
};

//Class Fila (FIFO)
class Fila{

    private:
    NodoSimple* inicio; //Puntero inicio fila
    NodoSimple* final; //Puntero final fila

    public:
    Fila(){inicio = final = nullptr;} //Inicializar puntero
    ~Fila(); //Liberar memoria
    bool Vacia() const{return inicio == nullptr;} //Inicializa si lista = vacia
    void Insertar(int); //Insertar nodo al final de la lista
    int Eliminar(); //Elimina nodo al frente de la lista y devuelve su codigo
};

//Class Pila (LIFO)
class Pila{

    private:
    NodoSimple* top; //Puntero al top de la fila

    public:
    Pila(){top = nullptr;}//Inicializamos pointer
    ~Pila(); //Liberar memoria de los nodos
    bool Vacia() const{ return top == nullptr;} // Inicializa si lista = vacia
    void Insertar(int c); //Insertar nodo al inicio de fila
    int Eliminar(); //Elimina nodo al top de la list
};
