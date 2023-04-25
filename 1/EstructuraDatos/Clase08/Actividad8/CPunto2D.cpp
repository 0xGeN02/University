#include "CPunto2D.h"
//Declaraciones de los métodos de la clase
// Constructores
Punto2D::Punto2D() {
this->x = 0.0; 
this->y = 0.0;
}
Punto2D::Punto2D(float x, float y) {
this->x = x;
this->y = y;
}
// Seters
void Punto2D::setX(float x){
this->x = x;
}
void Punto2D::setY(float y){
this->y = y;
}
//Geters
float Punto2D::getX(){
    return this->x;
}
float Punto2D::getY(){
    return this->y;
}
// Entrada
void Punto2D::Leer_Punto(){
cout<<"Indique coordenada x : ";
cin>>this->x;
cout<<"Indique ordenada   y : ";
cin>>this->y;
}

//Mostrar Punto
void Punto2D::Mostrar_Punto(int num_punto) {
    cout << fixed << setprecision(2) << "Punto "<< num_punto <<" =[" << x << "," << y << "]" << endl;
}

//Cuandrante
void Punto2D::Cuadrante(int num_punto){
    if(x>0 && y>0){
        cout << "El Punto " << "" << num_punto << "" << " se encuentra en el Cuadrante 1" << endl;
    }
    else if (x<0 && y<0){
        cout << "El Punto " << "" << num_punto << "" << " se encuentra en el Cuadrante 3" << endl;
    }
    else if (x>0 && y<0){
        cout << "El Punto " << "" << num_punto << "" << " se encuentra en el Cuadrante 4" << endl;
    }
    else if(x>0 || y>0){
        cout << "El Punto " << "" << num_punto << "" << " se encuentra en el Cuadrante 2" << endl;
    }
    else{
        cout << "El Punto " << "" << num_punto << "" << " se encuentra en Ningún Cuadrante" << endl;
    }    
}

//Distancia Punto-Punto2D
void Punto2D::DistanciaP_2P(int num_punto){
    float punto;
    cout << "Ingrese el punto de 1 dimension: ";
    cin >> punto;
    for(int i = 0; i < num_punto; i++){
        float Prod_Vect_2D =  sqrt(pow(x,2)+ pow(y,2));
        float Prod_Vect_1D = sqrt(pow(punto, 2));
        if(Prod_Vect_1D > Prod_Vect_2D){
            float Distancia_Vect = Prod_Vect_1D - Prod_Vect_2D;
            cout << "La disntancia entre el punto y el punto2D es :" << "" << Distancia_Vect << endl;
        }
        else{
            float Distancia_Vect = Prod_Vect_2D - Prod_Vect_1D;
            cout << "La disntancia entre el punto y el punto2D es :" << "" << Distancia_Vect << endl;
        } 
    }
}