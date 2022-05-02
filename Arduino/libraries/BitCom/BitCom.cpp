#include "BitCom.h"

#include "Arduino.h"

BitCom::BitCom() {
  _ledCallback = NULL;
  _toneCallback = NULL;
  _lastByteWasToneCommand = false;
  _frequency = 0;
}

/**
 * Handle a newly received byte.
 */
void BitCom::handleRxByte(byte newRxByte) {
  // TODO: Remove these debug lines, once everything works.
  Serial.print("newRxByte --> ");
  Serial.println(newRxByte, HEX);

  if (_lastByteWasToneCommand) {
    _frequency = _frequency | newRxByte;
    if (_toneCallback != NULL) {
      _toneCallback(_frequency);
    }
    _lastByteWasToneCommand = false;
    return;
  }

  if ((newRxByte & 0xF0) == COMMAND_ID_LED) {
    if (_ledCallback != NULL) {
        _ledCallback(newRxByte & 0x0F);
    }
    return;
  }

  if ((newRxByte & 0xF0) == COMMAND_ID_TONE) {
    _lastByteWasToneCommand = true;
    _frequency = newRxByte & 0x0F;
    _frequency = _frequency << 8;
    return;
  }
  Serial.println("Your byte was NOT handled!");
}

void BitCom::registerLedCallback(void (*ledCallback)(uint8_t isLedOn)) {
  _ledCallback = ledCallback;
}

void BitCom::registerToneCallback(void (*toneCallback)(uint16_t frequency)) {
  _toneCallback = toneCallback;
}

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
