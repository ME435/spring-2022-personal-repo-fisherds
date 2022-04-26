#include "Arduino.h"
#include "MyLibrary.h"

/**
 * Constructor
 * Uses the default pin numbers as servo pin numbers.
 */
MyLibrary::MyLibrary() {
	Serial.println("Created a MyLibrary object");
}

/**
 * Constructor
 * Uses pin numbers given to determine servo pin numbers.
 */
void MyLibrary::repeater(String msg) {
	Serial.print(msg);
	Serial.println(msg);
}

/**
 * Perform initialization work as needed.
 * Called by all constructors for common work during instantiation.
 */
int MyLibrary::doubler(int x) {
    return 2 * x;
}
