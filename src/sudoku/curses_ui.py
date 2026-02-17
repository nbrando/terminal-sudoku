import curses

from sudoku.curses_renderer import draw_board, init_colours
from sudoku.game_logic import update
from sudoku.model import new_game


def run(puzzle):
    def wrapped(stdscr):
        return curses_main(stdscr, puzzle)

    curses.wrapper(wrapped)


def curses_main(stdscr, puzzle):
    curses.curs_set(0)  # Hide terminals default cursor
    stdscr.nodelay(False)
    stdscr.keypad(True)

    init_colours()

    game = new_game(puzzle)

    cursor_row, cursor_col = 0, 0

    while True:
        stdscr.clear()

        if game["solved"]:
            draw_board(stdscr, game["board"])
            stdscr.addstr(14, 2, "You Win!")
            stdscr.addstr(15, 2, "Play again? (y/n)")
        else:
            draw_board(stdscr, game["board"], cursor_pos=(cursor_row, cursor_col))
            stdscr.addstr(14, 2, "Navigate with WASD or arrow keys: ↑ ↓ ← →")
            stdscr.addstr(15, 2, "Press 'q' to quit")

        stdscr.refresh()
        key = stdscr.getch()

        # Quit if 'q' or 'Q' is pressed
        if key in (ord("q"), ord("Q"), ord("n"), ord("N")):
            break

        # Start new game
        elif key in (ord("y"), ord("Y")):
            game = new_game(puzzle)

        # Handle number input 0–9
        elif ord("0") <= key <= ord("9"):
            number = key - ord("0")  # Convert key code to integer 0–9
            game = update(game, (cursor_row, cursor_col, number))

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
