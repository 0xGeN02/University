#include "Biblio_Asig_02.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Definición de constantes
#define MAX_LONG_CODIGO 8
#define MAX_LONG_NOMBRE 15
#define PI 3.14159265
#define Limpiar "clear"

// Función para crear un nuevo nodo con los datos indicados
Nodo* crear_nodo(char codigo[MAX_LONG_CODIGO + 1], float latitud, float longitud, char estado, char origen[MAX_LONG_NOMBRE + 1], char destino[MAX_LONG_NOMBRE + 1]) {
  Nodo* nodo = (Nodo*)malloc(sizeof(Nodo));
  if (nodo != NULL) {
    strncpy(nodo->codigo, codigo, MAX_LONG_CODIGO);
    nodo->latitud = latitud;
    nodo->longitud = longitud;
    nodo->estado = estado;
    nodo->delante = NULL;
    nodo->detras = NULL;
    strncpy(nodo->origen, origen, MAX_LONG_NOMBRE);
    strncpy(nodo->destino, destino, MAX_LONG_NOMBRE);
  }
  return nodo;
}

// Función para insertar un nodo en una posición determinada de la lista
int insertar_nodo(Nodo** lista, Nodo* nuevo_nodo, int posicion) {
  // Verificar que la posición sea válida
  if (posicion < 1) {
    return 0;
  }
  // Si la lista está vacía, el nuevo nodo será el primer elemento
  if (*lista == NULL) {
    *lista = nuevo_nodo;
    return 1;
  }
  // Si la posición es 1, insertar el nuevo nodo al inicio de la lista
  if (posicion == 1) {
    nuevo_nodo->detras = *lista;
    (*lista)->delante = nuevo_nodo;
    *lista = nuevo_nodo;
    return 1;
  }
  // Buscar la posición indicada en la lista
  Nodo* actual = *lista;
  int contador = 1;
  while (actual->detras != NULL && contador < posicion - 1) {
    actual = actual->detras;
    contador++;
  }
  // Si la posición es mayor a la cantidad de elementos en la lista, el nuevo nodo será el último
  if (actual->detras == NULL && contador == posicion - 1) {
    actual->detras = nuevo_nodo;
    nuevo_nodo->delante = actual;
    return 1;
  }
  // Si la posición es válida, insertar el nuevo nodo en esa posición
  if (contador == posicion - 1) {
    nuevo_nodo->delante = actual;
    nuevo_nodo->detras = actual->detras;
    actual->detras->delante = nuevo_nodo;
    actual->detras = nuevo_nodo;
    return 1;
  }
  // Si la posición no es válida, no se puede insertar el nodo
  return 0;
}

// Función para modificar el estado de un nodo en la lista
int modificar_estado(Nodo* lista, char codigo[MAX_LONG_CODIGO + 1], char nuevo_estado) {
  // Buscar el nodo con el código indicado en la lista
  Nodo* actual = lista;
  while (actual != NULL && strcmp(actual->codigo, codigo) != 0) {
    actual = actual->delante;
  }
  if (actual == NULL) {
    // El código indicado no se encontró en la lista
    return 0;
  } else {
    // Modificar el estado del nodo
    actual->estado = nuevo_estado;
    return 1;
  }
}
// Función para calcular la distancia entre dos puntos en una esfera (usando la fórmula de Haversine)
float calcular_distancia(float lat1, float lon1, float lat2, float lon2) {
  float dlat = (lat2 - lat1) * PI / 180.0;
  float dlon = (lon2 - lon1) * PI / 180.0;
  float a = sin(dlat/2) * sin(dlat/2) + cos(lat1 * PI / 180.0) * cos(lat2 * PI / 180.0) * sin(dlon/2) * sin(dlon/2);
  float c = 2 * atan2(sqrt(a), sqrt(1-a));
  float distancia = 6371 * c;
  return distancia;
}

// Función para imprimir los datos de un nodo
void imprimir_nodo(Nodo* nodo) {
  printf("Código: %s\n", nodo->codigo);
  printf("Latitud: %.2f\n", nodo->latitud);
  printf("Longitud: %.2f\n", nodo->longitud);
  printf("Estado: %c\n", nodo->estado);
  printf("Origen: %s\n", nodo->origen);
  printf("Destino: %s\n", nodo->destino);
}

