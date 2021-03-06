String inputString = "";
bool stringComplete = false;

void setup() {
  Serial.begin(9600);
  inputString.reserve(200);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (stringComplete) {

    // Simulated PlateLoader!
    if (inputString.equals("RESET")) {
      delay(4);  // simulated PlateLoader delay
      Serial.println("READY, SAGIAN PE LOADER, ROM VER. 1.1.6, 12APR2001");
    } else if (inputString.equals("Z-AXIS EXTEND") || inputString.equals("GRIPPER OPEN")) {
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1);  // simulated PlateLoader delay
      Serial.print("LED on --> ");
      Serial.println(inputString);
    } else if (inputString.equals("Z-AXIS RETRACT") || inputString.equals("GRIPPER CLOSE")) {
      digitalWrite(LED_BUILTIN, LOW);
      delay(1);  // simulated PlateLoader delay
      Serial.print("LED off --> ");
      Serial.println(inputString);
    } else if (inputString.startsWith("MOVE ")) {
      delay(7);  // simulated PlateLoader delay
      Serial.print("(long delay) --> ");
      Serial.println(inputString);
    } else {
      Serial.print("From Arduino --> ");
      delay(0.5);  // simulated PlateLoader delay
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
