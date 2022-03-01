#!/usr/bin/env python3

# Application
from curses import wrapper

from GameEngine.Game import Game


def main(stdscr):
    game = Game(stdscr)


if __name__ == '__main__':
    wrapper(main)
