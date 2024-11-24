#include <Arduino.h>

void setup() {
    Serial.begin(9600); // Inicializa la comunicación serial

    // Print de inicio
    Serial.println("Station1 iniciado");
}

void loop() {
    //Print:  enviando number
    for (int i = 1; i <= 10; i++) {
        Serial.print("enviando ");
        Serial.println(i);
        delay(1000); // Espera 1 segundo
    }
}