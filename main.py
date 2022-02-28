# Application
from GameEngine.Game import Game
import platform, os
from curses import wrapper

def main(stdscr):
    g = Game(stdscr)



if __name__ == '__main__':
    wrapper(main)
