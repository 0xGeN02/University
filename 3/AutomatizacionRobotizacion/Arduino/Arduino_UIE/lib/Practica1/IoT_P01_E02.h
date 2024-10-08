#ifndef IOT_P01_E02_H
#define IOT_P01_E02_H

#include <Arduino.h>

// Definición de variables y constantes
extern const int Pin_V;  // Pin conectado a verde
extern const int Pin_A;  // Pin conectado a amarillo
extern const int Pin_R;  // Pin conectado a Rojo
extern const int tv;     // Evento tiempo en verde    segundos
extern const int ta;     // Evento tiempo en amarillo segundos
extern const int tr;     // Evento tiempo en rojo     segundos
extern char Estado_Actual; // Estado del Sistema
extern int Next_t;       // Próximo tiempo de permanencia en el estado actual

// Definición de prototipos de rutinas
char F_Transicion(char estado, int t, int tv, int ta, int tr, int pinV, int pinA, int pinR);
void E_Verde();
void E_Amarillo();
void E_Rojo();

#endif // IOT_P01_E02_H