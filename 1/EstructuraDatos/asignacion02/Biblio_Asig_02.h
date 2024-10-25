
#ifndef BIBLIO_ASIG_02_H
#define BIBLIO_ASIG_02_H


// Definición del struct "Data" 

struct Data {
  char codigo[9]; 
  float latitud; // %.2f ; > 0 Norte ,, < 0 Sur
  float longitud; // %.2f ; > 0 este 1er meridiano ,, > oeste 1er meridiano
  
  char estado; // Estado = {0,1,2,3} 0 => detenido en origen, 1 => tránsito origen destino, 2 => detenido en destino, 3 => detenido en trayecto por avería
  char origen[16];
  char destino[16];

  float x; //Coordenada x del nodo 
  float y; //Coordenada y del nodo

} Data;

// Definición del struct "Nodo"
struct Nodo {

  struct Data Data;
  struct Nodo *siguiente;
  struct Nodo *anterior;
  
} Nodo;


// Definición de constantes
#define MAX_LONG_CODIGO 8
#define MAX_LONG_NOMBRE 15
#define PI 3.14159265
#define RADIO_TIERRA_KM 6371.0
#define RAD_TO_DEG (180.0/PI)
#define DEG_TO_RAD (PI/180.0)



// Ciudades
#define ORIGEN "Madrid" // /*Longitud*/ O 3° 42' 9.22'' /*Latitud*/ N 40° 24' 59.4''
#define DESTINO "Sevilla" //  /*Longitud*/ O 5° 58' 23.41'' /*Latitud*/ N 37° 22' 58.19''


// Prototipos de las funciones
//1
void Crear_Nodo(struct Nodo **nodo, struct Data data);
void Insertar_Data(struct Data *data);
void Insertar_Nodo_Posicion(struct Nodo **nodo, struct Data data, int posicion);
struct Nodo *Buscar_Nodo(char codigo[9], struct Nodo *Nodo);
void Imprimir_Nodo(struct Nodo *nodo);
//2
void Editar_Data_Nodo(struct Nodo *nodo, struct Data nuevaData);
//3
void Print_Nodo_Ubicacion(struct Nodo *nodo);
//4
int compararUbicacion(const void *p1, const void *p2);
void Mostrar_Codigos_Ordenados(struct Nodo *nodo);
//5
void Mostrar_Nodo_yuxtapuestos(struct Nodo *nodo);

//6
struct Nodo *Retirar_Nodo(struct Nodo *nodo);
void Reingresar_Nodo(struct Nodo *nodo_retirado, struct Nodo *nodo_anterior, struct Nodo *nodo_siguiente);
void Eliminar_Nodo(struct Nodo *nodo);
//7
void Distancia_Nodos(struct Nodo *nodo1,struct Nodo *nodo2);
void Distancia_Haversine(struct Nodo *nodo1, struct Nodo *nodo2);
// Reto:
void Calcular_Angulo_Azimuth(struct Nodo *nodo1, struct Nodo *nodo2);

//Reto2:
void Crear_Lista_Invertida(struct Nodo **inicial);

//Finalizar y vaciar lista
void VaciarLista(struct Nodo **nodo);

#endif
