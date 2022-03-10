import gpiozero as gz
import time

def main():
    print("Ready")
    servo = gz.AngularServo(17, min_angle=-90, max_angle=90)

    while True:
        angle_str = input("What angle would you like? ")
        if angle_str == "":
            print("Goodbye")
            break
        servo.angle = int(angle_str)
        
        # servo.angle = -90
        # time.sleep(2)
        # servo.angle = -45
        # time.sleep(2)
        # servo.angle = 0
        # time.sleep(2)
        # servo.angle = 45
        # time.sleep(2)
        # servo.angle = 90
        # time.sleep(2)


main()


