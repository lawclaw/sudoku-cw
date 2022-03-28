import curses

from ConsolePrint.ui import clear_screen, text_list_to_screen

game_loop_text = [
    "Enter x, y coordinates and desired value [1-9] separated by comma:",
    "Enter U to undo, R to redo",
    "Enter Q to quit"
]

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
    text_list_to_screen(victory_text, stdscr)


def print_game_loop_text(stdscr: curses.wrapper):
    y, x = curses.getsyx()
    for i, line in enumerate(game_loop_text):
        stdscr.addstr(
            y + i + 1,
            curses.COLS // 2 - (len(game_loop_text[i]) // 2),
            game_loop_text[i],
            curses.A_BOLD
        )
