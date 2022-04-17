import curses
import sys

from ConsolePrint.board_print import print_board_state
from ConsolePrint.game_loop_print import print_victory, print_input_prompt
from ConsolePrint.menu_print import print_menu
from ConsolePrint.sidebar_print import print_sidebar, print_scoreboard
from ConsolePrint.ui import clear_screen, print_input_error_text, curses_prep, move_cursor
from GameEngine.board import Board
from GameEngine.immutable_square_exception import ImmutableSquareException


class Game:
    def __init__(self, stdscr: curses.wrapper) -> None:
        """
        Constructor
        :param stdscr: main window
        """
        curses_prep()
        menu(stdscr)


def menu(stdscr: curses.wrapper) -> None:
    """
    Top menu node, the main menu
    :param stdscr: main window
    :return: None
    """
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
            new_game_screen(stdscr)

        # Load game option
        elif key == '2':
            current_board = load_game()
            if game_loop(current_board, stdscr):
                game_loop(current_board, stdscr)

        # Any other input
        else:
            print_input_error_text(stdscr)


def new_game_screen(stdscr: curses.wrapper) -> None:
    """
    Prints the new game screen with difficulty selection
    :param stdscr: main window
    :return: None
    """
    while True:
        clear_screen(stdscr)
        print_menu(stdscr, True)
        stdscr.refresh()
        difficulty = get_user_input(stdscr)
        if difficulty == 'Q' or difficulty == "q":
            return
        elif difficulty == '1' or difficulty == '2' or difficulty == '3':
            board = Board(int(difficulty))
            if game_loop(board, stdscr):
                game_loop(board, stdscr)
            else:
                return
        else:
            print_input_error_text(stdscr)


def game_loop(current_board: Board, stdscr) -> bool:
    """
    Main game loop where user can play Sudoku
    :param stdscr: main window
    :param current_board: Board object
    :return: bool: True if user chooses to replay, otherwise False
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
        print_scoreboard(stdscr, current_board)
        stdscr.refresh()

        if curses.LINES > 40:
            move_cursor(stdscr, 4, -43)
        elif curses.LINES > 30:
            move_cursor(stdscr, 6, -43)
        else:
            move_cursor(stdscr, 8, -43)

        stdscr.refresh()

        # Print prompt
        print_input_prompt(stdscr)
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


def replay(stdscr: curses.wrapper, current_board: Board) -> None:
    """
    Replays the user's game by displaying each state with delays
    :param stdscr: main window
    :param current_board: Board object
    :return: None
    """
    clear_screen(stdscr)

    curses.curs_set(0)

    for n in range(len(current_board.board_states)):
        print_board_state(stdscr, current_board, n)
        stdscr.refresh()
        curses.napms(1000)

    curses.curs_set(1)


def get_user_input(stdscr: curses.wrapper, n_characters: int = None, visible: bool = True) -> str:
    """
    Retrieving user input
    :param stdscr: main window
    :param n_characters: number of characters to be read
    :param visible: visibility of prompt
    :return: str - user input key
    """
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


def save_game(board) -> None:
    """
    Save board into json save file
    :param board: Board object
    :return: None
    """
    board.to_json()


def load_game() -> Board:
    """
    Load board from json save file
    :return: Board: loaded Sudoku board
    """
    board = Board(4, True)
    return board
