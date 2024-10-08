```cpp
#include <Arduino.h>
#include "IoT_P00_E01.h"

int pin = 10
int seg = 1

void setup() {
  setupIoTP00E01(pin);
}

void loop() {
  loopIoTP00E01(pin, seg);
}
```