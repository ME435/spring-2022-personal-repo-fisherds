String inputString = "";
bool stringComplete = false;

void setup() {
  Serial.begin(9600);
  inputString.reserve(200);
  pinMode(13, OUTPUT);
}

void loop() {
  if (stringComplete) {
    Serial.println(inputString);
    // TODO: Do something with the ASCII message
    if (inputString.equalsIgnoreCase("ON")) {
        digitalWrite(13, HIGH);
    }
    if (inputString.equalsIgnoreCase("OFF")) {
        digitalWrite(13, LOW);
    }
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}