// Función para imprimir todos los nodos de la lista
void imprimir_lista(Nodo* lista) {
  Nodo* actual = lista;
  int contador = 1;
  while (actual != NULL) {
    printf("Nodo %d:\n", contador);
    imprimir_nodo(actual);
    printf("\n");
    actual = actual->delante;
    contador++;
  }
}

// Función para eliminar un nodo de la lista
int eliminar_nodo(Nodo** lista, char codigo[MAX_LONG_CODIGO + 1]) {
  // Buscar el nodo con el código indicado en la lista
  Nodo* actual = *lista;
  while (actual != NULL && strcmp(actual->codigo, codigo) != 0) {
    actual = actual->delante;
  }
  if (actual == NULL) {
    // El código indicado no se encontró en la lista
    return 0;
  } else {
    // Eliminar el nodo de la lista
    if (actual->delante == NULL) {
      *lista = actual->detras;
    } else {
      actual->delante->detras = actual->detras;
    }
    if (actual->detras != NULL) {
      actual->detras->delante = actual->delante;
    }
    free(actual);
    return 1;
  }
}
Nodo* crear_nodo(char codigo[MAX_LONG_CODIGO + 1], float latitud, float longitud, char estado, char origen[MAX_LONG_NOMBRE + 1], char destino[MAX_LONG_NOMBRE + 1]) {
  Nodo* nodo = (Nodo*)malloc(sizeof(Nodo));
  if (nodo != NULL) {
    strncpy(nodo->codigo, codigo, MAX_LONG_CODIGO);
    nodo->latitud = latitud;
    nodo->longitud = longitud;
    nodo->estado = estado;
    nodo->delante = NULL;
    nodo->detras = NULL;
    strncpy(nodo->origen, origen, MAX_LONG_NOMBRE);
    strncpy(nodo->destino, destino, MAX_LONG_NOMBRE);
  }
  return nodo;
}

// Función para insertar un nodo en una posición determinada de la lista
int insertar_nodo(Nodo** lista, Nodo* nuevo_nodo, int posicion) {
  // Verificar que la posición sea válida
  if (posicion < 1) {
    return 0;
  }
  // Si la lista está vacía, el nuevo nodo será el primer elemento
  if (*lista == NULL) {
    *lista = nuevo_nodo;
    return 1;
  }
  // Si la posición es 1, insertar el nuevo nodo al inicio de la lista
  if (posicion == 1) {
    nuevo_nodo->detras = *lista;
    (*lista)->delante = nuevo_nodo;
    *lista = nuevo_nodo;
    return 1;
  }
  // Buscar la posición indicada en la lista
  Nodo* actual = *lista;
  int contador = 1;
  while (actual->detras != NULL && contador < posicion - 1) {
    actual = actual->detras;
    contador++;
  }
  // Si la posición es mayor a la cantidad de elementos en la lista, el nuevo nodo será el último
  if (actual->detras == NULL && contador == posicion - 1) {
    actual->detras = nuevo_nodo;
    nuevo_nodo->delante = actual;
    return 1;
  }
  // Si la posición es válida, insertar el nuevo nodo en esa posición
  if (contador == posicion - 1) {
    nuevo_nodo->delante = actual;
    nuevo_nodo->detras = actual->detras;
    actual->detras->delante = nuevo_nodo;
    actual->detras = nuevo_nodo;
    return 1;
  }
  // Si la posición no es válida, no se puede insertar el nodo
  return 0;
}

int modificar_estado(Nodo* lista, char codigo[MAX_LONG_CODIGO + 1], char nuevo_estado) {
  // Buscar el nodo con el código indicado en la lista
  Nodo* actual = lista;
  while (actual != NULL && strcmp(actual->codigo, codigo) != 0) {
    actual = actual->delante;
  }
  if (actual == NULL) {
    return 0;
  } else {
    actual->estado = nuevo_estado;
    // Eliminar el nodo
    if (actual->delante == NULL && actual->detras == NULL) {
      // Si el nodo es el único elemento de la lista
      lista = NULL;
    } else if (actual->delante == NULL) {
      // Si el nodo es el primer elemento de la lista
      lista = actual->detras;
      actual->detras->delante = NULL;
    } else if (actual->detras == NULL) {
      // Si el nodo es el último elemento de la lista
      actual->delante->detras = NULL;
    } else {
      // Si el nodo está en medio de la lista
      actual->delante->detras = actual->detras;
      actual->detras->delante = actual->delante;
    }
    free(actual);
    return 1;
  }
}