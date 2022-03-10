import gpiozero as gz
import time

def main():
    print("Ready to blink via main")
    my_led = gz.LED(18)

    while True:
        my_led.on()
        # print("The LED should be on")
        time.sleep(1)
        my_led.off()
        # print("The LED should be off")
        time.sleep(1)



main()
