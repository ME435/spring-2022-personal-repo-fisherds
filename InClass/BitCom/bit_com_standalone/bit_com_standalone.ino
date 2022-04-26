#define BUZZER_PIN 8

void setup() {
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.println("Led On");
    // Play a tone for 100 mS at a frequency of 440 Hz
    tone(BUZZER_PIN, 440, 100);
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
    Serial.println("Led Off");
    delay(1000);
}
