import time
import serial


def wait_for_reply(ser):
    while (ser.in_waiting == 0):
        time.sleep(0.1) # Done to avoid the ser.readline timeout
    received = ser.readline()
    print("Received --> " + str(received))

def handle_x_axis(ser):
    answer = int(input("What X location would you like [1-5]? "))
    command = f"X-AXIS {answer}\n".encode()
    ser.write(command)

def main_menu(ser):
    while True:
        answer = input("What would you like to do? [R, X]? ")
        answer = answer.upper()
        if answer == "R":
            ser.write(b'RESET\n')
        elif answer == "X":
            handle_x_axis(ser)
        elif answer == "":
            print("Goodbye")
            break
        else:
            print("Invalid. Please make a valid choice next time.")
        
        wait_for_reply(ser)


def main():
    ser = serial.Serial("/dev/tty.usbserial-110", baudrate = 19200, 
                        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, 
                        bytesize=serial.EIGHTBITS, timeout=1)
    print("Connected")
    ser.reset_input_buffer()
    main_menu(ser)


main()