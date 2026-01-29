# Enter value into cell
def update_board(board, move):
    cell_index = move[0] * 9 + move[1]
    if not board[cell_index]["given"]:
        board[cell_index]["value"] = move[2]

    return board


def validate_board(board):
    pass


def is_valid_row(row):
    pass


def validateColumn(col):
    pass


def validateBox(box):
    pass
