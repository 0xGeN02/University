```cpp
#include <Arduino.h>
#include "IoT_P01_E01.h"

int Pin_Led = 10;
int Seg = 1;

void setup() {
    pinMode(Pin_Led, OUTPUT);
}

void loop() {

    PARPADEO(Pin_Led, Seg);
}
```