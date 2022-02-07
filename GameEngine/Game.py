from GameEngine.Board import Board
from GameEngine.TextColors import paint_print
import random

def clear_screen():  # https://stackoverflow.com/a/50560686
    print("\033[H\033[J", end="")


def print_board(board: Board):
    # Indices
    paint_print("g", f"{' '.join(str(x) for x in range(0, 9)).center(25)}", "\n")
    print(f"{'-' * 19}".center(25))

    # Values
    # for i, row in enumerate(board.current_state):
    #     paint_print("g", f"{i} ", "")
    #     paint_print("y", f"{str(row)[1:-1]}", "")
    #     print(" |", end="")
    #     paint_print("g", f" {i}", "\n")

    # Colored Values
    for row in range(9):
        paint_print("g", f"{row} ", "")
        print("| ", end="")
        for col in range(9):
            if board.original_state[row][col] == 0:
                paint_print("y", f"{str(board.current_state[row][col])}", " ")
            else:
                print(board.current_state[row][col], end=" ")
        print("|", end="")
        paint_print("g", f" {row}", "\n")

    # Indices
    print(f"{'-' * 19}".center(25))
    paint_print("g", f"{' '.join(str(i) for i in range(0, 9)).center(25)}", "\n")

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
        while True:
            clear_screen()
            print_board(current_board)
            print()
            try:
                x, y, v = input("Enter x, y coordinates and desired value [1-9] separated by comma: ").split(',')
                if not 10 > int(v) >= 0:
                    input("Invalid value...(Press any key to try again)\n")
                    continue
                if current_board.original_state[int(x)][int(y)] != 0:
                    input("Immutable square...(Press any key to try again)\n")
                    continue
                current_board.current_state[int(x)][int(y)] = int(v)
            except IndexError:
                input("Invalid coordinates...(Press any key to try again)\n")
            except ValueError:
                input("Invalid input...(Press any key to try again)\n")
