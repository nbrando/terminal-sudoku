from src.sudoku.game_logic import update
from src.sudoku.model import new_game


def test_update_board_does_not_mutate_orginal_board():
    teststring = "0" * 81
    original_game = new_game(teststring)
    move = (0, 0, 5)  # Row: 2, Col: 2, Value: 5
    modified_game = update(original_game, move)

    assert original_game != new_game
    assert original_game["board"][0]["value"] != move[2]
    assert modified_game["board"][0]["value"] == move[2]
