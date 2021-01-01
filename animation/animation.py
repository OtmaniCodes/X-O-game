from kivy.animation import Animation
from random import randint
from kivy.clock import Clock


class MyAnimation:
    widget_id1 = ''
    widget_id2 = ''
    clr = [1,1,1,1]

    def __init__(self, widget_id1, widget_id2):
        self.widget_id1 = widget_id1
        self.widget_id2 = widget_id2
        self.get_color()

    def animate_widget(self, *args):
        anime = Animation(xx=0.5, d=1, background_color= self.clr)
        anime2 = Animation(xxx=0.5, d=1, background_color=[1,1,1,1])
        anime.start(self.widget_id1)
        anime2.start(self.widget_id2)

    def get_color(self):
        Clock.schedule_interval(self.gredient_animation, 1)
        Clock.schedule_interval(self.animate_widget, 1)

    def gredient_animation(self):
        colors = [[1,1,1,1],[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,0,0,1],[0,0,1,1]]
        self.clr = colors[randint(0,len(colors)-1)]
        
        
