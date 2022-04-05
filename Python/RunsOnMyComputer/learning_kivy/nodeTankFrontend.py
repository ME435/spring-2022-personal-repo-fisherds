from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class TankRemote(App):
    def send_stop(self, event):
        print("TODO: Send stop")

    def build(self):
        stop_btn = Button(text="Forward")
        stop_btn.bind(on_press = self.send_stop)
        return stop_btn


if __name__ == '__main__':
    TankRemote().run()