import serial
import time
# /dev/ttyS0

def main():
    print("Ready")
    # ser = serial.Serial('/dev/ttyS0', baudrate=9600)
    ser = serial.Serial('/dev/serial0', baudrate=9600)
    ser.reset_input_buffer()
    print("Connected")
    time.sleep(1.0)

    while True:
        ser.write(b'hello')
        print("Sent") 
        time.sleep(1.0)
        received = ser.readline()
        time.sleep(1.0)
        print(f"Recevied --> {received}")

main()
