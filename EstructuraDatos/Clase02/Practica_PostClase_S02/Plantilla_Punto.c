// Asignatura: Estructura de Datos
// Pruebas de la Biblioteca Punto2D
// Programa de uso académico
// Realizado por: Santiago Souto Ortega
// Fecha 20/01/2023        
// Inclusión de Bibliotecas

#include "Punto2D.h"

// Programa principal
int main(){

    // Declarar variables para almacenar dos puntos.
    
    Punto2D p1, p2;

    //Ingresar las coordenadas de los puntos en la variables creadas

    p1 = Ingresa_Punto(); p2 = Ingresa_Punto();

    // Mostrar por pantalla ambos puntos identificados y el cuadrante en que se ubican

    Escribe_Punto(p1); Escribe_Punto(p2);

    printf("El punto 1 se encuentra en el cuadrante: %d\n", Cuadrante(p1));
    printf("El punto 2 se encuentra en el cuadrante: %d\n", Cuadrante(p2));

    // Mostrar la distancia entre los dos puntos

    printf("La distancia entre los dos puntos es de: %4.2f \n", Distancia(p1,p2));

    // Mostrar el punto medio entre los dos puntos.

    printf("El punto medio de los dos puntos se encuentra en la posici%cn: [%4.2f,%4.2f]\n",162, PuntoMedio(p1,p2).x, PuntoMedio(p1,p2).y);
    
    return 0;
}
