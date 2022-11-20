"""Provide class to manage integer variable label in gui."""

import tkinter as tk


class IntValue(tk.Frame):
    """Implement a value frame widget."""

    def __init__(self, parent=None, label_text="", init_value: int = 0, **kw):
        """Initialize the class."""
        tk.Frame.__init__(self, parent, kw)
        self.value = tk.IntVar()
        self.value.set(init_value)
        self.init_value = init_value

        self.lab = tk.Label(self, text=label_text)
        self.lab.pack(fill=tk.X, expand=tk.NO, pady=2, padx=2)
        self.value_lab = tk.Label(self, textvariable=self.value)
        self.value_lab.pack(fill=tk.X, expand=tk.NO, pady=2, padx=2)

    def update(self, new_value):
        """Update the value."""
        self.value.set(new_value)

    def reset(self):
        """Reset the value."""
        self.value.set(self.init_value)

    def get(self):
        """Get the value."""
        return self.value.get()


class TextValueFrame(tk.Frame):
    """Implement a text value frame widget."""

    def __init__(self, parent=None, init_text="", **kw):
        """Initialize the class."""
        tk.Frame.__init__(self, parent, kw)
        self.text = tk.StringVar()
        self.text.set(init_text)
        self.init_text = init_text

        self.text_lab = tk.Label(self, textvariable=self.text)
        self.text_lab.pack(fill=tk.X, expand=tk.NO, pady=2, padx=2)

    def update(self, new_value):
        """Update the value."""
        self.text.set(new_value)

    def reset(self):
        """Reset the value."""
        self.text.set(self.init_text)
