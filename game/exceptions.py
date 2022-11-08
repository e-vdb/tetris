"""Provide custom exceptions."""


class GameOver(Exception):
    """Exception raised when the game is over."""

    def __init__(self):
        """Build the class."""
        super().__init__('Game Over')
