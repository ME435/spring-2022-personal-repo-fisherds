from kivymd.app import MDApp
from kivy.core.window import Window


class WirelessMqttGuiApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.frequency = 440

    def build(self):
        print("Ready")
        Window.size = (400, 400)
        return

WirelessMqttGuiApp().run()
