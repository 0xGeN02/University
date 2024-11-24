#include <Arduino.h>
#include <SoftwareSerial.h>
#include <NewSoftSerial.h>

// Pines de comunicación
#define RX1 5
#define TX1 6
#define RX2 10
#define TX2 11

// SoftwareSerial (si no usas puertos Serial adicionales)
#include <SoftwareSerial.h>
SoftwareSerial station1(TX1, RX1); // TX, RX
SoftwareSerial station2(TX2, RX2); // TX, RX

void setup() {
    // Initialize hardware serial for debugging
    Serial.begin(9600);
    
    // Initialize SoftwareSerial ports
    station1.begin(9600);
    station2.begin(9600);
    
    Serial.println("Master running...");
    
}

void loop() {
    // Listen for data from station 1
    if (station1.available()) {
        String number = station1.readStringUntil('\n');
        Serial.print("Received from Station 1: ");
        Serial.println(number);
        
        // Send the number to station 2
        station2.print(number);
        station2.print('\n');
    }
    
    // Listen for data from station 2
    if (station2.available()) {
        String result = station2.readStringUntil('\n');
        Serial.print("Result from Station 2: ");
        Serial.println(result);
    }
    
}
