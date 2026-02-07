COLOUR = {
    "given": "\033[38;5;244m",  # Grey
    "user": "\033[38;5;15m",  # White
    "conflict": "\033[38;5;196m",  # Red
    "reset": "\033[0m",  # Reset colour to default
}


def draw_board(board):
    lines = []

    # Border styles
    top = "┏━━━━━━━┯━━━━━━━┯━━━━━━━┓"
    middle = "┣━━━━━━━┿━━━━━━━┿━━━━━━━┫"
    bottom = "┗━━━━━━━┷━━━━━━━┷━━━━━━━┛"

    boxDivider = "│"
    BLANK = "."

    # Insert top border
    lines.append(top)

    line = []

    for i, cell in enumerate(board):
        colour = COLOUR["user"]

        # Set text colour
        if cell["conflict"]:
            colour = COLOUR["conflict"]

        elif cell["given"]:
            colour = COLOUR["given"]

        value = (
            BLANK if cell["value"] is None else f"{colour}{cell['value']}{COLOUR['reset']}"
        )
        line.append(value)

        # Insert divider between boxes
        if i % 9 in (2, 5):
            line.append(boxDivider)

        # End of row
        if i % 9 == 8:
            lines.append("┃ " + " ".join(line) + " ┃")
            line = []

            # Insert middle borders
            if i // 9 in (2, 5):
                lines.append(middle)

    # Insert bottom border
    lines.append(bottom)

    print("\n".join(lines))
