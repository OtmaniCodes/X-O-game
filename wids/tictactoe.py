from itertools import permutations as per
from wids.score import Score


class TicTacToe:
    player_moves1 = []
    player_moves2 = []
    winner = ''
    crossed_boxs = 0
    uncrossed_boxs = 9
    app = ''

    def win(self, turn, app, mode):
        self.app = app
        self.mode = mode
        self.crossed_boxs += 1
        self.uncrossed_boxs -= 1
        winning_cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                         [1, 4, 7], [2, 4, 8], [0, 4, 8], [2, 4, 6]]
        if turn == 1:
            lista = self.player_moves1
        else:
            lista = self.player_moves2

        for case in winning_cases:
            for combination in list(per(lista, len(lista))):
                for case2 in list(per(case, len(case))):
                    if list(combination) == list(case2):
                        return True
                    else:
                        pass
        return False


        # TO-DO: fixing and using this block of code instead of the one aboce...  
        
        # count = 0
        # wanted_line = ''
        # btns_nums = []
        
        # btn_ids_txts = []
        # for one in btn_ids:
        #     btn_ids_txts.append(one.text)
        # btns_nums = map(lambda x: self.app.get_id(x), btn_ids_txts)
        # print(btn_ids_txts)
        # print(btns_nums)
        # for case in winning_cases:
        #     for num in case:
        #         if num in btns_nums:
        #             count += 1
        #     if count == 3:
        #         wanted_line = case
        #         break
        #     else:
        #         count = 0
        # print(count)
        # print(wanted_line)

    def tie(self):
        if self.crossed_boxs == 9 and self.uncrossed_boxs == 0:
            self.app.open_score('tie', self.mode)
        else:
            pass

    def reset(self):
        # resets everything
        self.player_moves1.clear()
        self.player_moves2.clear()
        self.crossed_boxs = 0
        self.uncrossed_boxs = 9
        self.winner = ''
        self.app = ''