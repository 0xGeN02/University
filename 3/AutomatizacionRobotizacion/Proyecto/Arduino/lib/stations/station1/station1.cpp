#include <Arduino.h>
#include "station1.h"

void setupStation1() {
    // Configuración inicial del Arduino en la estación 1
    Serial.begin(9600);
}

void loopStation1() {
    // Lógica principal del Arduino en la estación 1
    Serial.println("Station 1 running...");
    delay(1000);
}