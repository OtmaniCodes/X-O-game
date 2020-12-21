from itertools import permutations as per


class TicTacToe:
    player_moves1 = []
    player_moves2 = []
    score = 0
    crossed_boxs = 0
    uncrossed_boxs = 9

    def win(self, turn):
        self.crossed_boxs += 1
        self.uncrossed_boxs -= 1
        print(self.crossed_boxs, self.uncrossed_boxs)
        winning_cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                         [1, 4, 7], [2, 4, 8], [0, 4, 8], [2, 4, 6]]
        if turn == 1:
            lista = self.player_moves1
        else:
            lista = self.player_moves2
        for case in winning_cases:
            for case2 in per(case, len(case)):
                for combination in per(lista, len(lista)):
                    if combination == case2:
                        return True
                    else:
                        pass
        return False

    def tie(self):
        if self.crossed_boxs == 9 and self.uncrossed_boxs == 0:
            print('tie')
        else:
            return False
