class Board:
    size = 9
    board = []

    def __init__(self, board = None):
        if board is None:
            self.board = [[0 for i in range(9)] for j in range(9)]
        else:
            self.board = board

    def print_board(self):
        for row in self.board:
            print(row)
