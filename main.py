#!python3
import curses
import sys
from curses import wrapper
from GameEngine.game import Game


def screen_check(stdscr: curses.wrapper) -> None:
    """
    Checks terminal window size
    :param stdscr: main window
    :return:
    """
    max_y, max_x = stdscr.getmaxyx()
    if max_x < 81 or max_y < 25:
        stdscr.addstr(f"Too small window! Increase to at least 81x25")
        stdscr.getch()
        sys.exit()


def main(stdscr):
    """
    Application main method
    :param stdscr: main window
    :return: None
    """
    screen_check(stdscr)
    Game(stdscr)


if __name__ == '__main__':
    wrapper(main)
