def clear_screen():  # https://stackoverflow.com/a/50560686
    print("\033[H\033[J", end="")

class Game:
    def __init__(self):
        choice = self.menu()
        if choice == 0:
            exit()

    def menu(self):
        while True:
            clear_screen()
            print("Kondoku")
            print("| Easy. 1")
            print("| Medium. 2")
            print("| Hard. 3")
            print("| Quit. 0")
            choice = input("Enter: ")
            if choice.isnumeric():
                if int(choice) in range(1,4):
                    return int(choice)


