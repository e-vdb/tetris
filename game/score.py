"""Provide class to manage the score."""

import tkinter as tk


class Score(tk.Frame):
    """Implement a score frame widget."""

    def __init__(self, parent=None, **kw):
        """Initialize the class."""
        tk.Frame.__init__(self, parent, kw)
        self.score = tk.IntVar()
        self.score.set(0)
        self.score_lab = tk.Label(self, textvariable=self.score)
        self.score_lab.pack(fill=tk.X, expand=tk.NO, pady=2, padx=2)

    def update(self, score):
        """Update the score."""
        self.score.set(score)

    def reset(self):
        """Reset the score."""
        self.score.set(0)

    def get(self):
        """Get the score."""
        return self.score.get()
