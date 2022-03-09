import gpiozero as gz
import time


def servo_sweep():
    servo = gz.Servo(17)

    while True:
        servo.min()
        time.sleep(2)
        print("Min")
        servo.mid()
        time.sleep(2)
        servo.max()
        time.sleep(2)

def main():
    print("Ready")
    servo_sweep()

main()