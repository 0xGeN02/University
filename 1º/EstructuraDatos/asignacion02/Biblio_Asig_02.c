//Incluimos Bibliotecas

#include "Biblio_Asig_02.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


//Comenzamos con las funciones de la lista enlazada

/***************       CREAR NODO    *****************/
void Crear_Nodo(struct Nodo **nodo, struct Data data) {
  *nodo = (struct Nodo*)malloc(sizeof(struct Nodo));
  
  (*nodo)->Data = data;
  
  if (Crear_Lista_Invertida) {
    strcpy((*nodo)->Data.destino, ORIGEN);
    strcpy((*nodo)->Data.origen, DESTINO);
  } else {
    strcpy((*nodo)->Data.origen, ORIGEN);
    strcpy((*nodo)->Data.destino, DESTINO);
  }
  
  (*nodo)->siguiente = NULL;
  (*nodo)->anterior = NULL;
}

/************   INSERTAR DATA  ***********/
void Insertar_Data(struct Data *data) {

  printf("Ingrese el código del tren: ");
  scanf("%s", data->codigo);
  
  printf("Ingrese la latitud de la ubicación del tren (mayor que 0 para Norte, menor que 0 para Sur): ");
  scanf("%f", &data->latitud);
  
  printf("Ingrese la longitud de la ubicación del tren (mayor que 0 para este del primer meridiano, menor que 0 para oeste del primer meridiano): ");
  scanf("%f", &data->longitud);
  
  printf("Ingrese el estado del tren (0 para detenido en origen, 1 para tránsito origen destino, 2 para detenido en destino, 3 para detenido en trayecto por avería): ");
  scanf("%d", &data->estado);
  
  printf("Ingrese la ubicación de origen del tren (máximo 15 caracteres): ");
  scanf("%s", data->origen);
  
  printf("Ingrese la ubicación de destino del tren (máximo 15 caracteres): ");
  scanf("%s", data->destino);
  
  printf("Ingrese la coordenada x del nodo: ");
  scanf("%f", &data->x);
  
  printf("Ingrese la coordenada y del nodo: ");
  scanf("%f", &data->y);
}


//1.2 Función para Insertar un Nodo en la lista en Posicion Especifica
void Insertar_Nodo_Posicion(struct Nodo **nodo, struct Data data, int posicion) {
  struct Nodo *nuevoNodo;
  struct Nodo *nodoActual;
  int contador = 1;

  nuevoNodo = (struct Nodo*)malloc(sizeof(struct Nodo));
  nuevoNodo->Data = data;

  if (posicion == 1) {
    nuevoNodo->siguiente = *nodo;
    nuevoNodo->anterior = NULL;
    if (*nodo != NULL) {
      (*nodo)->anterior = nuevoNodo;
    }
    *nodo = nuevoNodo;
  } 
  else {
    nodoActual = *nodo;
    while (nodoActual->siguiente != NULL && contador < posicion - 1) {
      nodoActual = nodoActual->siguiente;
      contador++;
    }
    nuevoNodo->siguiente = nodoActual->siguiente;
    nuevoNodo->anterior = nodoActual;
    if (nodoActual->siguiente != NULL) {
      nodoActual->siguiente->anterior = nuevoNodo;
    }
    nodoActual->siguiente = nuevoNodo;
  }
}

void Imprimir_Nodo(struct Nodo *nodo) {
  printf("Código: %s\n", nodo->Data.codigo);
  printf("Latitud: %.2f\n", nodo->Data.latitud);
  printf("Longitud: %.2f\n", nodo->Data.longitud);
  printf("Estado: %d\n", nodo->Data.estado);
  printf("Origen: %s\n", nodo->Data.origen);
  printf("Destino: %s\n", nodo->Data.destino);
  printf("Coordenada x: %.2f\n", nodo->Data.x);
  printf("Coordenada y: %.2f\n", nodo->Data.y);
}

struct Nodo* Buscar_Nodo(char codigo[9], struct Nodo *nodo) {

    char codigo_busqueda[9]; 
    struct Nodo* nodo_actual = nodo;
    char respuesta;
    
