String inputString = "";
bool stringComplete = false;

void setup() {
  Serial.begin(9600);
  inputString.reserve(200);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (stringComplete) {

    // TODO: Do something real with the message!
    if (inputString.equalsIgnoreCase("ON")) {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("The LED is now on!");
    } else if (inputString.equalsIgnoreCase("OFF")) {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("The LED is now off!");
    } else {
      Serial.print("From Arduino --> ");
      Serial.println(inputString);
    }

    // clear the string:
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
