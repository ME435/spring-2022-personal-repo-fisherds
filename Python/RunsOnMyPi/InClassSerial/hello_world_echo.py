import serial
import time
# /dev/ttyS0

def main():
    print("Ready")
    # ser = serial.Serial('/dev/ttyS0', baudrate=9600)
    ser = serial.Serial('/dev/ttyACM0', baudrate=9600)
    # ser = serial.Serial('/dev/tty.usbmodem2101', baudrate=9600)
    ser.reset_input_buffer()
    print("Connected")
    time.sleep(1.0)
    counter = 0 
    while True:
        counter += 1
        ser.write(b'count = %d\n' % counter)
        print("Sent") 
        time.sleep(1.0)

        time.sleep(0.1)
        while (ser.in_waiting > 0):
            received = ser.readline()
            print(f"Received --> {received.decode().strip()}")

main()
