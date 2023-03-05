import random

class Cell:

    def __init__(self, mine=False, around_mines=0):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:

    def __init__(self, N, M):
        """
        :param N: Размер поля
        :param M: Число мин
        """
        self.N = N
        self.M = M
        self.pole = [[Cell(False) for _ in range(self.N)] for _ in range(self.N)]
        self.init()
        self.check_mines()

    def check_mines(self):
        index = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for i in range(self.N):
            for j in range(self.N):
                if not self.pole[i][j].mine:
                    mines = sum(self.pole[i + x][j + y].mine for x, y in index
                                if 0 <= x + i < self.N
                                and 0 <= y + j < self.N)
                    self.pole[i][j].around_mines = mines

    def init(self):
        m = 0
        while m < self.M:
            x, y = [random.randint(0, self.N - 1) for _ in range(2)]

            if self.pole[x][y].mine:
                continue
            self.pole[x][y].mine = True
            m += 1

    def show(self):
        for i in self.pole:
            for j in i:
                if j.fl_open:
                    print(j.around_mines if not j.mine else '*', end=' ')
                else:
                    print("#", end=' ')
            print()


pole_game = GamePole(N=10, M=12)
pole_game.show()
