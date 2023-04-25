#include "Biblio_Asig_03.h"

/******* Funciones de la Fila *******/

Fila::~Fila(){
    NodoSimple * aux;
    while(inicio != nullptr){
        aux = inicio;
        inicio = inicio -> getSiguiente();
        delete aux;
    }
    final = nullptr;
}

void Fila::Insertar(int c){
    NodoSimple *newNodo = new NodoSimple(c);
    if(inicio == nullptr){
        inicio = final = newNodo;
    }
    else{
        final->setSiguiente(newNodo);
        final = newNodo;
    }
}

int Fila::Eliminar(){
    if (inicio == nullptr){
        //Lista Vacia
        return -1; //excepcion
    }
    else{
        //getValue primer nodo
        int codigo = inicio->getCodigo();

        //Puntero a siguiente nodo
        NodoSimple *aux = inicio;
        inicio = inicio->getSiguiente();

        //Eliminar nodo
        delete aux;

        //Revisamos si fila Vacia
        if(inicio == nullptr){
            final = nullptr;
        }
        return codigo;
    }
}

/********  Funciones de la Pila  *********/

Pila::~Pila(){
    NodoSimple* aux; 
    while (top != nullptr){
        aux = top;
        top = top->getSiguiente();
        delete aux;
    }
    top = nullptr;  
}

void Pila::Insertar(int c){
    NodoSimple *newNodo = new NodoSimple(c);
    if(top == nullptr){
        top = newNodo;
    }
    else{
        top->setSiguiente(newNodo);
        top = newNodo;
    }
}

int Pila::Eliminar(){
    if(top == nullptr){
        //Lista Vacia
        return -1;
    }
    else{
        // get codigo top nodo
        int codigo = top->getCodigo();

        //Puntero a nodo anterior
        NodoSimple *aux = top;

        //Actualizamos top
        top = top->getSiguiente();
        
        //Eliminamos nodo
        delete aux;

        return codigo;
    }
}