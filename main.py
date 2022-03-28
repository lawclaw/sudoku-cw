#!/usr/bin/env python3

# Application
from curses import wrapper

from GameEngine.game import Game


def main(stdscr):
    Game(stdscr)


if __name__ == '__main__':
    wrapper(main)
