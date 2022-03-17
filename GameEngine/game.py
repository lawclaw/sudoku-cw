import curses
import sys

from ConsolePrint.ui import print_menu, hide_cursor, clear_screen, print_board, color_prepare, print_victory, \
    print_game_loop_text, print_input_error_text
from GameEngine.board import Board
from GameEngine.immutable_square_exception import ImmutableSquareException


class Game:
    def __init__(self, stdscr: curses.wrapper):
        """
        Main game
        """
        # Curses initialization
        curses.echo()
        color_prepare()

        # Check if screen size is big enough
        max_y, max_x = stdscr.getmaxyx()
        if max_x < 66 or max_y < 25:
            stdscr.addstr(f"Too small window! Increase to at least 66x25")
            stdscr.getch()
            sys.exit()

        while True:
            # Menu
            print_menu(stdscr)

            stdscr.addstr(
                curses.LINES // 2 + 4,
                curses.COLS // 2 - (len("Enter: ") - 1 // 2),
                "Enter: ",
                curses.A_BOLD)
            stdscr.refresh()

            # Input
            try:
                raw_input = stdscr.getstr(1)
                key = str(raw_input, "utf-8")
                # Exit condition
                if key == 'Q' or key == "q":
                    sys.exit()
                # Check if key is numeric
                if key == '4':
                    board = load_game()
                    game_loop(board, stdscr)
                elif key == '1' or key == '2' or key == '3':
                    board = Board(int(key))
                    game_loop(board, stdscr)
                else:
                    raise UnicodeError
            except UnicodeError:
                print_input_error_text(stdscr)


def save_game(board):
    """
    Save board
    :param board:
    :return: None
    """
    board.to_json()


def load_game():
    """
    Load board
    :return: Board: loaded Sudoku board
    """
    board = Board(4, True)
    return board


def game_loop(current_board, stdscr):
    """
    Game loop
    :param stdscr:
    :param current_board:
    :return: None
    """
    # Main loop
    while not current_board.is_solved():

        # Print board
        print_board(current_board, stdscr)

        # Print prompt
        print_game_loop_text(stdscr)

        try:
            y, x = curses.getsyx()
            stdscr.move(
                y + 4,
                curses.COLS // 2 - 3
            )
            raw_inputs = stdscr.getstr(5)
            str_input = str(raw_inputs, "utf-8").split(',')
            if str_input[0] == "Q" or str_input[0] == "q":
                save_game(current_board)
                break
            elif str_input[0] == "U" or str_input[0] == "u":
                current_board.undo()
            elif str_input[0] == "R" or str_input[0] == "r":
                current_board.redo()
            else:
                current_board.set_square(str_input[0], str_input[1], str_input[2])
        except ImmutableSquareException:
            print_input_error_text(stdscr, True)

        except (ValueError, IndexError):
            print_input_error_text(stdscr)

    # Solved board!
    if current_board.is_solved():
        print_victory(stdscr)
        hide_cursor(stdscr)

        # TODO: Victory screen with the option of replaying and (or) saving the current board
        clear_screen(stdscr)
