#define COMMAND_ID_LED 0x10
#define COMMAND_ID_TONE 0x20

#define PAYLOAD_LED_OFF 0x00
#define PAYLOAD_LED_ON 0x01

#define TONE_PIN 8
#define LED_PIN 13

bool lastByteWasToneCommand = false;
uint16_t toneFrequency = 0x0000;  // 16 bits

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  pinMode(TONE_PIN, OUTPUT);
}

void loop() {
  delay(10);
}

void serialEvent() {
  while (Serial.available()) {
    byte inByte = Serial.read();
    Serial.print("Received --> ");
    Serial.println(inByte, HEX);
    if (lastByteWasToneCommand) {
      toneFrequency = toneFrequency << 8 | inByte;
      tone(TONE_PIN, toneFrequency, 100);
      Serial.print("Playing tone ");
      Serial.println(toneFrequency);
      lastByteWasToneCommand = false;
      return;
    }
    if ((inByte & 0xF0) == COMMAND_ID_LED) {
      if ((inByte & 0x0F) == PAYLOAD_LED_OFF) {
        digitalWrite(LED_PIN, LOW);
        Serial.println("LED OFF");
        return;
      }
      if ((inByte & 0x0F) == PAYLOAD_LED_ON) {
        digitalWrite(LED_PIN, HIGH);
        Serial.println("LED ON");
        return;
      }
    }
    if ((inByte & 0xF0) == COMMAND_ID_TONE) {
      toneFrequency = inByte & 0x0F; // Keep only the bottom 4 bits
      lastByteWasToneCommand = true;
      return;
    }
    Serial.println("Your message wasn't handled!");
  }
}