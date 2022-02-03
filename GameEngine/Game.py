from GameEngine.Board import Board
import random

def clear_screen():  # https://stackoverflow.com/a/50560686
    print("\033[H\033[J", end="")


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
            print("Kondoku")
            print("| Easy. 1")
            print("| Medium. 2")
            print("| Hard. 3")
            print("| Quit. 0")
            choice = input("Enter: ")
            if choice.isnumeric():
                if int(choice) in range(0, 4):
                    return int(choice)

    def startGame(self, current_board):
        clear_screen()
        while True:
            current_board.print_board()
            x, y, v = input("Enter x, y and desired value [1-9] separated by comma: ").split(',')
            print("-" * 27)
            if not (9 > int(y) >= 0 and 9 > int(x) >= 0):
                print("Invalid square coordinate")
                continue
            if not 10 > int(v) >= 0:
                print("Invalid value")
                continue
            current_board.board[int(y)][int(x)] = int(v)

