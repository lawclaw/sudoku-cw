import curses
import sys

from ConsolePrint.board_print import print_board_state
from ConsolePrint.game_loop_print import print_game_loop_text, print_victory
from ConsolePrint.menu_print import print_menu
from ConsolePrint.ui import clear_screen, print_input_error_text, curses_prep

from GameEngine.board import Board
from GameEngine.immutable_square_exception import ImmutableSquareException


class Game:
    def __init__(self, stdscr: curses.wrapper):
        """
        Main game
        """
        curses_prep()
        stdscr.refresh()
        screen_check(stdscr)
        menu(stdscr)


def screen_check(stdscr: curses.wrapper):
    # Check if screen size is big enough
    max_y, max_x = stdscr.getmaxyx()
    if max_x < 66 or max_y < 25:
        stdscr.addstr(f"Too small window! Increase to at least 66x25")
        stdscr.getch()
        sys.exit()





def menu(stdscr: curses.wrapper):
    while True:
        # Menu
        clear_screen(stdscr)
        print_menu(stdscr)
        stdscr.refresh()
        # Input
        key = get_menu_input(stdscr)
        # Exit condition
        if key == 'Q' or key == "q":
            sys.exit()

        # New game option
        if key == '1':
            while True:
                clear_screen(stdscr)
                print_menu(stdscr, True)
                stdscr.refresh()
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
            game_loop(board, stdscr)
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
        clear_screen(stdscr)

        # Print board
        print_board_state(stdscr, current_board)

        stdscr.refresh()

        # Print prompt
        print_game_loop_text(stdscr)

        try:
            y, _ = curses.getsyx()
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
            stdscr.refresh()

        except (ValueError, IndexError):
            print_input_error_text(stdscr)
            stdscr.refresh()

    # Solved board!
    # TODO: Victory screen with the option of replaying and (or) saving the current board
    if current_board.is_solved():
        print_victory(stdscr)
        stdscr.refresh()
        choice = get_menu_input(stdscr)
        if choice == '1':
            replay(stdscr, current_board)


def replay(stdscr: curses.wrapper, current_board: Board):
    clear_screen(stdscr)
    for n in range(len(current_board.board_states)):
        print_board_state(stdscr, current_board, n)
        stdscr.refresh()

        curses.napms(1000)
