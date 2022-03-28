import curses

from ConsolePrint.ui import text_list_to_screen

difficulty_text = [
    "(dan)doku",
    "Easy. 1",
    "Medium. 2",
    "Hard. 3",
    "Quit. Q"
]


menu_text = [
    "(dan)doku",
    "Author: lawclaw",
    "New game. 1",
    "Load game. 2",
    "Quit. Q"
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
