testGame = "300789024504002607062509008600030180030820760120050040046200050000090006005108000"
testGameSolved = "391786524584312697762549318657934182439821765128657943946273851813495276275168439"

DEBUG = True

COLOUR = {
    "given": "\033[38;5;244m",  # Grey
    "user": "\033[38;5;15m",  # White
    "conflict": "\033[38;5;196m",  # Red
    "reset": "\033[0m",  # Reset colour to default
}

conflicts = []


def debug(msg):
    if DEBUG:
        print(msg)


# Load board from string.
def loadBoard(gameString):
    # Create empty 9x9 grid, and given mask
    board = [[0] * 9 for _ in range(9)]
    given = [[False] * 9 for _ in range(9)]

    # Fill board rows/columns and mask
    for i, digit in enumerate(gameString):
        row, column = divmod(i, 9)  # Returns (row, column) of index in the 9x9 grid.

        if digit in "123456789":
            board[row][column] = int(digit)
            given[row][column] = True

    return board, given


# Return game array as printable string
def drawBoard(board, given):
    lines = []

    # Border styles
    top = "┏━━━━━━━┯━━━━━━━┯━━━━━━━┓"
    middle = "┣━━━━━━━┿━━━━━━━┿━━━━━━━┫"
    bottom = "┗━━━━━━━┷━━━━━━━┷━━━━━━━┛"

    boxDivider = "│"
    BLANK = "."

    # Insert top border
    lines.append(top)

    for row in range(len(board)):
        line = []
        for col in range(len(board)):
            value = board[row][col]

            colour = COLOUR["user"]

            if (row, col) in conflicts:
                colour = COLOUR["conflict"]
            elif given[row][col]:
                colour = COLOUR["given"]

            cell = BLANK if value == 0 else f"{colour}{value}{COLOUR["reset"]}"  
            line.append(cell)

            # Insert divider between boxes
            if col in (2, 5):
                line.append(boxDivider)

        lines.append("┃ " + " ".join(line) + " ┃")

        # Insert middle borders
        if row in (2, 5):
            lines.append(middle)

    # Insert bottom border
    lines.append(bottom)

    return "\n".join(lines)


# Enter value into cell
def updateBoard(board, move):
    board[move[0]][move[1]] = move[2]

    return board
    

def validateBoard(board, move):
    pass


def validateRow(row):
    for i in range(1, 10):
        if row.count(i) > 1:
            return row



def validateColumn(col):
    pass


def validateBox(box):
    pass


# Accept row,col and value from player.
def playerInput():
    row = int(input("Enter Row (1-9): "))
    col = int(input("Enter Column (1-9): "))
    value = int(input("Enter input value (0-9): "))

    return (row - 1, col - 1, value)


game, given = loadBoard(testGame)


move = ""

while move != exit:
    print(drawBoard(game, given))
    move = playerInput()

    game = updateBoard(game, move)
