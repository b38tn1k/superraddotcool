from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.image import Image
from os import path, getcwd, listdir, system
from scBridge import *


class PopgasmTester(App):

    def say_something(self, instance):
        scSpeak(self.words.text, self.pitch.text)
        print "SPEAK!"

    def build(self):

        self.main_thing = BoxLayout(orientation="vertical")

        self.words = TextInput(test='shit for the masses', multiline=False, font_size=30)
        self.pitch = TextInput(test='pitch 0 - 127', multiline=False, font_size=30)

        self.do_it = Button(text='Do It', font_size=30)
        self.do_it.bind(on_press=self.say_something)

        self.main_thing.add_widget(self.words)
        self.main_thing.add_widget(self.pitch)
        self.main_thing.add_widget(self.do_it)

        return self.main_thing

if __name__ == '__main__':
    PopgasmTester().run()
