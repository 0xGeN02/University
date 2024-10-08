#include "IoT_P01_E03.h"

// Definición de pines
const int Led_V1 = 3;
const int Led_A1 = 5;
const int Led_R1 = 7;
const int Led_V2 = 9;
const int Led_A2 = 11;
const int Led_R2 = 13;



// Definición de estados
char Estado_Actual = '0';

// Implementación de funciones
void setupP01E03(int Led_V1, int Led_A1, int Led_R1, int Led_V2, int Led_A2, int Led_R2) {
    setupLed();
}

void setupLed(){
    pinMode(Led_V1, OUTPUT);
    pinMode(Led_A1, OUTPUT);
    pinMode(Led_R1, OUTPUT);
    pinMode(Led_V2, OUTPUT);
    pinMode(Led_A2, OUTPUT);
    pinMode(Led_R2, OUTPUT);
}

void setupTime(int timeVR, int timeAR, int timeRV, int timeRA) {
    const int tVR = timeVR * 1000; 
    const int tAR = timeAR * 1000; 
    const int tRV = timeRV * 1000; 
    const int tRA = timeRA * 1000;
    
    int timeArr[4] = {tVR, tAR, tRV, tRA};

    return timeArr;
}

void loopP01E03() {
    static unsigned long tiempoInicio = millis();
    unsigned long tiempoActual = millis();

    char F_Transicion(int tiempoActual, int tiempoInicio);
}

char F_Transicion(int tiempoActual, int tiempoInicio) {
        switch (Estado_Actual) {
        case '0':  // Estado Verde-Rojo
            E_VR();  // Llamada a la función del estado
            if (tiempoActual - tiempoInicio >= tVR) {
                Estado_Actual = '1';  // Cambio al siguiente estado
                tiempoInicio = tiempoActual;
            }
            break;

        case '1':  // Estado Amarillo-Rojo
            E_AR();
            if (tiempoActual - tiempoInicio >= tAR) {
                Estado_Actual = '2';
                tiempoInicio = tiempoActual;
            }
            break;

        case '2':  // Estado Rojo-Verde
            E_RV();
            if (tiempoActual - tiempoInicio >= tRV) {
                Estado_Actual = '3';
                tiempoInicio = tiempoActual;
            }
            break;

        case '3':  // Estado Rojo-Amarillo
            E_RA();
            if (tiempoActual - tiempoInicio >= tRA) {
                Estado_Actual = '0';
                tiempoInicio = tiempoActual;
            }
        break;
    }
}
// Definición de las funciones para cada estado
void E_VR() {
    digitalWrite(Led_V1, HIGH);  // Led verde encendido
    digitalWrite(Led_A1, LOW); 
    digitalWrite(Led_R1, LOW);   
    digitalWrite(Led_V2, LOW);   
    digitalWrite(Led_A2, LOW);   
    digitalWrite(Led_R2, HIGH);  // Led rojo encendido
}

void E_AR() {
    digitalWrite(Led_V1, LOW);
    digitalWrite(Led_A1, HIGH);
    digitalWrite(Led_R1, LOW);
    digitalWrite(Led_V2, LOW);
    digitalWrite(Led_A2, LOW);
    digitalWrite(Led_R2, HIGH);
}

void E_RV() {
    digitalWrite(Led_V1, LOW);
    digitalWrite(Led_A1, LOW);
    digitalWrite(Led_R1, HIGH);
    digitalWrite(Led_V2, HIGH);
    digitalWrite(Led_A2, LOW);
    digitalWrite(Led_R2, LOW);
}

void E_RA() {
    digitalWrite(Led_V1, LOW);
    digitalWrite(Led_A1, LOW);
    digitalWrite(Led_R1, HIGH);
    digitalWrite(Led_V2, LOW);
    digitalWrite(Led_A2, HIGH);
    digitalWrite(Led_R2, LOW);
}
