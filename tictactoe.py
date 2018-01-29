import sys
import os

"""
    python 2.7 compatible code 
"""

def str_to_int(val):
    try:
        return int(val)
    except Exception as e:
        return ''

def main(argv=sys.argv):
    os.system('cls' if os.name == 'nt' else 'clear')
    turn = 1
    while True:
        print 'Enter board size (NxN): '
        sys.stdout.write('>> ')
        board_size = raw_input()
        board_size = str_to_int(board_size)
        if type(board_size) is int and board_size >= 3:
            tic_tac_toe = TicTacToe(board_size)
            break
    while True:
        print 'Enter name for Player 1:'
        sys.stdout.write('>> ')
        player_1 = raw_input()
        if len(player_1) > 0:
            break
    while True:
        print 'Enter name for Player 2:'
        sys.stdout.write('>> ')
        player_2 = raw_input()
        if len(player_2) > 0:
            break
    while True:
        while True:
            tic_tac_toe.printArr()
            if turn == 1:
                print player_1 + ', choose a box to place an "O" into:'
            else:
                print player_2 + ', choose a box to place an "X" into:'
            sys.stdout.write('>> ')
            value = raw_input()
            value = str_to_int(value)
            if type(value) is int:
                if tic_tac_toe.place(turn, value) is True:
                    turn = -1 if turn == 1 else 1
                    break

        result = tic_tac_toe.determine()
        if result != 0:
            tic_tac_toe.printArr()
            if result == 1 or result == 2:
                winner = player_1 if result == 1 else player_2
                print 'Congraturations ' + winner + ' ! You have won'
            elif result == 3:
                print 'Draw!'
            break
    return

class TicTacToe():
    def __init__(self, size):
        self.arr_size = size
        self.arr = []
        for x in xrange(size):
            self.arr.append([0] * size)

    def place(self, turn, value):
        if type(value) is not int:
            return False
        if value < 0 or value > pow(2, self.arr_size):
            return False
        col = (value - 1) / self.arr_size
        row = (value - 1) % self.arr_size
        if self.arr[col][row] != 0:
            return False
        else:
            self.arr[col][row] = turn
            return True

    def printArr(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print ' '
        for x in xrange(self.arr_size):
            txt = ''
            for y in xrange(self.arr_size):
                val = (self.arr_size * x) + y + 1
                if self.arr[x][y] == 0:
                    txt += str(val).center(8)
                elif self.arr[x][y] == -1:
                    txt += 'X'.center(8)
                else:
                    txt += 'O'.center(8)
                if y < self.arr_size - 1:
                    txt += '|'
            print txt
            print '-' * len(txt)
        print ' '

    """
        determining game with a brute force approach
        return value
            0: not done
            1: player 1 won
            2: player 2 won
            3: draw
    """
    def determine(self):
        completed = True
        for x in xrange(self.arr_size):
            for y in xrange(self.arr_size):
                if self.arr[x][y] == 0:
                    completed = False
                    continue
                if x + 2 < self.arr_size and y + 2 < self.arr_size:
                    new_arr = []
                    for t in self.arr[x:x+3]:
                        new_arr.append(t[y:y+3])
                    result = self.check(new_arr)
                    if result == 1 or result == 2:
                        return result

        return 0 if not completed else 3

    def check(self, arr):
        # horizontal check
        for x in arr:
            if sum(x) == -3:
                return 2
            elif sum(x) == 3:
                return 1
        # vertical check
        for x in range(3):
            summ = 0
            for y in range(3):
                summ += arr[y][x]
            if summ == -3:
                return 2
            elif summ == 3:
                return 1

        # diagonal check
        axe1 = arr[0][0] + arr[1][1] + arr[2][2]
        axe2 = arr[0][2] + arr[1][1] + arr[2][0]
        if axe1 == -3 or axe2 == -3:
            return 2
        elif axe1 == 3 or axe2 == 3:
            return 1

        return 0

if __name__ == '__main__':
    main()
