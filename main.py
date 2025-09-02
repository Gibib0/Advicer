from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.graphics import Color, Rectangle
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
        self.click_sound = SoundLoader.load('assets/sounds/click_sound.wav')
        self.cat_sound = SoundLoader.load('assets/sounds/cat_sound.wav')
        self.duck_sound = SoundLoader.load('assets/sounds/duck_sound.wav')
        self.applause_sound = SoundLoader.load('assets/sounds/applause_sound.wav')
        self.judge_sound = SoundLoader.load('assets/sounds/judge_sound.wav')
        self.drum_sound = SoundLoader.load('assets/sounds/drum_sound.wav')
        self.screamer_sound = SoundLoader.load('assets/sounds/screamer_sound.wav')

        if self.background_sound:
            self.background_sound.loop = True
            self.background_sound.volume = 0.2
            self.background_sound.play()

        Clock.schedule_interval(self.change_background, 0.5)

        self.secret_sequence = ['cat', 'drum', 'duck', 'duck', 'cat', 'applause', 'duck']
        self.user_sequence = []

        self.advice_counter = 0

        self.advices = [
            'Не сутулься',
            'Ешь суп ложкой, а не вилкой',
            'Притворись что ты утка',
            'Серьёзно? Ты снова нажал на эту кнопку?',
            'Ты молодец',
            'Умничка',
            'Не нужно этого делать',
            'Иди выпей воды',
            'Пора спать',
            'bruh',
            'Зачем ты нажимаешь на эту кнопку?',
            'Нет, правда. Зачем?',
            'У тебя все получиться',
            'Иди посмотри на картинки с котиками',
            'Почему ты все еще здесь?',
            'Знал, что все люди, которые пили воду, умерли?',
            'Херней страдаешь, а?',
            'Может, отдохнешь?',
            'Иди потрогай траву, червь',
            'Ты любишь уток?',
            'Действительно думал, что тут будет умный совет?',
            'Сделай шаг вперед',
            'Я тут видела хороший совет, для стояния на крыше)',
            'А ты не так прост',
            'Я люблю уток',
            'Коты милые, задумайся',
            'Как думаешь, сколько тут еще советов?',
            'Ни конца, ни края не видно...',
            'Устал? Иди отдохни. Умные советы от тебя никуда не денуться',
            'Знал, что если нажать на эту кнопку определенное количество раз будет что-то интересное',
            'Иди почитай книгу',
            'Motherfucker',
            'Подумай о чем-нибудь хорошем',
            'Разомни шею, падла',
            'Ты милый',
            'Послушай хорошую музыку',
            'Приятно общаться умным человеком',
            'Нажми еще, что уж там',
            'Не надоело?',
            'Интересно, ты мысленно как-то отвечаешь на каждый сгенерированный тут совет?',
            'Похоже это надолго',
            'Их очень много..',
            'Не дели на ноль',
            'Я бы на твоем месте пошла бы спать',
            'Зачем нажал?',
            'Кот, барабаны, две утки, кот, аплодисменты, утка',
            'Ты думаешь советы бесконечные?',
            'Nigga',
        ]

    def change_background(self, dt):
        r = random.random()
        g = random.random()
        b = random.random()

        self.canvas.before.clear()
        with self.canvas.before:
            Color(r, g, b, 1)
            Rectangle(pos=self.pos, size=self.size)

    def play_click_sound(self):
        if self.click_sound:
            self.click_sound.play()

    def play_cat_sound(self):
        if self.cat_sound:
            self.cat_sound.play()

    def play_duck_sound(self):
        if self.duck_sound:
            self.duck_sound.play()

    def play_applause_sound(self):
        if self.applause_sound:
            self.applause_sound.play()

    def play_judge_sound(self):
        if self.judge_sound:
            self.judge_sound.play()

    def play_drum_sound(self):
        if self.drum_sound:
            self.drum_sound.play()

    def stop_background_sound(self):
        if self.background_sound and self.background_sound.state == 'play':
            self.background_sound.stop()

    def stop_screamer_sound(self, instance=None):
        if self.error_sound and self.error_sound.state == 'play':
            self.error_sound.stop()

        if self.background_sound and self.background_sound.state != 'play':
            self.background_sound.play()

    def advice_button(self):
        self.advice_counter += 1

        if self.advice_counter == 100:
            self.show_error()
            self.advice_counter = 0
            return

        if self.advice_counter == 69:
            self.show_rizz()
            return

        random_advice = random.choice(self.advices)
        self.ids.display.text = random_advice

    def show_error(self):
        self.stop_background_sound()

        screamer = ScreamerPopup()
        screamer.open()

        if self.screamer_sound:
            self.screamer_sound.volume = 1.0
            self.screamer_sound.play()

    def show_rizz(self):
        popup = RizzUpPopup()
        popup.open()

        Clock.schedule_once(lambda dt: popup.dismiss(), 2)

    def cat_button(self):
        self.check_secret_sequence('cat')

    def duck_button(self):
        self.check_secret_sequence('duck')

    def applause_button(self):
        self.check_secret_sequence('applause')

    def judge_button(self):
        self.check_secret_sequence('judge')

    def drum_button(self):
        self.check_secret_sequence('drum')

    def check_secret_sequence(self, button_name):
        self.user_sequence.append(button_name)

        self.user_sequence = self.user_sequence[-len(self.secret_sequence):]

        if self.user_sequence == self.secret_sequence:
            self.show_rickroll()
            self.user_sequence = []

    def show_rickroll(self):
        rickroll = RickrollPopup()
        rickroll.open()

class AdvicerApp(App):
    def build(self):
        self.icon = 'assets/icons/icon.ico'
        return AdvicerLayout()

class ScreamerPopup(Popup):
    pass
class RizzUpPopup(Popup):
    pass
class RickrollPopup(Popup):
    pass

if __name__ == '__main__':
    AdvicerApp().run()


