// Special protocol bytes
#define START_BYTE 0x7E
#define ESCAPE_BYTE 0x7D
#define ESCAPE_XOR 0x20

#define COMMAND_ID_NUMBER 0x01
#define COMMAND_ID_STRING 0x02

byte inputBuffer[200];
uint8_t nextAvailableInputBufferIndex = 0;
int8_t bytesRemainingInMessage = -1;  // Unknown

bool lastByteWasStartByte = false;
bool lastByteWasEscapeByte = false;
uint8_t crc = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  delay(100);
}

void parseValidMessage() {
  Serial.print("Recieved a valid message for team ");
  byte teamNumber = inputBuffer[0];
  Serial.println(teamNumber);
  byte commandId = inputBuffer[1];
  if(commandId == COMMAND_ID_STRING) {
      Serial.print("STRING --> ");
      String receivedString = String((char*)(inputBuffer + 2));
      Serial.println(receivedString);
  }
  if(commandId == COMMAND_ID_NUMBER) {
      Serial.print("NUMBER --> ");
      int32_t num = inputBuffer[2];
      num = (num << 8) | inputBuffer[3];
      num = (num << 8) | inputBuffer[4];
      num = (num << 8) | inputBuffer[5];
      Serial.println(num);
  }
}

void serialEvent() {
  while (Serial.available()) {
    byte inByte = Serial.read();
    Serial.print("inByte --> ");
    Serial.println(inByte, HEX);
    // Highest priority is the start byte.
    if (inByte == START_BYTE) {
      lastByteWasStartByte = true;
      lastByteWasEscapeByte = false;
      Serial.println("Found start byte");
      return;
    }

    // Make sure we are expecting bytes or the prior byte was the start byte
    if (!lastByteWasStartByte && bytesRemainingInMessage < 0) {
      // This is an unexpected byte
      Serial.println("Unexpected byte! No bytes remaining!");
      return;
    }

    // Handle the escape byte
    if (!lastByteWasEscapeByte && inByte == ESCAPE_BYTE) {
      lastByteWasEscapeByte = true;
      Serial.println("Found an escape byte");
      return;
    }

    // Handle escapes
    if (lastByteWasEscapeByte) {
      Serial.print("Escaped this byte.  Was ");
      Serial.print(inByte, HEX);
      inByte ^= ESCAPE_XOR;
      Serial.print(" is now ");
      Serial.println(inByte, HEX);
    }
    lastByteWasEscapeByte = false;

    // Handle length byte
    if (lastByteWasStartByte) {
      bytesRemainingInMessage = inByte;
      crc = 0;
      nextAvailableInputBufferIndex = 0;
      lastByteWasStartByte = false;
      Serial.print("Got the legth as");
      Serial.println(bytesRemainingInMessage);
      return;
    }

    // Handle normal bytes
    crc += inByte;
    if (bytesRemainingInMessage > 0) {
      inputBuffer[nextAvailableInputBufferIndex] = inByte;
      nextAvailableInputBufferIndex++;
    } else {
      if (crc == 0) {
        parseValidMessage();
      } else {
        Serial.println("Failed the CRC check.");
      }
       
    }
    bytesRemainingInMessage--;
  }
}