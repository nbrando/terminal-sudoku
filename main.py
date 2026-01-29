from model import new_board
from renderer import draw_board
from player_input import player_input
from game_logic import update_board


testboard = "300789024504002607062509008600030180030820760120050040046200050000090006005108000"
testGameSolved = "391786524584312697762549318657934182439821765128657943946273851813495276275168439"


if __name__ == "__main__":
    board = new_board(testboard)
    while True:
        draw_board(board)
        msg = player_input()
        board = update_board(board, msg)

        if msg == "exit":
            break
