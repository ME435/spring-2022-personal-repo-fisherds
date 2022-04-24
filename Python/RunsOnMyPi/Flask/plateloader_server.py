from flask import Flask
import serial
import time

app = Flask(__name__)

# ser = serial.Serial("/dev/ttyACM1", baudrate = 19200, timeout=10)
ser = serial.Serial("/dev/ttyUSB0", baudrate = 19200, timeout=30)

print("Connected")
ser.reset_input_buffer()

def wait_for_reply():
    while (ser.in_waiting == 0):
        time.sleep(0.1) # Done to avoid the ser.readline timeout
    received = ser.readline()
    print("Received --> " + received.decode())
    return received.decode()

@app.route('/api/<command>')
def api_move(command):
    command = command.upper() + "\n"
    ser.reset_input_buffer()
    print("Sending", command)
    ser.write(command.encode())
    return wait_for_reply()
