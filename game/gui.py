"""GUI module."""

import tkinter as tk
from tetris import Tetris

COLUMNS = 10
ROWS = 22
WIDTH = 20
LENGTH = 20

root = tk.Tk()
main_frame = tk.Frame(root)
main_frame.pack()
canvas = tk.Canvas(main_frame, width=500, height=500)
canvas.pack()

tetris = Tetris(canvas)

start_button = tk.Button(main_frame, text='Start', command=tetris.game)
start_button.pack()
stop_button = tk.Button(main_frame, text='Reset', command=tetris.reinit)
stop_button.pack()

root.bind('<Left>', lambda event,x='left': tetris.tetromino.move(x))
root.bind('<Right>', lambda event,x='right': tetris.tetromino.move(x))

root.mainloop()
