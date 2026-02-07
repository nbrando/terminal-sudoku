import copy


# Enter value into cell
def update_board(board, move):
    new_board = copy.deepcopy(board)

    # Convert 2D coordinates to 1D index for flat board
    cell_index = move[0] * 9 + move[1]  # ((Row * 9) + Column)

    if board[cell_index]["given"]:
        # Cannot modify pre-filled cells
        return board

    # Apply the player's move
    new_board[cell_index]["value"] = move[2] if move[2] != 0 else None

    # Validate the board (recalculate all conflicts)
    return validate_board(new_board)


def validate_board(board):
    # Recalculate all conflicts on the board
    clear_conflicts(board)
    check_rows(board)
    check_columns(board)
    check_boxes(board)

    return board


def clear_conflicts(board):
    # Reset all conflicts on the board to false
    for cell in board:
        cell["conflict"] = False

    return board


def mark_conflicts(board, indices):
    # Mark conflicts among a input set of cells (rows, columns, or boxes)
    seen = {}

    for index in indices:
        value = board[index]["value"]
        if value is None:
            continue

        # Both current and previously seen cell are in conflict
        if value in seen:
            board[index]["conflict"] = True
            board[seen[value]]["conflict"] = True

        else:
            seen[value] = index


def check_rows(board):
    # Check each row for duplicate values and mark conflicts.
    for row in range(9):
        indices = [row * 9 + column for column in range(9)]
        mark_conflicts(board, indices)


def check_columns(board):
    # Check each column for duplicate values and mark conflicts.
    for column in range(9):
        indices = [row * 9 + column for row in range(9)]
        mark_conflicts(board, indices)


def check_boxes(board):
    # Check each 3x3 box for duplicate values and mark conflicts.
    for box_row in range(3):
        for box_column in range(3):
            indices = []

            for row in range(box_row * 3, (box_row * 3) + 3):
                for column in range(box_column * 3, (box_column * 3) + 3):
                    indices.append(row * 9 + column)

            mark_conflicts(board, indices)
