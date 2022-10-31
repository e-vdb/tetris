"""Module with classes for shapes."""

from random import randint


class ShapeI:
    """Class for shape I."""

    def __init__(self, can):
        """Initialize shape I."""
        self.length = 4
        self.width = 20
        self.can = can
        self.pieces = []
        self.angle = 0
        self.rotation = {
            0: [(1, -2), (0, -1), (-1, 0), (-2, 1)],
            90: [(2, 1), (1, 0), (0, -1), (-1, -2)],
            180: [(-1, 2), (0, 1), (1, 0), (2, -1)],
            270: [(-2, -1), (-1, 0), (0, 1), (1, 2)]
        }

    def init_piece(self):
        """Create piece on canvas."""
        init_x = randint(0, 9) * 20

        for i in range(self.length):
            init_y = (-4 + i) * 20
            self.pieces.append(self.can.create_rectangle(
                init_x,
                init_y,
                init_x + self.width,
                init_y + self.width,
                fill='cyan'
            ))


class ShapeL:
    """Class for shape L."""

    def __init__(self, can):
        """Initialize shape L."""
        self.length = 3
        self.width = 20
        self.can = can
        self.pieces = []
        self.angle = 0
        self.rotation = {
            0: [(0, -2), (-1, -1), (-2, 0), (-1, 1)],
            90: [(2, 0), (1, -1), (0, -2), (-1, -1)],
            180: [(0, 2), (1, 1), (2, 0), (1, -1)],
            270: [(-2, 0), (-1, 1), (0, 2), (1, 1)]
        }

    def init_piece(self):
        """Create piece on canvas."""
        init_x = randint(0, 8) * 20
        init_y = (-4) * 20

        for _ in range(self.length):
            init_y = init_y + 20
            self.pieces.append(self.can.create_rectangle(
                init_x,
                init_y,
                init_x + self.width,
                init_y + self.width,
                fill='orange'
            ))
        init_x = init_x + 20
        self.pieces.append(self.can.create_rectangle(
            init_x,
            init_y,
            init_x + self.width,
            init_y + self.width,
            fill='orange'
        ))


class ShapeJ:
    """Class for shape J."""

    def __init__(self, can):
        """Initialize shape J."""
        self.length = 3
        self.width = 20
        self.can = can
        self.pieces = []
        self.angle = 0
        self.rotation = {
            0: [(1, 0), (0, 1), (-1, 2), (-2, 1)],
            90: [(0, 2), (-1, 1), (-2, 0), (-1, -1)],
            180: [(-2, 0), (-1, -1), (0, -2), (1, -1)],
            270: [(0, -2), (1, -1), (2, 0), (1, 1)]
        }

    def init_piece(self):
        """Create piece on canvas."""
        init_x = randint(1, 9) * 20
        init_y = (-4) * 20

        for _ in range(self.length):
            init_y = init_y + 20
            self.pieces.append(self.can.create_rectangle(
                init_x,
                init_y,
                init_x + self.width,
                init_y + self.width,
                fill='blue'
            ))
        init_x = init_x - 20
        self.pieces.append(self.can.create_rectangle(
            init_x,
            init_y,
            init_x + self.width,
            init_y + self.width,
            fill='blue'
        ))


class ShapeT:
    """Class for shape T."""

    def __init__(self, can):
        """Initialize shape T."""
        self.length = 3
        self.width = 20
        self.can = can
        self.pieces = []
        self.angle = 0
        self.rotation = {
            0: [(1, -1), (0, 0), (-1, 1), (-1, -1)],
            90: [(1, 1), (0, 0), (-1, -1), (1, -1)],
            180: [(-1, 1), (0, 0), (1, -1), (1, 1)],
            270: [(-1, -1), (0, 0), (1, 1), (-1, 1)]
        }

    def init_piece(self):
        """Create piece on canvas."""
        init_x = randint(1, 9) * 20
        init_y = (-4) * 20

        for _ in range(self.length):
            init_y = init_y + 20
            self.pieces.append(self.can.create_rectangle(
                init_x,
                init_y,
                init_x + self.width,
                init_y + self.width,
                fill='violet'
            ))
        init_x = init_x - 20
        init_y = init_y - 20
        self.pieces.append(self.can.create_rectangle(
            init_x,
            init_y,
            init_x + self.width,
            init_y + self.width,
            fill='violet'
        ))


