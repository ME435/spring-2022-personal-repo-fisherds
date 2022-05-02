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


def print_replies(ser):
    time.sleep(0.1)
    while(ser.in_waiting > 0):
        received = ser.readline()
        print("Recieved --> " + received.decode().strip())

def handleLedCommand(ser):
    answer = input("Would you like to turn the LED ON or OFF? [ON OFF] ")
    answer = answer.upper()
    if answer == "ON":
        #  DONE: Send the byte to turn ON the LED
        ser.write((COMMAND_ID_LED | PAYLOAD_LED_ON).to_bytes(1, 'big'))
        print("Sent LED on command")
    elif answer == "OFF":
        #  DONE: Send the byte to turn OFF the LED
        ser.write((COMMAND_ID_LED | PAYLOAD_LED_OFF).to_bytes(1, 'big'))
        print("Sent LED off command")
    else:
        print("No command sent.  Please use ON or OFF next time.")

def handleToneCommand(ser):
    answer = input("Would frequency would like (in Hz)? [120 to 1500] ")
    answer = int(answer)
    print(f"Sent a TONE command with the frequency {answer}")
    play_note(ser, answer)

def play_note(ser, frequency):
    top_4_bits = (frequency >> 8) & 0x0F
    bottom_8_bits = frequency & 0xFF
    ser.write((COMMAND_ID_TONE | top_4_bits).to_bytes(1, 'big'))
    ser.write(bottom_8_bits.to_bytes(1, 'big'))
    time.sleep(0.15)
    
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
    
def main():
    print("Ready")
    # Done: Open the serial port
    ser = serial.Serial("/dev/tty.usbmodem2101")
    print("Connected")
    time.sleep(1.5)
    ser.reset_input_buffer()

    
    
    while True:
        answer = input("Command? [LED TONE SONG] ")
        answer = answer.upper()
        if answer == "LED":
            handleLedCommand(ser)
        elif answer == "TONE":
            handleToneCommand(ser)
        elif answer == "SONG":
            play_song(ser)
        elif answer == "":
            print("Goodbye")
            break
        else:
            print("Please select LED, TONE, or SONG (or leave blank to exit)")
        print_replies(ser)

main()
