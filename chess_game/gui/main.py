import pygame
import sys

from constants import *
from game import Game


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):

        game = self.game
        screen = self.screen
        board = self.game.board
        mouse = self.game.mouse

        while True:
            # show methods
            game.show_background(screen)
            game.show_pieces(screen)
            game.show_last_move(screen) ##TODO

            # event checking
            for event in pygame.event.get():
                # checking for clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse.update_mouse(event.pos)
                # checking for movement
                elif event.type == pygame.MOUSEMOTION:
                    pass
                # checking for clicks release
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                
                
                # quitting
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            pygame.display.update()




main = Main()
main.mainloop()