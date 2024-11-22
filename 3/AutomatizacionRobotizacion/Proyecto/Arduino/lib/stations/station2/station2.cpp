#include <Arduino.h>
#include "station2.h"

void setupStation2() {
    // Configuración inicial del Arduino en la estación 2
    Serial.begin(9600);
}

void loopStation2() {
    // Lógica principal del Arduino en la estación 2
    Serial.println("Station 2 running...");
    delay(1000);
}