import os


class Piece():
    def __init__(self, name, colour, value, sprite=None, sprite_rect=None):
        self.name = name
        self.colour = colour
        value_sign = 1 if colour == 'white' else -1
        self.value = value * value_sign
        self.sprite = sprite
        self.set_sprite()
        self.sprite_rect = sprite_rect
    
    def set_sprite(self, size=80):
        self.sprite = os.path.join(
            f'resources/imgs/imgs-{size}px/{self.colour}_{self.name}.png')


class Pawn(Piece):
    def __init__(self, colour):
        super().__init__('pawn', colour, 1.0)

class Knight(Piece):
    def __init__(self, colour):
        super().__init__('knight', colour, 3.0)

class Bishop(Piece):
    def __init__(self, colour):
        super().__init__('bishop', colour, 3.01)

class Rook(Piece):
    def __init__(self, colour):
        super().__init__('rook', colour, 5.0)

class Queen(Piece):
    def __init__(self, colour):
        super().__init__('queen', colour, 9.0)

class King(Piece):
    def __init__(self, colour):
        super().__init__('king', colour, 10000)