"""GUI module."""

import tkinter as tk
from tetris import Tetris
from exceptions import GameOver
from stop_watch import StopWatch
from widget_gui import IntValue
from save_score import show_high_score, check_high_score
from pathlib import Path
from os.path import dirname, join


def start_game(tetris: Tetris, sw: StopWatch, score: IntValue):
    """Start the game."""
    try:
        sw.Start()
        tetris.game()
    except GameOver:
        tetris.stop()
        sw.Stop()
        check_high_score(score.get())


def reset_game(tetris: Tetris, sw: StopWatch, score: IntValue,
               lines: IntValue, level: IntValue) -> None:
    """Reset the game."""
    sw.Stop()
    sw.Reset()
    tetris.reinit()
    score.reset()
    lines.reset()
    level.reset()


COLUMNS = 10
ROWS = 22
WIDTH = 20
LENGTH = 20

root = tk.Tk()

sw = StopWatch(root)
sw.grid(row=0, column=0, columnspan=2)

score = IntValue(root, label_text="Score")
score.grid(row=1, column=2, columnspan=2)

level = IntValue(root, label_text="Level", init_value=1)
level.grid(row=2, column=2, columnspan=2)

lines = IntValue(root, label_text="Lines")
lines.grid(row=3, column=2, columnspan=2)

main_frame = tk.Frame(root)
main_frame.grid(row=2, column=1)
canvas = tk.Canvas(main_frame, width=500, height=500)
canvas.grid(row=1, column=2, rowspan=2)

tetris = Tetris(canvas, score, lines, level)

button_frame = tk.Frame(root)
button_frame.grid(row=0, column=0)
start_button = tk.Button(
    button_frame,
    text='Start',
    command=lambda: start_game(tetris, sw, score)
)
start_button.grid(row=0, column=0)
stop_button = tk.Button(
    button_frame,
    text='Reset',
    command=lambda: reset_game(tetris, sw, score, lines, level)
)
stop_button.grid(row=1, column=0)


# Keyboards events
root.bind('<Left>', lambda event, x='left': tetris.tetromino.move(x))
root.bind('<Right>', lambda event, x='right': tetris.tetromino.move(x))
root.bind('<Up>', lambda event: tetris.tetromino.rotate())

top = tk.Menu(root)
root.config(menu=top)
game_menu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=game_menu)

name = join(Path(dirname(__file__)).parent, 'data/highScore.gif')
image_high_score = tk.PhotoImage(file=name)
game_menu.add_command(label='Exit', command=root.destroy)
game_menu.add_command(
    label='Scores',
    command=lambda: show_high_score(image_high_score)
)

root.mainloop()
