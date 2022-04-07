import curses

from ConsolePrint.ui import clear_screen, str_list_to_screen

victory_text = [
    "👍You solved the puzzle!👍",
    "Enter 1 to get a replay of game",
    "Enter 2 to replay the game",
    "Enter 3 to save the game",
    "Press Enter to return"
]


def print_victory(stdscr: curses.wrapper):
    """
    Prints victory
    :param stdscr:
    :return:
    """
    str_list_to_screen(victory_text, stdscr)


def print_game_loop_text(stdscr: curses.wrapper):
    y, x = curses.getsyx()
    prompt = "Input: "
    stdscr.addstr(
        y,
        curses.COLS // 2 - (len(prompt) // 2) - 5,
        prompt,
        curses.A_BOLD
    )
