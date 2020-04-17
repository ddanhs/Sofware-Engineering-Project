from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout


class MainApp(App):
    def build(self):
        return FloatLayout()


MainApp().run()