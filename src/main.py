from sudoku.curses_ui import run as run_curses
from sudoku.game_logic import update
from sudoku.model import new_game
from sudoku.player_input import player_input
from sudoku.renderer import draw_board

PUZZLE = (
    "300786024504002607062509008600030180030820760120050040046200050000090006005108000"
)
SOLVED = (
    "091786524584312697762549318657934182439821765128657943946273851813495276275168439"
)


def run_ascii():
    game = new_game(PUZZLE)
    while True:
        draw_board(game["board"])
        msg = player_input()
        game = update(game, msg)

        if msg == "exit":
            break


if __name__ == "__main__":
    # run_ascii()
    run_curses(SOLVED)
