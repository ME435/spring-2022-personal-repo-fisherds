import time
import serial

# ser = serial.Serial("/dev/ttyS0", baudrate = 9600, 
#                     parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, 
#                     bytesize=serial.EIGHTBITS, timeout=1)


# ser = serial.Serial("/dev/ttyS0", baudrate = 9600)
ser = serial.Serial("/dev/tty.usbmodem2101", baudrate = 9600)


print("Connected")
ser.reset_input_buffer()
time.sleep(1)

counter = 0
while True:
    counter += 1
    print(f"Sent     --> {b'Write counter: %d' % (counter)}")
    ser.write(b'Write counter: %d\n'%(counter))
    
    time.sleep(0.1)
    while (ser.in_waiting > 0):
        received = ser.readline()
        print("Received --> " + str(received))
    

    time.sleep(3)
