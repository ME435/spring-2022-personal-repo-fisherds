import serial
import time
# /dev/ttyS0

def main():
    print("Ready")
    # ser = serial.Serial('/dev/ttyS0', baudrate=9600)
    ser = serial.Serial('/dev/tty.usbmodem2101', baudrate=9600)
    ser.reset_input_buffer()
    print("Connected")
    time.sleep(1.0)

    while True:
        ser.write(b'hello\n')
        print("Sent") 
        time.sleep(1.0)

        time.sleep(0.1)
        while (ser.in_waiting > 0):
            received = ser.readline()
            print("Received --> " + str(received))

main()
