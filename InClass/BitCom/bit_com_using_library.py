import bit_com as bc

def handleLedCommand(robot):
    answer = input("Would you like to turn the LED ON or OFF? [ON OFF] ")
    answer = answer.upper()
    if answer == "ON":
        robot.send_led_on()
        print("Sent LED on command")
    elif answer == "OFF":
        robot.send_led_off()
        print("Sent LED off command")
    else:
        print("No command sent.  Please use ON or OFF next time.")

def handleToneCommand(robot):
    answer = input("Would frequency would like (in Hz)? [120 to 1500] ")
    frequency = int(answer)
    print(f"Sent a TONE command with the frequency {frequency}")
    robot.send_tone(frequency)
    
def main():
    print("Ready")
    robot = bc.BitCom("/dev/tty.usbmodem2101")
    
    while True:
        answer = input("Command? [LED TONE SONG] ")
        answer = answer.upper()
        if answer == "LED":
            handleLedCommand(robot)
        elif answer == "TONE":
            handleToneCommand(robot)
        elif answer == "SONG":
            robot.play_mary()
        elif answer == "":
            print("Goodbye")
            break
        else:
            print("Please select LED, TONE, or SONG (or leave blank to exit)")
        
        # print_replies(ser)
        robot.print_replies()

main()
