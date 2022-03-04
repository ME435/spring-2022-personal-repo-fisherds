
#define DEFAULT_JOINT_1_SERVO_PIN 12
#define DEFAULT_JOINT_2_SERVO_PIN 11
#define DEFAULT_JOINT_3_SERVO_PIN 10
#define DEFAULT_JOINT_4_SERVO_PIN  9
#define DEFAULT_JOINT_5_SERVO_PIN  8
#define DEFAULT_GRIPPER_SERVO_PIN  6

#include <Servo.h>

Servo myservo;
int pos = 0;    // variable to store the servo position

void setup() {
  myservo.attach(DEFAULT_GRIPPER_SERVO_PIN);  // attaches the servo on pin 9 to the servo object
  myservo.write(90);
}

void loop() {
//   for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
//     myservo.write(pos);              // tell servo to go to position in variable 'pos'
//     delay(15);                       // waits 15 ms for the servo to reach the position
//   }
//   for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
//     myservo.write(pos);              // tell servo to go to position in variable 'pos'
//     delay(15);                       // waits 15 ms for the servo to reach the position
//   }
delay(100);
}