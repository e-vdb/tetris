"""Provide class for tetris game."""

import itertools

from game.player import Player
from game.tetrominoes import Tetromino


COLUMNS = 10
ROWS = 22
WIDTH = 20
LENGTH = 20


class Tetris:
    """Class for Tetris."""

    def __init__(self, can, score, lines, level):
        """Build the class."""
        self.can = can
        self.game_over = False
        self.cell = self.init_cell()
        self.draw_grid()
        self.player = Player()
        self.score = score
        self.lines = lines
        self.level = level

    def init_cell(self):
        """Initialise the cell table."""
        return [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

    def draw_grid(self):
        """Draw the tetris grid."""
        for i, j in itertools.product(range(ROWS), range(COLUMNS)):
            self.can.create_rectangle(
                0 + WIDTH * j,
                0 + WIDTH * i, 0 + LENGTH + WIDTH * j,
                0 + LENGTH + WIDTH * i,
                outline='black'
            )

    def reinit(self):
        """Reinit tetris game."""
        self.game_over = True
        self.can.delete('all')
        self.cell = self.init_cell()
        self.draw_grid()
        self.player.reset()
        self.game_over = False

    def game(self):
        """Play."""
        while not self.game_over:
            self.tetromino = Tetromino(self.can, self.cell, self.player.level)
            self.tetromino.play()
            self.fix_piece()
            self.check_row()

    def pause(self):
        """Pause the game (To do)."""
        pass

    def fix_piece(self):
        """Fill the cell table."""
        for piece in self.tetromino.pieces:
            x1, y1 = self.tetromino.get_one_piece_position(piece)
            self.cell[int(y1)][int(x1)] = 1

    def stop(self):
        """Stop the game."""
        self.game_over = True

    def check_row(self):
        """Check if there are full rows."""
        full_rows: int = 0
        for count, row in enumerate(self.cell):
            if sum(row) == COLUMNS:
                print(f'row {count} is full')
                self.find_all_items_in_canvas_above_row(count)
                self.cell.pop(count)
                self.cell.insert(0, [0 for _ in range(COLUMNS)])
                full_rows += 1
        self.player.update_score(lines=full_rows)
        self.player.update_lines(full_rows)
        self.score.update(self.player.score)
        self.lines.update(self.player.lines)
        self.level.update(self.player.level)

    def get_item_position(self, item):
        """Get cell position of an item."""
        x1, y1, _, _ = self.can.coords(item)
        return x1//20, y1//20

    def find_all_items_in_canvas_above_row(self, row):
        """Find all items in canvas above a given row."""
        all_items = [item for item in self.can.find_all()
                     if item >= ROWS*COLUMNS+1]
        for item in all_items:
            x, y = self.get_item_position(item)
            if y == row:
                self.can.delete(item)
            elif y < row:
                self.can.move(item, 0, 20)
