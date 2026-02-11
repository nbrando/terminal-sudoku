# Terminal Sudoku (Python) WIP

A Python Sudoku terminal app. Right now it has both a basic print-based UI, and a curses UI.

I’ve been working on this mainly as a learning project: practicing Git/GitHub workflows (small commits, decent structure, readable history) and trying to keep the repo layout closer to how “real” projects are organized. Those are two areas I feel my degree didn’t spend much time on.

I’m loosely following the Elm Architecture / TEA idea: keeping a single model of the game state, update state in one place, and have the UI just render what it’s given, translate input into messages/actions (haven't sorted this out properly yet). That should make it easier to add features later (undo/redo, hints, solver, etc.) without the UI and game logic getting tangled.


## Run

Install requirements, then run:

```bash
python src/main.py