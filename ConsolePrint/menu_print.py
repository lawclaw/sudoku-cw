import curses

from ConsolePrint.ui import str_list_to_screen

difficulty_text = [
    "(dan)doku²",
    "━━━━━━━━━━━━",
    "▶ 1.    Easy",
    "▶ 2.  Medium",
    "▶ 3.    Hard",
    "▶ Go back. Q",
    "━━━━━━━━━━━━",
    "Enter:"
]


menu_text = [
    "(dan)doku²",
    "━━━━━━━━━━━━━━",
    "▶ 1.  New game",
    "▶ 2. Load game",
    "▶      Quit. Q",
    "━━━━━━━━━━━━━━",
    "Enter:"
]


def print_menu(stdscr: curses.wrapper, new_game: bool = None):
    """
    Prints game menu
    :param new_game:
    :param stdscr: Main window
    :return:
    """
    if new_game is None:
        str_list_to_screen(menu_text, stdscr)
    elif new_game:
        str_list_to_screen(difficulty_text, stdscr)
