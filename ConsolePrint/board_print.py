import curses

from ConsolePrint.ui import clear_screen
from GameEngine.board import Board


def print_board_state(stdscr: curses.wrapper, board: Board, n: int = None):
    """
    Prints board state
    :param n:
    :param stdscr: Main window
    :param board: Sudoku board
    """
    if n is None:
        n = -1
    y_offset = 0
    clear_screen(stdscr)

    add_line(stdscr, "🆇", y_offset)
    y_offset += 1
    add_line(stdscr, '┏━━━┳━━━━━━━━━━━━━━━━━━━┳━━━┓', y_offset)
    y_offset += 1

    ui = ['', '']
    ui[0] = '┃ ◆ ┃ 0 1 2 3 4 5 6 7 8 ┃ ◆ ┃'
    ui[1] = '┣━━━╋━━━━━━━━━━━━━━━━━━━╋━━━┫'
    for line in ui:
        add_line(stdscr, line, y_offset)
        y_offset += 1

    for y in range(9):
        x_offset = -15

        if y == 4:
            add_line(stdscr, "🆈", y_offset, -18)

        add_line(stdscr, "┃", y_offset, x_offset)
        x_offset += 2
        add_line(stdscr, str(y), y_offset, x_offset)
        x_offset += 2
        add_line(stdscr, "┃", y_offset, x_offset)
        x_offset += 2

        if y == 4:
            add_line(stdscr, "🆈", y_offset, 15)

        for x in range(9):
            if board.is_immutable(y, x):
                add_digit(stdscr, y_offset, x_offset, board.board_states[n][y][x])
            else:
                add_digit(stdscr, y_offset, x_offset, board.board_states[n][y][x], x)
            x_offset += 2

        add_line(stdscr, "┃", y_offset, x_offset)
        x_offset += 2
        add_line(stdscr, str(y), y_offset, x_offset)
        x_offset += 2
        add_line(stdscr, "┃", y_offset, x_offset)
        x_offset += 2

        y_offset += 1

    for line in reversed(ui):
        add_line(stdscr, line, y_offset)
        y_offset += 1
    add_line(stdscr, '┗━━━┻━━━━━━━━━━━━━━━━━━━┻━━━┛', y_offset)
    y_offset += 1

    add_line(stdscr, "🆇", y_offset)


def add_digit(stdscr, y_offset, x_offset, value: str, color: int = None):
    """
    Add digit/char to screen
    :param stdscr:
    :param y_offset:
    :param x_offset:
    :param value:
    :param color:
    :return:
    """
    if color is None:
        stdscr.addstr(
            curses.LINES // 10 + y_offset,
            curses.COLS // 2 + x_offset,
            f"{value} ",
            curses.A_BOLD
        )
    else:
        # Empty squares (mutable squares)
        if value == 0:
            stdscr.addstr(
                curses.LINES // 10 + y_offset,
                curses.COLS // 2 + x_offset,
                "⯀ ",
                curses.color_pair((color % 6) + 1)
            )
        else:
            stdscr.addstr(
                curses.LINES // 10 + y_offset,
                curses.COLS // 2 + x_offset,
                f"{value} ",
                curses.color_pair((color % 6) + 1) | curses.A_BOLD
            )


def add_line(stdscr: curses.wrapper, line: str, y_offset: int, x_offset: int = None):
    """
    Add line to screen
    :param stdscr:
    :param line:
    :param y_offset:
    :param x_offset:
    :return:
    """
    if x_offset is None:
        stdscr.addstr(
            curses.LINES // 10 + y_offset,
            curses.COLS // 2 - ((len(line) + 1) // 2),
            f"{line}\n",
            curses.color_pair(2) | curses.A_BOLD
        )
    else:
        stdscr.addstr(
            curses.LINES // 10 + y_offset,
            curses.COLS // 2 + x_offset,
            f"{line} ",
            curses.color_pair(2) | curses.A_BOLD
        )