    printf("Ingrese el código del nodo a buscar: ");
    scanf("%s", codigo_busqueda); 
    
    while (nodo_actual != NULL) {
        if (strcmp(nodo_actual->Data.codigo, codigo_busqueda) == 0) {
            printf("Se encontró el nodo con código %s:\n", codigo_busqueda);
            printf("Quieres los datos del nodo? (Y/N): ");
            scanf(" %c", &respuesta);
            if(respuesta == 'Y' || respuesta == 'y'){ 
              Imprimir_Nodo(nodo_actual);
            }
            return nodo_actual;
        }
        nodo_actual = nodo_actual->siguiente;
    }
    
    printf("No se encontró el nodo con código %s\n", codigo_busqueda);
    return NULL;
}


/***************       MODIFICAR DATA    *****************/
void Editar_Data_Nodo(struct Nodo *nodo, struct Data nuevaData) {
  strcpy(nodo->Data.codigo, nuevaData.codigo);
  nodo->Data.latitud = nuevaData.latitud;
  nodo->Data.longitud = nuevaData.longitud;
  nodo->Data.estado = nuevaData.estado;
  strcpy(nodo->Data.origen, nuevaData.origen);
  strcpy(nodo->Data.destino, nuevaData.destino);
  nodo->Data.x = nuevaData.x;
  nodo->Data.y = nuevaData.y;
}

/***************       MOSTRAR NODO Y UBICACION   *****************/
void Print_Nodo_Ubicacion(struct Nodo *nodo) {
  printf("Código: %s\n", nodo->Data.codigo);
  
  // Show latitude
  if (nodo->Data.latitud >= 0) {
    printf("Latitud: %.0fº %.0f' %.2f\" N\n", floor(nodo->Data.latitud), floor((nodo->Data.latitud - floor(nodo->Data.latitud)) * 60), fmod(nodo->Data.latitud * 3600, 60));
  } 
  
  else {
    printf("Latitud: %.0fº %.0f' %.2f\" S\n", ceil(nodo->Data.latitud), ceil((fabs(nodo->Data.latitud) - floor(fabs(nodo->Data.latitud))) * 60), fmod(fabs(nodo->Data.latitud) * 3600, 60));
  }

  // Show longitude
  if (nodo->Data.longitud >= 0) {
    printf("Longitud: %.0fº %.0f' %.2f\" E\n", floor(nodo->Data.longitud), floor((nodo->Data.longitud - floor(nodo->Data.longitud)) * 60), fmod(nodo->Data.longitud * 3600, 60));
  } 
  
  else {
    printf("Longitud: %.0fº %.0f' %.2f\" W\n", ceil(nodo->Data.longitud), ceil((fabs(nodo->Data.longitud) - floor(fabs(nodo->Data.longitud))) * 60), fmod(fabs(nodo->Data.longitud) * 3600, 60));
  }

  printf("Estado: %d\n", nodo->Data.estado);
  printf("Origen: %s\n", nodo->Data.origen);
  printf("Destino: %s\n", nodo->Data.destino);
  printf("Coordenada x: %.2f\n", nodo->Data.x);
  printf("Coordenada y: %.2f\n", nodo->Data.y);
}


/***************     LISTA ORDENADA   *****************/

// Función de comparación para ordenar los nodos según su ubicación
int compararUbicacion(const void *p1, const void *p2) {
  struct Nodo *nodo1 = *(struct Nodo **)p1;
  struct Nodo *nodo2 = *(struct Nodo **)p2;

  if (nodo1->Data.longitud > nodo2->Data.longitud) {
    return 1;
  } else if (nodo1->Data.longitud < nodo2->Data.longitud) {
    return -1;
  } else if (nodo1->Data.latitud > nodo2->Data.latitud) {
    return 1;
  } else if (nodo1->Data.latitud < nodo2->Data.latitud) {
    return -1;
  } else {
    return 0;
  }
}

