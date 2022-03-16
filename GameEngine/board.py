import json
import random
from GameEngine import solver
from GameEngine.immutable_square_error import ImmutableSquareError
from copy import deepcopy


class Board:
    _size = 9

    def __init__(self, difficulty: int) -> None:
        """
        Constructor: Handles generation of board
        :param difficulty: game difficulty
        """
        self.board_states = []
        self.undone_states = []

        # Generate 8 empty rows
        board = [[0 for i in range(self._size)] for j in range(self._size - 1)]  # Empty board

        # Generate 1 1-9 shuffled row at top
        board.insert(0, [*range(1, self._size + 1)])
        random.shuffle(board[0])

        # Fill the 8 remaining rows by bruteforce solving
        solver.brute_solve(board)

        """
        Shuffling rows for random board
        """

        # Shuffles the rows within each 3x3 borders 4-10 times
        # https://blog.forret.com/2006/08/14/a-sudoku-challenge-generator/
        for n in range(random.randint(4, 10)):
            r1 = random.randint(0, 2)
            r2 = random.randint(0, 2)
            board[r1], board[r2] = board[r2], board[r1]
            board[r1 + 3], board[r2 + 3] = board[r2 + 3], board[r1 + 3]
            board[r1 + 6], board[r2 + 6] = board[r2 + 6], board[r1 + 6]

        self.solved_state = deepcopy(board)

        """
        Remove squares
        """
        max_removals = self._size ** 2 // 2
        if difficulty == 3:
            max_removals += random.randint(15, 25)
        elif difficulty == 2:
            max_removals += random.randint(10, 15)

        removals = 0
        while removals < max_removals:
            y = random.randint(0, self._size - 1)
            x = random.randint(0, self._size - 1)
            if board[y][x] == 0:
                continue
            board[y][x] = 0
            removals += 1

        self.board_states.append(deepcopy(board))

    def undo(self) -> []:
        """
        Undo function
        :return:
        """
        if len(self.board_states) == 1:
            return
        self.undone_states.append(self.board_states.pop())

    def redo(self) -> None:
        """
        Redo function
        :return:
        """
        if not self.undone_states:
            return
        self.board_states.append(self.undone_states.pop())

    def is_immutable(self, y, x) -> bool:
        """
        Checks if board is immutable
        :param y: row number (y-coordinate)
        :param x: column number (x-coordinate)
        """
        return self.board_states[0][y][x] != 0

    def is_solved(self) -> bool:
        """
        Check if board is solved
        :return:
        """
        for row_num in range(self._size):
            if self.board_states[-1][row_num] != self.solved_state[row_num]:
                return False
        return True

    def set_square(self, x, y, v) -> None:
        """
        Set digit to square
        :param x:
        :param y:
        :param v:
        :return:
        """
        y, x, v = int(y), int(x), int(v)
        for value in (y, x):
            if not self._size > value >= 0:
                raise ValueError
        if not self._size >= v >= 0:
            raise ValueError
        if self.is_immutable(y, x):
            raise ImmutableSquareError
        self.board_states.append(deepcopy(self.board_states[-1]))
        self.board_states[-1][y][x] = v

    def to_json(self):
        """
        Serialize to JSON file
        :return:
        """
        with open('save_file.json', 'w') as file:
            file.write(json.dumps(self, default=lambda o: o.__dict__, indent=4))
