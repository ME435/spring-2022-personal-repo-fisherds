from kivymd.app import MDApp
from kivy.properties import StringProperty

class HelloWorldApp(MDApp):

    my_text = StringProperty("Default value goes here")

    def build(self):
        self.my_text = "Hello, David Fisher"
        return

HelloWorldApp().run()