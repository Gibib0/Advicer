from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.graphics import Color
from kivy.clock import Clock
import random
from kivy.core.audio import SoundLoader
import os

class AdvicerLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_advice = None
        self.reset_screen = False

        self.background_sound = SoundLoader.load('assets/sounds/background_sound.wav')
        self.cat_sound = SoundLoader.load('assets/sounds/cat_sound.wav')
        self.duck_sound = SoundLoader.load('assets/sounds/duck_sound.wav')
        self.applause_sound = SoundLoader.load('assets/sounds/applause_sound.wav')
        self.judge_sound = SoundLoader.load('assets/sounds/judge_sound.wav')
        self.drum_sound = SoundLoader.load('assets/sounds/drum_sound.wav')
        self.screamer_sound = SoundLoader.load('assets/sounds/screamer_sound.wav')
        self.explosion_sound = SoundLoader.load('assets/sounds/explosion_sound.wav')

        if self.background_sound:
            self.background_sound.loop = True
            self.background_sound.volume = 0.2
            self.background_sound.play()


    def advice_button(self, advice):
        if self.reset_screen:
            self.current_advice = advice
            self.reset_screen = False

        self.ids.display.text = self.current_advice


class AdvicerApp(App):
    def build(self):
        self.icon = 'assets/icons/icon.ico'
        return AdvicerLayout()


