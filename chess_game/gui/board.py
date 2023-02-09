from constants import *
from piece import *
import chess

class Square:

    def __init__(self, rank, file, piece=None):
        self.rank = rank
        self.file = file
        self.piece = piece
        self.highlighted = False

    def has_piece(self):
        return self.piece != None

class Board:

    def __init__(self):
        self.squares = [FILES*[0] for rank in range(RANKS)]
        self.last_move = None
        self._create()
        self._add_piece('white')
        self._add_piece('black')


    def move(self, piece, move, enpassant=False, promotion=False, kingcastling=False, queencastling=False, piece_colour='white'):
        initial = move.initial
        final = move.final

        if enpassant==True:
            self.squares[initial.rank][final.file].piece = None
        if promotion==True:
            self.squares[initial.rank][initial.file].piece = None
            self.squares[final.rank][final.file].piece = Queen(piece_colour)
        if kingcastling==True:
            # king move
            self.squares[initial.rank][initial.file].piece = None
            self.squares[final.rank][final.file].piece = piece
            # rook move
            self.squares[final.rank][final.file+1].piece = None
            self.squares[final.rank][final.file-1].piece = Rook(piece_colour)
        if queencastling==True:
            # king move
            self.squares[initial.rank][initial.file].piece = None
            self.squares[final.rank][final.file].piece = piece
            # rook move
            self.squares[final.rank][final.file-2].piece = None
            self.squares[final.rank][final.file+1].piece = Rook(piece_colour)
        elif promotion==False:
            self.squares[initial.rank][initial.file].piece = None
            self.squares[final.rank][final.file].piece = piece
    
    def valid_move(self, move, current_board):
        
        valid_moves = [str(idx) for idx in current_board.legal_moves]
        print(valid_moves) #CHECKPOINT
        is_valid = True if move in valid_moves else False
        print(is_valid) #CHECKPOINT
        return True if move in valid_moves else False

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
