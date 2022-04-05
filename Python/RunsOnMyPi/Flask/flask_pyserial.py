from flask import Flask
import serial
import time

app = Flask(__name__)

ser = serial.Serial("/dev/ttyACM1", baudrate = 19200, timeout=10)
print("Connected")
ser.reset_input_buffer()


def wait_for_reply():
    while (ser.in_waiting == 0):
        time.sleep(0.1) # Done to avoid the ser.readline timeout
    received = ser.readline()
    print("Received --> " + received.decode())
    return received.decode()

@app.route('/api/on')
def api_on():
    ser.write(b'Z-AXIS EXTEND\n')
    return wait_for_reply()


@app.route('/api/off')
def api_off():
    ser.write(b'Z-AXIS RETRACT\n')
    return wait_for_reply()


@app.route('/api/move/<from_position>/<to_position>')
def api_move(from_position, to_position):
    ser.reset_input_buffer()
    command = f"MOVE {from_position} {to_position}\n"
    print("Sending",command)
    ser.write(command.encode())
    return wait_for_reply()

@app.route('/api/reset')
def api_reset():
    ser.write(b'RESET\n')
    return wait_for_reply()