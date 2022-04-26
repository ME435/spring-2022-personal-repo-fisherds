#include "Arduino.h"
#include "BitCom.h"

BitCom::BitCom() {
	// _nextOpenByteInMessageBuffer = 0;
	// _ledCallback = NULL;
	// _toneCallback = NULL;
}

/**
 * Handle a newly received byte.
 */
// void BitCom::handleRxByte(byte newRxByte) {

// }

// void BitCom::registerLedCallback(void (*ledCallback)(uint8_t isLedOn)) {
// 	_ledCallback = ledCallback;
// }

// void BitCom::registerToneCallback(void (*toneCallback)(uint16_t frequency)) {
// 	_toneCallback = toneCallback;
// }

void BitCom::printDouble(String stringToPrint) {
	Serial.print(stringToPrint);
	Serial.print(" ");
	Serial.println(stringToPrint);
}

void BitCom::flashAndBeep() {
	digitalWrite(LED_BUILTIN, HIGH);
    Serial.println("Led On");
    // Play a tone for 100 mS at a frequency of 440 Hz
    tone(8, 440, 100);
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
    Serial.println("Led Off");
    delay(1000);
}
