import copy
import os

from GameEngine.Board import Board
from GameEngine.ImmutableSquareError import ImmutableSquareError


def clear_screen():  # https://stackoverflow.com/a/50560686
    """
    Clears terminal screen
    """
    print("\033[H\033[J", end="")


def center_text(lines, width=None):
    """
    Center text to terminal screen
    :param lines: lines to be centered
    :param width: optional width length
    :return lines: centered lines
    """
    if width is None:
        width = os.get_terminal_size().columns  # https://stackoverflow.com/a/33595028
    for i in range(len(lines)):
        lines[i] = lines[i].center(width)
    return lines


def print_board(board: Board):
    clear_screen()
    """
    Prints board
    :param board: Sudoku board
    """
    # Indices
    to_print = [' '.join(str(i) for i in range(0, 9)), '—' * 19]

    # Values
    for row_num, row in enumerate(board.current_state):
        to_print.append(f"{row_num} | {' '.join([str(d) for d in row])} | {row_num}")

    # Indices
    to_print.append('—' * 19)
    to_print.append(' '.join(str(i) for i in range(0, 9)))

    center_text(to_print)

    print(*to_print, sep="\n")


def print_menu(menu_text):
    """
    Prints game menu
    :param menu_text:
    :return:
    """
    clear_screen()
    to_print = copy.deepcopy(menu_text)
    max_len = len(max(menu_text, key=len))
    to_print.insert(0, "-" * max_len)
    to_print.insert(3, "-" * max_len)
    to_print.append("-" * max_len)

    center_text(to_print, max_len)

    print(*to_print, sep="\n")
    print()


class Game:
    menu_text = [
        "(dan)doku",
        "Author: lawclaw",
        "Easy. 1",
        "Medium. 2",
        "Hard. 3",
        "Quit. Q"
    ]

    game_loop_text = [
        "Enter x, y coordinates and desired value [1-9] separated by comma:",
        "Enter Q to quit",
        "Immutable square...(Press Enter key to try again)\n",
        "Invalid input...(Press Enter key to try again)\n"
    ]

    def __init__(self):
        """
        Main game
        """
        while True:
            # Menu
            print_menu(self.menu_text)
            choice = input("Enter: ")
            if len(choice) > 1:
                continue

            if choice in "Qq":
                exit()
            elif int(choice) in range(0, 4):
                current_board = Board(choice)
                self.game_loop(current_board)

    def game_loop(self, current_board):
        """
        Game loop
        :param current_board:
        :return:
        """
        while not current_board.is_solved():
            print_board(current_board)
            print()
            print(*center_text([self.game_loop_text[0]]))
            print(*center_text([self.game_loop_text[1]]))

            try:
                user_inputs = input("".center(os.get_terminal_size().columns // 2 - 2)).split(',')
                if user_inputs[0] in "Qq":
                    break
                current_board.set_square(user_inputs[0], user_inputs[1], user_inputs[2])
            except ImmutableSquareError:
                input(*center_text([self.game_loop_text[2]]))
            except ValueError:
                input(*center_text([self.game_loop_text[3]]))
