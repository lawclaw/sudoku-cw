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


def print_board(board: Board, stdscr: curses.wrapper):
    """
    Prints board
    :param board: Sudoku board
    """
    clear_screen(stdscr)
    # Indices
    to_print = [' '.join(str(i) for i in range(0, 9)), '—' * 19]

    # Values
    for row_num, row in enumerate(board.current_state):
        to_print.append(f"{row_num} | {' '.join([str(d) for d in row])} | {row_num}")

    # Indices
    to_print.append('—' * 19)
    to_print.append(' '.join(str(i) for i in range(0, 9)))

    # Add lines to stdscr
    for i, line in enumerate(to_print):
        stdscr.addstr(
            curses.LINES // 10 + i,
            curses.COLS // 2 - ((len(line) + 1) // 2),
            f"{line}\n"
        )

    # Refresh screen
    stdscr.refresh()

def print_menu(menu_text, stdscr):
    """
    Prints game menu
    :param menu_text:
    :return:
    """
    clear_screen(stdscr)
    for i, str in enumerate(menu_text):
        stdscr.addstr(
            curses.LINES // 3 + i,
            curses.COLS // 2 - ((len(str) + 1) // 2),
            f"{str}\n"
        )

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

            stdscr.addstr(
                curses.LINES // 2 + 3,
                curses.COLS // 2 - (len("Enter: ") - 1 // 2),
                "Enter: ")
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
                    self.game_loop(board, stdscr)
                    break
                else:
                    stdscr.addstr("\nInvalid input, press Enter to try again")
                    stdscr.refresh()
                    stdscr.getch()




    def game_loop(self, current_board, stdscr):
        """
        Game loop
        :param current_board:
        :return:
        """
        while not current_board.is_solved():
            clear_screen(stdscr)
            # Print board
            print_board(current_board, stdscr)
            # Print prompt
            y, x = curses.getsyx()

            stdscr.addstr(
                y + 1,
                curses.COLS // 2 - ((len(self.game_loop_text[0]) + 1) // 2),
                f"{self.game_loop_text[0]}\n")

            stdscr.addstr(
                y + 2,
                curses.COLS // 2 - ((len(self.game_loop_text[1]) + 1) // 2),
                f"{self.game_loop_text[1]}\n")

            try:
                y, x = curses.getsyx()
                stdscr.move(
                    y + 3,
                    curses.COLS // 2 - 3
                )
                raw_inputs = stdscr.getstr(5)
                str_input = str(raw_inputs, "utf-8").split(',')
                if str_input[0] == "Q" or str_input[0] == "q":
                    break
                current_board.set_square(str_input[0], str_input[1], str_input[2])
            except ImmutableSquareError:
                stdscr.addstr(self.game_loop_text[2])
                stdscr.refresh()
                stdscr.getch()
            except ValueError:
                stdscr.addstr(self.game_loop_text[3])
                stdscr.refresh()
                stdscr.getch()
            except IndexError:
                stdscr.addstr(self.game_loop_text[3])
                stdscr.refresh()
                stdscr.getch()

