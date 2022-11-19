"""Provide functions to save the score of the player in a text file."""

import tkinter as tk
from pathlib import Path
from os.path import dirname


def read_high_score():
    """
    Load the text document 'highScore.txt' used to recover the high score.

    Returns
    -------
    current_high_score : integer
        current high score.
    """
    with open(f'{Path(dirname(__file__)).parent}/data/highScore.txt') as f:
        score_recovery = f.readlines()
    return int(score_recovery[0].split()[-1])


def show_high_score(image_high_score):
    """
    Open a secondary window in the GUI with the current highest score.

    A Button allows the player to reset the high score.
    Parameters
    ----------
    image_high_score : PhotoImage object of tkinter module
        gif image illustrating the high score.
    Returns
    -------
    None.
    """
    high_score_window = tk.Toplevel()
    high_score_window.title("High score")
    with open(f'{Path(dirname(__file__)).parent}/data/highScore.txt') as f:
        score_recovery = f.read()
    lbl_image = tk.Label(master=high_score_window, image=image_high_score)
    lbl_image.pack()
    lbl_score_recovery = tk.Label(high_score_window, text=score_recovery,
                                  fg="black", font='Arial 22')
    lbl_score_recovery.pack(side=tk.TOP)
    btn_reset = tk.Button(master=high_score_window,
                          text="Reset", fg="red", font='Arial 15',
                          command=lambda: reset_high_score(high_score_window))
    btn_reset.pack()
    high_score_window.resizable(0, 0)
    high_score_window.mainloop()


def reset_high_score(high_score_window: tk.Toplevel) -> None:
    """
    Reset the high score to 0.

    Erase the current high score.
    Close the window displaying the high score.
    Parameters
    ----------
    high_score_window : tk.Toplevel
        Window displaying the high score.
    Returns
    -------
    None.
    """
    player_name = "Player"
    with open(f'{Path(dirname(__file__)).parent}/data/highScore.txt', 'w') as f:  # noqa E501
        f.write(player_name + '\t' + str(0) + '\n')
    high_score_window.destroy()


def write_high_score(max_seq: int, ent_name: tk.Entry,
                     new_high_score_window: tk.Toplevel) -> None:
    """
    Read the player name from new_high_score_window and closes this window.

    Parameters
    ----------
    max_seq : int
        Score performed by the player.
    ent_name : tk.Entry
        player name extracted from the entry widget of new_high_score_window
    new_high_score_window : tkinter window
        Window where the player can enter his name.
    Returns
    -------
    None.
    """
    player_name = ent_name.get()
    with open(f'{Path(dirname(__file__)).parent}/data/highScore.txt', 'w') as f:  # noqa E501
        f.write(player_name + '\t' + str(max_seq) + '\n')
    new_high_score_window.destroy()


def new_high_score(max_seq: int) -> None:
    """
    Open a secondary window where the player enters his name.

    Parameters
    ----------
    max_seq : int
        Score performed by the player
    Returns
    -------
    None.
    """
    new_high_score_window = tk.Toplevel()
    new_high_score_window.title("New high score")
    lbl_text = tk.Label(new_high_score_window,
                        text="Congratulations.\n You have the new high score",
                        fg="black", font='Arial 22')
    lbl_text.pack()
    lbl_score = tk.Label(new_high_score_window, text=str(max_seq), fg="black",
                         font='Arial 15')
    lbl_score.pack()
    lbl_enter_name = tk.Label(new_high_score_window, text="Enter your name",
                              fg="black")
    lbl_enter_name.pack()
    ent_name = tk.Entry(new_high_score_window)
    ent_name.insert(0, 'Player')
    ent_name.pack()
    btn_enter_name = tk.Button(
        new_high_score_window,
        text="Enter",
        command=lambda:
        write_high_score(max_seq, ent_name, new_high_score_window)
    )
    btn_enter_name.pack()
    new_high_score_window.resizable(0, 0)
    new_high_score_window.mainloop()


def check_high_score(max_seq: int) -> None:
    """
    Compare the score obtained by the player with the high score.

    If it is larger, it saves the new high score.
    Parameters
    ----------
    max_seq : int
        score performed by the player.
    Returns
    -------
    None.
    """
    high_score = read_high_score()
    if max_seq > high_score:
        new_high_score(max_seq)
