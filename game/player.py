"""Provide class to manage the player."""


class Player:
    """Implement a player."""

    def __init__(self):
        """Initialize the class."""
        self.score = 0
        self.level = 1
        self.lines = 0

    def reset(self):
        """Reset score and level."""
        self.score = 0
        self.level = 1
        self.lines = 0

    def update_score(self, lines):
        """Update the score."""
        self.score += ((lines * 20) + 10*2**lines) * self.level
        self.level = self.score // 500 + 1

    def update_lines(self, full_lines):
        """Update the lines."""
        self.lines += full_lines

    def get_score(self):
        """Return the score."""
        return self.score

    def get_level(self):
        """Return the level."""
        return self.level
