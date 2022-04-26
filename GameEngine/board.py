import json
import random
from GameEngine import solver
from GameEngine.immutable_square_exception import ImmutableSquareException
from copy import deepcopy


class Board:
    _size = 9   # Board size

    def __init__(self, difficulty: int, load: bool = None) -> None:
        """
        Constructor: Handles generation of board
        :param difficulty: game difficulty
        """
        # TODO: Implement stack using deque
        self.board_states = []  # List of board states
        self.undone_states = []  # List of all undone player moves
        self.solved_state = []  # Solved state

        # If not loading from JSON
        if load is None:
            self.generate_new_board(difficulty)
        else:  # If load option is selected
            self.from_json()

    def generate_new_board(self, difficulty: int) -> None:
        """
        Generates Sudoku board
        :param difficulty: chosen player difficulty
        :return: None
        """
        # Generate 8 empty rows
        board = [[0 for _ in range(self._size)] for _ in range(self._size - 1)]  # Empty board

        # Generate 1 1-9 shuffled row at top
        board.insert(0, [*range(1, self._size + 1)])
        random.shuffle(board[0])

        # Fill the 8 remaining rows by bruteforce solving
        solver.brute_solve(board)

        # Shuffles the rows within each 3x3 borders 4-10 times
        # https://blog.forret.com/2006/08/14/a-sudoku-challenge-generator/
        for n in range(random.randint(4, 10)):
            r1 = random.randint(0, 2)
            r2 = random.randint(0, 2)
            board[r1], board[r2] = board[r2], board[r1]
            board[r1 + 3], board[r2 + 3] = board[r2 + 3], board[r1 + 3]
            board[r1 + 6], board[r2 + 6] = board[r2 + 6], board[r1 + 6]

        self.solved_state = deepcopy(board)

        # Remove squares
        max_removals = self._size ** 2 // 2
        if difficulty == 3:
            max_removals += random.randint(15, 25)
        elif difficulty == 2:
            max_removals += random.randint(10, 15)

        removals = 0
        # DEBUG
        removals = max_removals - 3

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
        Undo functionality
        :return: None
        """
        if len(self.board_states) == 1:
            return
        self.undone_states.append(self.board_states.pop())

    def redo(self) -> None:
        """
        Redo functionality
        :return: None
        """
        if not self.undone_states:
            return
        self.board_states.append(self.undone_states.pop())

    def reset(self) -> None:
        """
        Resets the board to its original state
        :return:
        """
        temp = self.board_states[0]
        self.board_states.clear()
        self.board_states.append(temp)

    def get_number_of_empty_squares(self) -> int:
        """
        Gets the number of empty squares
        :return: number of unfilled squares
        """
        empty_squares: int = 0
        for y in range(self._size):
            for x in range(self._size):
                if self.board_states[-1][y][x] == 0:
                    empty_squares += 1
        return empty_squares

    def is_immutable(self, y, x) -> bool:
        """
        Checks if board is immutable
        :param y: row number (y-coordinate)
        :param x: column number (x-coordinate)
        :return: bool: if board square is immutable
        """
        return self.board_states[0][y][x] != 0

    def is_solved(self) -> bool:
        """
        Check if board is solved
        :return: bool: if board is solved
        """
        for row_num in range(self._size):
            if self.board_states[-1][row_num] != self.solved_state[row_num]:
                return False
        return True

    def set_square(self, x, y, value) -> None:
        """
        Set digit to square
        :param x: x coordinate (column number)
        :param y: y coordinate (row number)
        :param value: digit to insert
        :return: None
        """
        y, x, v = int(y), int(x), int(value)
        for value in (y, x):
            if not self._size > value >= 0:
                raise ValueError
        if not self._size >= v >= 0:
            raise ValueError
        if self.is_immutable(y, x):
            raise ImmutableSquareException
        self.board_states.append(deepcopy(self.board_states[-1]))  # Copy current state and append on list
        self.board_states[-1][y][x] = v  # Change top state square with digit

    def to_json(self) -> None:
        """
        Serialize to JSON file
        :return: None
        """
        with open('save_file.json', 'w') as file:
            file.write(json.dumps(self, default=lambda o: o.__dict__, indent=4))

    def from_json(self) -> None:
        """
        Read from JSON file
        :return: None
        """
        with open('save_file.json', 'r') as file:
            attributes = json.loads(file.read())
        self.board_states = attributes['board_states']
        self.undone_states = attributes['undone_states']
        self.solved_state = attributes['solved_state']

    @property
    def size(self):
        return self._size ** 2