class ShapeZ:
    """Class for shape Z."""

    def __init__(self, can):
        """Initialize shape Z."""
        self.height = 2
        self.width = 20
        self.can = can
        self.pieces = []
        self.angle = 0
        self.rotation = {
            0: [(0, -2), (1, -1), (0, 0), (1, 1)],
            90: [(2, 0), (1, 1), (0, 0), (-1, 1)],
            180: [(0, 2), (-1, 1), (0, 0), (-1, -1)],
            270: [(-2, 0), (-1, -1), (0, 0), (1, -1)]
        }

    def init_piece(self):
        """Create piece on canvas."""
        init_x = randint(0, 7) * 20
        init_y = -2 * 20

        for i in range(self.height):
            init_x = init_x + i * 20

            self.pieces.append(self.can.create_rectangle(
                init_x,
                init_y,
                init_x + self.width,
                init_y + self.width,
                fill='red'
            ))
        init_y = -1 * 20
        for i in range(self.height):
            init_x = init_x + i * 20

            self.pieces.append(self.can.create_rectangle(
                init_x,
                init_y,
                init_x + self.width,
                init_y + self.width,
                fill='red'
            ))


class ShapeS:
    """Class for shape S."""

    def __init__(self, can):
        """Initialize shape S."""
        self.height = 2
        self.width = 20
        self.can = can
        self.pieces = []
        self.angle = 0
        self.rotation = {
            0: [(2, 0), (1, -1), (0, 0), (-1, -1)],
            90: [(0, 2), (1, 1),  (0, 0), (1, -1)],
            180: [(-2, 0), (-1, 1), (0, 0), (1, 1)],
            270: [(0, -2), (-1, -1), (0, 0), (-1, 1)]
        }

    def init_piece(self):
        """Create piece on canvas."""
        init_x = randint(2, 9) * 20
        init_y = -2 * 20

        for i in range(self.height):
            init_x = init_x - i * 20

            self.pieces.append(self.can.create_rectangle(
                init_x,
                init_y,
                init_x + self.width,
                init_y + self.width,
                fill='green'
            ))
        init_y = -1 * 20
        for i in range(self.height):
            init_x = init_x - i * 20

            self.pieces.append(self.can.create_rectangle(
                init_x,
                init_y,
                init_x + self.width,
                init_y + self.width,
                fill='green'
            ))


class ShapeSquare:
    """Class for shape square."""

    def __init__(self, can):
        """Initialize shape square."""
        self.height = 2
        self.width = 20
        self.can = can
        self.pieces = []
        self.angle = 0
        self.rotation = {
            0: [(0, 0), (0, 0), (0, 0), (0, 0)],
            90: [(0, 0), (0, 0), (0, 0), (0, 0)],
            180: [(0, 0), (0, 0), (0, 0), (0, 0)],
            270: [(0, 0), (0, 0), (0, 0), (0, 0)]
        }

    def init_piece(self):
        """Create piece on canvas."""
        init_x = randint(0, 8) * 20
        init_y = -2 * 20

        for i in range(self.height):
            init_x = init_x + i * 20

            self.pieces.append(self.can.create_rectangle(
                init_x,
                init_y,
                init_x + self.width,
                init_y + self.width,
                fill='yellow'
            ))
        init_y = -1 * 20
        for i in range(self.height):
            init_x = init_x - i * 20

            self.pieces.append(self.can.create_rectangle(
                init_x,
                init_y,
                init_x + self.width,
                init_y + self.width,
                fill='yellow'
            ))
