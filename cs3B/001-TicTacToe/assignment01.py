"""
CS3B, Assignment #1, Tic-tac-toe (Part 1)
Nicholas Noochla-or
I wasn't able to get the winner method to fully function correctly. 
"""

import time
from enum import Enum, auto


class GameBoardPlayer(Enum):
    """
    An enum that represents a player on a game board; it's used to denote:
    . which player occupies a space on the board (can be NONE if unoccupied)
    . which player is the winner of the game (can be DRAW)
    """
    NONE = auto()
    X = auto()
    O = auto()
    DRAW = auto()
    def __str__(self):
        if(self.name == 'NONE'):
            return(' ')
        return (f"{self.name}")



class ArrayGameBoard:
    """A class that represents a rectangular game board"""
    board = []

    def __init__(self, nrows, ncols):
        try:
            if(nrows >= 0 and ncols >= 0):
                self.nrows = nrows
                self.ncols = ncols
                self.board = [[] for i in range(nrows)]
                for i in range(nrows):
                    for j in range(ncols):
                        self.board[i].append(GameBoardPlayer.NONE)
            else:
                raise ValueError
        except ValueError:
            print("Please input a positive integer for rows and columns")

    def get_nrows(self):
        print(self.ncols.values)
        return (self.nrows.values)

    def get_ncols(self):
        return self.ncols.name

    def set(self, row, col, value):
        if(row >= 0 and col >= 0):
            self.board[row][col] = value

    def get(self, row, col):
        if(row >= 0 and col >= 0):
            return (self.board[row][col])

    def __str__(self):
        x = []
        
        for i in range(self.nrows):
            r_support = 0
            for j in range(self.ncols):
                
                if(self.board[i][j].name == 'NONE'):
                    x.append(' ')
                else:
                    x.append(self.board[i][j].name)

                if(j < self.ncols-1):
                    x.append('|')
                    r_support += 1
                elif(i < self.nrows-1):
                    x.append('\n-+-+-\n')
            
        return f"{''.join(x)}"

    def get_winner(self):
        # check rows for winner
        linecheck = 0
        for x in range(self.nrows):
            for y in range(self.ncols):
                if((self.board[x][y].name != 'NONE') and (y < self.ncols - 1) and (self.board[x][y] == self.board[x][y+1])):
                    linecheck += 1
                elif((self.board[x][y].name != 'NONE') and (linecheck == self.ncols-1)):
                    print("row check")
                    return self.board[x][y]

        # check colunms for winner
        linecheck = 0
        for x in range(self.ncols):
            for y in range(self.nrows):
                if((self.board[x][y].name != 'NONE') and (x < self.ncols - 1) and (self.board[x][y] == self.board[x+1][y])):
                    linecheck += 1
                    print(linecheck)
                elif((self.board[x][y].name != 'NONE') and (linecheck == self.nrows-1)):
                    return self.board[x][y]


        # check diags
        linecheck = 0
        if(self.nrows == self.ncols):
            for x in range(self.nrows):
                for y in range(self.ncols):
                    if((self.board[x][y].name != 'NONE' and (y < self.ncols-1) and (x < self.nrows-1) and (self.board[x][y] == self.board[x+1][y+1]))):
                        linecheck += 1
                        print(linecheck)
                    elif((self.board[x][y].name != 'NONE') and (linecheck == self.nrows-1)):
                        print("diag check")
                        return self.board[0][0]
        
        # check draw
        draw_check = 0
        for x in range(self.nrows):
            for y in range(self.ncols):
                if((self.board[x][y].name != 'NONE')):
                    draw_check += 1
                elif(draw_check == (self.ncols * self.nrows)):
                    return GameBoardPlayer.DRAW


        return GameBoardPlayer.NONE


class BitGameBoard:
    """A class that represents a rectangular game board"""

    def __init__(self, nrows, ncols):
        pass

    def get_nrows(self):
        pass

    def get_ncols(self):
        pass

    def set(self, row, col, player):
        pass

    def get(self, row, col):
        pass

    def __str__(self):
        return "(To be implemented)"

    def get_winner(self):
        return GameBoardPlayer.NONE


class TicTacToeBoard:
    """
    A class that represents a Tic Tac Toe game board.
    It's a thin wrapper around the actual game board
    """
    NROWS = 3
    NCOLS = 3

    def __init__(self):
        # The two game boards can be used interchangeably.
        self.board = ArrayGameBoard(self.NROWS, self.NCOLS)
        # self.board = BitGameBoard(self.NROWS, self.NCOLS)

    def set(self, row, col, value):
        if self.board.get(row, col) != GameBoardPlayer.NONE:
            raise ValueError(f"{row} {col} already has {self.board.get(row, col)}")
        self.board.set(row, col, value)

    def clear(self, row, col):
        self.board.set(row, col, GameBoardPlayer.NONE)

    def get(self, row, col):
        return self.board.get(row, col)

    def get_winner(self):
        return self.board.get_winner()

    def __str__(self):
        return self.board.__str__()


def test_game_board(gb):
    # Test __str__()
    print(gb)

    print(f"winner of empty board is '{gb.get_winner()}'")

    # gb.set(0, 0, GameBoardPlayer.X)
    # gb.set(0, 1, GameBoardPlayer.X)
    # gb.set(0, 2, GameBoardPlayer.X)
    gb.set(0, 0, GameBoardPlayer.X)
    gb.set(1, 0, GameBoardPlayer.X)
    gb.set(2, 0, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print("gb.get(0, 2) returns", gb.get(0, 2))
    print(gb)
    print(gb.get_ncols)
    # print(gb.get_nrows)



    try:
        gb.get(100, 100)
        print("gb.get(100, 100) fails to raise IndexError")
    except IndexError:
        print("gb.get(100, 100) correctly raises IndexError")

    print(f"winner of board with 1 row of X is '{gb.get_winner()}'")

    # TODO add other tests (GameBoardPlayer.O, different rows, columns, diagonal, etc)


if __name__ == '__main__':
    # The same tests should work for both types of *GameBoard
    test_game_board(ArrayGameBoard(3, 3))
    # test_game_board(BitGameBoard(3, 3))
