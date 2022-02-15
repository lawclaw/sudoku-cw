import random
from GameEngine import Solver
from copy import deepcopy


class Board:
    __size = 9
    current_state = []
    original_state = []
    solved_state = []
    max_removals = 60

    def __init__(self, difficulty):
        # Generate 8 empty rows
        self.current_state = [[0 for i in range(self.__size)] for j in range(self.__size - 1)]  # Empty board

        # Generate 1 1-9 shuffled row at top
        self.current_state.insert(0, [*range(1, 10)])
        random.shuffle(self.current_state[0])

        # Fill the 8 remaining rows by bruteforce
        Solver.brute_solve(self.current_state)

        # Shuffles the rows within each 3x3 borders 3 times
        # https://blog.forret.com/2006/08/14/a-sudoku-challenge-generator/
        for n in range(random.randint(4, 30)):
            r1 = random.randint(0, 2)
            r2 = random.randint(0, 2)
            self.current_state[r1], self.current_state[r2] = self.current_state[r2], self.current_state[r1]
            self.current_state[r1 + 3], self.current_state[r2 + 3] = self.current_state[r2 + 3], self.current_state[r1 + 3]
            self.current_state[r1 + 6], self.current_state[r2 + 6] = self.current_state[r2 + 6], self.current_state[r1 + 6]

        self.solved_state = deepcopy(self.current_state)
        # Remove squares
        removals = 0
        if difficulty == 1:
            self.max_removals -= random.randint(15, 20)
        elif difficulty == 2:
            self.max_removals -= random.randint(5, 10)

        while removals < self.max_removals:
            y = random.randint(0, 8)
            x = random.randint(0, 8)
            if self.current_state[y][x] == 0:
                continue

            self.current_state[y][x] = 0

            removals += 1

        self.original_state = deepcopy(self.current_state)

    def is_immutable(self, y, x):
        return self.original_state[y][x] != 0
