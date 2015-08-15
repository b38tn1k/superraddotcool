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
from composer import *


class RingTones(App):

    def playRingtone(self, instance):
        if self.mobile_number.text == '0413946140':
            self.genre = 'JAMES'
        if self.play_already_pressed is False:
            mobile_number = self.mobile_number.text
            self.active_mobile_number = self.mobile_number.text
            genre = self.genre
            length_number = len(mobile_number)
            if mobile_number.isdigit():
                if (length_number == 10) or (length_number == 11) or (length_number == 12):
                    # hash mobile number for loop seeds
                    hash_mobile = str(abs(hash(mobile_number)))
                    print 'hash: {!s}'.format(hash_mobile)
                    variant = int(hash_mobile[0:5])
                    bass_val = int(hash_mobile[5:10])
                    drum_val = int(hash_mobile[10:14])
                    mel_val = int(hash_mobile[15:])
                    print 'var: {!s}'.format(variant)
                    print 'bass: {!s}'.format(bass_val)
                    print 'drum: {!s}'.format(drum_val)
                    print 'mel: {!s}'.format(mel_val)
                    # Create Composer Object
                    composer = Composer(genre, variant, bass_val, mel_val, drum_val, self.buffer_number)
                    composer.play()
                    self.play_already_pressed = True
                    self.buffer_number += self.number_of_buffers
                else:
                    if mobile_number == '':
                        mobile_number = 'This'
                    button = Button(text='{!s} is not a recognisable Mobile Number! \nMaybe try something else?\nClick to TRY AGAIN\nYou should probably restart the server also'.format(mobile_number), font_size=30, halign='center')
                    popup = Popup(title='Invalid Mobile Number',content=button, auto_dismiss=False)
                    button.bind(on_press=popup.dismiss)
                    popup.open()
            else:
                if mobile_number == '':
                    mobile_number = 'This'
                button = Button(text='{!s} is not a recognisable Mobile Number!\nMaybe try something else?\nOmit the international "+" symbol\nClick to TRY AGAIN\nYou should probably restart the server also'.format(mobile_number), font_size=30, halign='center')
                popup = Popup(title='Invalid Mobile Number',content=button, auto_dismiss=False)
                button.bind(on_press=popup.dismiss)
                popup.open()

    def stopCallback(self, instance):
        if self.play_already_pressed is True:
            stop()
            self.play_already_pressed = False
        # panic()

    def panicCallback(self, instance):
        panic()
        self.buffer_number = 0
        print("Resetting Server")

    def setJazz(self, instance):
        if not(self.genre == 'JAZZ') or not(self.active_mobile_number == self.mobile_number.text):
            self.jazzButton.background_color = self.red
            self.danceButton.background_color = self.blue
            self.dubButton.background_color = self.blue
            self.hipButton.background_color = self.blue
            self.genre = 'JAZZ'
            if self.play_already_pressed is True:
                self.stopCallback('hi')
                self.playRingtone('hi')
            else:
                self.playRingtone('hi')

    def setDubstep(self, instance):
        if not(self.genre == 'DUBSTEP') or not(self.active_mobile_number == self.mobile_number.text):
            self.dubButton.background_color = self.red
            self.danceButton.background_color = self.blue
            self.jazzButton.background_color = self.blue
            self.hipButton.background_color = self.blue
            self.genre = 'DUBSTEP'
            if self.play_already_pressed is True:
                self.stopCallback('hi')
                self.playRingtone('hi')
            else:
                self.playRingtone('hi')

    def setDance(self, instance):
        if not(self.genre == 'DANCE') or not(self.active_mobile_number == self.mobile_number.text):
            self.jazzButton.background_color = self.blue
            self.danceButton.background_color = self.red
            self.dubButton.background_color = self.blue
            self.hipButton.background_color = self.blue
            self.genre = 'DANCE'
            if self.play_already_pressed is True:
                self.stopCallback('hi')
                self.playRingtone('hi')
            else:
                self.playRingtone('hi')

    def setHiphop(self, instance):
        if not(self.genre == 'HIPHOP') or not(self.active_mobile_number == self.mobile_number.text):
            self.jazzButton.background_color = self.blue
            self.danceButton.background_color = self.blue
            self.dubButton.background_color = self.blue
            self.hipButton.background_color = self.red
            self.genre = 'HIPHOP'
            if self.play_already_pressed is True:
                self.stopCallback('hi')
                self.playRingtone('hi')
            else:
                self.playRingtone('hi')

    def dismiss_welcome(self, instance):
        self.main_interface.remove_widget(self.welcome_interface)
        # LAYOUT STUFF
        self.control_interface = BoxLayout(orientation="horizontal")
        self.genre_interface = BoxLayout(orientation="horizontal")
        self.genre_interface.add_widget(self.jazzButton)
        self.genre_interface.add_widget(self.danceButton)
        self.genre_interface.add_widget(self.dubstepButton)
        self.genre_interface.add_widget(self.hipButton)
        self.control_interface.add_widget(self.playButton)
        self.control_interface.add_widget(self.stopButton)
        self.control_interface.add_widget(self.recordButton)
        self.control_interface.add_widget(self.panicButton)
        self.main_interface.add_widget(self.mobile_number)
        self.main_interface.add_widget(self.genre_interface)
        self.main_interface.add_widget(self.control_interface)

    def recordCallback(self, instance):
        if self.record_state == 1:
            # Arm Track
            armRecord()
            self.recordButton.background_color = self.red
            self.recordButton.text = 'REC'
            self.record_state += 1
        elif self.record_state == 2:
            # Record Track
            beginRecord()
            self.recordButton.background_color = self.morered
            self.recordButton.text = 'STOP'
            self.record_state += 1
        elif self.record_state == 3:
            # Stop Recording
            stopRecord()
            self.recordButton.background_color = self.blue
            self.recordButton.text = 'ARM to REC'
            self.record_state = 1

    def normaliseCallback(self, instance):
        if self.normalised is False:
            self.normalised = True
            self.normalButton.background_color = self.red
        else:
            self.normalised = False
            self.normalButton.background_color = self.blue

    def quitCallback(self, instance):
        quitSc()
        exit()

    def build(self):
        # INITIALISERS
        # panic()
        start_up_instructions = False
        self.play_already_pressed = False
        self.red = [3, 2, 0, 1]
        self.blue = [0, 2, 3, 1]
        self.morered = [2, 0, 0, 1]
        self.number_of_buffers = 3
        self.buffer_number = 0
        self.active_mobile_number = 0
        self.genre = 'JAZZ'
        self.normalised = False
        self.record_state = 1
        # MOBILE NUMBER TEXT FIELD
        self.mobile_number = TextInput(
            hint_text='Please Enter Your Mobile Number', multiline=False, font_size=50)
        # PRESS FOR JAZZ
        self.jazzButton = Button(text='Jazz', font_size=30, halign='center')
        self.jazzButton.bind(on_press=self.setJazz)
        self.jazzButton.background_color = self.red
        # PRESS FOR DANCE
        self.danceButton = Button(text='Dance', font_size=30, halign='center')
        self.danceButton.bind(on_press=self.setDance)
        self.danceButton.background_color = self.blue
        # PRESS FOR DUBSTEP
        self.dubButton = Button(text='Dubstep', font_size=30, halign='center')
        self.dubButton.bind(on_press=self.setDubstep)
        self.dubButton.background_color = self.blue
        # PRESS FOR HIPHOP
        self.hipButton = Button(text='Hiphop', font_size=30, halign='center')
        self.hipButton.bind(on_press=self.setHiphop)
        self.hipButton.background_color = self.blue
        # BUTTON TO START PROCESS
        self.playButton = Button(text='Play', font_size=20, halign='center')
        self.playButton.bind(on_press=self.playRingtone)
        self.playButton.background_color = self.blue
        # BUTTON TO STOP
        self.stopButton = Button(text='Stop', font_size=20, halign='center')
        self.stopButton.bind(on_press=self.stopCallback)
        self.stopButton.background_color = self.blue
        # RESET SERVER BUTTON
        self.panicButton = Button(text='Reset Server', font_size=20, halign='center')
        self.panicButton.bind(on_press=self.panicCallback)
        self.panicButton.background_color = self.blue
        # RECORD AUDIO BUTTON
        self.recordButton = Button(text='ARM to REC', font_size=20, halign='center')
        self.recordButton.bind(on_press=self.recordCallback)
        self.recordButton.background_color = self.blue
        # NORMALISE AUDIO BUTTON
        self.normalButton = Button(text='Normalise', font_size=20, halign='center')
        self.normalButton.bind(on_press=self.normaliseCallback)
        self.normalButton.background_color = self.blue
        # QUIT
        self.quitButton = Button(text='Quit', font_size=20, halign='center')
        self.quitButton.bind(on_press=self.quitCallback)
        self.quitButton.background_color = self.blue

        # LAYOUT
        self.main_interface = BoxLayout(orientation="vertical")
        if start_up_instructions is True:
            # START UP INSTRUCTIONS
            image = Image(source='Help.png', pos=(400, 100), size=(400, 400))
            image.background_color = self.blue
            welcome_button = Button(text='Continue', font_size=20, size_hint=(1, .1))
            welcome_button.bind(on_press=self.dismiss_welcome)
            self.welcome_interface = BoxLayout(orientation="vertical")
            self.welcome_interface.add_widget(image)
            self.welcome_interface.add_widget(welcome_button)
            self.main_interface.add_widget(self.welcome_interface)
        else:
            self.control_interface = BoxLayout(orientation="horizontal")
            self.genre_interface = BoxLayout(orientation="horizontal")
            self.genre_interface.add_widget(self.jazzButton)
            self.genre_interface.add_widget(self.danceButton)
            self.genre_interface.add_widget(self.dubButton)
            self.genre_interface.add_widget(self.hipButton)
            self.control_interface.add_widget(self.playButton)
            self.control_interface.add_widget(self.stopButton)
            self.control_interface.add_widget(self.recordButton)
            self.control_interface.add_widget(self.panicButton)
            self.control_interface.add_widget(self.quitButton)
            self.main_interface.add_widget(self.mobile_number)
            self.main_interface.add_widget(self.genre_interface)
            self.main_interface.add_widget(self.control_interface)


        return self.main_interface

if __name__ == '__main__':
    RingTones().run()
