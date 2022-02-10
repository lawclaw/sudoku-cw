from GameEngine.Board import Board
from GameEngine.TextColors import paint_print
import os


def clear_screen():  # https://stackoverflow.com/a/50560686
    print("\033[H\033[J", end="")


def center_text(lines=None, width=None):
    # Centering
    if width is None:
        width = os.get_terminal_size().columns  # https://stackoverflow.com/a/33595028
    for i in range(len(lines)):
        lines[i] = lines[i].center(width)
    return lines


def print_board(board: Board):
    # Indices
    to_print = [' '.join(str(i) for i in range(0, 9)), '—' * 19]

    # Colored Values
    for row_num, row in enumerate(board.current_state):
        to_print.append(f"{row_num} | {' '.join([str(d) for d in row])} | {row_num}")

    # Indices
    to_print.append('—' * 19)
    to_print.append(' '.join(str(i) for i in range(0, 9)))

    center_text(to_print)

    print(*to_print, sep="\n")


class Game:
    menu_text = [
        "(dan)doku",
        "Author: lawclaw",
        "Easy. 1",
        "Medium. 2",
        "Hard. 3",
        "Quit. 0"
    ]

    game_loop_text = [
        "Enter row, column coordinates and desired value [1-9] separated by comma:",
        "Invalid value...(Press any key to try again)\n",
        "Immutable square...(Press any key to try again)\n",
        "Invalid coordinates...(Press any key to try again)\n",
        "Invalid input...(Press any key to try again)\n"
    ]

    def __init__(self):
        while True:
            # Menu
            choice = self.menu(self.menu_text)
            if choice == 0:
                exit()
            current_board = Board(choice)

            # TODO: Playing function
            self.game_loop(current_board)

    def menu(self, menu_text):
        while True:
            clear_screen()

            max_len = len(max(menu_text, key=len))
            menu_text.insert(0, "-" * max_len)
            menu_text.insert(3, "-" * max_len)
            menu_text.append("-" * max_len)

            center_text(menu_text, max_len)

            print(*menu_text, sep="\n")
            print()

            choice = input("Enter: ")
            if choice.isnumeric():
                if int(choice) in range(0, 4):
                    return int(choice)

    def game_loop(self, current_board):
        while True:
            clear_screen()
            print_board(current_board)
            print()
            try:
                print(*center_text([self.game_loop_text[0]]))
                x, y, v = [int(x) for x in input("".center(os.get_terminal_size().columns // 2 - 2)).split(",")]
                if not 10 > v >= 0:
                    input(*center_text([self.game_loop_text[1]]))
                    continue
                if current_board.original_state[y][x] != 0:
                    input(*center_text([self.game_loop_text[2]]))
                    continue
                current_board.current_state[y][x] = int(v)
            except IndexError:
                input(*center_text([self.game_loop_text[3]]))
            except ValueError:
                input(*center_text([self.game_loop_text[4]]))
