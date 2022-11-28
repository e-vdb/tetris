"""Define help functions for GUI menu."""

import tkinter as tk
from pathlib import Path
from os.path import dirname, join

TEXT_FOLDER = join(Path(dirname(__file__)).parent, 'data')


def print_rules() -> None:
    """
    Display rules and gameplay.

    Load a text files 'how-to.txt'.
    Open a second window.
    Write the content of the text document.
    Returns
    -------
    None.
    """
    rule_window = tk.Toplevel()
    rule_window.resizable(False, False)
    rule_window.title("How to play?")
    with open(f'{TEXT_FOLDER}/how-to.txt') as f:
        how_to = f.read()
    lab_rule = tk.Label(rule_window, text=how_to,
                        fg="black", anchor="e", justify=tk.LEFT)
    lab_rule.pack(side=tk.TOP)
    rule_window.mainloop()


def about() -> None:
    """
    Display licence information.

    Load the text document 'about.txt'.
    Open a secondary window.
    Write the content of the text document.

    Returns
    -------
    None.
    """
    about_window = tk.Toplevel()
    about_window.resizable(False, False)
    about_window.title("About")
    with open(f'{TEXT_FOLDER}/about.txt') as f:
        about = f.read()
    lbl_about = tk.Label(about_window, text=about,
                         fg="black", anchor="e", justify=tk.LEFT)
    lbl_about.pack(side=tk.TOP)
    about_window.mainloop()
