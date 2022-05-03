from kivymd.app import MDApp
from kivy.core.window import Window

import bit_com

class DirectSerialGuiApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.frequency = 440
        self.robot = bit_com.BitCom("/dev/tty.usbmodem2101")

    def build(self):
        print("Ready")
        Window.size = (400, 400)
        return

DirectSerialGuiApp().run()
