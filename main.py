# Application
from curses import wrapper

from GameEngine.Game import Game


def main(stdscr):
    g = Game(stdscr)



if __name__ == '__main__':
    wrapper(main)
