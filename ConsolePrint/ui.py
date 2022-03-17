import curses

from GameEngine.board import Board
from GameEngine.immutable_square_exception import ImmutableSquareException

menu_text = [
    "(dan)doku",
    "Author: lawclaw",
    "Easy. 1",
    "Medium. 2",
    "Hard. 3",
    "Load game. 4",
    "Quit. Q"
]

game_loop_text = [
    "Enter x, y coordinates and desired value [1-9] separated by comma:",
    "Enter U to undo, R to redo",
    "Enter Q to quit"
]

input_error_text = [
    "Immutable square...(Press Enter key to try again)",
    "Invalid input...(Press Enter key to try again)"
]

victory_text = [
    "You solved the puzzle!"
]


def color_prepare():
    """
    Prepare color pair for printing
    :return:
    """
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)


def hide_cursor(stdscr):
    """
    Hide cursor
    :param stdscr:
    :return:
    """
    curses.curs_set(0)
    stdscr.getch()
    curses.curs_set(1)


def clear_screen(stdscr):  # https://stackoverflow.com/a/50560686
    """
    Clears terminal screen
    """
    stdscr.clear()
    stdscr.refresh()


def add_digit(stdscr, y_offset, x_offset, value: str, color: int = None):
    """
    Add digit/char to screen
    :param stdscr:
    :param y_offset:
    :param x_offset:
    :param value:
    :param color:
    :return:
    """
    if color is None:
        stdscr.addstr(
            curses.LINES // 10 + y_offset,
            curses.COLS // 2 + x_offset,
            f"{value} ",
            curses.A_BOLD
        )
    else:
        # Empty squares (mutable squares)
        if value == 0:
            stdscr.addstr(
                curses.LINES // 10 + y_offset,
                curses.COLS // 2 + x_offset,
                "⯀ ",
                curses.color_pair((color % 6) + 1)
            )
        else:
            stdscr.addstr(
                curses.LINES // 10 + y_offset,
                curses.COLS // 2 + x_offset,
                f"{value} ",
                curses.color_pair((color % 6) + 1) | curses.A_BOLD
            )


def add_line(stdscr: curses.wrapper, line: str, y_offset: int, x_offset: int = None):
    """
    Add line to screen
    :param stdscr:
    :param line:
    :param y_offset:
    :param x_offset:
    :return:
    """
    if x_offset is None:
        stdscr.addstr(
            curses.LINES // 10 + y_offset,
            curses.COLS // 2 - ((len(line) + 1) // 2),
            f"{line}\n",
            curses.color_pair(2) | curses.A_BOLD
        )
    else:
        stdscr.addstr(
            curses.LINES // 10 + y_offset,
            curses.COLS // 2 + x_offset,
            f"{line} ",
            curses.color_pair(2) | curses.A_BOLD
        )


def print_board(board: Board, stdscr: curses.wrapper):
    """
    Prints board
    :param stdscr: Main window
    :param board: Sudoku board
    """
    y_offset = 0
    clear_screen(stdscr)

    add_line(stdscr, "🆇", y_offset)
    y_offset += 1
    add_line(stdscr, '┏━━━┳━━━━━━━━━━━━━━━━━━━┳━━━┓', y_offset)
    y_offset += 1

    ui = ['', '']
    ui[0] = '┃ ◆ ┃ 0 1 2 3 4 5 6 7 8 ┃ ◆ ┃'
    ui[1] = '┣━━━╋━━━━━━━━━━━━━━━━━━━╋━━━┫'
    for line in ui:
        add_line(stdscr, line, y_offset)
        y_offset += 1

    for y in range(9):
        x_offset = -15

        if y == 4:
            add_line(stdscr, "🆈", y_offset, -18)

        add_line(stdscr, "┃", y_offset, x_offset)
        x_offset += 2
        add_line(stdscr, str(y), y_offset, x_offset)
        x_offset += 2
        add_line(stdscr, "┃", y_offset, x_offset)
        x_offset += 2

        if y == 4:
            add_line(stdscr, "🆈", y_offset, 15)

        for x in range(9):
            if board.is_immutable(y, x):
                add_digit(stdscr, y_offset, x_offset, board.board_states[-1][y][x])
            else:
                add_digit(stdscr, y_offset, x_offset, board.board_states[-1][y][x], x)
            x_offset += 2

        add_line(stdscr, "┃", y_offset, x_offset)
        x_offset += 2
        add_line(stdscr, str(y), y_offset, x_offset)
        x_offset += 2
        add_line(stdscr, "┃", y_offset, x_offset)
        x_offset += 2

        y_offset += 1

    for line in reversed(ui):
        add_line(stdscr, line, y_offset)
        y_offset += 1
    add_line(stdscr, '┗━━━┻━━━━━━━━━━━━━━━━━━━┻━━━┛', y_offset)
    y_offset += 1

    add_line(stdscr, "🆇", y_offset)

    stdscr.refresh()


def print_menu(stdscr: curses.wrapper):
    """
    Prints game menu
    :param stdscr: Main window
    :param menu_text: Menu text
    :return:
    """
    clear_screen(stdscr)
    for i, menu_line in enumerate(menu_text):
        stdscr.addstr(
            curses.LINES // 3 + i,
            curses.COLS // 2 - ((len(menu_line) + 1) // 2),
            f"{menu_line}\n",
            curses.color_pair(i + 1) | curses.A_BOLD
        )


def print_game_loop_text(stdscr: curses.wrapper):
    y, _ = curses.getsyx()
    for i, line in enumerate(game_loop_text):
        stdscr.addstr(
            y + i + 1,
            curses.COLS // 2 - (len(game_loop_text[i]) // 2),
            game_loop_text[i],
            curses.A_BOLD
        )


def print_input_error_text(stdscr: curses.wrapper, immutable_exception: bool = None):
    y, x = curses.getsyx()

    immutable = 0
    if immutable_exception is None:
        immutable += 1

    stdscr.addstr(
        y - 1,
        curses.COLS // 2 - (len(input_error_text[immutable]) // 2),
        input_error_text[immutable])
    stdscr.refresh()
    hide_cursor(stdscr)




def print_victory(stdscr: curses.wrapper):
    """
    Prints victory
    :param stdscr:
    :return:
    """
    clear_screen(stdscr)
    stdscr.addstr(
        curses.LINES // 2,
        curses.COLS // 2 - (len(victory_text[0]) // 2),
        victory_text[0]
    )
