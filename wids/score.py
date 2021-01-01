from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class Score(Popup):
    winner = ''
    mode = ''

    def __init__(self, winner, app, mode, **kwargs):
        super(Score, self).__init__(**kwargs)
        self.winner = winner
        self.app = app
        self.mode = mode
        # title ans positioning
        self.title = "GAME over".upper()
        self.size_hint = [None, None]
        self.pos_hint = {'center_x': 0.5, "top": .7}
        self.height = 250
        self.width = 310
        self.auto_dismiss = False
        # separator
        self.separator_color = [1, 1, 1, 1]
        self.separator_height: 10
        # content
        self.float = FloatLayout(size_hint=[1, 1], pos_hint={'top': 1})
        self.box = BoxLayout(size_hint_y=.25, padding=10, spacing=10, pos_hint={
                             'top': .32, 'center_x': .5}, orientation='horizontal')
        self.statement = Label(text=self.get_txt().upper(), pos_hint={
            'top': .9, 'center_x': .5}, font_size='25sp', size_hint=[None, None], bold=True, markup=True)
        self.exit_btn = Button(text="EXIT", background_normal='', background_down='', background_color=[
            1, 1, 1, 1], color=[.2, .4, .4, 1], font_size="18sp", bold=True)
        self.home_btn = Button(text="HOME", background_normal='', background_down='', background_color=[
            1, 1, 1, 1], color=[.2, .4, .4, 1], font_size="18sp", bold=True)
        self.exit_btn.bind(on_release=self.app.exit_game)
        self.home_btn.bind(on_release=self.go_home)
        self.box.add_widget(self.exit_btn)
        self.box.add_widget(self.home_btn)
        self.float.add_widget(self.statement)
        self.float.add_widget(self.box)
        self.add_widget(self.float)

    def get_txt(self):
        if self.winner != '' and self.winner != 'tie':
            txt = f'the winner is:\nplayer {self.winner}!'
        else:
            txt = 'we have a tie!'
        return txt

    def go_home(self, *args):
        self.app.change_screen('home', 'up', self.mode)
        self.dismiss()
