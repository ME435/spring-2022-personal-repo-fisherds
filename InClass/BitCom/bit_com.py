def handleLedCommand():
    answer = input("Would you like to turn the LED ON or OFF? [ON OFF] ")
    answer = answer.upper()
    if answer == "ON":
        #  TODO: Send the byte to turn ON the LED
        print("TODO: Send LED on command")
    elif answer == "OFF":
        #  TODO: Send the byte to turn OFF the LED
        print("TODO: Send LED off command")
    else:
        print("No command sent.  Please use ON or OFF next time.")

def handleToneCommand():
    answer = input("Would frequency would like (in Hz)? [120 to 1500] ")
    answer = int(answer)
    print(f"TODO: Send a TONE command with the frequency {answer}")

def main():
    print("Ready")
    # TODO: Open the serial port
    
    while True:
        answer = input("Command? [LED TONE SONG] ")
        answer = answer.upper()
        if answer == "LED":
            handleLedCommand()
        elif answer == "TONE":
            handleToneCommand()
        elif answer == "SONG":
            print("handle SONG command")
        elif answer == "":
            print("Goodbye")
            break
        else:
            print("Please select LED, TONE, or SONG (or leave blank to exit)")


main()
