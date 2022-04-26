import curses

from ConsolePrint.ui import str_list_to_screen

victory_text = [
    "Solved puzzle!",
    "━━━━━━━━━━━━━━━━━━",
    "▶ 1.  Watch replay",
    "▶ 2.  Replay game ",
    "▶ 3.  Save game   ",
    "▶ Enter to return ",
    "━━━━━━━━━━━━━━━━━━",
    "Enter:"
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
