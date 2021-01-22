from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from wids.options import OptionTable
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from wids.tictactoe import TicTacToe
from wids.score import Score
from animation.animation import MyAnimation
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
    all_btns_ids = []
    btns_ids = []
    turn = True
    player1 = TicTacToe()
    player2 = TicTacToe()
    winner = ''
    found_winner = False

    def build(self):
        Window.size = (360, 640)
        Window.minimum_width, Window.minimum_height = (360, 640)
        return Builder.load_file('main.kv')

    def on_start(self):
        target1 = self.root.ids.home.ids.btn1
        target2 = self.root.ids.home.ids.btn2
        anime = MyAnimation(target1, target2)
        anime.animate_widget()

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
        for i in range(3):
            box = BoxLayout(orientation='horizontal', spacing=5)
            for j in range(3):
                btn = Button(text=f'{i}-{j}', background_normal='', color=[0, 0, 0, 0],
                             background_down='', background_color=[1, 1, 1, 1])
                if not(btn in self.all_btns_ids):
                    self.all_btns_ids.append(btn)
                btn.bind(on_release=self.change_icon)
                box.add_widget(btn)
            net.box.add_widget(box)

    def computer_player(self):
        chosen_btn = ''
        btns_txt = ['0-0', '0-2', '2-0', '2-2',
                    '0-1', '1-0', '1-2', '2-1', '1-1']
        available_btns_ids = [x for x in self.all_btns_ids if x.text in btns_txt]
        available_btns_to_use = [x for x in available_btns_ids if (x.background_normal == '') and (x not in self.btns_ids)]
        if len(available_btns_to_use) >= 1:
            chosen_btn = available_btns_to_use[randint(0, len(available_btns_to_use)-1)]
        if chosen_btn != '':
            self.computer_move(chosen_btn)
        else:
            print('no free place!')
        print(available_btns_to_use, '\n', len(available_btns_to_use))

    def computer_move(self, chosen_btn):
        Clock.schedule_once(lambda x: self.change_icon(chosen_btn), 0.5)

    def reset_net(self, mode):
        net = self.root.ids[mode].ids.box
        net.clear_widgets()
        self.player1.reset()
        self.player2.reset()
        self.found_winner = False
        self.turn = True
        self.mode = ''
        self.btns_ids.clear()
        self.all_btns_ids.clear()
        self.user_choice = ''

    def change_icon(self, idd):
        self.btns_ids.append(idd)
        if self.user_choice == 'x':
            unchecked = 'imgs/x.png'
            self.user_choice = 'o'
        elif self.user_choice == 'o':
            unchecked = 'imgs/o.png'
            self.user_choice = 'x'
        self.turn = not self.turn
        if idd.background_normal == '':
            idd.background_normal = unchecked
            self.get_id(idd.text)
        else: pass
        if (self.turn == False and self.mode == 'solo') and self.found_winner != True:
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
            res = self.player1.win(1, app, self.mode)
            # self.player1.win(1, app, self.mode, self.btns_ids)

        elif self.turn == False:
            self.player2.player_moves2.append(idd)
            moves = self.player2.player_moves2
            res = self.player1.win(2, app, self.mode)
            # self.player2.win(2, app, self.mode, self.btns_ids)

        if res == True:
            self.check_boxes(moves)
            self.found_winner = True
        else:
            self.player1.tie()

    def choose_img(self, samples):
        x_img = ''
        o_img = ''
        if ('0-0' in samples and '0-2' in samples) or ('1-0' in samples and '1-2' in samples) or ('2-0' in samples and '2-2' in samples):
            x_img = 'xch'
            o_img = 'och'
        elif ('0-0' in samples and '2-0' in samples) or ('0-1' in samples and '2-1' in samples) or ('0-2' in samples and '2-2' in samples):
            x_img = 'xcv'
            o_img = 'ocv'
        elif ('0-0' in samples and '2-2' in samples):
            x_img = 'xc'
            o_img = 'oc'
        elif ('0-2' in samples and '2-0' in samples):
            x_img = 'xc2'
            o_img = 'oc2'
        return [x_img, o_img]

    def check_boxes(self, moves):
        boxes = []
        for move in moves:
            boxes.append(self.get_id(move, get_num=True))
        imgs = self.choose_img(boxes)
        for idd in self.btns_ids:
            if idd.text in boxes:
                if idd.background_normal == 'imgs/x.png':
                    idd.background_normal = 'imgs/'+imgs[0]+'.png'
                    self.open_score('x', self.mode)
                else:
                    idd.background_normal = 'imgs/'+imgs[1]+'.png'
                    self.open_score('o', self.mode)

    def open_score(self, winner, mode):
        score = Score(winner, app, mode)
        Clock.schedule_once(lambda x: score.open(), 1)

    def exit_game(self, *args):
        self.stop()

    def dismiss_score(self, obj):
        obj.dismiss()


if __name__ == '__main__':
    app = MyApp()
    app.run()