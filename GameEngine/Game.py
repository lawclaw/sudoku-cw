import copy
import os
import curses

from curses.textpad import Textbox
from GameEngine.Board import Board
from GameEngine.ImmutableSquareError import ImmutableSquareError

def clear_screen(stdscr):  # https://stackoverflow.com/a/50560686
    """
    Clears terminal screen
    """
    stdscr.clear()
    stdscr.refresh()


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


def print_menu(menu_text, stdscr):
    """
    Prints game menu
    :param menu_text:
    :return:
    """
    clear_screen(stdscr)
    for str in menu_text:
        stdscr.addstr(f"{str}\n")

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

    def __init__(self, stdscr: curses.wrapper):
        """
        Main game
        """
        while True:
            curses.echo()
            # Menu
            print_menu(self.menu_text, stdscr)
            stdscr.addstr("Enter: ")
            stdscr.refresh()

            # Input
            key = None
            while key is None:
                key = stdscr.getkey()
                # Exit condition
                if key in 'Qq':
                    exit()
                # Check if key is numeric
                elif key in '123':
                    board = Board(key)
                    self.game_loop(board)
                    break
                else:
                    stdscr.addstr("\nInvalid input, press Enter to try again")
                    stdscr.refresh()
                    stdscr.getch()




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
                if user_inputs[0] == "Q" or user_inputs[0] == "q":
                    break
                current_board.set_square(user_inputs[0], user_inputs[1], user_inputs[2])
            except ImmutableSquareError:
                input(*center_text([self.game_loop_text[2]]))
            except ValueError:
                input(*center_text([self.game_loop_text[3]]))
            except IndexError:
                input(*center_text([self.game_loop_text[3]]))
