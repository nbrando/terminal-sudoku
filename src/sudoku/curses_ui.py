import curses

from curses_renderer import draw_board
from model import new_board


def curses_main(stdscr):
    curses.curs_set(1)
    stdscr.nodelay(False)
    stdscr.keypad(True)

    testboard = (
    "300786024504002607062509008600030180030820760120050040046200050000090006005108000"
    )

    board = new_board(testboard)

    while True:
        stdscr.clear()

        draw_board(stdscr, board)

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord("q"):
            break

curses.wrapper(curses_main)