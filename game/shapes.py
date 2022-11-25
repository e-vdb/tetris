"""Module with classes for shapes."""

from random import randint, choice
from game.exceptions import GameOver
import time


class Shape:
    """Parent class for all shapes."""

    def __init__(self, cell, can, refresh_sec, width=20):
        """Initialize class."""
        self.cell = cell
        self.can = can
        self.pieces = []
        self.width = width
        self.refresh_sec = refresh_sec

    def check_init_position(self, coords):
        """
        Check if initial position is free.

        Parameters
        ----------
        coords:

        Returns
        -------
        None
        Raises
        ------
        GameOver
        """
        for coord in coords:
            x, y = coord
            if self.cell[y][x] == 1:
                print('Game Over')
                raise GameOver

    def place_piece_if_valid(self, init_coords, color):
        """Create piece on canvas."""
        self.check_init_position(init_coords)
        for coord in init_coords:
            x, y = coord
            self.pieces.append(
                self.can.create_rectangle(x * 20, y * 20, (x + 1) * 20,
                                          (y + 1) * 20, fill=color))
        self.can.update()
        time.sleep(self.refresh_sec)


class ShapeI(Shape):
    """Class for shape I."""

    def __init__(self, can, cell, refresh_sec):
        """Initialize shape I."""
        super(ShapeI, self).__init__(cell, can, refresh_sec)
        self.color = 'cyan'

        self.rotation = {
            0: [(1, -2), (0, -1), (-1, 0), (-2, 1)],
            90: [(2, 1), (1, 0), (0, -1), (-1, -2)],
            180: [(-1, 2), (0, 1), (1, 0), (2, -1)],
            270: [(-2, -1), (-1, 0), (0, 1), (1, 2)]
        }
        self.angle = choice([0, 90])
        self.init_x = randint(3, 6)
        self.init_y = 0 if self.angle == 0 else -1
        self.init_coords = [
            (self.init_x, self.init_y),
            (self.init_x, self.init_y+1),
            (self.init_x, self.init_y+2),
            (self.init_x, self.init_y+3)
        ]

        if self.angle != 0:
            self.init_coords = [(x + self.rotation[self.angle][i][0], y + self.rotation[self.angle][i][1]) for i, (x, y) in enumerate(self.init_coords)]  # noqa E501

    def init_piece(self):
        """Create piece on canvas."""
        self.place_piece_if_valid(self.init_coords, self.color)


class ShapeL(Shape):
    """Class for shape L."""

    def __init__(self, can, cell, refresh_sec):
        """Initialize shape L."""
        super(ShapeL, self).__init__(cell, can, refresh_sec)
        self.color = 'orange'
        self.angle = choice([0, 90])
        self.rotation = {
            0: [(0, -2), (-1, -1), (-2, 0), (-1, 1)],
            90: [(2, 0), (1, -1), (0, -2), (-1, -1)],
            180: [(0, 2), (1, 1), (2, 0), (1, -1)],
            270: [(-2, 0), (-1, 1), (0, 2), (1, 1)]
        }

        self.init_x = randint(3, 6)
        self.init_y = 0

        self.init_coords = [
            (self.init_x, self.init_y),
            (self.init_x, self.init_y + 1),
            (self.init_x, self.init_y + 2),
            (self.init_x+1, self.init_y + 2)
        ]

        if self.angle != 0:
            self.init_coords = [(x + self.rotation[self.angle][i][0], y + self.rotation[self.angle][i][1]) for i, (x, y) in enumerate(self.init_coords)]  # noqa E501

    def init_piece(self):
        """Create piece on canvas."""
        self.place_piece_if_valid(self.init_coords, self.color)


class ShapeJ(Shape):
    """Class for shape J."""

    def __init__(self, can, cell, refresh_sec):
        """Initialize shape J."""
        super(ShapeJ, self).__init__(cell, can, refresh_sec)
        self.color = 'blue'

        self.rotation = {
            0: [(1, 0), (0, 1), (-1, 2), (-2, 1)],
            90: [(0, 2), (-1, 1), (-2, 0), (-1, -1)],
            180: [(-2, 0), (-1, -1), (0, -2), (1, -1)],
            270: [(0, -2), (1, -1), (2, 0), (1, 1)]
        }

        self.angle = choice([0, 90])
        self.init_x = randint(3, 6)
        self.init_y = 0 if self.angle == 0 else -1

        self.init_coords = [
            (self.init_x, self.init_y),
            (self.init_x, self.init_y + 1),
            (self.init_x, self.init_y + 2),
            (self.init_x - 1, self.init_y + 2)
        ]

        if self.angle != 0:
            self.init_coords = [(x + self.rotation[self.angle][i][0],
                                 y + self.rotation[self.angle][i][1]) for
                                i, (x, y) in
                                enumerate(self.init_coords)]  # noqa E501

    def init_piece(self):
        """Create piece on canvas."""
        self.place_piece_if_valid(self.init_coords, self.color)


