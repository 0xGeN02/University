#ifndef BIBLIO_ASIG_02_H
#define BIBLIO_ASIG_02_H

// Definición del struct "Nodo"
typedef struct Nodo {
  char codigo[9]; 
  float latitud; // %.2f ; > 0 Norte ,, < 0 Sur
  float longitud; // %.2f ; > 0 este 1er meridiano ,, > oeste 1er meridiano
  char estado; // Estado = {0,1,2,3} 0 => detenido en origen, 1 => tránsito origen destino, 2 => detenido en destino, 3 => detenido en trayecto por avería
  struct Nodo *delante;
  struct Nodo *detras;
  char origen[16];
  char destino[16];
} Nodo;

// Definición del struct "Data" 
// typedef struct {
//   ...
// } Data;

// Constantes
#define ORIGEN "Madrid"
#define DESTINO "Sevilla"

// Prototipos de las funciones
void crearLista(Nodo **inicio, Nodo **fin);
void agregarNodo(Nodo **inicio, Nodo **fin, Nodo *nuevoNodo, int posicion);
void modificarEstado(Nodo *nodo, char estado);
void mostrarNodo(Nodo *nodo);
void mostrarListaOrdenada(Nodo *inicio);
void mostrarNodosAdyacentes(Nodo *nodo);
void retirarNodo(Nodo **inicio, Nodo **fin, Nodo *nodo);
// Reto:
// float distanciaNodos(Nodo *nodo1, Nodo *nodo2);
// float anguloNodos(Nodo *nodo1, Nodo *nodo2);

// Menú de opciones
void mostrarMenu_Opciones();

#endif
