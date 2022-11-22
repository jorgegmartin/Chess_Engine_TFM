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