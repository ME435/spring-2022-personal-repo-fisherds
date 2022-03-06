import time
import serial
import robot_byte_com


def handle_string_command(robot_com: robot_byte_com.RobotByteCom):
    answer = input("What string would you like to send? ")
    robot_com.send_string_command(answer)
    
def handle_number_command(robot_com: robot_byte_com.RobotByteCom):
    answer = input("What 32 bit number would you like to send? ")
    robot_com.send_number_command(int(answer))


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
    robot_com = robot_byte_com.RobotByteCom(ser, 13)

    while True:
        answer = input("What would you like to send? [N or S] ")
        answer = answer.upper()
        if answer == "N":
            handle_number_command(robot_com)
        elif answer == "S":
            handle_string_command(robot_com)
        elif answer == "":
            print("Goodbye")
            break
        else:
            print("Please answer with a valid choice next time.")
        print_replies(ser)

main()