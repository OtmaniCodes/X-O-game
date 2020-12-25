from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class Score(Popup):
    result = ''
    score1 = 0
    score2 = 2

    def __init__(self, result, **kwargs):
        super(Score, self).__init__(**kwargs)
        if result == 'win':
            self.result = 'win'
        elif result == 'tie':
            self.result = 'tie'
        # stuff
        self.title = "the score"
        self.size_hint = [None, None]
        self.pos_hint = {'center_x': 0.5, "top": .7}
        self.height = 250
        self.width = 310
        #self.auto_dismiss = False
        # separator
        self.separator_color = [1, 1, 1, 1]
        self.separator_height: 10
        # content
        self.float = FloatLayout(size_hint=[1, 1], pos_hint={'top':1})
        self.box = BoxLayout(size_hint_y=.25, padding=10, spacing=10, pos_hint={
                             'top': .32, 'center_x': .5}, orientation='horizontal')
        self.statement = Label(text=f'we have a {self.result}!'.upper(), pos_hint={
            'top': 1, 'center_x': .5}, font_size='37sp', size_hint=[None, None])
        self.score = Label(text='THE SCORE:', size_hint=[None, None], pos_hint={
            'top': .75, 'x': 0.1}, font_size=24)
        self.x_player = Label(text=f'X player: {self.score1}!', size_hint=[None, None], pos_hint={
            'top': .8, 'x': 0.47}, font_size=18)
        self.y_player = Label(text=f'O player: {self.score2}!',size_hint=[None, None],  pos_hint={
            'top': .7, 'x': 0.47}, font_size=18)
        self.again_btn = Button(text="  AGAIN", background_normal='', background_down='', background_color=[
            1, 1, 1, 1], color=[.2, .4, .4, 1], font_size="18sp", bold=True)
        self.home_btn = Button(text="HOME", background_normal='', background_down='', background_color=[
            1, 1, 1, 1], color=[.2, .4, .4, 1], font_size="18sp", bold=True)
        self.box.add_widget(self.again_btn)
        self.box.add_widget(self.home_btn)
        self.float.add_widget(self.statement)
        self.float.add_widget(self.score)
        self.float.add_widget(self.x_player)
        self.float.add_widget(self.y_player)
        self.float.add_widget(self.box)
        self.add_widget(self.float)
