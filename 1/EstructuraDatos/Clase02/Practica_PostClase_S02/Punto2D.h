// Asignatura: Estructura de Datos
// Biblioteca para operaciones con puntos en el plano
// Fichero cabecera Punto2D.h
// Definición de tipos de datos y prototipos de rutinas
// Programa de uso académico
// Realizado por: Eladio Dapena Gonzalez
// Fecha 20/01/2023    
// Inclusión de bibliotecas
#include <stdio.h>
#include <math.h>
// Definicion del tipo de dato Punto2D
typedef struct {
    float x, y; // Coordenada sobre el eje de las abscisas // Coordenada sobre el eje de las ordenadas
    }Punto2D;
    // Definiciones de Prototipos de las rutinas
Punto2D     Ingresa_Punto();
void 	    Escribe_Punto(Punto2D);
float       Distancia(Punto2D,Punto2D);
Punto2D     PuntoMedio(Punto2D,Punto2D);
int         Cuadrante(Punto2D);
