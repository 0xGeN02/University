#include <Arduino.h>
#include <SoftwareSerial.h>
#include "master.h"

// Define the pins for SoftwareSerial
SoftwareSerial station1Serial(10, 11); // RX, TX
SoftwareSerial station2Serial(12, 13); // RX, TX

void setup() {
    // Initialize hardware serial for debugging
    Serial.begin(9600);
    
    // Initialize SoftwareSerial ports
    station1Serial.begin(9600);
    station2Serial.begin(9600);
    
    Serial.println("Master running...");
    
    setupMaster();
}

void loop() {
    // Listen for data from station 1
    if (station1Serial.available()) {
        String number = station1Serial.readStringUntil('\n');
        Serial.print("Received from Station 1: ");
        Serial.println(number);
        
        // Send the number to station 2
        station2Serial.print(number);
        station2Serial.print('\n');
    }
    
    // Listen for data from station 2
    if (station2Serial.available()) {
        String result = station2Serial.readStringUntil('\n');
        Serial.print("Result from Station 2: ");
        Serial.println(result);
    }
    
    loopMaster();
}