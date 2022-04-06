#!/usr/bin/env python3

# Application
import curses
import sys
from curses import wrapper

from GameEngine.game import Game


def screen_check(stdscr: curses.wrapper):
    max_y, max_x = stdscr.getmaxyx()
    if max_x < 81 or max_y < 25:
        stdscr.addstr(f"Too small window! Increase to at least 81x25")
        stdscr.getch()
        sys.exit()


def main(stdscr):
    screen_check(stdscr)
    Game(stdscr)


# Color check
def color_check(stdscr):
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    stdscr.addstr(0, 0, '{0} colors available'.format(curses.COLORS))
    maxy, maxx = stdscr.getmaxyx()
    maxx = maxx - maxx % 5
    x = 0
    y = 1
    try:
        for i in range(0, curses.COLORS):
            stdscr.addstr(y, x, '{0:5}'.format(i), curses.color_pair(i))
            x = (x + 5) % maxx
            if x == 0:
                y += 1
    except curses.ERR:
        pass
    stdscr.getch()


if __name__ == '__main__':
    # wrapper(color_check)
    wrapper(main)
