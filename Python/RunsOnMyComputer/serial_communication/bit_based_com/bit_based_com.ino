// Special protocol bytes
#define START_BYTE 0x7E
#define ESCAPE_BYTE 0x7D
#define ESCAPE_XOR 0x20

byte inputBuffer[10];
uint8_t inputBufferIndex = 0;
int8_t bytesRemainingInMessage = -1; // Unknown
bool messageComplete = false;

bool lastByteWasStartByte = false;
bool lastByteWasEscapeByte = false;

void setup() {
  Serial.begin(9600);
}

void loop() {
}

void serialEvent() {
  while (Serial.available()) {
    byte inByte = Serial.read();
    if (inByte == START_BYTE) {
      inputBufferIndex = 0;  // Start of a new message
      lengthRemaining = -1;  // Unknown

      lastByteWasStartByte = false;
      lastByteWasEscapeByte = false;
    } else {
      inputBuffer
    }
  }
}