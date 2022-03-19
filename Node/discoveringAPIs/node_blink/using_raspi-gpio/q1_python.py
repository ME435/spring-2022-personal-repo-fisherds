import gpiozero as gz
import time
import signal

def handle_servo_move(angle, servo, led):
    print("Run servo to ", angle)
    servo.angle = angle
    led.on()
    time.sleep(1)
    led.off()

def main():
    print("Ready")
    led = gz.LED(14)
    button_22 = gz.Button(22)
    button_23 = gz.Button(23)
    button_25 = gz.Button(25)
    servo = gz.AngularServo(17, min_angle=-90, max_angle=90)
    button_22.when_pressed = lambda : handle_servo_move(-90, servo, led)
    button_23.when_pressed = lambda : handle_servo_move(0, servo, led)
    button_25.when_pressed = lambda : handle_servo_move(90, servo, led)

    signal.pause()


main()