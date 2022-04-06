import curses
import sys

from ConsolePrint.board_print import print_board_state, add_line
from ConsolePrint.game_loop_print import print_game_loop_text, print_victory
from ConsolePrint.menu_print import print_menu
from ConsolePrint.sidebar_print import print_sidebar, score
from ConsolePrint.ui import clear_screen, print_input_error_text, curses_prep, move_cursor

from GameEngine.board import Board
from GameEngine.immutable_square_exception import ImmutableSquareException

from curses.textpad import rectangle


class Game:
    def __init__(self, stdscr: curses.wrapper):
        """
        Main game
        """
        curses_prep()
        menu(stdscr)


def menu(stdscr: curses.wrapper):
    while True:
        # Menu
        clear_screen(stdscr)
        print_menu(stdscr)
        # Input
        key = get_user_input(stdscr)

        # Exit condition
        if key == 'Q' or key == "q":
            sys.exit()

        # New game option
        if key == '1':
            while True:
                clear_screen(stdscr)
                print_menu(stdscr, True)
                stdscr.refresh()
                difficulty = get_user_input(stdscr)
                if difficulty == 'Q' or difficulty == "q":
                    break
                elif difficulty == '1' or difficulty == '2' or difficulty == '3':
                    board = Board(int(difficulty))
                    if game_loop(board, stdscr):
                        game_loop(board, stdscr)
                    else:
                        break
                else:
                    print_input_error_text(stdscr)

        # Load game option
        elif key == '2':
            current_board = load_game()
            if game_loop(current_board, stdscr):
                game_loop(current_board, stdscr)
        else:
            print_input_error_text(stdscr)

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

        # Print sidebar
        print_sidebar(stdscr)

        stdscr.refresh()

        score(stdscr, current_board)

        stdscr.refresh()

        if curses.LINES > 30:
            move_cursor(stdscr, curses.LINES // 9, -43)

        else:
            move_cursor(stdscr, curses.LINES // 4, -43)

        # Print prompt
        #print_game_loop_text(stdscr)

        stdscr.refresh()

        try:
            str_input = get_user_input(stdscr, 5).split(',')
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

    # Victory screen
    # TODO: Victory screen with the option of replaying and (or) saving the current board
    # Replay works, just need to add text
    if current_board.is_solved():
        while True:
            clear_screen(stdscr)

            print_victory(stdscr)

            stdscr.refresh()

            choice = get_user_input(stdscr)

            if choice == '1':
                replay(stdscr, current_board)
            elif choice == '2':
                current_board.reset()
                return True
            elif choice == '3':
                save_game(current_board)
            else:
                return False


def replay(stdscr: curses.wrapper, current_board: Board):
    clear_screen(stdscr)

    curses.curs_set(0)

    for n in range(len(current_board.board_states)):
        print_board_state(stdscr, current_board, n)
        stdscr.refresh()
        curses.napms(1000)

    curses.curs_set(1)


def get_user_input(stdscr: curses.wrapper, n_characters: int = None, visible: bool = True):
    if n_characters is None:
        n_characters = 1

    if not visible:
        move_cursor(stdscr, 1, -11)

    try:
        raw_input = stdscr.getstr(n_characters)
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
