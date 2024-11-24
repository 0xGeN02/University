#include <Arduino.h>

void setup() {
    // Initialize hardware serial
    Serial.begin(9600);
    
    Serial.println("Station 2 running...");
    
}

void loop() {
    // Listen for number from master
    if (Serial.available()) {
        int number = Serial.parseInt();
        int result = number * number;
        
        // Send result back to master
        Serial.print("Calculando: ");
        Serial.println(result);
    }
    
}