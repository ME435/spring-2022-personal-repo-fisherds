from kivymd.app import MDApp
from kivy.properties import (
    StringProperty
)
from kivy.core.window import Window

class HelloButtonApp(MDApp):

    my_text = StringProperty("Default value goes here")
    # my_text = "Default value"
    counter = 0

    def build(self):
        Window.size = (400, 300)
        self.update_view()
        return

    def change(self, amount):
        self.counter += amount
        self.update_view()

    def set(self, amount):
        self.counter = amount
        self.update_view()

    def update_view(self):
        self.my_text = f"Counter = {self.counter}"
    

HelloButtonApp().run()