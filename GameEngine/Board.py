import random
from GameEngine import Solver
from GameEngine.ImmutableSquareError import ImmutableSquareError
from copy import deepcopy


class Board:
    __size = 9
    current_state = []
    original_state = []
    solved_state = []
    max_removals = __size ** 2 // 2

    def __init__(self, difficulty: int):
        """
        Constructor: Handles generation of board
        :param difficulty: game difficulty
        """
        # Generate 8 empty rows
        self.current_state = [[0 for i in range(self.__size)] for j in range(self.__size - 1)]  # Empty board

        # Generate 1 1-9 shuffled row at top
        self.current_state.insert(0, [*range(1, self.__size + 1)])
        random.shuffle(self.current_state[0])

        # Fill the 8 remaining rows by bruteforce solving
        Solver.brute_solve(self.current_state)

        """
        Shuffling rows for random board
        """

        # Shuffles the rows within each 3x3 borders 3 times
        # https://blog.forret.com/2006/08/14/a-sudoku-challenge-generator/
        for n in range(random.randint(4, 30)):
            r1 = random.randint(0, 2)
            r2 = random.randint(0, 2)
            self.current_state[r1], self.current_state[r2] = self.current_state[r2], self.current_state[r1]
            self.current_state[r1 + 3], self.current_state[r2 + 3] = self.current_state[r2 + 3], self.current_state[
                r1 + 3]
            self.current_state[r1 + 6], self.current_state[r2 + 6] = self.current_state[r2 + 6], self.current_state[
                r1 + 6]

        self.solved_state = deepcopy(self.current_state)

        """
        Remove squares
        """
        if difficulty == 3:
            self.max_removals += random.randint(15, 25)
        elif difficulty == 2:
            self.max_removals -= random.randint(10, 15)

        removals = 0
        while removals < self.max_removals:
            y = random.randint(0, self.__size - 1)
            x = random.randint(0, self.__size - 1)
            if self.current_state[y][x] == 0:
                continue
            self.current_state[y][x] = 0
            removals += 1

        self.original_state = deepcopy(self.current_state)

    def is_immutable(self, y, x):
        """
        Checks if board is immutable
        :param y: row number (y-coordinate)
        :param x: column number (x-coordinate)
        """
        return self.original_state[y][x] != 0

    def is_solved(self):
        """
        Checks if the board is solved
        """
        for row_num in range(self.__size):
            if self.current_state[row_num] != self.solved_state[row_num]:
                return False;
        return True

    def set_square(self, y, x, v):
        y, x, v = int(y), int(x), int(v)
        for value in [y, x, v]:
            if not self.__size > value >= 0:
                raise ValueError
        if self.is_immutable(y, x):
            raise ImmutableSquareError
        self.current_state[y][x] = v
