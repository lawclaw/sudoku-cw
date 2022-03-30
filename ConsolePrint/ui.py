import curses

input_error_text = [
    "Immutable square...(Press Enter key to try again)",
    "Invalid input...(Press Enter key to try again)"
]


def curses_prep():
    """
    Curses initialization and prepare color pair for printing
    :return:
    """
    curses.echo()
    
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)

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


def text_list_to_screen(text_list, stdscr):
    for i, list_line in enumerate(text_list):
        stdscr.addstr(
            curses.LINES // 3 + i,
            curses.COLS // 2 - ((len(list_line) + 1) // 2),
            f"{list_line}",
            curses.color_pair(i % 6 + 1) | curses.A_BOLD
        )

