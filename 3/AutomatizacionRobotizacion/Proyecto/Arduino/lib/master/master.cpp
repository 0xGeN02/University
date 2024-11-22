#include <Arduino.h>
#include "master.h"

void setupMaster() {
    // Configuración inicial del Arduino master
    Serial.begin(9600);
}

void loopMaster() {
    // Lógica principal del Arduino master
    Serial.println("Master running...");
    delay(1000);
}