class ShapeT(Shape):
    """Class for shape T."""

    def __init__(self, can, cell, refresh_sec):
        """Initialize shape T."""
        super(ShapeT, self).__init__(cell, can, refresh_sec)
        self.color = 'violet'
        self.angle = 0
        self.rotation = {
            0: [(1, -1), (0, 0), (-1, 1), (-1, -1)],
            90: [(1, 1), (0, 0), (-1, -1), (1, -1)],
            180: [(-1, 1), (0, 0), (1, -1), (1, 1)],
            270: [(-1, -1), (0, 0), (1, 1), (-1, 1)]
        }
        self.angle = choice([0, 90])
        self.init_x = randint(3, 6)
        self.init_y = 0

        self.init_coords = [
            (self.init_x, self.init_y),
            (self.init_x, self.init_y+1),
            (self.init_x, self.init_y+2),
            (self.init_x - 1, self.init_y + 1)
        ]

        if self.angle != 0:
            self.init_coords = [(x + self.rotation[self.angle][i][0],
                                 y + self.rotation[self.angle][i][1]) for
                                i, (x, y) in
                                enumerate(self.init_coords)]  # noqa E501

    def init_piece(self):
        """Create piece on canvas."""
        self.place_piece_if_valid(self.init_coords, self.color)


class ShapeZ(Shape):
    """Class for shape Z."""

    def __init__(self, can, cell, refresh_sec):
        """Initialize shape Z."""
        super(ShapeZ, self).__init__(cell, can, refresh_sec)
        self.color = 'red'
        self.rotation = {
            0: [(0, -2), (1, -1), (0, 0), (1, 1)],
            90: [(2, 0), (1, 1), (0, 0), (-1, 1)],
            180: [(0, 2), (-1, 1), (0, 0), (-1, -1)],
            270: [(-2, 0), (-1, -1), (0, 0), (1, -1)]
        }

        self.angle = choice([0, 90])
        self.init_x = randint(3, 6)
        self.init_y = 0

        self.init_coords = [
            (self.init_x, self.init_y),
            (self.init_x+1, self.init_y),
            (self.init_x + 1, self.init_y + 1),
            (self.init_x + 2, self.init_y + 1)
        ]

        if self.angle != 0:
            self.init_coords = [(x + self.rotation[self.angle][i][0],
                                 y + self.rotation[self.angle][i][1]) for
                                i, (x, y) in
                                enumerate(self.init_coords)]  # noqa E501

    def init_piece(self):
        """Create piece on canvas."""
        self.place_piece_if_valid(self.init_coords, self.color)


class ShapeS(Shape):
    """Class for shape S."""

    def __init__(self, can, cell, refresh_sec):
        """Initialize shape S."""
        super(ShapeS, self).__init__(cell, can, refresh_sec)
        self.color = 'green'
        self.rotation = {
            0: [(2, 0), (1, -1), (0, 0), (-1, -1)],
            90: [(0, 2), (1, 1),  (0, 0), (1, -1)],
            180: [(-2, 0), (-1, 1), (0, 0), (1, 1)],
            270: [(0, -2), (-1, -1), (0, 0), (-1, 1)]
        }

        self.angle = choice([0, 90])
        self.init_x = randint(3, 6)
        self.init_y = 0

        self.init_coords = [
            (self.init_x, self.init_y),
            (self.init_x - 1, self.init_y),
            (self.init_x - 1, self.init_y + 1),
            (self.init_x - 2, self.init_y + 1)
        ]

        if self.angle != 0:
            self.init_coords = [(x + self.rotation[self.angle][i][0],
                                 y + self.rotation[self.angle][i][1]) for
                                i, (x, y) in
                                enumerate(self.init_coords)]  # noqa E501

    def init_piece(self):
        """Create piece on canvas."""
        self.place_piece_if_valid(self.init_coords, self.color)


class ShapeSquare(Shape):
    """Class for shape square."""

    def __init__(self, can, cell, refresh_sec):
        """Initialize shape square."""
        super(ShapeSquare, self).__init__(cell, can, refresh_sec)
        self.color = 'yellow'

        self.rotation = {
            0: [(0, 0), (0, 0), (0, 0), (0, 0)],
            90: [(0, 0), (0, 0), (0, 0), (0, 0)],
            180: [(0, 0), (0, 0), (0, 0), (0, 0)],
            270: [(0, 0), (0, 0), (0, 0), (0, 0)]
        }

        self.angle = 0
        self.init_x = randint(3, 6)
        self.init_y = 0

        self.init_coords = [
            (self.init_x, self.init_y),
            (self.init_x + 1, self.init_y),
            (self.init_x, self.init_y + 1),
            (self.init_x + 1, self.init_y + 1)
        ]

    def init_piece(self):
        """Create piece on canvas."""
        self.place_piece_if_valid(self.init_coords, self.color)
