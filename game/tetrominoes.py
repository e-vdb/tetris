"""Tetromino class."""

from random import choice
import time
from shapes import ShapeL, ShapeSquare, ShapeZ, ShapeI, ShapeJ, ShapeS, ShapeT

Refresh_Sec = 0.5
Ball_min_movement = 1
all_shapes = [ShapeI, ShapeL, ShapeJ, ShapeSquare, ShapeZ, ShapeS, ShapeT]
ROWS_COUNT = 22


class Tetromino:
    """Class for tetromino."""

    def __init__(self, can, cell):
        """Initialize class."""
        self.can = can
        self.cell = cell
        self.shape = choice(all_shapes)(self.can, self.cell)
        self.shape.init_piece()
        self.pieces = self.shape.pieces
        self.piece_in_motion = False

        self.shift_x = 0
        self.shift_y = 20

    def move(self, side):
        """Move tetromino left or right."""
        if self.piece_in_motion:
            xmin, _, xmax, _ = self.get_position()

            if side == 'right' and xmax < 9:
                shift_x = 20
            elif side == 'left' and xmin > 0:
                shift_x = -20
            else:
                shift_x = 0
            if self.check_valid_move(shift_x,  0):
                for piece in self.pieces:
                    self.can.move(piece, shift_x, 0)

    def check_valid_move(self, shift_x, shift_y):
        """Check if move is valid."""
        for piece in self.pieces:
            x, y = self.get_one_piece_position(piece)
            if x + shift_x//20 < 0 or x + shift_x//20 > 9:
                return False
            if int(y + shift_y // 20) >= 0 and self.cell[int(y + shift_y // 20)][int(x + shift_x//20)] == 1:  # noqa E501
                return False
        return True

    def motion(self):
        """Move tetromino down."""
        if self.check_valid_move(self.shift_x,  self.shift_y):
            for piece in reversed(self.pieces):
                self.can.move(piece, self.shift_x, self.shift_y)
            self.can.update()
            time.sleep(Refresh_Sec)
        else:
            self.piece_in_motion = False
        xmin, ymin, xmax, ymax = self.get_position()
        if ymax >= ROWS_COUNT-1:
            self.piece_in_motion = False

    def get_one_piece_position(self, piece):
        """Get position of one piece."""
        x1, y1, _, _ = self.can.coords(piece)
        return x1//20, y1//20

    def get_position(self):
        """Get position of tetromino."""
        all_x = []
        all_y = []
        for piece in self.pieces:
            x, y = self.get_one_piece_position(piece)
            all_x.append(x)
            all_y.append(y)
        return min(all_x), min(all_y), max(all_x), max(all_y)

    def check_valid_rotation(self, angle):
        """Check if rotation is valid."""
        for cooord, piece in zip(self.shape.rotation[angle], self.pieces):
            shift_x = cooord[0] * 20
            shift_y = cooord[1] * 20
            if not self.check_valid_move(shift_x, shift_y):
                return False
        return True

    def rotate(self):
        """Rotate tetromino."""
        init_angle = self.shape.angle
        next_angle = (init_angle + 90) % 360
        if self.check_valid_rotation(next_angle):
            self.shape.angle = next_angle
            for cooord, piece in zip(self.shape.rotation[next_angle],
                                     self.pieces):
                self.can.move(piece, cooord[0]*20, cooord[1]*20)
                self.can.update()

    def play(self):
        """Play tetromino."""
        self.piece_in_motion = True
        while self.piece_in_motion:
            self.motion()
            self.get_position()

    def stop(self):
        """Stop tetromino."""
        self.piece_in_motion = False
