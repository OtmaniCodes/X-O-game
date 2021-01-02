from kivy.animation import Animation
from random import randint
from kivy.clock import Clock


class MyAnimation:
    widget_id1 = ''
    widget_id2 = ''

    def __init__(self, widget_id1, widget_id2):
        self.widget_id1 = widget_id1
        self.widget_id2 = widget_id2

    def animate_widget(self, *args):
        anime = Animation(xx=0.5, d=1, background_color= [1,1,1,1])
        anime2 = Animation(xx=0.5, d=1, background_color= [1,1,1,1])
        anime.start(self.widget_id1)
        anime2.start(self.widget_id2)