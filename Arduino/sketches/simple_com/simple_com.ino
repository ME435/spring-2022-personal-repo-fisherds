String inputString = "";
bool stringComplete = false;

void setup() {
  Serial.begin(9600);
  inputString.reserve(200);
}

void loop() {
  if (stringComplete) {
    Serial.print("From Arduino --> ");
    Serial.println(inputString);

    // TODO: Do something real with the message!

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
