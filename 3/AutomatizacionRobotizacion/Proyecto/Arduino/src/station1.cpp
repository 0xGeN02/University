#include <Arduino.h>
#include "station1.h"

int number = 1;

void setup() {
    // Initialize hardware serial
    Serial.begin(9600);
    
    Serial.println("Station 1 running...");
    
    setupStation1();
}

void loop() {
    // Send number to master
    Serial.println(number);
    number++;
    
    loopStation1();
    delay(1000); // Delay to avoid flooding the serial communication
}