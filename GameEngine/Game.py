from GameEngine.Board import Board
from GameEngine.TextColors import paint_print
import os


def clear_screen():  # https://stackoverflow.com/a/50560686
    print("\033[H\033[J", end="")


def print_board(board: Board):
    # Indices
    to_print = [' '.join(str(i) for i in range(0, 9)), '—' * 19]

    # Colored Values
    for row_num, row in enumerate(board.current_state):
        to_print.append(f"{row_num} | {' '.join([str(d) for d in row])} | {row_num}")

    # Indices
    to_print.append('—' * 19)
    to_print.append(' '.join(str(i) for i in range(0, 9)))

    # Centering
    max_len = os.get_terminal_size().columns  # https://stackoverflow.com/a/33595028
    for i, line in enumerate(to_print):
        to_print[i] = to_print[i].center(max_len)

    print(*to_print, sep="\n")


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
            clear_screen()

            to_print = [
                        "(dan)doku",
                        "Author: lawclaw",
                        "Easy. 1",
                        "Medium. 2",
                        "Hard. 3",
                        "Quit. 0"
                        ]

            max_len = len(max(to_print, key=len))
            to_print.insert(2, "-" * max_len)
            to_print.insert(-1, "-" * max_len)
            for i, line in enumerate(to_print):
                to_print[i] = to_print[i].center(max_len)

            print(*to_print, sep="\n")
            print()

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
                if current_board.original_state[int(y)][int(x)] != 0:
                    input("Immutable square...(Press any key to try again)\n")
                    continue
                current_board.current_state[int(y)][int(x)] = int(v)
            except IndexError:
                input("Invalid coordinates...(Press any key to try again)\n")
            except ValueError:
                input("Invalid input...(Press any key to try again)\n")
