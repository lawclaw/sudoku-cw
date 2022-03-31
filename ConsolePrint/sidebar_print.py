import curses

from ConsolePrint.ui import move_cursor


sidebar_text = [
    "┏━━━┳━━━━━━━━━━┳━━━┓",
    "┃ ◆ ┃ Controls ┃ ◆ ┃",
    "┣━━━┻━━━━━━━━━━┻━━━┫",
    "┃ Input: x,y,value ┃",
    "┣━━━━━━━━━━━━━━━━━━┫",
    "┃    Undo: U,u     ┃",
    "┣━━━━━━━━━━━━━━━━━━┫",
    "┃    Redo: R,r     ┃",
    "┣━━━━━━━━━━━━━━━━━━┫",
    "┃    Quit: Q,q     ┃",
    "┗━━━━━━━━━━━━━━━━━━┛"

]


def print_sidebar(stdscr: curses.wrapper):
    uly, ulx = curses.LINES // 2 - 8, 1

    for i, list_line in enumerate(sidebar_text):
        stdscr.addstr(
            uly + i,
            ulx,
            f"{list_line}",
            curses.color_pair(70)
        )
    stdscr.refresh()

