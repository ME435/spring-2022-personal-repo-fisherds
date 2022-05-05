import mqtt_helper
import time
import bit_com

def main():
    print("Ready")
    mqtt_client = mqtt_helper.MqttClient()
    robot = bit_com.BitCom("/dev/ttyACM0")
    mqtt_client.callback = lambda type, payload: mqtt_callback(type, payload, robot)
    mqtt_client.connect("fisherds2pi", "fisherds2computer")

    while True:
        time.sleep(0.1)

# MQTT on_message callback (use via a lambda function below)
def mqtt_callback(type_name, payload, robot):
    print("Received message type: ", type_name)
    print("Received message payload: ", payload)
    # TODO: Do whatever is needed with the received message...
    if type_name.lower() == "led":
        if payload == 1:
            robot.send_led_on()
        elif payload == 0:
            robot.send_led_off()
    elif type_name.lower() == "tone":
        robot.send_tone(payload)
    elif type_name.lower() == "song":
        robot.play_mary()
    

    robot.print_replies()



main()