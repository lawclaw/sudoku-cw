import curses
import random

input_error_text = [
    "Immutable square...(Press Enter key to try again)",
    "Invalid input...(Press Enter key to try again)"
]


def curses_prep():
    """
    Curses initialization
    Preparation of colored console text
    :return:
    """
    curses.echo()

    curses.start_color()
    curses.use_default_colors()

    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)


def hide_cursor(stdscr):
    """
    Hide cursor
    :param stdscr:
    :return:
    """
    curses.curs_set(0)
    stdscr.getch()
    curses.curs_set(1)


def clear_screen(stdscr):  # https://stackoverflow.com/a/50560686
    """
    Clears terminal screen
    """
    stdscr.clear()
    stdscr.refresh()


def print_input_error_text(stdscr: curses.wrapper, immutable_exception: bool = None):
    y, _ = curses.getsyx()

    immutable = 0
    if immutable_exception is None:
        immutable = 1

    stdscr.addstr(
        y - 1,
        curses.COLS // 2 - (len(input_error_text[immutable]) // 2),
        input_error_text[immutable])
    hide_cursor(stdscr)


def str_list_to_screen(text_list, stdscr):
    for i, list_line in enumerate(text_list):
        stdscr.addstr(
            curses.LINES // 3 + i,
            curses.COLS // 2 - ((len(list_line) + 1) // 2),
            f"{list_line}",
            curses.color_pair(i + 2) | curses.A_BOLD
        )
    stdscr.refresh()


def move_cursor(stdscr, y: int = None, x: int = None):
    line, col = curses.getsyx()
    if y is None:
        y = 0
    if x is None:
        x = 0

    stdscr.move(y + line, x + col)
    stdscr.refresh()
