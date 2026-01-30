from src.sudoku.model import new_board
from src.sudoku.game_logic import update_board

def test_update_board_does_not_mutate_orginal_board():
    teststring = "0" * 81
    original_board = new_board(teststring)
    move = (0,0,5) # Row: 2, Col: 2, Value: 5
    modified_board = update_board(original_board, move)

    assert original_board != new_board
    assert original_board[0]["value"] != move[2]
    assert modified_board[0]["value"] == move[2]
    
