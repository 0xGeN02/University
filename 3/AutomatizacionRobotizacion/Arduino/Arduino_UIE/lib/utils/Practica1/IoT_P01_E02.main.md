```cpp
#include <Arduino.h>
#include "Practica0/IoT_P01_E02.h"

void setup() {
    // Configuración inicial
    pinMode(Pin_V, OUTPUT);
    pinMode(Pin_A, OUTPUT);
    pinMode(Pin_R, OUTPUT);
    Estado_Actual = 'V'; // Estado inicial en verde
}

void loop() {
    LoopIoTP01E02();
}
```