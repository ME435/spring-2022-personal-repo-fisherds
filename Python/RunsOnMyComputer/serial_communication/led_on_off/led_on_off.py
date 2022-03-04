import time
from urllib import response
import serial

def toggle(ser):
    counter = 0
    while True:
        counter += 1
        if counter % 2 == 0:
            print(f"Sent     --> ON")
            ser.write(b'ON\n')
        else:
            print(f"Sent     --> OFF")
            ser.write(b'OFF\n')
        
        time.sleep(0.1)
        if (ser.in_waiting > 0):
            response = ser.readline()
            print("Received --> " + str(response))
        

        time.sleep(2)

def ask_user(ser):
    while True:
        answer = input("Would you like to turn ON or OFF the LED? ")
        answer = answer.upper()
        if answer == "ON":
            ser.write(b'ON\n')
        elif answer == "OFF":
            ser.write(b'OFF\n')
        elif answer == "":
            print("Goodbye")
            break
        else:
            print("Please answer ON or OFF next time.")


def main():
    ser = serial.Serial("/dev/tty.usbmodem1131401", baudrate = 9600, 
                        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, 
                        bytesize=serial.EIGHTBITS, timeout=1)
    print("Connected")
    ser.reset_input_buffer()
    time.sleep(1)

    # toggle(ser)
    ask_user(ser)


main()