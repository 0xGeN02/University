#include <Arduino.h>
#include "station2.h"

void setup() {
    // Initialize hardware serial
    Serial.begin(9600);
    
    Serial.println("Station 2 running...");
    
    setupStation2();
}

void loop() {
    // Listen for number from master
    if (Serial.available()) {
        String numberStr = Serial.readStringUntil('\n');
        int number = numberStr.toInt();
        int result = number * number;
        
        // Send result back to master
        Serial.print("Calculating: ");
        Serial.println(result);
    }
    
    loopStation2();
}