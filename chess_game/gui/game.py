import pygame
from constants import *
from board import *

class Game:

    def __init__(self):
        self.board = Board()

    # SHOW methods

    def show_background(self, surface):
        for rank in range(RANKS):
            for file in range(FILES):
                if (rank + file) % 2 == 0:
                    colour = (234, 235, 200) # light green
                else:
                    colour = (119, 154, 88) # dark green 

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