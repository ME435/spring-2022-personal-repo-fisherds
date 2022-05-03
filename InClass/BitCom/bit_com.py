import serial
import time

COMMAND_ID_LED = 0x10
COMMAND_ID_TONE = 0x20

PAYLOAD_LED_OFF = 0x00
PAYLOAD_LED_ON = 0x01

#https://www.tutorialspoint.com/arduino/arduino_tone_library.htm
NOTE_C4 = 262
NOTE_D4 = 294
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_G4 = 392

class BitCom:
    def __init__(self, serial_port_name="/dev/tty.usbmodem2101", timeout=5):
        self.ser = serial.Serial(serial_port_name)
        print("Connected")
        time.sleep(1.5)
        self.ser.reset_input_buffer()
    
    def send_led_on(self):
        self.ser.write((COMMAND_ID_LED | PAYLOAD_LED_ON).to_bytes(1, 'big'))

    def send_led_off(self):
        self.ser.write((COMMAND_ID_LED | PAYLOAD_LED_OFF).to_bytes(1, 'big'))

    def send_tone(self, frequency):
        top_4_bits = (frequency >> 8) & 0x0F
        bottom_8_bits = frequency & 0xFF
        self.ser.write((COMMAND_ID_TONE | top_4_bits).to_bytes(1, 'big'))
        self.ser.write(bottom_8_bits.to_bytes(1, 'big'))
        time.sleep(0.15)
    
    def play_mary(self):
        self.send_tone(NOTE_C4)
        self.send_tone(NOTE_D4)
        self.send_tone(NOTE_C4)
        self.send_tone(NOTE_D4)

        self.send_tone(NOTE_E4)
        self.send_tone(NOTE_E4)
        self.send_tone(NOTE_E4)
        time.sleep(0.1)

        self.send_tone(NOTE_D4)
        self.send_tone(NOTE_D4)
        self.send_tone(NOTE_D4)
        time.sleep(0.1)

        self.send_tone(NOTE_E4)
        self.send_tone(NOTE_G4)
        self.send_tone(NOTE_G4)
        time.sleep(0.1)

        self.send_tone(NOTE_C4)
        self.send_tone(NOTE_D4)
        self.send_tone(NOTE_C4)
        self.send_tone(NOTE_D4)

        self.send_tone(NOTE_E4)
        self.send_tone(NOTE_E4)
        self.send_tone(NOTE_E4)
        self.send_tone(NOTE_E4)

        self.send_tone(NOTE_D4)
        self.send_tone(NOTE_D4)

        self.send_tone(NOTE_E4)
        self.send_tone(NOTE_D4)
        self.send_tone(NOTE_C4)

    def print_replies(self):
        time.sleep(0.1)
        while(self.ser.in_waiting > 0):
            received = self.ser.readline()
            print("Received --> " + received.decode().strip())
