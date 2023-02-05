import pygame
import os

class Config:

    def __init__(self):
        self.theme = Theme((234, 235, 200), (119, 154, 88), (244, 247, 116), (172, 195, 51), '#C86464', '#C84646')
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.move_sound = Sound(
            os.path.join('chess_game/gui/resources/sounds/move.wav'))
        self.capture_sound = Sound(
            os.path.join('chess_game/gui/resources/sounds/capture.wav'))

class Sound:

    def __init__(self, path):
        self.path = path
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        pygame.mixer.Sound.play(self.sound)

class Color:

    def __init__(self, light, dark):
        self.light = light
        self.dark = dark

class Theme:

    def __init__(self, light_background, dark_background, 
                       light_trace, dark_trace,
                       light_moves, dark_moves):
        
        self.background = Color(light_background, dark_background)
        self.trace = Color(light_trace, dark_trace)
        self.moves = Color(light_moves, dark_moves)