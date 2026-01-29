testGame = "300789024504002607062509008600030180030820760120050040046200050000090006005108000"
testGameSolved = "391786524584312697762549318657934182439821765128657943946273851813495276275168439"

DEBUG = True


def debug(msg):
    if DEBUG:
        print(msg)


# Load board from string.
def loadBoard(gameString):
    # Create empty 9x9 grid
    board = [[0] * 9 for _ in range(9)]

    # Fill rows/columns
    for i, digit in enumerate(gameString):
        row, column = divmod(i, 9)  # Returns (row, column) of index in the 9x9 grid.

        board[row][column] = int(digit)

    return board


# Return game array as printable string
def drawBoard(board):
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
            cell = BLANK if value == 0 else str(value)  # Replace 0 with .
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


def validateBoard(board):
    pass


def validateRows():
    pass


def validateColumns():
    pass


def validateBoxes():
    pass


# Accept row,col and value from player.
def playerInput():
    row = int(input("Enter Row (1-9): "))
    col = int(input("Enter Column (1-9): "))
    value = int(input("Enter input value (0-9): "))

    return (row - 1, col - 1, value)


game1 = loadBoard(testGame)
move = ""

while move != exit:
    print(drawBoard(game1))
    move = playerInput()

    game1 = updateBoard(game1, move)
