import curses
from GameEngine.board import Board

sidebar_text = [
    "┏━━━┳━━━━━━━━━━┳━━━┓",
    "┃ ◆ ┃ Controls ┃ ◆ ┃",
    "┣━━━┻━━━━━━━━━━┻━━━┫",
    "┃ Move: x,y,value  ┃",
    "┣━━━━━━━━━━━━━━━━━━┫",
    "┃   Undo: U / u    ┃",
    "┣━━━━━━━━━━━━━━━━━━┫",
    "┃   Redo: R / r    ┃",
    "┣━━━━━━━━━━━━━━━━━━┫",
    "┃    Quit: Q,q     ┃",
    "┗━━━━━━━━━━━━━━━━━━┛"

]

number_of_player_actions = 0


def print_sidebar(stdscr: curses.wrapper) -> None:
    """
    Prints control sidebar
    :param stdscr: main window
    :return: None
    """
    uly, ulx = curses.LINES // 2 - 9, curses.COLS // 2 - 40

    for i, list_line in enumerate(sidebar_text):
        stdscr.addstr(
            uly + i,
            ulx,
            f"{list_line}",
            curses.color_pair(75)
        )
    stdscr.refresh()


def print_scoreboard(stdscr: curses.wrapper, board: Board) -> None:
    """
    Prints scoreboard sidebar
    :param stdscr: main window
    :param board: current Sudoku board state
    :return: None
    """
    uly, ulx = curses.LINES // 2 - 8, curses.COLS // 2 + 20

    scoreboard_text = [
        "┏━━━┳━━━━━━━━━━┳━━━┓",
        "┃ ◆ ┃  Score   ┃ ◆ ┃",
        "┣━━━┻━━━━━━━━━━┻━━━┫",
        "",
        "┣━━━━━━━━━━━━━━━━━━┫",
        "",
        "┣━━━━━━━━━━━━━━━━━━┫",
        "┃ ◆ ┃  Score   ┃ ◆ ┃",
        "┗━━━━━━━━━━━━━━━━━━┛"
    ]

    scoreboard_text[3] = add_score_line("Empty squares:", str(board.get_number_of_empty_squares()))
    scoreboard_text[5] = add_score_line("Filled squares:", str(board.get_number_of_empty_squares()))

    for i, list_line in enumerate(scoreboard_text):
        if not list_line:
            list_line = add_score_line("PLACEHOLDER:", 10)
        stdscr.addstr(
            uly + i,
            ulx,
            f"{list_line}",
            curses.color_pair(75)
        )
    stdscr.refresh()


def add_score_line(line: str, value: str) -> str:
    """
    String formatting for scoreboard sidebar
    :param line: score text
    :param value: score
    :return: str - formatted score
    """
    base_str = f"{line}{value}".center(20)
    return_str = '┃' + base_str[1:-1] + '┃'
    return return_str
