from random import randint, choice
import time
from shapes import ShapeL, ShapeSquare, ShapeZ, ShapeI, ShapeJ, ShapeS, ShapeT

Refresh_Sec = 0.5
Ball_min_movement = 1
all_shapes = [ShapeI, ShapeL, ShapeJ, ShapeSquare, ShapeZ, ShapeS, ShapeT]
ROWS_COUNT = 22


class Tetromino:

    def __init__(self, can, cell):
        self.length = 4
        self.width = 20
        self.can = can
        self.cell = cell
        self.shape = choice(all_shapes)(self.can)
        self.shape.init_piece()
        self.pieces = self.shape.pieces
        self.piece_in_motion = False

        self.shift_x = 0
        self.shift_y = 20

    def init_piece(self):
        init_x = randint(0, 9) * 20

        for i in range(self.length):
            init_y = (0+i) * 20
            self.pieces.append(self.can.create_rectangle(
                init_x,
                init_y,
                init_x + self.width,
                init_y + self.width,
                fill='cyan'
            ))

    def move(self, side):
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
        for piece in self.pieces:
            x, y = self.get_one_piece_position(piece)
            if int(y + shift_y // 20) >= 0 and self.cell[int(y + shift_y // 20)][int(x + shift_x//20)] == 1:
                return False
        return True

    def motion(self):
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
        x1, y1, _, _ = self.can.coords(piece)
        return x1//20, y1//20

    def get_position(self):
        all_x = []
        all_y = []
        for piece in self.pieces:
            x, y = self.get_one_piece_position(piece)
            all_x.append(x)
            all_y.append(y)
        return min(all_x), min(all_y), max(all_x), max(all_y)

    def play(self):
        self.piece_in_motion = True
        while self.piece_in_motion:
            self.motion()
            self.get_position()

    def stop(self):
        self.piece_in_motion = False
