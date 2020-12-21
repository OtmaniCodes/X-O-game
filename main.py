from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from wids.options import OptionTable
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from wids.tictactoe import TicTacToe
from random import randint


class Home(Screen):
    pass


class Soloplayer(Screen):
    pass


class Multiplayer(Screen):
    pass


class MyApp(App):
    mode = ""
    user_choice = ""
    btns_ids = []
    turn = False
    player1 = TicTacToe()
    player2 = TicTacToe()

    def build(self):
        Window.size = (360, 640)
        Window.minimum_width, Window.minimum_height = (360, 640)
        return Builder.load_file('main.kv')

    def change_screen(self, sc, way, mode=''):
        if sc == 'home':
            self.reset_net(mode)
        manager = self.root.ids.screen_manager
        manager.transition.duration = 0.5
        manager.transition.direction = way
        manager.current = sc

    def show_options(self, mode):
        pop = OptionTable(mode, app)
        pop.open()

    def execute_show_options(self, mode):
        Clock.schedule_once(lambda x: self.show_options(mode), 0.5)

    def draw_net(self, mode):
        self.mode = mode
        net = self.root.ids[mode].ids
        for f in range(3):
            for i in range(3):
                box = BoxLayout(orientation='horizontal', spacing=5)
                for j in range(3):
                    btn = Button(text=f'{f}-{j}', background_normal='', color=[0, 0, 0, 0],
                                 background_down='', background_color=[1, 1, 1, 1])
                    btn.bind(on_release=self.change_icon)
                    box.add_widget(btn)
            net.box.add_widget(box)

    def computer_player(self):
        available_moves = [x for x in self.btns_ids if x.background_normal == '']
        move_index = randint(0, len(available_moves))
        self.change_icon(available_moves[move_index]) 
    
    def reset_net(self, mode):
        net = self.root.ids[mode].ids.box
        net.clear_widgets()

    def change_icon(self, idd):
        self.btns_ids.append(idd)
        if self.user_choice == 'x':
            unchecked = 'imgs/x.png'
            checked = 'imgs/xc.png'
            self.user_choice = 'o'
        elif self.user_choice == 'o':
            unchecked = 'imgs/o.png'
            checked = 'imgs/oc.png'
            self.user_choice = 'x'
        self.turn = not self.turn
        if idd.background_normal == '':
            idd.background_normal = unchecked
            self.get_id(idd.text)
        else:
            pass
        if self.turn == False and self.mode == 'solo':
            self.computer_player()

    def get_id(self, member, get_num=False):
        ids = {'0-0': 0, '0-1': 1, '0-2': 2, '1-0': 3,
               '1-1': 4, '1-2': 5, '2-0': 6, '2-1': 7, '2-2': 8}
        if get_num == True:
            keys = list(ids.keys())
            values = list(ids.values())
            index = values.index(member)
            return keys[index]
        else:
            self.check_win(ids[member])

    def check_win(self, idd):
        if self.turn == True:
            self.player1.player_moves1.append(idd)
            moves = self.player1.player_moves1
            res = self.player1.win(1)
            self.player1.tie()
        elif self.turn == False:
            self.player2.player_moves2.append(idd)
            moves = self.player2.player_moves2
            res = self.player1.win(2)
            self.player1.tie()
        if res == True:
            self.check_boxes(moves)

    def check_boxes(self, moves):
        boxes = []
        for move in moves:
            boxes.append(self.get_id(move, get_num=True))
        for idd in self.btns_ids:
            if idd.text in boxes:
                if idd.background_normal == 'imgs/x.png':
                    idd.background_normal = 'imgs/xc.png'
                else:
                    idd.background_normal = 'imgs/oc.png'


if __name__ == '__main__':
    app = MyApp()
    app.run()
