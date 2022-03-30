import curses

from ConsolePrint.ui import text_list_to_screen

difficulty_text = [
    "(dan)doku²",
    "━━━━━━━━━━━━",
    "▶ 1.   Easy",
    "▶ 2. Medium",
    "▶ 3.   Hard",
    "▶   Quit. Q",

]


menu_text = [
    "(dan)doku²",
    "━━━━━━━━━━━━━━",
    "▶ 1.  New game",
    "▶ 2. Load game",
    "▶      Quit. Q",


]


def print_menu(stdscr: curses.wrapper, new_game: bool = None):
    """
    Prints game menu
    :param new_game:
    :param stdscr: Main window
    :return:
    """
    if new_game is None:
        text_list_to_screen(menu_text, stdscr)
    elif new_game:
        text_list_to_screen(difficulty_text, stdscr)
