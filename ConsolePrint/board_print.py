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
    Prints board state
    :param n:
    :param stdscr: Main window
    :param board: Sudoku board
    """
    if n is None:
        n = -1

    clear_screen(stdscr)

    l, c = curses.getsyx()

    # Top frame
    for line in board_frame_top:
        add_line(stdscr, line)

    move_cursor(stdscr, None, curses.COLS // 2 - 15)

    # Board
    for y in range(9):
        add_coordinates(stdscr, y)

        for x in range(9):
            move_cursor(stdscr, None, 0)
            digit = board.board_states[n][y][x]
            if board.is_immutable(y, x):
                add_char(stdscr, str(digit))
            else:
                add_char(stdscr, str(digit), x)
            move_cursor(stdscr, None, 2)

        add_coordinates(stdscr, y)

        move_cursor(stdscr, 1, -30)

    # Bottom frame
    for line in board_frame_bottom:
        add_line(stdscr, line)


def add_coordinates(stdscr, y):
    add_char(stdscr, "┃", 1)
    move_cursor(stdscr, None, 2)

    add_char(stdscr, str(y), 1, True)
    move_cursor(stdscr, None, 2)

    add_char(stdscr, "┃", 1)
    move_cursor(stdscr, None, 2)


def add_char(stdscr: curses.wrapper, char: str, color: int = None, is_coordinate: bool = False):
    """
    Add digit/char to screen
    :param is_coordinate:
    :param char:
    :param stdscr:
    :param color:
    :return:
    """
    y, x = curses.getsyx()

    if color is None:
        stdscr.addstr(
            y,
            x,
            f"{char} ",
            curses.A_BOLD
        )
    else:
        if char == '0' and not is_coordinate:
            stdscr.addstr(
                y,
                x,
                "⯀",
                curses.color_pair((color % 6) + 1) | curses.A_BOLD
            )
        else:
            stdscr.addstr(
                y,
                x,
                f"{char}",
                curses.color_pair((color % 6) + 1) | curses.A_BOLD
            )


def add_line(stdscr: curses.wrapper, line: str) -> None:
    y, x = curses.getsyx()
    stdscr.addstr(
        y,
        curses.COLS // 2 - ((len(line) + 1) // 2),
        f"{line}\n",
        curses.color_pair(2) | curses.A_BOLD
    )
    move_cursor(stdscr, 1)