void Mostrar_Codigos_Ordenados(struct Nodo *nodo) {
  // Contamos la cantidad de nodos en la lista
  int numNodos = 0;
  struct Nodo *nodoActual = nodo;
  while (nodoActual != NULL) {
    numNodos++;
    nodoActual = nodoActual->siguiente;
  }

  // Creamos un array de punteros a nodos y los copiamos de la lista
  struct Nodo *nodos[numNodos];
  nodoActual = nodo;
  int i = 0;
  while (nodoActual != NULL) {
    nodos[i] = nodoActual;
    nodoActual = nodoActual->siguiente;
    i++;
  }

  // Ordenamos el array de nodos según su ubicación
  qsort(nodos, numNodos, sizeof(struct Nodo *), compararUbicacion);

  // Mostramos los códigos ordenados
  printf("Códigos ordenados según su ubicación:\n");
  for (int i = 0; i < numNodos; i++) {
    printf("%s\n", nodos[i]->Data.codigo);
  }
}

/***************     Mostrar Nodo y Yuxtapuestos   *****************/

void Mostrar_Nodo_yuxtapuestos(struct Nodo *nodo) {
  printf("Información del Nodo:\n");
  printf("Código: %s\n", nodo->Data.codigo);
  printf("Latitud: %.2f %c\n", fabs(nodo->Data.latitud), (nodo->Data.latitud >= 0) ? 'N' : 'S');
  printf("Longitud: %.2f %c\n", fabs(nodo->Data.longitud), (nodo->Data.longitud >= 0) ? 'E' : 'W');
  printf("Estado: %d\n", nodo->Data.estado);
  printf("Origen: %s\n", nodo->Data.origen);
  printf("Destino: %s\n", nodo->Data.destino);
  printf("Coordenadas X,Y: (%.2f, %.2f)\n", nodo->Data.x, nodo->Data.y);

  if (nodo->anterior != NULL) {
    printf("Nodo anterior:\n");
    printf("Código: %s\n", nodo->anterior->Data.codigo);
    printf("Latitud: %.2f %c\n", fabs(nodo->anterior->Data.latitud), (nodo->anterior->Data.latitud >= 0) ? 'N' : 'S');
    printf("Longitud: %.2f %c\n", fabs(nodo->anterior->Data.longitud), (nodo->anterior->Data.longitud >= 0) ? 'E' : 'W');
    printf("Estado: %d\n", nodo->anterior->Data.estado);
    printf("Origen: %s\n", nodo->anterior->Data.origen);
    printf("Destino: %s\n", nodo->anterior->Data.destino);
    printf("Coordenadas X,Y: (%.2f, %.2f)\n", nodo->anterior->Data.x, nodo->anterior->Data.y);
  } 
  
  else {
    printf("Nodo anterior: No existe\n");
  }

  if (nodo->siguiente != NULL) {
    printf("Nodo siguiente:\n");
    printf("Código: %s\n", nodo->siguiente->Data.codigo);
    printf("Latitud: %.2f %c\n", fabs(nodo->siguiente->Data.latitud), (nodo->siguiente->Data.latitud >= 0) ? 'N' : 'S');
    printf("Longitud: %.2f %c\n", fabs(nodo->siguiente->Data.longitud), (nodo->siguiente->Data.longitud >= 0) ? 'E' : 'W');
    printf("Estado: %d\n", nodo->siguiente->Data.estado);
    printf("Origen: %s\n", nodo->siguiente->Data.origen);
    printf("Destino: %s\n", nodo->siguiente->Data.destino);
    printf("Coordenadas X,Y: (%.2f, %.2f)\n", nodo->siguiente->Data.x, nodo->siguiente->Data.y);
  }
  
   else {
    printf("Nodo siguiente: No existe\n");
  }
}


/***************       Retirar Nodo    *******************/
struct Nodo* Retirar_Nodo(struct Nodo *nodo) {
    if (nodo->anterior != NULL) {
        nodo->anterior->siguiente = nodo->siguiente;
    }
    if (nodo->siguiente != NULL) {
        nodo->siguiente->anterior = nodo->anterior;
    }
    nodo->anterior = NULL;
    nodo->siguiente = NULL;

    return nodo;
}

