import time
import serial

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

def handle_led_command(ser):
    answer = input("Would you like to turn ON or OFF the LED? ")
    answer = answer.upper()
    if answer == "ON":
        ser.write((COMMAND_ID_LED | PAYLOAD_LED_ON).to_bytes(1, 'big'))
        print("Sent LED On command")
    elif answer == "OFF":
        ser.write((COMMAND_ID_LED | PAYLOAD_LED_OFF).to_bytes(1, 'big'))
        print("Sent LED Off command")
    else:
        print("No LED command sent, please answer ON or OFF next time")


def handle_tone_command(ser):
    answer = input("Would frequency would you like (120 Hz to 1500 Hz as an int)? ")
    answer = int(answer)
    print(f"Playing tone {answer}")
    play_note(ser, answer)

def play_song(ser):
    play_note(ser, NOTE_E4)
    play_note(ser, NOTE_D4)
    play_note(ser, NOTE_C4)
    play_note(ser, NOTE_D4)

    play_note(ser, NOTE_E4)
    play_note(ser, NOTE_E4)
    play_note(ser, NOTE_E4)
    time.sleep(0.1)

    play_note(ser, NOTE_D4)
    play_note(ser, NOTE_D4)
    play_note(ser, NOTE_D4)
    time.sleep(0.1)

    play_note(ser, NOTE_E4)
    play_note(ser, NOTE_G4)
    play_note(ser, NOTE_G4)
    time.sleep(0.1)

def play_note(ser, frequency):
    top_4_bits = (frequency >> 8) & 0x03
    bottom_8_bits = frequency & 0xFF
    ser.write((COMMAND_ID_TONE | top_4_bits).to_bytes(1, 'big'))
    ser.write((bottom_8_bits).to_bytes(1, 'big'))
    time.sleep(0.1)

def print_replies(ser):
    time.sleep(0.1)
    while (ser.in_waiting > 0):
        received = ser.readline()
        print("Received --> " + str(received))

def main():
    ser = serial.Serial("/dev/tty.usbmodem1201", baudrate = 9600, 
                        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, 
                        bytesize=serial.EIGHTBITS, timeout=1)
    print("Connected")
    ser.reset_input_buffer()
    time.sleep(0.1)

    while True:
        answer = input("What command would you like to send? [LED TONE SONG] ")
        answer = answer.upper()
        if answer == "LED":
            # ser.write((COMMAND_ID_LED | PAYLOAD_LED_ON).to_bytes(1, 'big'))
            handle_led_command(ser)
        elif answer == "TONE":
            # ser.write((COMMAND_ID_LED | PAYLOAD_LED_OFF).to_bytes(1, 'big'))
            handle_tone_command(ser)
        elif answer == "SONG":
            play_song(ser)
        elif answer == "":
            print("Goodbye")
            break
        else:
            print("Please answer LED or TONE next time.")
        print_replies(ser)


main()