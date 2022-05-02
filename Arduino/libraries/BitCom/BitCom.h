#ifndef BitCom_h
#define BitCom_h

#include "Arduino.h"

#define COMMAND_ID_LED 0x10
#define COMMAND_ID_TONE 0x20

#define PAYLOAD_LED_OFF 0x00
#define PAYLOAD_LED_ON 0x01

class BitCom {
  public:
    BitCom();
    void handleRxByte(byte newRxByte);
    void registerLedCallback(void (* ledCallback)(uint8_t isLedOn) );
    void registerToneCallback(void (* toneCallback)(uint16_t frequency) );

    void printDouble(String stringToPrint);
    void flashAndBeep();

  private:
    void (* _ledCallback)(uint8_t isLedOn);
    void (* _toneCallback)(uint16_t frequency);

    bool _lastByteWasToneCommand = false;
    uint16_t _frequency = 0;
};

#endif
