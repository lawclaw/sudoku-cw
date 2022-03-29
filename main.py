#!/usr/bin/env python3

# Application
import curses
import sys
from curses import wrapper

from GameEngine.game import Game


def screen_check(stdscr: curses.wrapper):
    max_y, max_x = stdscr.getmaxyx()
    if max_x < 66 or max_y < 25:
        stdscr.addstr(f"Too small window! Increase to at least 66x25")
        stdscr.getch()
        sys.exit()


def main(stdscr):
    screen_check(stdscr)
    Game(stdscr)


if __name__ == '__main__':
    wrapper(main)
