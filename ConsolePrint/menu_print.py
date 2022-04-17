import curses

from ConsolePrint.ui import str_list_to_screen

difficulty_text = [
    "(crs)doku²",
    "━━━━━━━━━━━━",
    "▶ 1.    Easy",
    "▶ 2.  Medium",
    "▶ 3.    Hard",
    "▶ Go back. Q",
    "━━━━━━━━━━━━",
    "Enter:"
]


menu_text = [
    "(crs)doku²",
    "━━━━━━━━━━━━━━",
    "▶ 1.  New game",
    "▶ 2. Load game",
    "▶      Quit. Q",
    "━━━━━━━━━━━━━━",
    "Enter:"
]


def print_menu(stdscr: curses.wrapper, new_game: bool = None) -> None:
    """
    Prints game menu
    :param stdscr: Main window
    :param new_game: True if new game, otherwise False
    :return: None
    """
    if new_game is None:
        str_list_to_screen(menu_text, stdscr)
    elif new_game:
        str_list_to_screen(difficulty_text, stdscr)
