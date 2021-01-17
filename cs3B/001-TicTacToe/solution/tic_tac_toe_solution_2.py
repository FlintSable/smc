"""
CS3B, Assignment #1, Tic Tac Toe, Part 1
Copyright 2020 Zibin Yang
Instructor's solution
"""

from enum import Enum


class GameBoardPlayer(Enum):
    """
    An enum that represents a player on a game board; it's used to denote:
    . which player occupies a space on the board (can be NONE if unoccupied)
    . which player is the winner of the game (can be DRAW)
    """
    NONE = 0
    X = 1
    O = 2
    DRAW = 3

    def __str__(self):
        if self is GameBoardPlayer.NONE:
            return " "
        else:
            return self.name


class ArrayGameBoard:
    """A class that represents a rectangular game board"""

    def __init__(self, nrows, ncols):
        """
        Initialize a game board that internally represents the board using
        Python list of lists.
        :param nrows: number of rows
        :param ncols: number of columns
        """
        if nrows <= 0 or ncols <= 0:
            raise ValueError(f"Invalid nrows={nrows} ncols={ncols}")
        self.board = [[GameBoardPlayer.NONE for _ in range(ncols)]
                      for _ in range(nrows)]

    def get_nrows(self):
        return len(self.board)

    def get_ncols(self):
        return len(self.board[0])

    def set(self, row, col, value):
        """Set row/col on the board to value"""
        # No need to validate row/col ourselves; Python list[][] does that.
        self.board[row][col] = value

    def get(self, row, col):
        """Return the value at row/col on the board"""
        return self.board[row][col]

    # From here on, it's exactly the same code in both ArrayGameBoard and
    # BitGameBoard
    def __str__(self):
        s = ""
        for row in range(self.get_nrows()):
            # The row
            s += "|".join([str(self.get(row, col))
                           for col in range(self.get_ncols())]) + "\n"

            # The separator
            if row != self.get_nrows() - 1:
                s += "-+" * (self.get_ncols() - 1) + "-\n"
        return s

    def get_row_winner(self, row):
        """Given row index, see if there's a winner on that row"""

        # # Using Python's set and/or all() can make code shorter
        # if all(self.get(row, 0) == self.get(row, i) for i in range(self.get_ncols())):
        #     return self.get(row, 0)
        # else:
        #     return GameBoardPlayer.NONE

        # The code here shows how to do it with plain old for loop.
        for col in range(self.get_ncols()):
            if self.get(row, 0) != self.get(row, col):
                # If any other element on the row is different from the first
                # one, there's no winner in this row
                return GameBoardPlayer.NONE

        # Every element in the row is the same as the first, so it's a winner.
        # All elements may be NONE, but the caller checks for that.
        return self.get(row, 0)

    def get_col_winner(self, col):
        """Given column index, see if there's a winner on that column"""
        for row in range(self.get_nrows()):
            if self.get(0, col) != self.get(row, col):
                return GameBoardPlayer.NONE

        return self.get(0, col)

    def get_diag_winner(self):
        """If a square board, check if the two diagonals have winner"""
        if self.get_nrows() != self.get_ncols():
            return GameBoardPlayer.NONE

        # Get the winner in the \ diagonal
        upper_left = self.get(0, 0)
        if upper_left is not GameBoardPlayer.NONE:
            for row in range(self.get_nrows()):
                if upper_left != self.get(row, row):
                    break
            else:
                # If the for loop completes without break, all elements in
                # the diagonal is the same, so it's a winner
                return upper_left

        # Get the winner in the / diagonal
        upper_right = self.get(0, self.get_ncols() - 1)
        if upper_right is not GameBoardPlayer.NONE:
            for row in range(self.get_nrows()):
                if upper_right != self.get(row, -row - 1):
                    break
            else:
                return upper_right

        return GameBoardPlayer.NONE

    def check_for_draw(self):
        """Check if the game is DRAW; used after checking for winners."""
        for row in range(self.get_nrows()):
            for col in range(self.get_ncols()):
                if self.get(row, col) is GameBoardPlayer.NONE:
                    # If any space is unoccupied, it's not a draw
                    return GameBoardPlayer.NONE

        return GameBoardPlayer.DRAW

    def get_winner(self):
        """
        Get the winner on the board
        :return: one of GameBoardPlayer members to indicate the winner.
        """
        # Check for horizontal rows
        for row in range(self.get_nrows()):
            winner = self.get_row_winner(row)
            if winner is not GameBoardPlayer.NONE:
                return winner

        # Check for vertical columns
        for col in range(self.get_ncols()):
            winner = self.get_col_winner(col)
            if winner is not GameBoardPlayer.NONE:
                return winner

        # Check for diagonal if it's a square
        winner = self.get_diag_winner()
        if winner is not GameBoardPlayer.NONE:
            return winner

        # Finally, check for ties
        return self.check_for_draw()

    def get_winner_pythonic(self):
        # This is a succinct and pythonic way of writing get_winner().  It's not required
        # understanding, because it uses things we haven't covered, like nested function,
        # set(), and generator.  It does demonstrate Python's capabilities.
        # (Credits to Shoshi C. for the inspiration.)

        def same(list_):
            """This returns True if all elements in list_ are the same, False otherwise."""
            # Convert list into set, and because set doesn't allow duplicate,
            # length of 1 means all elements in the list are the same element.
            return len(set(list_)) == 1

        def rows():
            """Yields (returns) all rows on the board."""
            # The commented line accesses the 2d list directly; actual line uses get().
            # yield from (row for row in self.board)
            yield from ([self.get(r, c) for c in range(self.get_ncols())]
                        for r in range(self.get_nrows()))

        def cols():
            """Yields (returns) all rows on the board."""
            # zip(*self.board) transposes the board.
            # yield from (row for row in zip(*self.board))
            yield from ([self.get(r, c) for r in range(self.get_nrows())]
                        for c in range(self.get_ncols()))

        def combos():
            """This generates all rows, columns, then diagonals"""

            # We can return a complete list of all rows, columns and diagonals, but that's
            # likely wasteful if there's a winner on the board.  So use a generator instead
            # (that's the "yield" and "yield from", and using () instead of []), so we only
            # generate the next one if we haven't found a winner yet.

            # Yield all rows
            yield from rows()

            # Yield all columns
            yield from cols()

            if self.get_nrows() == self.get_ncols():
                # Yield / diagonal
                # yield [row[i] for i, row in enumerate(self.board)]
                yield [self.get(i, i) for i in range(self.get_nrows())]
                # Yield | diagonal (reverse every row first, so \ becomes /)
                # yield [row[i] for i, row in enumerate(list(reversed(row)) for row in self.board)]
                yield [self.get(i, -i-1) for i in range(self.get_nrows())]

        # This is what get_winner() actually does.
        # Check for winners in rows, columns, diagonals
        for combo in combos():
            if combo[0] is not GameBoardPlayer.NONE and same(combo):
                return combo[0]

        # If no winner, check if there's any empty space
        if any(GameBoardPlayer.NONE in row for row in rows()):
            return GameBoardPlayer.NONE

        # No winner and no empty space, it's a draw
        return GameBoardPlayer.DRAW


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
    """A class that represents a Tic Tac Toe game board"""
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

    gb.set(0, 0, GameBoardPlayer.X)
    gb.set(0, 1, GameBoardPlayer.X)
    gb.set(0, 2, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print("gb.get(0, 2) returns", gb.get(0, 2))

    try:
        gb.get(100, 100)
        print("gb.get(100, 100) fails to raise IndexError")
    except IndexError:
        print("gb.get(100, 100) correctly raises IndexError")

    print(f"winner of board with 1 row of X is '{gb.get_winner()}'")

    # TODO add other tests (GameBoardPlayer.O, different rows, columns, diagonal, etc)
    # Additional tests not added in instructor's solution.  See the accompanied
    # unittest test (when available) for test coverage.


if __name__ == '__main__':
    # The same tests should work for both types of *GameBoard
    test_game_board(ArrayGameBoard(3, 3))
    # test_game_board(BitGameBoard(3, 3))