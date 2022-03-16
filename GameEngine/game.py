import curses
import sys

from ConsolePrint.ui import print_menu, hide_cursor, clear_screen, print_board, color_prepare
from GameEngine.board import Board
from GameEngine.immutable_square_error import ImmutableSquareError


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
        "Enter x, y coordinates and desired value [1-9] separated by comma:\n",
        "Enter Q to quit\n",
        "Immutable square...(Press Enter key to try again)\n",
        "Invalid input...(Press Enter key to try again)\n",
        "You solved the puzzle!"
    ]

    def __init__(self, stdscr: curses.wrapper):
        """
        Main game
        """
        while True:
            # Curses initialization
            curses.echo()
            color_prepare()

            # Check if screen size is big enough
            max_y, max_x = stdscr.getmaxyx()
            if max_y < 25 or max_x < 66:
                stdscr.addstr(f"Too small window! Increase to at least 23x66")
                stdscr.getch()
                sys.exit()

            # Menu
            print_menu(self.menu_text, stdscr)
            stdscr.addstr(
                curses.LINES // 2 + 3,
                curses.COLS // 2 - (len("Enter: ") - 1 // 2),
                "Enter: ")
            stdscr.refresh()

            # Input
            try:
                raw_input = stdscr.getstr(1)
                key = str(raw_input, "utf-8")
                # Exit condition
                if key == 'Q' or key == "q":
                    sys.exit()
                # Check if key is numeric
                elif key == '1' or key == '2' or key == '3':
                    board = Board(int(key))
                    self.game_loop(board, stdscr)
                else:
                    raise UnicodeError
            except UnicodeError:
                stdscr.addstr(
                    curses.LINES // 2 + 4,
                    curses.COLS // 2 - (len("Invalid input, press Enter to try again") // 2),
                    "Invalid input, press Enter to try again")
                stdscr.refresh()
                hide_cursor(stdscr)

    def load(self, board):
        """
        Load board
        :param board:
        :return:
        """

    def save(self, board):
        """
        Save board
        :param board:
        :return:
        """
        board.to_json()

    def game_loop(self, current_board, stdscr):
        """
        Game loop
        :param stdscr:
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
                curses.COLS // 2 - (len(self.game_loop_text[0]) // 2),
                f"{self.game_loop_text[0]}")

            stdscr.addstr(
                y + 2,
                curses.COLS // 2 - (len(self.game_loop_text[1]) // 2),
                f"{self.game_loop_text[1]}")

            try:
                y, x = curses.getsyx()
                stdscr.move(
                    y + 3,
                    curses.COLS // 2 - 3
                )
                raw_inputs = stdscr.getstr(5)
                str_input = str(raw_inputs, "utf-8").split(',')
                if str_input[0] == "Q" or str_input[0] == "q":
                    self.save(current_board)
                    break
                elif str_input[0] == "U" or str_input[0] == "u":
                    current_board.undo()
                elif str_input[0] == "R" or str_input[0] == "r":
                    current_board.redo()
                else:
                    current_board.set_square(str_input[0], str_input[1], str_input[2])
            except ImmutableSquareError:
                stdscr.addstr(
                    y + 4,
                    curses.COLS // 2 - ((len(self.game_loop_text[2]) + 1) // 2),
                    self.game_loop_text[2])
                stdscr.refresh()
                hide_cursor(stdscr)

            except (ValueError, IndexError):
                stdscr.addstr(
                    y + 4,
                    curses.COLS // 2 - ((len(self.game_loop_text[3]) + 1) // 2),
                    self.game_loop_text[3])
                stdscr.refresh()
                hide_cursor(stdscr)

        # Solved puzzle!
        if current_board.is_solved():
            stdscr.addstr(
                y + 4,
                curses.COLS // 2 - ((len(self.game_loop_text[4]) + 1) // 2),
                self.game_loop_text[4])
            stdscr.refresh()
            hide_cursor(stdscr)
