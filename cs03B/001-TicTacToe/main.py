"""
CS3B, Assignment #1, Tic Tac Toe
Copyright 2020 Zibin Yang
Starter code
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
        return self.nrows

    def get_ncols(self):
        return self.ncols

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
        for x in range(self.nrows):
            linecheck = False
            for y in range(self.ncols):
                # if(self.board[x][y].name == 'NONE'):
                #     return self.board[x][y].name
                print(x, y)
                # print(self.board[x][y].name != 'NONE')
                print(self.board[x][y].name)
                # print((self.board[x][y] == self.board[x][y+1]))
                if((self.board[x][y].name != 'NONE') and (y < self.ncols - 1) and (self.board[x][y] == self.board[x][y+1])):
                    linecheck = True
                elif((self.board[x][y].name != 'NONE') and (linecheck)):
                    return self.board[x][y]

        # check colums for winner
        for x in range(self.nrows):
            for y in range(self.ncols):
                if((self.board[x][y].name != 'NONE') and (y < self.ncols - 1) and (self.board[x][y] == self.board[x+1][y])):
                    linecheck = True
                elif((self.board[x][y].name != 'NONE') and (linecheck)):
                    return self.board[x][y]

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
    # gb.set(1, 0, GameBoardPlayer.X)
    # gb.set(1, 1, GameBoardPlayer.X)
    # gb.set(1, 2, GameBoardPlayer.X)
    gb.set(0, 2, GameBoardPlayer.X)
    gb.set(1, 2, GameBoardPlayer.X)
    gb.set(2, 2, GameBoardPlayer.X)    
    # print(gb.board)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print("gb.get(0, 2) returns", gb.get(0, 2))
    print(gb)

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
    
    # print(GameBoardPlayer.NONE)

