// Asignatura: Estructura de Datos
// Biblioteca Para oPeraciones con Puntos en el Plano
// Fichero  Punto2D.c Declaraciones de rutinas
// Programa de uso académico
// Realizado Por: Santiago Souto Ortega
// Fecha 20/01/2023        
// Inclusión de Bibliotecas

#include "Punto2D.h"

// Declaración de funciones
/*  Funcion    : Ingresa_Punto    TiPo: Punto2D
    Parametros : NO
    Comentario : Entrada de un dato tiPo Punto2D
*/

Punto2D Ingresa_Punto(){
    Punto2D P;
    printf("Ingresa Coordenadas Punto en X y en Y(Formato (x,y)): \n");
    scanf("(%f, %f)",&P.x, &P.y);
    return P;
}
// Procedimiento: Escribe_Punto   TiPo: ()
// Parametros   :  1   TiPo: Punto2D   Indentificador: P  Forma: Valor
//
// Comentario   : Escribe en Pantalla las coordenadas de un Punto  (x,y)


void Escribe_Punto(Punto2D P){

    printf("El valor de x = %4.2f \t el valor de y =  %4.2f \n",P.x, P.y);
}

// Funcion: Distancia    TiPo: float
// Parametros : 1  TiPo: Punto2D  Identificador : P1  Forma: Valor
//              2  TiPo: Punto2D  Identificador : P2  Forma: Valor
//
// Comentario: Calcular la distancia entre dos Puntos

    float Distancia(Punto2D P1,Punto2D P2){
        return (sqrt(pow((P2.x-P1.x),2) + pow((P2.y-P1.x),2)));  
    }

// Funcion: PuntoMedio    TiPo: Punto2D
// Parametros : 1  TiPo: Punto2D  Identificador : P1  Forma: Valor
//              2  TiPo: Punto2D  Identificador : P2  Forma: Valor
//
// Comentario: Calcular el Punto medio entre dos Puntos


    Punto2D PuntoMedio(Punto2D P1,Punto2D P2){

        Punto2D PFinal;

        PFinal.x = ((P2.x + P1.x)/2);
        PFinal.y = ((P2.y + P1.y)/2);
        
        return PFinal;
    }

// Funcion: Cuadrante   TiPo: int
// Parametros   :  1   TiPo: Punto2D   Indentificador: P  Forma: Valor
//
// Comentario   : Calcula el cuadrante en el que esta un Punto  

    int Cuadrante(Punto2D P1){
        if((P1.x > 0) && (P1.y > 0)){
            return 1;
        }else{
            if((P1.x > 0) && (P1.y < 0)){
                return 4;
            }else{
                if((P1.x < 0) && (P1.y < 0)){
                    return 3;
                }else{
                    return 2;
                }
            }
        }
    }
