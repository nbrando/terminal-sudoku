import curses

curses.initscr()
curses.start_color()

# Colour pairs
COLOUR_GIVEN = curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
COLOUR_USER = curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
COLOUR_CONFLICT = curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)


def draw_board(stdscr, board):
    # Border styles
    top = "┏━━━━━━━┯━━━━━━━┯━━━━━━━┓"
    middle = "┣━━━━━━━┿━━━━━━━┿━━━━━━━┫"
    bottom = "┗━━━━━━━┷━━━━━━━┷━━━━━━━┛"
    box_divider = "│"

    BLANK = "."

    y = 0

    stdscr.addstr(y, 0, top)
    y += 1

    for row in range(9):
        x = 0
        stdscr.addstr(y, x, "┃ ")
        x += 2

        for col in range(9):
            cell = board[row * 9 + col]
            value = BLANK if cell["value"] is None else str(cell['value'])


            stdscr.addstr(y, x, value)
            x += 2

            if col in (2,5):
                stdscr.addstr(y, x, box_divider)
                x += 2

        stdscr.addstr(y, x, "┃")
        y += 1

        if row in (2,5):
            stdscr.addstr(y, 0, middle)
            y += 1

    stdscr.addstr(y, 0, bottom)

