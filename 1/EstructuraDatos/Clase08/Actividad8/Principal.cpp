
#include "CPunto2D.h"
int main(){
    Punto2D p1,p2;
    p1.Leer_Punto();
    p2.Leer_Punto();

    p1.Mostrar_Punto(1);
    p2.Mostrar_Punto(2);   

    p1.Cuadrante(1);
    p2.Cuadrante(2);

    p1.DistanciaP_2P(1);
    p2.DistanciaP_2P(2);

    return 0;
}

