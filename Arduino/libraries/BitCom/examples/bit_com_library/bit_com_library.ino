#include <BitCom.h>

BitCom bitCom;

#define BUZZER_PIN 8

void setup() {
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);
    pinMode(BUZZER_PIN, OUTPUT);
    // bitCom.printDouble("Hello World");

    // Register callbacks
    bitCom.registerLedCallback(myLedCallback);
    bitCom.registerToneCallback(myToneCallback);
}

void myLedCallback(uint8_t isLedOn) {
    Serial.print("Set the LED to ");
    Serial.println(isLedOn);
    digitalWrite(LED_BUILTIN, isLedOn);
}

void myToneCallback(uint16_t frequency) {
    tone(BUZZER_PIN, frequency, 100);
    Serial.print("Playing tone @ frequency ");
    Serial.println(frequency);
}

void loop() {
    // bitCom.flashAndBeep();

}

void serialEvent() {
    while(Serial.available()) {
        byte newByte = Serial.read();
        bitCom.handleRxByte(newByte);
    }
}