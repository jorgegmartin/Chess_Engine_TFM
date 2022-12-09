from constants import *
from piece import *

class Square:

    def __init__(self, rank, file, piece=None):
        self.rank = rank
        self.file = file
        self.piece = piece
        self.highlighted = False

    def has_piece(self):
        return self.piece != None

class Board():

    def __init__(self):
        self.squares = [RANKS*[0] for file in range(FILES)]
        self.last_move = None
        self._create()
        self._add_piece('white')
        self._add_piece('black')

    def move(self, piece, move, testing=False):
        initial = move.initial
        final = move.final

       # en_passant_empty = self.squares[final.rank][final.file].isempty()

        # console board move update
        self.squares[initial.rank][initial.file].piece = None
        self.squares[final.rank][final.file].piece = piece
    
    def valid_move(self, move):
        return True #TODO aqui comprobar los movimientos extraidos del paquete chess.com
    
    def _create(self):
        for rank in range(RANKS):
            for file in range(FILES):
                self.squares[rank][file] = Square(rank, file)

    def _add_piece(self, colour):
        pawn_rank, major_rank = (6, 7) if colour == 'white' else (1, 0)
        
        # pawns
        for file in range(FILES):
            self.squares[pawn_rank][file] = Square(pawn_rank, file, Pawn(colour))
        
        # knights
        self.squares[major_rank][1] = Square(major_rank, 1, Knight(colour))
        self.squares[major_rank][6] = Square(major_rank, 6, Knight(colour))

        # bishops
        self.squares[major_rank][2] = Square(major_rank, 2, Bishop(colour))
        self.squares[major_rank][5] = Square(major_rank, 5, Bishop(colour))

        # rooks
        self.squares[major_rank][0] = Square(major_rank, 0, Rook(colour))
        self.squares[major_rank][7] = Square(major_rank, 7, Rook(colour))

        # queen
        self.squares[major_rank][3] = Square(major_rank, 3, Queen(colour))

        # king
        self.squares[major_rank][4] = Square(major_rank, 4, King(colour))