/***************       Reingresar Nodo   *****************/
void Reingresar_Nodo(struct Nodo *nodo_retirado, struct Nodo *nodo_anterior, struct Nodo *nodo_siguiente) {
    nodo_retirado->anterior = nodo_anterior;
    nodo_retirado->siguiente = nodo_siguiente;

    if (nodo_anterior != NULL) {
        nodo_anterior->siguiente = nodo_retirado;
    }
    if (nodo_siguiente != NULL) {
        nodo_siguiente->anterior = nodo_retirado;
    }
}

/***************       ELIMINAR NODO    *****************/
void Eliminar_Nodo(struct Nodo *nodo) {
  if (nodo->anterior != NULL) {
    nodo->anterior->siguiente = nodo->siguiente;
  }
  if (nodo->siguiente != NULL) {
    nodo->siguiente->anterior = nodo->anterior;
  }
  free(nodo);
}

/***************       DISTANCIA NODOS    *****************/
void Distancia_Nodos(struct Nodo* nodo1,struct Nodo* nodo2){

  float distancia = sqrt(pow(nodo2->Data.x - nodo1->Data.x, 2) + pow(nodo2->Data.y - nodo1->Data.y, 2));
  printf("La distancia entre el nodo1 y el nodo2 es: " "%f", distancia);
}

/***************       CALCULA DISTANCIA NODOS    *****************/

              /*       usando la fórmula de Haversine         */
void Distancia_Haversine(struct Nodo *nodo1, struct Nodo *nodo2) {

  float lat1 = nodo1->Data.latitud * PI / 180.0; // Convertir a radianes
  float lon1 = nodo1->Data.longitud * PI / 180.0;
  float lat2 = nodo2->Data.latitud * PI / 180.0;
  float lon2 = nodo2->Data.longitud * PI / 180.0;
  float dlat = lat2 - lat1;
  float dlon = lon2 - lon1;
  float a = sin(dlat/2) * sin(dlat/2) + cos(lat1) * cos(lat2) * sin(dlon/2) * sin(dlon/2);
  float c = 2 * atan2(sqrt(a), sqrt(1-a));
  float distancia = RADIO_TIERRA_KM * c;
  printf("La distancia entre el nodo1 y nodo2 es: " "%f", distancia);
}

                    //  RETO  1  //
/*****************   Angulo Azimuth    *****************/

void Calcular_Angulo_Azimuth(struct Nodo *nodo1, struct Nodo *nodo2) {
  
  float lat1 = DEG_TO_RAD * nodo1->Data.latitud;
  float lon1 = DEG_TO_RAD * nodo1->Data.longitud;
  float lat2 = DEG_TO_RAD * nodo2->Data.latitud;
  float lon2 = DEG_TO_RAD * nodo2->Data.longitud;

  float y = sin(lon2 - lon1) * cos(lat2);
  float x = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(lon2 - lon1);

  float angulo = atan2(y, x);
  angulo *= RAD_TO_DEG;

  printf("El ángulo acimut entre los nodos es: %.2f\n", angulo);
}

                //  RETO 2 //
/***********     LISTA INVERTIDA    ************/
void Crear_Lista_Invertida(struct Nodo **inicial) {
  if (*inicial == NULL) {
    return;
  }

  struct Nodo *nodo_actual = *inicial;
  struct Nodo *siguiente_nodo = NULL;

  while (nodo_actual != NULL) {
    // Cambiar los punteros 'siguiente' y 'anterior' del nodo actual
    siguiente_nodo = nodo_actual->siguiente;
    nodo_actual->siguiente = nodo_actual->anterior;
    nodo_actual->anterior = siguiente_nodo;

    // Avanzar al siguiente nodo en la lista original
    nodo_actual = siguiente_nodo;
  }

  // Cambiar el puntero 'inicial' a apuntar al último nodo en la nueva lista
  *inicial = (*inicial)->anterior;
}


/***********     Vaciar Lista       ************/
void VaciarLista(struct Nodo **nodo){

    struct Nodo *actual = *nodo;
    struct Nodo *siguiente;

    while(actual != NULL){
        siguiente = actual->siguiente;
        free(actual);
        actual = siguiente;
    }

    *nodo = NULL;

    printf("Lista vaciada correctamente.\n");
}