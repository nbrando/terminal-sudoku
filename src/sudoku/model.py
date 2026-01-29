def make_cell(value=None, given=False):
    return {
        "value": value,  # None or 1..9
        "given": given,  # bool
        "conflict": False,
    }


def new_board(initial_values=None):
    board = []
    for i in range(81):
        if initial_values:
            value = int(initial_values[i])
            given = bool(value)
        else:
            value = 0
            given = False
        board.append(make_cell(value=value, given=given))

    return board
