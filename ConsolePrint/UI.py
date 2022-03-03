import curses

from GameEngine.Board import Board


def hide_cursor(stdscr):
    curses.curs_set(0)
    stdscr.getch()
    curses.curs_set(1)


def clear_screen(stdscr):  # https://stackoverflow.com/a/50560686
    """
    Clears terminal screen
    """
    stdscr.clear()
    stdscr.refresh()


def add_digit(stdscr, y_offset, x_offset, value: str, color=None):
    if color is None:
        stdscr.addstr(
            curses.LINES // 10 + y_offset,
            curses.COLS // 2 + x_offset,
            f"{value} ",
            curses.color_pair(1)
        )
    elif color == 'CYAN':
        stdscr.addstr(
            curses.LINES // 10 + y_offset,
            curses.COLS // 2 + x_offset,
            f"{value} ",
            curses.color_pair(2)
        )


def add_line(stdscr, y_offset, line: str):
    stdscr.addstr(
        curses.LINES // 10 + y_offset,
        curses.COLS // 2 - ((len(line) + 1) // 2),
        f"{line}\n",
        curses.color_pair(1)
    )

def print_board(board: Board, stdscr: curses.wrapper):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    #curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    """
    Prints board
    :param board: Sudoku board
    """
    y_offset = 0
    clear_screen(stdscr)

    ui = [' '.join(str(i) for i in range(0, 9)), '—' * 19]
    for line in ui:
        add_line(stdscr, y_offset, line)
        y_offset += 1

    for y in range(9):
        x_offset = -13
        add_digit(stdscr, y_offset, x_offset, y)
        x_offset += 2
        add_digit(stdscr, y_offset, x_offset, "|")
        x_offset += 2
        for x in range(9):
            if board.is_immutable(y, x):
                add_digit(stdscr, y_offset, x_offset, board.current_state[y][x])
            else:
                add_digit(stdscr, y_offset, x_offset, board.current_state[y][x], "CYAN")
            x_offset += 2
        add_digit(stdscr, y_offset, x_offset, "|")
        x_offset += 2
        add_digit(stdscr, y_offset, x_offset, y)

        x_offset += 1
        y_offset += 1

    for line in reversed(ui):
        add_line(stdscr, y_offset, line)
        y_offset += 1

    # Refresh screen
    stdscr.refresh()


def print_menu(menu_text, stdscr: curses.wrapper):
    """
    Prints game menu
    :param menu_text:
    :return:
    """
    clear_screen(stdscr)
    for i, menu_line in enumerate(menu_text):
        stdscr.addstr(
            curses.LINES // 3 + i,
            curses.COLS // 2 - ((len(menu_line) + 1) // 2),
            f"{menu_line}\n"
        )
