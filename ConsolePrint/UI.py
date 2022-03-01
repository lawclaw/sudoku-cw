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


def print_board(board: Board, stdscr: curses.wrapper):
    """
    Prints board
    :param board: Sudoku board
    """
    clear_screen(stdscr)
    # Indices
    to_print = [' '.join(str(i) for i in range(0, 9)), '—' * 19]

    # Values
    for row_num, row in enumerate(board.current_state):
        to_print.append(f"{row_num} | {' '.join([str(d) for d in row])} | {row_num}")

    # Indices
    to_print.append('—' * 19)
    to_print.append(' '.join(str(i) for i in range(0, 9)))

    # Add lines to stdscr
    for i, line in enumerate(to_print):
        stdscr.addstr(
            curses.LINES // 10 + i,
            curses.COLS // 2 - ((len(line) + 1) // 2),
            f"{line}\n",
            curses.color_pair(1)
        )

    # Refresh screen
    stdscr.refresh()


def print_menu(menu_text, stdscr):
    """
    Prints game menu
    :param menu_text:
    :return:
    """
    clear_screen(stdscr)
    for i, str in enumerate(menu_text):
        stdscr.addstr(
            curses.LINES // 3 + i,
            curses.COLS // 2 - ((len(str) + 1) // 2),
            f"{str}\n"
        )