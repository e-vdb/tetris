"""GUI module."""

import tkinter as tk
from tetris import Tetris
from stop_watch import StopWatch


def start_game(tetris: Tetris, sw: StopWatch):
    """Start the game."""
    sw.Start()
    tetris.game()


def reset_game(tetris: Tetris, sw: StopWatch):
    """Reset the game."""
    sw.Stop()
    sw.Reset()
    tetris.reinit()


COLUMNS = 10
ROWS = 22
WIDTH = 20
LENGTH = 20

root = tk.Tk()
sw = StopWatch(root)
sw.grid(row=0, column=0, columnspan=2)

main_frame = tk.Frame(root)
main_frame.grid(row=1, column=1)
canvas = tk.Canvas(main_frame, width=500, height=500)
canvas.grid(row=1, column=2)

tetris = Tetris(canvas)

button_frame = tk.Frame(root)
button_frame.grid(row=0, column=0)
start_button = tk.Button(
    button_frame,
    text='Start',
    command=lambda: start_game(tetris, sw)
)
start_button.grid(row=0, column=0)
stop_button = tk.Button(
    button_frame,
    text='Reset',
    command=lambda: reset_game(tetris, sw)
)
stop_button.grid(row=1, column=0)


# Keyboards events
root.bind('<Left>', lambda event, x='left': tetris.tetromino.move(x))
root.bind('<Right>', lambda event, x='right': tetris.tetromino.move(x))
root.bind('<Up>', lambda event: tetris.tetromino.rotate())

root.mainloop()
