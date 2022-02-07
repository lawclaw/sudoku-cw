from GameEngine.Board import Board
from GameEngine.TextColors import paint_print
import random

def clear_screen():  # https://stackoverflow.com/a/50560686
    print("\033[H\033[J", end="")


def print_board(board):
    paint_print("g", f"{'  '.join(str(x) for x in range(0, 9)).center(34)}", "\n")
    print(f"{'-' * 27}".center(34))
    for i, row in enumerate(board):
        paint_print("g", f"{i} ", "")
        print("|", f"{str(row)[1:-1]}", "|", end="")
        paint_print("g", f" {i}", "\n")

    print(f"{'-' * 27}".center(34))
    paint_print("g", f"{'  '.join(str(x) for x in range(0, 9)).center(34)}", "\n")

    print()

class Game:
    def __init__(self):
        while True:
            # Menu
            choice = self.menu()
            if choice == 0:
                exit()
            current_board = Board(choice)

            # TODO: Playing function
            self.startGame(current_board)

    def menu(self):
        while True:
            #clear_screen()

            paint_print("r", """
  .o       .o8                        o.         .o8            oooo                    
 .8'      "888                        `8.       "888            `888                    
.8'   .oooo888   .oooo.   ooo. .oo.    `8.  .oooo888   .ooooo.   888  oooo  oooo  oooo  
88   d88' `888  `P  )88b  `888P"Y88b    88 d88' `888  d88' `88b  888 .8P'   `888  `888  
88   888   888   .oP"888   888   888    88 888   888  888   888  888888.     888   888  
`8.  888   888  d8(  888   888   888   .8' 888   888  888   888  888 `88b.   888   888  
 `8. `Y8bod88P" `Y888""8o o888o o888o .8'  `Y8bod88P" `Y8bod8P' o888o o888o  `V88V"V8P' 
  `"                                  "'                                               """, "\n")
            print("Author: lawclaw")
            print("-" * 14)
            print("| Easy. 1")
            print("| Medium. 2")
            print("| Hard. 3")
            print("| Quit. 0")
            print("-" * 14)
            choice = input("Enter: ")
            if choice.isnumeric():
                if int(choice) in range(0, 4):
                    return int(choice)

    def startGame(self, current_board):
        clear_screen()
        while True:
            print_board(current_board.board)
            print()
            x, y, v = input("Enter x, y coordinates and desired value [1-9] separated by comma: ").split(',')
            print("-" * 27)
            if not (9 > int(y) >= 0 and 9 > int(x) >= 0):
                print("Invalid square coordinate")
                continue
            if not 10 > int(v) >= 0:
                print("Invalid value")
                continue
            current_board.board[int(y)][int(x)] = int(v)

