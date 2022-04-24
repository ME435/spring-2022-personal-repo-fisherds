from kivymd.app import MDApp
from kivy.properties import StringProperty

class HelloWorldApp(MDApp):

    my_text = StringProperty("Hello David Fisher")

    def build(self):
        print("Ready")
        self.my_text = "The text has now changed!"
        return

HelloWorldApp().run()