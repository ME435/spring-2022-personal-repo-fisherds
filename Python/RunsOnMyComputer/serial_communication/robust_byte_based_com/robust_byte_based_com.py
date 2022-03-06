import time
import serial

START_BYTE = 0x7E
ESCAPE_BYTE = 0x7D
ESCAPE_XOR = 0x20

COMMAND_ID_NUMBER = 0x01
COMMAND_ID_STRING = 0x02

def handle_string_command(ser):
    answer = input("What string would you like to send? ")
    ser.write(START_BYTE.to_bytes(1, 'big'))
    ser.write((len(answer) + 2).to_bytes(1, 'big'))  # Length is string length plus 2
    ser.write((33).to_bytes(1, 'big')) # Team 33
    ser.write(COMMAND_ID_STRING.to_bytes(1, 'big')); # 2
    crc = - 33 - 2

    for one_byte in answer.encode():
        crc -= one_byte
        if one_byte == START_BYTE or one_byte == ESCAPE_BYTE:
            ser.write(ESCAPE_BYTE.to_bytes(1, 'big'))
            one_byte = one_byte ^ ESCAPE_XOR
        ser.write(one_byte.to_bytes(1, 'big'))
    crc = crc % 256
    ser.write(crc.to_bytes(1, 'big'))


    # Normal
    # ser.write(START_BYTE.to_bytes(1, 'big'))
    # ser.write((10).to_bytes(1, 'big'))  # Length is 10
    # ser.write((33).to_bytes(1, 'big')) # Team 33
    # ser.write(COMMAND_ID_STRING.to_bytes(1, 'big')); # 2
    # ser.write("P0P0P0P0".encode())         # 0x30 0x50 (repeated 4 times)
    # ser.write((256 - 33 - 2).to_bytes(1, 'big'))  # CRC is 256 - TeamNumber - Command

def handle_number_command(ser):
    answer = input("What 32 bit number would you like to send? ")
    # Hints on fun numbers to send:
    # 126 - the start byte which needs escaping
    # 125 - the escape byte which needs escaping
    # 116 - causes crc to be the start byte which needs escaping
    # 117 - causes crc to be the escape byte which needs escaping
    # 32 - the XOR byte which should NOT be escaped
    answer = int(answer)
    ser.write(START_BYTE.to_bytes(1, 'big'))
    ser.write((6).to_bytes(1, 'big'))  # Length is 6
    ser.write((44).to_bytes(1, 'big')) # Team 44
    ser.write(COMMAND_ID_NUMBER.to_bytes(1, 'big')); # 1
    crc = - 44 - 1
    for one_byte in answer.to_bytes(4, 'big'):
        crc -= one_byte
        if one_byte == START_BYTE or one_byte == ESCAPE_BYTE:
            ser.write(ESCAPE_BYTE.to_bytes(1, 'big'))
            one_byte = one_byte ^ ESCAPE_XOR
        ser.write(one_byte.to_bytes(1, 'big'))
    crc = crc % 256
    ser.write(crc.to_bytes(1, 'big'))

    # Normal number
    # ser.write(START_BYTE.to_bytes(1, 'big'))
    # ser.write((6).to_bytes(1, 'big'))  # Length is 6
    # ser.write((44).to_bytes(1, 'big')) # Team 44
    # ser.write(COMMAND_ID_NUMBER.to_bytes(1, 'big')); # 1
    # ser.write((84215045).to_bytes(4, 'big'))         # 0x05 0x05 0x05 0x05
    # ser.write((256 - 44 - 1 - 20).to_bytes(1, 'big'))  # CRC

    # Sending the start byte via an escape
    # ser.write(START_BYTE.to_bytes(1, 'big'))
    # ser.write((6).to_bytes(1, 'big'))  # Length is 6
    # ser.write((44).to_bytes(1, 'big')) # Team 44
    # ser.write(COMMAND_ID_NUMBER.to_bytes(1, 'big')) # 1
    # # ser.write((START_BYTE).to_bytes(4, 'big'))         # 0x00 0x00 0x00 0x7E --> escaped...
    # ser.write((0).to_bytes(3, 'big'))
    # ser.write((ESCAPE_BYTE).to_bytes(1, 'big'))  #126
    # ser.write((START_BYTE ^ ESCAPE_XOR).to_bytes(1, 'big'))
    # ser.write((256 - 44 - 1 - 126).to_bytes(1, 'big'))  # CRC


def print_replies(ser):
    time.sleep(0.1)
    while (ser.in_waiting > 0):
        received = ser.readline()
        print("Received --> " + str(received))
        time.sleep(0.1)

def main():
    ser = serial.Serial("/dev/tty.usbmodem11201", baudrate = 9600, 
                        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, 
                        bytesize=serial.EIGHTBITS, timeout=1)
    print("Connected")
    ser.reset_input_buffer()
    time.sleep(0.1)

    while True:
        answer = input("What would you like to send? [N or S] ")
        answer = answer.upper()
        if answer == "N":
            # ser.write((COMMAND_ID_LED | PAYLOAD_LED_ON).to_bytes(1, 'big'))
            handle_number_command(ser)
        elif answer == "S":
            # ser.write((COMMAND_ID_LED | PAYLOAD_LED_OFF).to_bytes(1, 'big'))
            handle_string_command(ser)
        elif answer == "":
            print("Goodbye")
            break
        else:
            print("Please answer with a valid choice next time.")
        print_replies(ser)


main()