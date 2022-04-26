#include "MyLibrary.h"

MyLibrary myLibrary;

int result;

void setup() {
    Serial.begin(9600);
    myLibrary.repeater("Hello");
    result = myLibrary.doubler(17);
    Serial.println(result);
}

void loop() {
    delay(100);
}