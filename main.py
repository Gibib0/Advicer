from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import webbrowser
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
import random
from kivy.core.audio import SoundLoader
import os
from kivy.lang import Builder

kv_path = os.path.join(os.path.dirname(__file__), 'advicer.kv')
Builder.load_file(kv_path)

sound = SoundLoader.load('assets/sounds/click_sound.wav')
if sound:
    print("AUDIO PROVIDER:", type(sound))
else:
    print("Не удалось загрузить звук!")


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
        self.screamer2_sound = SoundLoader.load('assets/sounds/screamer2_sound.wav')
        self.kostya_sound = SoundLoader.load('assets/sounds/kostya_sound.wav')

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
            'Обернись',
            'Пора сделать паузу',
            'Посчитай до десяти, потом до двадцати... а потом иди на.....',
            'Ты уникален, даже если пока не знаешь как',
            'Иди помой руки, вдруг пригодится',
            'Иногда стоит просто посидеть в тишине',
            'Подумай о котиках, даже если у тебя их нет',
            'Попробуй притвориться, что ты утка… снова',
            'Встань',
            'Сядь',
            'Ты уже нажал на эту кнопку слишком много раз… или нет?',
            'Ты все равно не сможешь перечитать все советы, которые я прописала',
            'И ради этого я лягла в 2 ночи',
            'Ты знал что в пинтересте нельзя напрямую найти расисткие картинки?',
            'Уже видел Бараша гигачада?',
            'Я кажись себе руку накачала пока это тестировала...',
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

    def advice_button(self):
        self.advice_counter += 1

        if self.advice_counter == 3:
            self.show_penguins()
            return

        if self.advice_counter == 18:
            self.show_sex()
            return
        
        if self.advice_counter == 30:
            self.show_what()
            return
        
        if self.advice_counter == 52:
            self.show_kostya()
            return

        if self.advice_counter == 69:
            self.show_rizz()
            return
        
        if self.advice_counter == 88:
            self.show_meme()
            return
        
        if self.advice_counter == 100:
            self.show_screamer()
            return
        
        if self.advice_counter == 150:
            self.show_madness()
            return
        
        if self.advice_counter == 180:
            self.show_giga()
            return
        
        if self.advice_counter == 200:
            self.show_screamer2()
            return
        
        if self.advice_counter == 250:
            self.show_grass()
            return
        
        if self.advice_counter == 300:
            self.show_message()
            return

        random_advice = random.choice(self.advices)
        self.ids.display.text = random_advice

        self.ids.counter.text = f'Смотри сколько советов: {self.advice_counter}'

    def show_screamer(self):
        self.stop_background_sound()

        screamer = ScreamerPopup()
        screamer.open()

        if self.screamer_sound:
            self.screamer_sound.volume = 1.0
            self.screamer_sound.play()

        Clock.schedule_once(lambda dt: screamer.dismiss(), 1)

    def show_screamer2(self):
        self.stop_background_sound()

        screamer = Screamer2Popup()
        screamer.open()

        if self.screamer2_sound:
            self.screamer2_sound.volume = 1.0
            self.screamer2_sound.play()

        Clock.schedule_once(lambda dt: screamer.dismiss(), 1)

    def show_kostya(self):
        self.stop_background_sound()

        kostya = KostyaPopup()
        kostya.open()

        if self.kostya_sound:
            self.kostya_sound.volume = 1.0
            self.kostya_sound.play()

        Clock.schedule_once(lambda dt: kostya.dismiss(), 1)

    def show_rizz(self):
        popup = RizzUpPopup()
        popup.open()

        Clock.schedule_once(lambda dt: popup.dismiss(), 1)
        
    def show_penguins(self):
        popup = PenguinsPopup()
        popup.open()

        Clock.schedule_once(lambda dt: popup.dismiss(), 1.5)

    def show_sex(self):
        popup = SexPopup()
        popup.open()

        Clock.schedule_once(lambda dt: popup.dismiss(), 1)

    def show_what(self):
        popup = WhatPopup()
        popup.open()

        Clock.schedule_once(lambda dt: popup.dismiss(), 1)

    def show_meme(self):
        popup = MemePopup()
        popup.open()

        Clock.schedule_once(lambda dt: popup.dismiss(), 1)
        
    def show_giga(self):
        popup = GigaPopup()
        popup.open()

        Clock.schedule_once(lambda dt: popup.dismiss(), 1)
        
    def show_message(self):
        popup = MessagePopup()
        popup.open()

    def show_madness(self):
        webbrowser.open('https://www.youtube.com/watch?v=8djnfFx_E0Y')

    def show_grass(self):
        webbrowser.open('https://www.youtube.com/watch?v=dzVahzHh2W4')

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
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1')

class AdvicerApp(App):
    def build(self):
        self.icon = 'assets/icons/icon.ico'
        return AdvicerLayout()

class ScreamerPopup(Popup):
    def on_dismiss(self):
        app = App.get_running_app()
        if hasattr(app.root, 'background_sound') and app.root.background_sound:
            if app.root.background_sound.state != 'play':
                app.root.background_sound.play()

class Screamer2Popup(Popup):
    def on_dismiss(self):
        app = App.get_running_app()
        if hasattr(app.root, 'background_sound') and app.root.background_sound:
            if app.root.background_sound.state != 'play':
                app.root.background_sound.play()

class KostyaPopup(Popup):
    def on_dismiss(self):
        app = App.get_running_app()
        if hasattr(app.root, 'background_sound') and app.root.background_sound:
            if app.root.background_sound.state != 'play':
                app.root.background_sound.play()

class MessagePopup(Popup):
    pass
class RizzUpPopup(Popup):
    pass
class PenguinsPopup(Popup):
    pass
class SexPopup(Popup):
    pass
class WhatPopup(Popup):
    pass
class MemePopup(Popup):
    pass
class GigaPopup(Popup):
    pass

if __name__ == '__main__':
    AdvicerApp().run()


