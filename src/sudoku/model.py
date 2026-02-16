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
            value = int(initial_values[i]) if initial_values[i] != "0" else None
            given = bool(value)
        else:
            value = None
            given = False
        board.append(make_cell(value=value, given=given))

    return board


def new_game(initial_values=None):
    return {"board": new_board(initial_values), "solved": False}
