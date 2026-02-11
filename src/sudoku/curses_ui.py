import curses

from curses_renderer import draw_board, init_colours
from game_logic import update_board
from model import new_board


def curses_main(stdscr):
    curses.curs_set(0)  # Hide terminals default cursor
    stdscr.nodelay(False)
    stdscr.keypad(True)

    init_colours()

    testboard = "300786024504002607062509008600030180030820760120050040046200050000090006005108000"

    board = new_board(testboard)

    cursor_row, cursor_col = 0, 0

    while True:
        stdscr.clear()

        draw_board(stdscr, board, cursor_pos=(cursor_row, cursor_col))
        stdscr.addstr(14, 2, "Navigate with WASD or arrow keys: ↑ ↓ ← →")
        stdscr.addstr(15, 2, "Press 'q' to quit")

        stdscr.refresh()
        key = stdscr.getch()

        # Quit if 'q' or 'Q' is pressed
        if key == ord("q") or key == ord("Q"):
            break

        # Handle number input 0–9
        elif ord("0") <= key <= ord("9"):
            number = key - ord("0")  # Convert key code to integer 0–9
            board = update_board(board, (cursor_row, cursor_col, number))

        # Handle Arrow keys and WASD for navigation
        elif (
            key == curses.KEY_UP or key == ord("w") or key == ord("W")
        ) and cursor_row > 0:
            cursor_row -= 1
        elif (
            key == curses.KEY_DOWN or key == ord("s") or key == ord("S")
        ) and cursor_row < 8:
            cursor_row += 1
        elif (
            key == curses.KEY_LEFT or key == ord("a") or key == ord("A")
        ) and cursor_col > 0:
            cursor_col -= 1
        elif (
            key == curses.KEY_RIGHT or key == ord("d") or key == ord("D")
        ) and cursor_col < 8:
            cursor_col += 1


curses.wrapper(curses_main)
