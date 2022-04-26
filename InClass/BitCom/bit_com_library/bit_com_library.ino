#include <BitCom.h>

BitCom bitCom;

void setup() {
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);
    bitCom.printDouble("Hello World");
}

void loop() {
    bitCom.flashAndBeep();
}