from GameEngine import Solver
from GameEngine.Board import Board


def clear_screen():  # https://stackoverflow.com/a/50560686
    print("\033[H\033[J", end="")


class Game:
    def __init__(self):
        while True:
            # Menu
            choice = self.menu()
            if choice == 0:
                exit()

            # TODO: Generate puzzle
            emptyBoard = Board()
            Solver.brute_solve(emptyBoard.board)
            emptyBoard.print_board()
            # TODO: Playing function


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