import pygame

from constants import *
from board import *
from mouse import Mouse
from config import Config

class Game:

    def __init__(self):
        self.board = Board()
        self.mouse = Mouse()
        self.config = Config()

    # SHOW methods

    def show_background(self, surface):
        theme = self.config.theme

        for rank in range(RANKS):
            for file in range(FILES):
                colour = theme.background.light if (file + rank) % 2 == 0 else theme.background.dark

                rect = (file * SQSIZE, rank * SQSIZE,  SQSIZE, SQSIZE)

                pygame.draw.rect(surface, colour, rect)
    
    def show_pieces(self, surface):
        for rank in range(RANKS):
            for file in range(FILES):

                #check for pieces in the square

                if self.board.squares[rank][file].has_piece():
                    piece = self.board.squares[rank][file].piece

                    #piece.set_sprite(size=80)
                    img = pygame.image.load(piece.sprite)
                    img_center = file * SQSIZE + SQSIZE // 2, rank * SQSIZE + SQSIZE // 2
                    piece.sprite_rect  = img.get_rect(center=img_center)
                    surface.blit(img, piece.sprite_rect)
    
    def show_last_move(self, surface):
        theme = self.config.theme

        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                # color
                color = theme.trace.light if (pos.rank + pos.file) % 2 == 0 else theme.trace.dark
                # rect
                rect = (pos.file * SQSIZE, pos.rank * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)