#include <Arduino.h>
#include "IoT_P00_E01.h"

void setupIoTP00E01(int pin) 
{          
    pinMode(pin, OUTPUT);
}    

void loopIoTP00E01(int pin, int seg) {
    digitalWrite(pin, HIGH);   
    delay(seg * 1000);
                  
    digitalWrite(pin, LOW);    
    delay(seg * 1000);             
}