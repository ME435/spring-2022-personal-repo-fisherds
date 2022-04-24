from kivymd.app import MDApp
from kivy.properties import (
    NumericProperty
)
from kivy.core.window import Window

class HelloButtonApp(MDApp):

    counter = NumericProperty(0)

    def build(self):
        Window.size = (400, 300)
        return

HelloButtonApp().run()