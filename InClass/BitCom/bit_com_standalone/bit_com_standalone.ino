#define COMMAND_ID_LED 0x10
#define COMMAND_ID_TONE 0x20

#define PAYLOAD_LED_OFF 0x00
#define PAYLOAD_LED_ON 0x01


#define BUZZER_PIN 8

uint16_t frequency = 0;
bool lastByteWasToneCommand = false;


void setup() {
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    // For testing the LED and buzzer only...

    // digitalWrite(LED_BUILTIN, HIGH);
    // Serial.println("Led On");
    // // Play a tone for 100 mS at a frequency of 440 Hz
    // tone(BUZZER_PIN, 440, 100);
    // delay(1000);
    // digitalWrite(LED_BUILTIN, LOW);
    // Serial.println("Led Off");
    // delay(1000);
}

void serialEvent() {
    while (Serial.available()) {
        byte newRxByte = Serial.read();
        Serial.print("newRxByte --> ");
        Serial.println(newRxByte, HEX);

        if (lastByteWasToneCommand) {
            // We are expecting the next 8 bits of the tone payload
            frequency = frequency | newRxByte;
            tone(BUZZER_PIN, frequency, 100);
            Serial.print("Playing tone @ frequency ");
            Serial.println(frequency);
            lastByteWasToneCommand = false;
            continue;
        }

        if ((newRxByte & 0xF0) == COMMAND_ID_LED) {
            if ((newRxByte & 0x0F) == PAYLOAD_LED_ON) {
                // digitalWrite(LED_BUILTIN, HIGH);
                Serial.println("Turning the LED on!");
            } else if ((newRxByte & 0x0F) == PAYLOAD_LED_OFF) {
                // digitalWrite(LED_BUILTIN, LOW);
                Serial.println("Turning the LED off!");
            }

            digitalWrite(LED_BUILTIN, newRxByte & 0x0F);
            continue;
        }

        if ((newRxByte & 0xF0) == COMMAND_ID_TONE) {
            lastByteWasToneCommand = true;
            frequency = newRxByte & 0x0F;
            frequency = frequency << 8;
            continue;
        }
        Serial.println("Your byte was NOT handled!");
    }
}
