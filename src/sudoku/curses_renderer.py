import curses


# Colour pairs
COLOUR_GIVEN = 1
COLOUR_USER = 2
COLOUR_CONFLICT = 3


def init_colours():
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(COLOUR_GIVEN, curses.COLOR_CYAN, -1)
    curses.init_pair(COLOUR_USER, curses.COLOR_WHITE, -1)
    curses.init_pair(COLOUR_CONFLICT, curses.COLOR_RED, -1) 


def draw_board(stdscr, board, cursor_pos):
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
            value = BLANK if cell["value"] is None else str(cell["value"])

            # Set colour based on cell state
            if cell["conflict"]:
                attr = curses.color_pair(COLOUR_CONFLICT)
            elif cell["given"]:
                attr = curses.color_pair(COLOUR_GIVEN)
            else:
                attr = curses.color_pair(COLOUR_USER)


            # Highlight cursor location and left/right to make a wider cursor.
            if cursor_pos and (row, col) == cursor_pos:
                stdscr.addstr(y, x - 1, f" {value} ", curses.A_STANDOUT)
            else:
                stdscr.addstr(y, x, value, attr)

            x += 2
            if col in (2, 5):
                stdscr.addstr(y, x, box_divider)
                x += 2

        stdscr.addstr(y, x, "┃")
        y += 1

        if row in (2, 5):
            stdscr.addstr(y, 0, middle)
            y += 1

    stdscr.addstr(y, 0, bottom)
