import curses

from ConsolePrint.ui import str_list_to_screen

victory_text = [
    "👍You solved the puzzle!👍",
    "Enter 1 to get a replay of game",
    "Enter 2 to replay the game",
    "Enter 3 to save the game",
    "Press Enter to return"
]


def print_victory(stdscr: curses.wrapper) -> None:
    """
    Prints victory
    :param stdscr: main window
    :return: None
    """
    str_list_to_screen(victory_text, stdscr)


def print_input_prompt(stdscr: curses.wrapper) -> None:
    """
    Prints the prompt for user input
    :param stdscr: main window
    :return: None
    """
    y, x = curses.getsyx()
    prompt = "Input: "
    stdscr.addstr(
        y,
        curses.COLS // 2 - (len(prompt) // 2) - 5,
        prompt,
        curses.A_BOLD
    )
