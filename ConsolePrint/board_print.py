import curses

from ConsolePrint.ui import clear_screen, move_cursor
from GameEngine.board import Board

board_frame_top = [
    "",
    "",
    "",
    "🆇",
    "┏━━━┳━━━━━━━━━━━━━━━━━━━┳━━━┓",
    "┃ ◆ ┃ 0 1 2 3 4 5 6 7 8 ┃ ◆ ┃",
    "┣━━━╋━━━━━━━━━━━━━━━━━━━╋━━━┫"
]

board_frame_bottom = [
    "┣━━━╋━━━━━━━━━━━━━━━━━━━╋━━━┫",
    "┃ ◆ ┃ 0 1 2 3 4 5 6 7 8 ┃ ◆ ┃",
    "┗━━━┻━━━━━━━━━━━━━━━━━━━┻━━━┛",
    "🆇",
    " "
]


def print_board_state(stdscr: curses.wrapper, board: Board, n: int = None):
    """
    Print board state to console
    :param n:
    :param stdscr: Main window
    :param board: Sudoku board
    """
    if n is None:
        n = -1

    clear_screen(stdscr)

    # Top frame
    for line in board_frame_top:
        add_line(stdscr, line)

    move_cursor(stdscr, 0, curses.COLS // 2 - 15)

    # Board
    for y in range(9):
        add_coordinates(stdscr, y)

        # Y symbol (left)
        if y == 4:
            add_y_symbol(stdscr, position='left')

        for x in range(9):
            move_cursor(stdscr, None, 0)
            digit = board.board_states[n][y][x]
            if board.is_immutable(y, x):
                add_char(stdscr, str(digit), is_immutable=True)
            else:
                add_char(stdscr, str(digit), coordinate=x)
            move_cursor(stdscr, None, 2)

        # Y symbol (right)
        if y == 4:
            add_y_symbol(stdscr, position='right')

        add_coordinates(stdscr, y)

        move_cursor(stdscr, 1, -30)  # Move down one line, and go back 30 columns

    # Bottom frame
    for line in board_frame_bottom:
        add_line(stdscr, line)

def add_y_symbol(stdscr: curses.wrapper, position: str) -> None:
    """
    Add y symbol on the side
    :param stdscr:
    :param position:
    :return:
    """
    if position == 'left':
        move_cursor(stdscr, y=None, x=-9)
        add_char(stdscr, char='🆈', is_coordinate=True)
        move_cursor(stdscr, y=None, x=9)
    elif position == 'right':
        move_cursor(stdscr, y=None, x=6)
        add_char(stdscr, char='🆈', is_coordinate=True)
        move_cursor(stdscr, y=None, x=-6)


def add_coordinates(stdscr: curses.wrapper, y: int) -> None:
    """
    Add y-coordinates on the side
    :param stdscr:
    :param y:
    :return:
    """
    add_char(stdscr, "┃", is_coordinate=True)
    move_cursor(stdscr, y=None, x=2)

    add_char(stdscr, str(y), is_coordinate=True)
    move_cursor(stdscr, y=None, x=2)

    add_char(stdscr, "┃", is_coordinate=True)
    move_cursor(stdscr, y=None, x=2)


def add_char(stdscr: curses.wrapper,
             char: str,
             is_immutable: bool = False,
             is_coordinate: bool = False,
             coordinate: int = 1):
    """
    Add individual character to console
    :param coordinate:
    :param is_immutable:
    :param is_coordinate:
    :param char:
    :param stdscr:
    :return:
    """
    y, x = curses.getsyx()

    def add_immutable_square(digit_char: str):
        """
        Add immutable square digit to console
        :param digit_char:
        :return:
        """
        stdscr.addstr(
            y,
            x,
            digit_char,
            curses.A_BOLD
        )

    def add_mutable_square(digit_char: str):
        """
        Add mutable square digit to console
        :param digit_char:
        :return:
        """
        stdscr.addstr(
            y,
            x,
            digit_char,
            curses.color_pair((coordinate + 70 + 140)) | curses.A_BOLD
        )

    def add_coordinate_symbol(coordinate_char: str):
        """
        Add coordinate character to console
        :param coordinate_char:
        :return:
        """
        stdscr.addstr(
            y,
            x,
            coordinate_char,
            curses.color_pair(70)
        )

    # Logic
    if is_immutable:
        add_immutable_square(char)
    elif is_coordinate:
        add_coordinate_symbol(char)
    elif char == '0':   # Empty mutable squares
        add_mutable_square("⯀")
    else:
        add_mutable_square(char) # Non-empty mutable squares


def add_line(stdscr: curses.wrapper, line: str) -> None:
    """
    Add string to console (centered)
    :param stdscr:
    :param line:
    :return:
    """
    y, x = curses.getsyx()
    stdscr.addstr(
        y,
        curses.COLS // 2 - ((len(line) + 1) // 2),
        f"{line}\n",
        curses.color_pair(70)
    )
    move_cursor(stdscr, 1)
