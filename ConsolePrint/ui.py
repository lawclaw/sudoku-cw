import curses

input_error_text = [
    "Immutable square...(Press Enter key to try again)",
    "Invalid input...(Press Enter key to try again)"
]


def curses_prep() -> None:
    """
    Curses initialization
    Preparation of colored console text
    :return: None
    """
    curses.echo()

    curses.start_color()
    curses.use_default_colors()

    for i in range(0, 255):
        curses.init_pair(i + 1, i, -1)


def hide_cursor(stdscr) -> None:
    """
    Hide cursor
    :param stdscr: main window
    :return: None
    """
    curses.curs_set(0)
    stdscr.getch()
    curses.curs_set(1)


def clear_screen(stdscr) -> None:
    """
    Clears terminal screen
    :param stdscr: main window
    """
    stdscr.clear()
    stdscr.refresh()


def print_input_error_text(stdscr: curses.wrapper, immutable_exception: bool = None) -> None:
    """
    Print input error message
    :param stdscr: main window
    :param immutable_exception: if exception is immutable_square_exception
    :return: None
    """
    y, _ = curses.getsyx()

    immutable = 0
    if immutable_exception is None:
        immutable = 1

    stdscr.addstr(
        y - 1,
        curses.COLS // 2 - (len(input_error_text[immutable]) // 2),
        input_error_text[immutable])
    hide_cursor(stdscr)


def str_list_to_screen(text_list, stdscr) -> None:
    """
    Prints list of str (in centered format)
    :param text_list: list of str
    :param stdscr: main window
    :return: None
    """
    for i, list_line in enumerate(text_list):
        stdscr.addstr(
            curses.LINES // 3 + i,
            curses.COLS // 2 - ((len(list_line) + 1) // 2),
            f"{list_line}",

            curses.color_pair(i + 210) | curses.A_BOLD
        )
    stdscr.refresh()


def move_cursor(stdscr, y: int = None, x: int = None) -> None:
    """
    Move cursor by x and/or y units
    :param stdscr: main window
    :param y: y offset
    :param x: x offset
    :return: None
    """
    line, col = curses.getsyx()
    if y is None:
        y = 0
    if x is None:
        x = 0

    stdscr.move(y + line, x + col)
    stdscr.refresh()
