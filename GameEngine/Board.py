from GameEngine import Solver
import random


class Board:
    size = 9
    current_state = []
    original_state = []
    solved_state = []
    max_removals = 60

    def __init__(self, difficulty):
        # TODO: Generate puzzle
        # No board is given on start:
        self.current_state = [[0 for i in range(9)] for j in range(9)]  # Empty board
        Solver.brute_solve(self.current_state)  # 123 board

        # Shuffles the rows within each 3x3 borders 3 times
        # https://blog.forret.com/2006/08/14/a-sudoku-challenge-generator/
        for n in range(random.randint(4, 30)):
            r1 = random.randint(0, 2)
            r2 = random.randint(0, 2)
            self.current_state[r1], self.current_state[r2] = self.current_state[r2], self.current_state[r1]
            self.current_state[r1 + 3], self.current_state[r2 + 3] = self.current_state[r2 + 3], self.current_state[r1 + 3]
            self.current_state[r1 + 6], self.current_state[r2 + 6] = self.current_state[r2 + 6], self.current_state[r1 + 6]
        self.solved_state = self.current_state
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
        self.original_state = self.current_state
