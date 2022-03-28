import curses
import sys

from ConsolePrint.ui import print_menu, hide_cursor, clear_screen, print_board, color_prepare, print_victory, \
    print_game_loop_text, print_input_error_text, print_new_game_menu
from GameEngine.board import Board
from GameEngine.immutable_square_exception import ImmutableSquareException


class Game:
    def __init__(self, stdscr: curses.wrapper):
        """
        Main game
        """
        curses_prep()
        screen_check(stdscr)
        menu(stdscr)

def screen_check(stdscr: curses.wrapper):
    # Check if screen size is big enough
    max_y, max_x = stdscr.getmaxyx()
    if max_x < 66 or max_y < 25:
        stdscr.addstr(f"Too small window! Increase to at least 66x25")
        stdscr.getch()
        sys.exit()

def curses_prep():
    # Curses initialization
    curses.echo()
    color_prepare()

def menu(stdscr: curses.wrapper):
    while True:
        # Menu
        print_menu(stdscr)
        # Input
        key = get_menu_input(stdscr)
        # Exit condition
        if key == 'Q' or key == "q":
            sys.exit()

        # New game option
        if key == '1':
            while True:
                print_new_game_menu(stdscr)
                difficulty = get_menu_input(stdscr)
                if difficulty == 'Q' or difficulty == "q":
                    break
                elif difficulty == '1' or difficulty == '2' or difficulty == '3':
                    board = Board(int(difficulty))
                    game_loop(board, stdscr)
                    break
                else:
                    print_input_error_text(stdscr)
                    continue

        # Load game option
        elif key == '2':
            board = load_game()
            game_loop(board, stdscr);
        else:
            print_input_error_text(stdscr)


def get_menu_input(stdscr: curses.wrapper):
    try:
        stdscr.addstr(
            curses.LINES // 2 + 1,
            curses.COLS // 2 - (len("Enter: ") - 1 // 2),
            "Enter: ",
            curses.A_BOLD)
        raw_input = stdscr.getstr(1)
        key = str(raw_input, "utf-8")
        return key
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
