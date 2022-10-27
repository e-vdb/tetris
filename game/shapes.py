from random import randint


class ShapeI:
    def __init__(self, can):
        self.length = 4
        self.width = 20
        self.can = can
        self.pieces = []

    def init_piece(self):
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
    def __init__(self, can):
        self.length = 3
        self.width = 20
        self.can = can
        self.pieces = []

    def init_piece(self):
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
    def __init__(self, can):
        self.length = 3
        self.width = 20
        self.can = can
        self.pieces = []

    def init_piece(self):
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
    def __init__(self, can):
        self.length = 3
        self.width = 20
        self.can = can
        self.pieces = []

    def init_piece(self):
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
    def __init__(self, can):
        self.height = 2
        self.width = 20
        self.can = can
        self.pieces = []

    def init_piece(self):
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
    def __init__(self, can):
        self.height = 2
        self.width = 20
        self.can = can
        self.pieces = []

    def init_piece(self):
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
    def __init__(self, can):
        self.height = 2
        self.width = 20
        self.can = can
        self.pieces = []

    def init_piece(self):
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
