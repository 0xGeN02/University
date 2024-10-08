#ifndef P01E03_H
#define P01E03_H

#include <Arduino.h>

//Definicion leds de los semaforos
extern const int Led_V1; //LED Verde 1
extern const int Led_V2; //LED Verde 2

extern const int Led_A1; //LED Amarillo 1
extern const int Led_A2; //LED Amarillo 2

extern const int Led_R1; //LED Rojo 1
extern const int Led_R2; //LED Rojo 2

//Definicion de tiempos de los eventos(ms)
extern const unsigned long tVR;
extern const unsigned long tAR;
extern const unsigned long tRV;
extern const unsigned long tRA;

//Definicion de estados
extern char Estado_Actual; // Estado del Sistema

//Definicion de prototipos de rutinas
void setupP01E03();
void loopP01E03();
char F_Transicion(int tiempoActual, int tiempoInicio);
void E_VR();
void E_AR();
void E_RV();
void E_RA();

#endif // P01E03_H