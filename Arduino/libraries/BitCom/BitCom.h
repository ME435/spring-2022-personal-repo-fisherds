#ifndef BitCom_h
#define BitCom_h

#include "Arduino.h"

class BitCom
{
  public:
    BitCom();
    // void handleRxByte(byte newRxByte);
    // void registerLedCallback(void (* ledCallback)(uint8_t isLedOn) );
    // void registerToneCallback(void (* toneCallback)(uint16_t frequency) );

    void printDouble(String stringToPrint);
    void flashAndBeep();

  private:
    // char _rxMessageBuffer[10];
    // void (* _ledCallback)(uint8_t isLedOn);
    // void (* _toneCallback)(uint16_t frequency);
};

#endif
