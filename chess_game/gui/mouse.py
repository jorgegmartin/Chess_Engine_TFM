import pygame

from constants import *

class Mouse():
    
    def __init__(self):
        self.piece = None
        self.picking = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_rank = 0
        self.initial_file = 0

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos # (xcoor, ycoor)

    def save_initial(self, pos):
        self.initial_rank = pos[1] // SQSIZE
        self.initial_file = pos[0] // SQSIZE
    
    def pick_piece(self, piece):
        self.piece = piece
        self.picking = True
    
    def unpick_piece(self):
        self.piece = None
        self.picking = False

    def update_blit(self, surface):
        # texture
        self.piece.set_sprite(size=128)
        sprite = self.piece.sprite
        # img
        img = pygame.image.load(sprite)
        # rect
        img_center = (self.mouseX, self.mouseY)
        self.piece.sprite_rect = img.get_rect(center=img_center)
        # blit
        surface.blit(img, self.piece.sprite_rect)

#####################################################################

    def set_hover(self, row, col):
        self.hovered_sqr = self.board.squares[row][col]

    def show_hover(self, surface):
        if self.hovered_sqr:
            # color
            color = (180, 180, 180)
            # rect
            rect = (self.hovered_sqr.col * SQSIZE, self.hovered_sqr.row * SQSIZE, SQSIZE, SQSIZE)
            # blit
            pygame.draw.rect(surface, color, rect, width=3)