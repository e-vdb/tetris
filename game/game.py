# game/game.py
"""Provide a class to manage the game gui."""

import tkinter as tk
from game.tetris import Tetris
from game.exceptions import GameOver
from game.stop_watch import StopWatch
from game.widget_gui import IntValue, TextValueFrame
from game.save_score import show_high_score, check_high_score
from game.help_functions import about, print_rules
from pathlib import Path
from os.path import dirname, join

COLUMNS = 10
ROWS = 22
WIDTH = 20
LENGTH = 20


class Game(tk.Tk):
    """Class to manage the tetris game UI."""

    def __init__(self):
        """Initialize the UI and start it."""
        tk.Tk.__init__(self)
        self.sw = StopWatch(self)
        self.sw.grid(row=0, column=0, columnspan=2)

        self.game_over_label = TextValueFrame(self, "")
        self.game_over_label.grid(row=1, column=0, columnspan=2)

        self.score = IntValue(self, label_text="Score")
        self.score.grid(row=1, column=2, columnspan=2)

        self.level = IntValue(self, label_text="Level", init_value=1)
        self.level.grid(row=2, column=2, columnspan=2)

        self.lines = IntValue(self, label_text="Lines")
        self.lines.grid(row=3, column=2, columnspan=2)

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=2, column=1)
        self.canvas = tk.Canvas(self.main_frame, width=500, height=500)
        self.canvas.grid(row=1, column=2, rowspan=2)

        self.tetris = Tetris(self.canvas, self.score, self.lines, self.level)

        self.set_up_buttons()
        self.set_up_keyboards_events()
        self.set_up_menu()

        # Start the game GUI
        self.mainloop()

    def set_up_buttons(self):
        """Set up the buttons in UI."""
        button_frame = tk.Frame(self)
        button_frame.grid(row=0, column=0)
        start_button = tk.Button(
            button_frame,
            text='Start',
            command=lambda: self.start_game()
        )
        start_button.grid(row=0, column=0)
        stop_button = tk.Button(
            button_frame,
            text='Reset',
            command=lambda: self.reset_game()
        )
        stop_button.grid(row=1, column=0)

    def set_up_keyboards_events(self):
        """Set up the keyboard events."""
        self.bind('<Left>',
                  lambda event, x='left': self.tetris.tetromino.move(x))
        self.bind('<Right>',
                  lambda event, x='right': self.tetris.tetromino.move(x))
        self.bind('<Up>', lambda event: self.tetris.tetromino.rotate())

    def set_up_menu(self):
        """Set up the menu."""
        top = tk.Menu(self)
        self.config(menu=top)
        game_menu = tk.Menu(top, tearoff=False)
        help_menu = tk.Menu(top, tearoff=False)
        top.add_cascade(label='Game', menu=game_menu)
        top.add_cascade(label='Help', menu=help_menu)

        name = join(Path(dirname(__file__)).parent, 'data/highScore.gif')
        image_high_score = tk.PhotoImage(file=name)
        game_menu.add_command(label='Exit', command=self.destroy)
        game_menu.add_command(
            label='Scores',
            command=lambda: show_high_score(image_high_score)
        )

        help_menu.add_command(label='About', command=about)
        help_menu.add_command(label='Rules', command=print_rules)

    def start_game(self) -> None:
        """Start the game."""
        try:
            self.sw.Start()
            self.tetris.game()
        except GameOver:
            self.tetris.stop()
            self.sw.Stop()
            self.game_over_label.update("Game Over")
            check_high_score(self.score.get())

    def reset_game(self) -> None:
        """Reset the game."""
        self.sw.Stop()
        self.sw.Reset()
        self.tetris.reinit()
        self.score.reset()
        self.lines.reset()
        self.level.reset()
        self.game_over_label.reset()
