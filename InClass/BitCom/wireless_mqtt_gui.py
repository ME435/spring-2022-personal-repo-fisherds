from kivymd.app import MDApp
from kivy.core.window import Window

import mqtt_helper as mh

class WirelessMqttGuiApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.frequency = 440

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.callback = lambda type, payload: self.mqtt_callback(type, payload)
        self.mqtt_client.connect("fisherds2computer", "fisherds2pi")  # "Send to" and "listen to" the same topic
        # self.mqtt_client.connect("fisherds", "fisherds")  # For testing development

    # MQTT on_message callback (use via a lambda function below)
    def mqtt_callback(self, type_name, payload):
        print("Received message type: ", type_name)
        print("Received message payload: ", payload)
        # TODO: Do whatever is needed with the received message...

    def build(self):
        print("Ready")
        Window.size = (400, 400)
        return

WirelessMqttGuiApp().run()
