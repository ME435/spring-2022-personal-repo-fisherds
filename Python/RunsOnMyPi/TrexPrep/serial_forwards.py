import time
import serial

# From: http://pythonhosted.org/pyserial/

# ser = serial.Serial("/dev/ttyS0", baudrate=9600)
# ser = serial.Serial("/dev/ttyAMA0", baudrate=9600)

# This doesn't crash
# ser = serial.Serial("/dev/tty1", baudrate = 9600, 
#                     parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, 
#                     bytesize=serial.EIGHTBITS, timeout=1)



ser = serial.Serial("/dev/ttyS0", baudrate = 9600, 
                    parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, 
                    bytesize=serial.EIGHTBITS, timeout=1)
print("Connected")
counter = 0
while True:
    counter += 1
    print('Write counter: %d \n' % (counter))
    # ser.write(b'Write counter: %d \n'%(counter))
    ser.write(b'forward\n')
    print("Sent")
    time.sleep(5)
